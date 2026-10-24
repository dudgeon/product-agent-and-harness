import {readFileSync, writeFileSync} from 'node:fs';
import {dirname, join, resolve} from 'node:path';
import {fileURLToPath} from 'node:url';
const here = dirname(fileURLToPath(import.meta.url)), out = resolve(here, '..');
const svg = (n) => readFileSync(join(out, `${n}.svg`), 'utf8').replace(/width="1080" height="1080"/, 'width="100%" height="100%"');
const LOOKS = [
  ['A', 'Ledger', 'The workspace as a paper ledger: hairline panes, the project’s typed slots on the left, the thread in the middle, provenance and the asks on the right. Reads as a product with screens. The accent is only ever the human’s hand.'],
  ['B', 'Board', 'No chrome. One persistent project card, Sam as the one actor on the left, personas and reviewers hanging off ink lines, the table of work on the right. Closest to the Managed Agents reference grammar; calmer at phone size; less of a “screen”.'],
  ['C', 'Plate', 'The ledger composition printed as a two-colour plate: slate ink on cool paper, halftone washes, the same clay accent. Marks the walkthroughs off from the story’s warm-paper scenes, the way the house style uses a duotone for a mode change.'],
];
const STATES = [['1', 'Start an intent', 'Sam types one line. The project is made with typed slots; Researcher and Dependency Mapper fan out; the provenance panel says what was read and what could not be found. Private to the project; personal sources off.'],
  ['2', 'Shape and classify', 'Shaper interrogates against the shaping standard with sources pre-filled; the completeness meter fills; Risk Advisor lays components against the taxonomy; mitigations become requirements; one cell is new and goes to Alex. Sam accepts the residual risk.'],
  ['3', 'Check, share, resume, ratify, hand off', 'Checker finds three things; Sam fixes two and overrides one with a logged reason. Priya, Jo and Alex sign v4, each seeing only what their access allows. Sam returns from a phone two days later. The hand-off packet goes to engineering or a coding agent.']];
