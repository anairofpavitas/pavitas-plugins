#!/usr/bin/env python3
"""Zo job runner for this Mac (pavitas-core).

Zo queues work for Claude Code on a named Mac (zo_agent.py job add on Zo, or an accepted digest offer). This runner,
started by launchd once a minute, asks Zo for the next job for this machine, runs Claude Code headless, and reports the
result back. Zo shows it in the Zo Home feed (and texts it when the job asked for that).

Commands:
  run-once     check for one job and run it (what launchd calls every 60 s; returns at once when there's none)
  setup        install and start the LaunchAgent (com.pavitas.agent-runner). Needs `agent_log.py setup` done first.
  uninstall    stop and remove the LaunchAgent
  off | on     pause or resume without uninstalling (a marker file in ~/.config/pavitas)
  status       configuration, LaunchAgent state, last log lines, and this machine's recent jobs

Safety:
  - read jobs: Claude may read files, search and browse the web. Nothing that changes anything.
  - edit jobs: also edit files and run a fixed list of build/test/inspect commands, and only inside a git repo, in a
    separate worktree on a new branch zo-job-<id> (your own checkout is never touched). Changes are committed to that
    branch and left for you to review. Never pushed, never merged. No rm, no git push, no arbitrary shell.
  - one job at a time per Mac; 30-minute limit; the folder must be inside your home folder.
Files: ~/.config/pavitas/runner.log (what happened), ~/.config/pavitas/runner-off (pause marker).
"""
import json
import os
import plistlib
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "hooks"))
import agent_log as al   # token, machine name, http helper, config dir  # noqa: E402

LABEL = "com.pavitas.agent-runner"
PLIST = Path.home() / "Library" / "LaunchAgents" / f"{LABEL}.plist"
CONF = Path(al.CONF)
LOG = CONF / "runner.log"
OFF = CONF / "runner-off"
LOCK = CONF / ".runner.lock"
# Stable path that survives plugin updates (the marketplace clone, refreshed by `claude plugin marketplace update`).
STABLE = Path.home() / ".claude/plugins/marketplaces/pavitas-plugins/pavitas-core/runner/agent_runner.py"
TIME_LIMIT = 30 * 60

READ_TOOLS = ["Read", "Glob", "Grep", "WebSearch", "WebFetch", "TodoWrite"]
EDIT_TOOLS = READ_TOOLS + ["Edit", "Write", "MultiEdit", "NotebookEdit"] + [f"Bash({c}:*)" for c in (
    "git status", "git diff", "git log", "git show", "git branch", "ls", "pwd", "wc", "head", "tail", "cat", "grep", "find",
    "xcodegen", "xcodebuild", "swift build", "swift test", "npm test", "npm run", "npx tsc", "bun test", "bun run",
    "python3 -m pytest", "python3 -m py_compile", "pytest", "make test")]

SYSTEM = """You are running unattended on Pavi Proczko's Mac for a job his assistant Zo queued. Nobody can answer \
questions while you work: make sensible choices, note them, and finish. {mode_note}
Final reply: plain short sentences. What you did, what you found or changed (files), anything left undone, and any \
action you wanted but weren't allowed to take, with the exact details so Pavi can do it or approve it next time."""
MODE_NOTES = {
    "read": "This is a read-only job: look, search and report. Do not try to change anything.",
    "edit": "You are in a separate git worktree on branch {branch}; edit freely there. Do not push, merge, or delete "
            "branches, and do not touch other folders. Build or test to check your work when you can.",
}


def log(msg):
    try:
        CONF.mkdir(parents=True, exist_ok=True)
        if LOG.exists() and LOG.stat().st_size > 300_000:
            LOG.replace(str(LOG) + ".1")
        with LOG.open("a", encoding="utf-8") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")
    except OSError:
        pass


def api(body, timeout=30):
    status, text = al.http("POST", "jobs", token=al.read_token(), body=body, timeout=timeout)
    return json.loads(text)


def report(job_id, **fields):
    try:
        api({"op": "update", "id": job_id, **fields})
    except Exception as e:
        log(f"job {job_id}: couldn't report {fields.get('status')}: {e}")


