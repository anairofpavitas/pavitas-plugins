#!/usr/bin/env python3
"""Shared agent log for Pavi's machines (pavitas-core hooks).

Every Claude Code session on every machine:
  - at start, prints Zo's "last 24 hours" briefing (it becomes context for the session), then
    quietly sends Zo any earlier sessions on this machine that never got logged;
  - at end, hands Zo a trimmed copy of the session (prompts, replies, files changed) in the
    background. Zo has Claude Haiku write a short entry and keeps only that entry.

Commands:
  start                 SessionStart hook (reads hook JSON on stdin)
  end                   SessionEnd hook (reads hook JSON on stdin, returns at once)
  sweep [options]       Log sessions that ended without the end hook (also used by Zo's nightly job)
  setup                 Save the Zo agent token and this machine's name, then test the connection
  status                Show configuration and the last few log lines

Files (all in ~/.config/pavitas, created by `setup`):
  zo-agent-token        the token (chmod 600). Never commit it anywhere.
  machine-name          e.g. office-macbook (matches the Activity Journal device names)
  agent-log-state.json  which sessions were already sent
  agent-log.log         what happened, newest at the bottom

Turn it off for one shell or script: export PAVITAS_AGENT_LOG=0
Python 3.9+ standard library only (macOS ships 3.9).
"""
import getpass
import glob
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

BASE = os.environ.get("PAVITAS_ZO_BASE", "https://paviproczko.zo.space/api/context")
CONF = os.path.expanduser(os.environ.get("PAVITAS_CONF_DIR", "~/.config/pavitas"))
TOKEN_FILE = os.environ.get("PAVITAS_AGENT_TOKEN_FILE", os.path.join(CONF, "zo-agent-token"))
MACHINE_FILE = os.path.join(CONF, "machine-name")
STATE_FILE = os.path.join(CONF, "agent-log-state.json")
LOG_FILE = os.path.join(CONF, "agent-log.log")
PROJECTS = os.path.expanduser("~/.claude/projects")

USER_MAX = 1500        # characters kept per prompt
ASSIST_HEAD = 500      # characters kept from the start of each reply
ASSIST_TAIL = 500      # ...and from the end
DIGEST_MAX = 60000     # whole digest; the middle is dropped when longer

SSN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
CARD = re.compile(r"\b\d(?:[ -]?\d){12,18}\b")
SECRETISH = re.compile(r"\b(?:sk|pk|ghp|gho|github_pat|xox[baprs]|AKIA|Bearer|zo_sk|mono_pat|hch)[-_A-Za-z0-9]{12,}\b")
HEX = re.compile(r"\b[a-f0-9]{40,}\b")
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
CMD_NOISE = re.compile(r"<(local-command-caveat|local-command-stdout|local-command-stderr|command-message|command-args)>.*?</\1>", re.S)
EDIT_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}


# ---------- small helpers ----------

def log(msg):
    try:
        os.makedirs(CONF, exist_ok=True)
        if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 200_000:
            os.replace(LOG_FILE, LOG_FILE + ".1")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")
    except OSError:
        pass


def disabled():
    return os.environ.get("PAVITAS_AGENT_LOG", "1") == "0"


def read_token():
    try:
        with open(TOKEN_FILE, encoding="utf-8") as f:
            return f.read().strip() or None
    except OSError:
        return None


def slug(s):
    return re.sub(r"[^a-z0-9._-]+", "-", s.lower()).strip("-") or "unknown"


def machine_name():
    try:
        with open(MACHINE_FILE, encoding="utf-8") as f:
            name = f.read().strip()
            if name:
                return slug(name)
    except OSError:
        pass
    try:
        out = subprocess.run(["scutil", "--get", "ComputerName"], capture_output=True, text=True, timeout=3).stdout.strip()
        if out:
            return slug(out)
    except (OSError, subprocess.SubprocessError):
        pass
    return slug(os.uname().nodename.split(".")[0])


def scrub(s):
    s = SSN.sub("[redacted]", s)
    s = CARD.sub("[redacted]", s)
    s = SECRETISH.sub("[redacted]", s)
    return HEX.sub("[redacted]", s)


def http(method, path, token=None, body=None, query=None, timeout=10):
    url = f"{BASE}/{path}"
    if query:
        url += "?" + urllib.parse.urlencode(query)
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "pavitas-agent-log/1")
    if token:
        req.add_header("X-Agent-Token", token)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode("utf-8", "replace")


def read_hook_input():
    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except (ValueError, OSError):
        return {}


