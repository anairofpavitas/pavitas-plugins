#!/usr/bin/env bun
// Generate 3 candidate slugs of the form <service>-mcp-<word>-<word>-<word>.
// Present them to Pavi and WAIT for him to pick before deploying — never pick
// a slug silently (his standing rule).
//
//   bun Skills/mcp-wrapper-builder/scripts/gen-slugs.ts <service-name>

const WORDS = [
  "amber", "anchor", "arbor", "aspen", "basin", "beacon", "birch", "bramble",
  "brisk", "cedar", "cinder", "cobalt", "copper", "coral", "cove", "crest",
  "drift", "ember", "fable", "fathom", "fern", "flint", "frost", "garnet",
  "glade", "granite", "harbor", "hazel", "heron", "indigo", "ivory", "jasper",
  "kestrel", "lagoon", "lantern", "larch", "lattice", "linen", "marble",
  "meadow", "mica", "moss", "nimbus", "oaken", "onyx", "opal", "orchard",
  "pebble", "pewter", "pollen", "quartz", "quill", "reach", "reef", "ridge",
  "ripple", "roan", "saffron", "sable", "sage", "slate", "sorrel", "spruce",
  "thicket", "thistle", "tidal", "timber", "topaz", "trade", "umber", "velvet",
  "verde", "vellum", "wander", "willow", "wisp", "woven", "yarrow", "zephyr",
];

function pick(): string {
  return WORDS[Math.floor(Math.random() * WORDS.length)];
}

function triple(): string {
  const a = pick();
  let b = pick();
  while (b === a) b = pick();
  let c = pick();
  while (c === a || c === b) c = pick();
  return `${a}-${b}-${c}`;
}

const raw = process.argv[2];
if (!raw) {
  console.error("usage: bun gen-slugs.ts <service-name>");
  process.exit(1);
}

// Normalize the service name: lowercase, strip a trailing "-mcp" if present,
// keep only [a-z0-9-].
const service = raw
  .toLowerCase()
  .replace(/[^a-z0-9-]+/g, "-")
  .replace(/-+/g, "-")
  .replace(/^-|-$/g, "")
  .replace(/-mcp$/, "");

const seen = new Set<string>();
const slugs: string[] = [];
while (slugs.length < 3) {
  const t = triple();
  if (seen.has(t)) continue;
  seen.add(t);
  slugs.push(`${service}-mcp-${t}`);
}

console.log(`\nCandidate slugs for "${service}":\n`);
for (const s of slugs) console.log(`  /${s}`);
console.log(`\nPresent these to Pavi and wait for him to pick before deploying.\n`);