def claude_path():
    for p in (Path.home() / ".local/bin/claude", Path("/opt/homebrew/bin/claude"), Path("/usr/local/bin/claude"),
              Path.home() / ".claude/local/claude"):
        if p.exists():
            return str(p)
    return None


def git(cwd, *args, check=True):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True, timeout=120, check=check).stdout.strip()


def prepare_edit(job, folder):
    """Separate worktree on a new branch, so Pavi's own checkout is never touched. Returns (workdir, branch, repo)."""
    top = git(folder, "rev-parse", "--show-toplevel", check=False)
    if not top:
        raise RuntimeError(f"edit jobs need a git repository; {folder} isn't in one")
    repo = Path(top)
    branch = f"zo-job-{job['id']}"
    tree = repo / ".claude" / "worktrees" / branch
    tree.parent.mkdir(parents=True, exist_ok=True)
    git(repo, "worktree", "add", "-b", branch, str(tree), "HEAD")
    sub = Path(folder).resolve().relative_to(repo.resolve()) if Path(folder).resolve() != repo.resolve() else Path(".")
    return tree / sub, branch, repo, tree


def finish_edit(job, tree, branch):
    """Commits whatever changed on the job branch. Returns the changed files."""
    git(tree, "add", "-A")
    files = [f for f in git(tree, "diff", "--cached", "--name-only").splitlines() if f]
    if files:
        git(tree, "-c", "user.name=Zo job runner", "-c", "user.email=pavi@paviproczko.com",
            "commit", "-q", "-m", f"zo-job {job['id']}: {job['title'][:60]}")
    return files


def run_job(job):
    jid = job["id"]
    folder = Path(os.path.expanduser(job["cwd"] or "~")).resolve()
    home = Path.home().resolve()
    if not str(folder).startswith(str(home)) or not folder.is_dir():
        report(jid, status="failed", error=f"folder not found or outside the home folder: {job['cwd']}")
        return
    claude = claude_path()
    if not claude:
        report(jid, status="failed", error="Claude Code isn't installed on this Mac (~/.local/bin/claude)")
        return
    branch = tree = None
    workdir = folder
    try:
        if job["mode"] == "edit":
            workdir, branch, _, tree = prepare_edit(job, folder)
    except Exception as e:
        report(jid, status="failed", error=str(e)[:500])
        return
    report(jid, status="running", branch=branch)
    note = MODE_NOTES[job["mode"]].format(branch=branch)
    allowed = EDIT_TOOLS if job["mode"] == "edit" else READ_TOOLS
    args = [claude, "-p", job["prompt"], "--output-format", "json", "--model", job.get("model") or "sonnet",
            "--permission-prompts", "none", "--append-system-prompt", SYSTEM.format(mode_note=note),
            "--allowedTools", *allowed]
    env = dict(os.environ, PAVITAS_AGENT_SOURCE="zo-job",
               PATH=f"{home}/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin")
    log(f"job {jid}: running [{job['mode']}] in {workdir}: {job['title']}")
    try:
        p = subprocess.run(args, cwd=str(workdir), env=env, capture_output=True, text=True, timeout=TIME_LIMIT,
                           stdin=subprocess.DEVNULL)
        out = json.loads(p.stdout or "{}")
    except subprocess.TimeoutExpired:
        out, p = {"is_error": True, "result": f"stopped after {TIME_LIMIT // 60} minutes"}, None
    except ValueError:
        out = {"is_error": True, "result": (p.stderr or p.stdout or "no output")[-600:]}
    files = []
    if tree is not None:
        try:
            files = finish_edit(job, tree, branch)
        except Exception as e:
            log(f"job {jid}: commit failed: {e}")
    result = (out.get("result") or "").strip()
    denied = out.get("permission_denials") or []
    if denied:
        result += "\n\nNot allowed in this job: " + "; ".join(
            f"{d.get('tool_name')} {json.dumps(d.get('tool_input', {}))[:160]}" for d in denied[:5])
    if branch and not files:
        result += f"\n(No files changed; branch {branch} is empty.)"
    if out.get("is_error"):
        report(jid, status="failed", error=result[:2000] or "Claude Code reported an error", session_id=out.get("session_id"),
               branch=branch, files=files)
    else:
        report(jid, status="done", result=result[:20000], session_id=out.get("session_id"), branch=branch, files=files)
    log(f"job {jid}: {'failed' if out.get('is_error') else 'done'} ({len(files)} files changed)")