def load_state():
    try:
        with open(STATE_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def save_state(state):
    cutoff = time.time() - 45 * 86400
    state = {k: v for k, v in state.items() if v.get("at", 0) > cutoff}
    os.makedirs(CONF, exist_ok=True)
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f)
    os.replace(tmp, STATE_FILE)


# ---------- reading a transcript ----------

def user_text(msg):
    c = msg.get("content")
    if isinstance(c, str):
        blocks = [c]
    else:
        blocks = [b.get("text", "") for b in (c or []) if isinstance(b, dict) and b.get("type") == "text"]
    if not blocks:
        return ""   # tool results and images only
    t = "\n".join(blocks)
    t = REMINDER.sub("", t)
    t = CMD_NOISE.sub("", t)
    i = t.find("USER QUERY:")          # Zo wraps chat messages in project instructions
    if i >= 0:
        t = t[i + len("USER QUERY:"):]
    elif t.lstrip().startswith("CURRENT PROJECT INSTRUCTIONS"):
        return ""
    t = re.sub(r"<command-name>(.*?)</command-name>", r"(ran \1)", t)
    return t.strip()


def assistant_parts(msg):
    texts, files = [], []
    c = msg.get("content")
    if isinstance(c, str):
        return [c], files
    for b in c or []:
        if not isinstance(b, dict):
            continue
        if b.get("type") == "text" and b.get("text", "").strip():
            texts.append(b["text"].strip())
        elif b.get("type") == "tool_use" and b.get("name") in EDIT_TOOLS:
            p = (b.get("input") or {}).get("file_path") or (b.get("input") or {}).get("notebook_path")
            if p:
                files.append(p)
    return texts, files


def trim_reply(t):
    if len(t) <= ASSIST_HEAD + ASSIST_TAIL + 20:
        return t
    return t[:ASSIST_HEAD] + " … " + t[-ASSIST_TAIL:]