const flow = ['0 · Home: the projects you are in, each with its state glyphs and who is waiting on you', '1 · Start: one line of intent becomes a project with typed slots (intent, evidence, risk, dependency, decision, hand-off), an owner, reviewers, connectors on, personal sources off', '2 · Fan out: Researcher and Dependency Mapper run in their own contexts and report what they read and could not find', '3 · Shape: Shaper interrogates against the versioned shaping standard; the meter fills; the draft spec grows beside the thread', '4 · Classify: Risk Advisor marks the taxonomy grid; mitigations become numbered requirements; off-taxonomy goes to a named person; the human resolves a trade-off and accepts residual risk', '5 · Check: Checker runs the completeness and quote checks; the human fixes or overrides, with reasons logged', '6 · Share and resume: reviewers join the project; the session executes as its owner; viewers are re-checked; the thread is there two days later from any device', '7 · Ratify and hand off: sign-offs against the spec version; the packet goes to engineering or a coding agent; a decision record is filed; the standard gets a proposed revision; the audit timeline shows who typed, who executed, what it cost'];
const steer = ['states the intent', 'answers or redirects the interrogation', 'resolves a trade-off', 'accepts residual risk', 'ratifies with the reviewers', 'approves the hand-off'];
let html = `<title>Helm frames</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,500;0,8..60,600;1,8..60,500&family=Source+Sans+3:wght@400;600&display=swap">
<style>
/* Layout: one column that reads top to bottom; frames in a 3-up grid that stacks at phone width. */
:root{--bg:#f6f4ee;--fg:#24221e;--muted:#6f6a60;--rule:#d9d3c6;--card:#fbfaf6;--accent:#c4673f;--serif:'Source Serif 4',Charter,Georgia,serif;--sans:'Source Sans 3','Avenir Next','Helvetica Neue',sans-serif}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#1d1b18;--fg:#ebe6dc;--muted:#a39d91;--rule:#3a362f;--card:#262320;--accent:#d9825c;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#1d1b18;--fg:#ebe6dc;--muted:#a39d91;--rule:#3a362f;--card:#262320;--accent:#d9825c;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:18px;line-height:1.5;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:24px 60px}
main{max-width:1100px;margin:0 auto}
h1{font-family:var(--serif);font-weight:600;font-size:2.1rem;line-height:1.15;margin:0 0 .4rem;text-wrap:balance}
h2{font-family:var(--serif);font-weight:600;font-size:1.5rem;margin:2.4rem 0 .6rem;text-wrap:balance}
h3{font-family:var(--sans);font-size:1.05rem;font-weight:600;margin:1.4rem 0 .4rem}
p{max-width:68ch;margin:.4rem 0}
.lede{color:var(--muted);max-width:68ch}
.eyebrow{font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-weight:600}
ol,ul{max-width:72ch;padding-left:1.3em}li{margin:.3rem 0}
.look{border-top:1px solid var(--rule);padding-top:1rem;margin-top:1.6rem}
.frames{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:.8rem 0}
@media (max-width:720px){.frames{grid-template-columns:1fr}}
.frame{aspect-ratio:1/1;max-width:100%;border:1px solid var(--rule);border-radius:6px;overflow:hidden;background:#f3f0e8}
.frame svg{display:block;width:100%;height:100%}
.cap{font-size:.9rem;color:var(--muted);margin:.2rem 0 0}
.pick{border:1.5px solid var(--accent);border-radius:10px;padding:14px 18px;margin-top:1.6rem;background:var(--card)}
.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}@media (max-width:720px){.grid2{grid-template-columns:1fr}}
code{font-family:Menlo,monospace;font-size:.9em}
</style>
<main>
<div class="eyebrow">Checkpoint B · the notional prototype</div>
<h1>Helm frames</h1>
<p class="lede">The user flow of the notional workspace, and three looks drawn on the same three key states. Helm is a concept to illustrate the potential, not the answer to the case. Everything here is drawn procedurally (SVG from a small library in <code>frames/src</code>), on the explainers’ restrained house look: warm paper, one ink, hairline drawing, square for phones. The one accent is reserved for the human’s hand: where the person in the product role steers, decides or overrides.</p>
<h2>The flow</h2>
<p>Eight states, one path. The same invented scenario runs through every demo: Sam, a PM, shaping “let finance approvers approve invoices in bulk”; Priya (engineering lead), Jo (designer) and Alex (risk) review.</p>
<ol>${flow.map((x) => `<li>${x}</li>`).join('')}</ol>
<div class="grid2"><div><h3>The personas, fully delegated</h3><ul><li><b>Researcher</b> reads the record and files evidence with quote links (S01, S03, S12)</li><li><b>Dependency Mapper</b> finds the systems, teams and in-flight work the intent touches</li><li><b>Shaper</b> interrogates against the versioned shaping standard and drafts the canonical spec (Action 4; S05 V3)</li><li><b>Risk Advisor</b> classifies against the taxonomy, turns mitigations into requirements, routes novel risk to a person (Intent Shaping doc)</li><li><b>Checker</b> runs the completeness standard and the quote check before any human review (S15)</li></ul></div>
<div><h3>Where the human steers</h3><ul>${steer.map((x) => `<li>${x}</li>`).join('')}</ul><p class="cap">Six points, drawn in the accent. Everything between them runs without the human, and everything they do is attributed.</p></div></div>
<h2>Three looks on the same frames</h2>
<p>Each row is one look; each column is one key state. Tap a frame to open it full size.</p>`;
for (const [k, name, blurb] of LOOKS) {
  html += `<section class="look"><div class="eyebrow">Look ${k}</div><h3 style="margin-top:.2rem;font-family:var(--serif);font-size:1.35rem">${name}</h3><p>${blurb}</p><div class="frames">`;
  for (const [n, title] of STATES) html += `<figure style="margin:0;min-width:0"><div class="frame">${svg(`${k}-s${n}`)}</div><figcaption class="cap">${n} · ${title}</figcaption></figure>`;
  html += `</div></section>`;
}
html += `<h2>Motion grammar, the same in every scene</h2>
<ul><li><b>Agents appear</b> as a hexagon that grows from the human’s mark along an ink line; hollow while working, filled when done; their card rises a few pixels with a short fade when they report.</li>
<li><b>Hand-off between agents</b> is a line that draws itself, with the artifact pill travelling along it; fan-in curves for merges.</li>
<li><b>Reporting</b> fills the slot in the project rail from hollow to filled on the word; counts are cells that fill, never numbers that spin.</li>
<li><b>Steering</b> is the accent: the person mark pulses one ring when a decision is asked; the gate chip is accent-outlined until answered, then filled with the human’s name; an override is a strike-through with a reason pill.</li>
<li><b>Persistence</b> is the frame stepping back (dimmed) and returning; resuming is a phone frame sliding in with the same thread inside it.</li>
<li><b>Sharing</b> is reviewer marks sliding onto the top bar; re-check is an evidence card turning hatched for the viewer who may not see it.</li>
<li><b>Camera</b> is still within a scene except gentle pushes into the table of work; scenes travel across one page, never cut.</li>
<li>Springs, not easing curves (k 9, damping 0.82 for marks, 1 for type); every frame a pure function of time; nothing moves unless the voice asks it to.</li></ul>
<div class="pick"><div class="eyebrow" style="color:var(--accent)">What to pick</div><p><b>Recommendation: A, Ledger.</b> The task asks for a notional application with screens and states, and the ledger reads as one while staying inside the house look. The board (B) is the calmest and would borrow into the ledger’s centre column anyway; the plate (C) is the same composition in a colder key and could instead be used only for the comparison beat (the same job three ways). The pick is in the question in the terminal.</p></div>
</main>`;
writeFileSync(join(out, 'checkpoint-b.html'), html);
console.log('wrote checkpoint-b.html', html.length);