def cmd_run_once():
    if OFF.exists() or al.disabled() or not al.read_token():
        return
    try:
        fd = os.open(str(LOCK), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
    except FileExistsError:
        if time.time() - LOCK.stat().st_mtime < TIME_LIMIT + 300:
            return   # a job is still running
        LOCK.unlink()
        return cmd_run_once()
    try:
        r = api({"op": "claim", "machine": al.machine_name()})
        if r.get("job"):
            run_job(r["job"])
    except Exception as e:
        log(f"run-once: {e}")
    finally:
        LOCK.unlink(missing_ok=True)


def cmd_setup():
    if not al.read_token():
        sys.exit("Set up the agent log first: python3 ~/.claude/plugins/marketplaces/pavitas-plugins/pavitas-core/hooks/agent_log.py setup")
    script = STABLE if STABLE.exists() else Path(__file__).resolve()
    PLIST.parent.mkdir(parents=True, exist_ok=True)
    home = str(Path.home())
    with PLIST.open("wb") as f:
        plistlib.dump({
            "Label": LABEL,
            "ProgramArguments": ["/usr/bin/python3", str(script), "run-once"],
            "StartInterval": 60,
            "RunAtLoad": True,
            "ProcessType": "Background",
            "LowPriorityIO": True,
            "StandardOutPath": str(LOG),
            "StandardErrorPath": str(LOG),
            "EnvironmentVariables": {"PATH": f"{home}/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"},
        }, f)
    uid = os.getuid()
    subprocess.run(["launchctl", "bootout", f"gui/{uid}/{LABEL}"], capture_output=True)
    r = subprocess.run(["launchctl", "bootstrap", f"gui/{uid}", str(PLIST)], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"launchctl bootstrap failed: {r.stderr.strip()}")
    OFF.unlink(missing_ok=True)
    print(f"Runner installed for {al.machine_name()}: checks Zo for jobs every minute while you're logged in.\n"
          f"Log: {LOG}. Pause: agent_runner.py off. Remove: agent_runner.py uninstall.")


def cmd_uninstall():
    subprocess.run(["launchctl", "bootout", f"gui/{os.getuid()}/{LABEL}"], capture_output=True)
    PLIST.unlink(missing_ok=True)
    print("Runner removed.")


def cmd_status():
    print(f"machine: {al.machine_name()}   token: {'present' if al.read_token() else 'MISSING'}   paused: {OFF.exists()}")
    r = subprocess.run(["launchctl", "print", f"gui/{os.getuid()}/{LABEL}"], capture_output=True, text=True)
    state = re.search(r"state = (\w+)", r.stdout)
    print(f"LaunchAgent: {'installed, ' + state.group(1) if r.returncode == 0 and state else 'not installed'}")
    try:
        _, text = al.http("GET", "jobs", token=al.read_token(), query={"machine": al.machine_name(), "limit": "5"}, timeout=10)
        for j in json.loads(text)["jobs"]:
            print(f"  #{j['id']} {j['status']:<9} [{j['mode']}] {j['title']}")
    except Exception as e:
        print(f"  couldn't list jobs: {e}")
    if LOG.exists():
        print("last log lines:")
        for line in LOG.read_text(errors="replace").splitlines()[-6:]:
            print("  " + line)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "run-once":
        cmd_run_once()
    elif cmd == "setup":
        cmd_setup()
    elif cmd == "uninstall":
        cmd_uninstall()
    elif cmd == "off":
        CONF.mkdir(parents=True, exist_ok=True)
        OFF.touch()
        print("Runner paused. `agent_runner.py on` resumes.")
    elif cmd == "on":
        OFF.unlink(missing_ok=True)
        print("Runner resumed.")
    elif cmd == "status":
        cmd_status()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