def condense(path):
    """Turn a Claude Code transcript (JSONL) into what Zo needs. Returns None if unreadable."""
    info = {"title": None, "first_ts": None, "last_ts": None, "cwd": None, "branch": None,
            "entrypoint": None, "turns": 0, "first_query": ""}
    lines, files = [], []
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for raw in f:
                try:
                    d = json.loads(raw)
                except ValueError:
                    continue
                if d.get("isSidechain"):
                    continue
                t = d.get("type")
                ts = d.get("timestamp")
                if ts:
                    info["first_ts"] = info["first_ts"] or ts
                    info["last_ts"] = ts
                info["cwd"] = info["cwd"] or d.get("cwd")
                info["branch"] = info["branch"] or d.get("gitBranch")
                info["entrypoint"] = info["entrypoint"] or d.get("entrypoint")
                if t == "ai-title" and d.get("aiTitle"):
                    info["title"] = d["aiTitle"]
                elif t == "user" and not d.get("isMeta"):
                    q = user_text(d.get("message") or {})
                    if q:
                        info["turns"] += 1
                        info["first_query"] = info["first_query"] or q[:200]
                        lines.append("USER: " + q[:USER_MAX])
                elif t == "assistant":
                    texts, fs = assistant_parts(d.get("message") or {})
                    files.extend(fs)
                    for x in texts:
                        lines.append("ASSISTANT: " + trim_reply(x))
    except OSError:
        return None
    digest = "\n".join(lines)
    if len(digest) > DIGEST_MAX:
        digest = digest[: DIGEST_MAX // 4] + "\n[… middle of the session left out …]\n" + digest[-(DIGEST_MAX * 3 // 4):]
    seen, uniq = set(), []
    for p in files:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    info["digest"] = scrub(digest)
    info["files"] = uniq[:40]
    return info


def project_name(cwd):
    if not cwd:
        return None
    try:
        top = subprocess.run(["git", "-C", cwd, "rev-parse", "--show-toplevel"], capture_output=True, text=True, timeout=3).stdout.strip()
        if top:
            return os.path.basename(top)
    except (OSError, subprocess.SubprocessError):
        pass
    return os.path.basename(cwd.rstrip("/")) or None


def send_session(token, machine, agent, session_id, path, reason=None):
    info = condense(path)
    if info is None:
        log(f"skip {session_id[:8]}: transcript unreadable")
        return False
    if info["turns"] < 1:
        log(f"skip {session_id[:8]}: no prompts")
        return True
    now = datetime.now(timezone.utc).isoformat()
    body = {
        "machine": machine, "agent": agent, "session_id": session_id,
        "started_at": info["first_ts"] or now, "ended_at": info["last_ts"] or now,
        "cwd": info["cwd"], "project": project_name(info["cwd"]), "git_branch": info["branch"],
        "user_turns": info["turns"], "files_changed": info["files"], "digest": info["digest"],
        "title_hint": info["title"], "reason": reason,
    }
    try:
        status, text = http("POST", "agent-session", token=token, body=body, timeout=120)
        log(f"sent {session_id[:8]} ({info['turns']} prompts, {len(info['digest'])} chars): {status} {text[:160]}")
        return 200 <= status < 300
    except urllib.error.HTTPError as e:
        log(f"send {session_id[:8]} failed: HTTP {e.code} {e.read()[:200]!r}")
    except (urllib.error.URLError, OSError) as e:
        log(f"send {session_id[:8]} failed: {e}")
    return False


def mark_sent(session_id, path):
    state = load_state()
    try:
        state[session_id] = {"mtime": os.path.getmtime(path), "at": time.time()}
    except OSError:
        return
    save_state(state)


# ---------- commands ----------

def ping(event, has_token):
    try:
        http("POST", "agent-ping", body={"event": event, "entrypoint": os.environ.get("CLAUDE_CODE_ENTRYPOINT", ""),
                                         "remote": os.environ.get("CLAUDE_CODE_REMOTE", ""), "has_token": has_token}, timeout=2)
    except Exception:
        pass


def cmd_start():
    hook = read_hook_input()
    if disabled():
        return
    token = read_token()
    if not token:
        if os.environ.get("CLAUDE_CODE_REMOTE") == "true":
            # Cloud session (Cowork, Claude Code on the web): no token here by design. One line so it's
            # visible that the hook ran; the Zo briefing comes through the Zo connector instead.
            print(f"(pavitas-core agent-log hook ran in a cloud session [{os.environ.get('CLAUDE_CODE_ENTRYPOINT', '?')}]; "
                  "no Zo token here, so no briefing. Use the Zo connector's `now` command if the briefing is needed.)")
        else:
            print("(Zo agent log isn't set up on this machine yet. To set it up: "
                  "python3 ~/.claude/plugins/marketplaces/pavitas-plugins/pavitas-core/hooks/agent_log.py setup)")
        ping("start", False)   # tells Zo a hook ran somewhere with no token; sends nothing else
        return
    machine = machine_name()
    try:
        status, text = http("GET", "now", token=token, timeout=6,
                            query={"machine": machine, "agent": "claude-code", "exclude": hook.get("session_id", "")})
        if status == 200 and text.strip():
            print(text)
    except Exception as e:
        log(f"briefing failed: {e}")
    # Catch up on sessions that closed without the end hook. Detached, so start-up isn't slowed.
    try:
        os.makedirs(CONF, exist_ok=True)
        lf = open(LOG_FILE, "a")
        subprocess.Popen([sys.executable, os.path.abspath(__file__), "sweep", "--skip", hook.get("session_id", "")],
                         stdin=subprocess.DEVNULL, stdout=lf, stderr=lf, start_new_session=True, close_fds=True)
    except OSError as e:
        log(f"sweep spawn failed: {e}")


def cmd_end():
    hook = read_hook_input()
    if disabled():
        return
    token = read_token()
    if not token:
        ping("end", False)
        return
    session_id, path = hook.get("session_id"), hook.get("transcript_path")
    if not session_id or not path:
        return
    # Return to Claude Code at once (SessionEnd has a 1.5-second budget); finish in a detached child.
    if os.fork() > 0:
        return
    os.setsid()
    devnull = os.open(os.devnull, os.O_RDWR)
    for fd in (0, 1, 2):
        os.dup2(devnull, fd)
    time.sleep(2)   # the transcript is written asynchronously; let the last lines land
    if send_session(token, machine_name(), "claude-code", session_id, path, hook.get("reason")):
        mark_sent(session_id, path)
    os._exit(0)


def arg(argv, flag, default=None):
    if flag in argv:
        i = argv.index(flag)
        if i + 1 < len(argv):
            return argv[i + 1]
    return default


def cmd_sweep(argv):
    if disabled():
        return
    token = read_token()
    if not token:
        return
    directory = arg(argv, "--dir")
    machine = slug(arg(argv, "--machine", "") or machine_name())
    agent = arg(argv, "--agent", "claude-code")
    days = float(arg(argv, "--days", "3"))
    idle = float(arg(argv, "--idle-minutes", "30")) * 60
    limit = int(arg(argv, "--limit", "20"))
    skip = arg(argv, "--skip", "")
    include_sdk = "--include-sdk" in argv
    prefixes = []
    pf = arg(argv, "--skip-prefixes")
    if pf and os.path.exists(pf):
        prefixes = [l.strip()[:60] for l in open(pf, encoding="utf-8") if l.strip()]
    prefixes += [p for p in (arg(argv, "--skip-prefix-also", "") or "").split("||") if p]

    pattern = os.path.join(directory, "*.jsonl") if directory else os.path.join(PROJECTS, "*", "*.jsonl")
    now = time.time()
    state = load_state()
    candidates = []
    for f in glob.glob(pattern):
        try:
            m = os.path.getmtime(f)
        except OSError:
            continue
        sid = os.path.splitext(os.path.basename(f))[0]
        if sid == skip or now - m > days * 86400 or now - m < idle:
            continue
        if sid in state and state[sid].get("mtime", 0) >= m:
            continue
        candidates.append((m, sid, f))
    candidates.sort()
    sent = skipped = 0
    for m, sid, f in candidates:
        if sent >= limit:
            break
        info = condense(f)
        if info is None:
            continue
        entry = info.get("entrypoint") or ""
        automated = (entry.startswith("sdk") and not include_sdk) or \
            any(info["first_query"].startswith(p) for p in prefixes)
        if automated or info["turns"] < 1:
            state[sid] = {"mtime": m, "at": now, "skipped": True}
            skipped += 1
            continue
        if send_session(token, machine, agent, sid, f, "sweep"):
            state[sid] = {"mtime": m, "at": time.time()}
            sent += 1
    save_state(state)
    if sent or skipped:
        log(f"sweep {machine}: sent {sent}, skipped {skipped}, {max(0, len(candidates) - sent - skipped)} left for next time")


def cmd_setup():
    os.makedirs(CONF, exist_ok=True)
    os.chmod(CONF, 0o700)
    print("Zo agent log setup. Paste the agent token (it won't show as you paste), then press Return.")
    tok = getpass.getpass("Token: ").strip()
    if not re.fullmatch(r"[A-Za-z0-9]{32,128}", tok):
        sys.exit("That doesn't look like the token (expected a long string of letters and numbers). Nothing saved.")
    suggested = machine_name()
    name = input(f"Name for this machine [{suggested}] (office-macbook / studio-macbook / zo): ").strip() or suggested
    old = os.umask(0o077)
    try:
        with open(TOKEN_FILE, "w", encoding="utf-8") as f:
            f.write(tok + "\n")
        with open(MACHINE_FILE, "w", encoding="utf-8") as f:
            f.write(slug(name) + "\n")
    finally:
        os.umask(old)
    os.chmod(TOKEN_FILE, 0o600)
    try:
        status, text = http("GET", "now", token=tok, query={"machine": slug(name), "agent": "setup"}, timeout=10)
        print(f"\nConnected (HTTP {status}). First lines of the briefing:\n" + "\n".join(text.splitlines()[:4]))
    except urllib.error.HTTPError as e:
        sys.exit(f"Saved, but Zo refused the token (HTTP {e.code}). Check you copied all of it and run setup again.")
    except Exception as e:
        sys.exit(f"Saved, but couldn't reach Zo: {e}")


def cmd_status():
    tok = read_token()
    print(f"token file:   {TOKEN_FILE} ({'present' if tok else 'MISSING — run setup'})")
    print(f"machine name: {machine_name()}")
    print(f"disabled:     {disabled()}")
    print(f"sessions recorded in state: {len(load_state())}")
    if tok:
        try:
            status, _ = http("GET", "now", token=tok, query={"machine": machine_name(), "agent": "status"}, timeout=10)
            print(f"Zo reachable: HTTP {status}")
        except Exception as e:
            print(f"Zo reachable: NO ({e})")
    if os.path.exists(LOG_FILE):
        print("\nlast log lines:")
        with open(LOG_FILE, encoding="utf-8", errors="replace") as f:
            for line in f.readlines()[-8:]:
                print("  " + line.rstrip())


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        if cmd == "start":
            cmd_start()
        elif cmd == "end":
            cmd_end()
        elif cmd == "sweep":
            cmd_sweep(sys.argv[2:])
        elif cmd == "setup":
            cmd_setup()
        elif cmd == "status":
            cmd_status()
        else:
            print(__doc__)
    except Exception as e:   # a hook must never break a session
        log(f"{cmd} crashed: {e!r}")
    sys.exit(0)


if __name__ == "__main__":
    main()
