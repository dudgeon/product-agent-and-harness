// Three key states of Helm, drawn in two layouts (ledger: a paper workspace with hairline panes; board: one persistent
// project card with agents hanging off the human, no chrome) and themed by lib.THEMES. Same scenario throughout: Sam (PM)
// shapes "Let finance approvers approve invoices in bulk"; Priya (engineering), Jo (design), Alex (risk) review.
import {S, f, text, rect, line, agent, person, glyph, lines, pill, meter, phone, wash} from './lib.mjs';

const SLOTS = ['Intent', 'Evidence', 'Dependencies', 'Risks', 'Decisions', 'Hand-off'];
const STATES = {
  1: {title: 'Start an intent', slots: ['done', 'working', 'working', 'idle', 'idle', 'idle'], counts: ['', '6', '', '', '', ''], members: ['S'], day: 'Day 1'},
  2: {title: 'Shape and classify', slots: ['done', 'done', 'done', 'working', 'needs', 'idle'], counts: ['', '6', '4', '2', '', ''], members: ['S'], day: 'Day 1'},
  3: {title: 'Check, share, ratify, hand off', slots: ['done', 'done', 'done', 'done', 'done', 'working'], counts: ['v4', '6', '4', '3', '3', ''], members: ['S', 'P', 'J', 'A'], day: 'Day 3'},
};

// Shared pieces -----------------------------------------------------------------------------------------------------------
const t = (T) => (x, y, s, o = {}) => text(x, y, s, {...o, T});
const card = (T, x, y, w, h, o = {}) => rect(x, y, w, h, {fill: T.paper, stroke: o.accent ? T.accent : (o.faint ? T.hair : T.ink), sw: o.accent ? 2.4 : 1.8, r: 10, ...o});

/** A thread card from an agent or the human: a mark, a name, a title line and body lines. */
function threadCard(T, id, x, y, w, h, who, name, title, body, o = {}) {
  const tx = t(T);
  let s = card(T, x, y, w, h, {accent: o.accent, faint: o.faint});
  s += who === 'human' ? person(T, x + 34, y + 54) : agent(T, x + 34, y + 36, who, {done: o.done, r: 19});
  s += tx(x + 70, y + 34, name, {size: 20, color: T.muted, weight: 600});
  s += tx(x + 70, y + 64, title, {size: 24, weight: 600});
  if (typeof body === 'number') s += lines(T, x + 70, y + 92, w - 100, body, {dy: 15});
  else body.forEach((b, i) => { s += tx(x + 70, y + 96 + i * 30, b, {size: 20, color: T.muted}); });
  return s;
}

/** The provenance list: what was read (tick) and what could not be found (dash, in the accent, because it asks you). */
function provenance(T, x, y, w) {
  const tx = t(T);
  let s = tx(x, y, 'What I read', {size: 18, color: T.muted, weight: 600, ls: 1.2});
  const rows = [['Tickets', '41', true], ['Customer calls', '6', true], ['Prior specs', '2', true], ['Approval policy', '1', true], ['Pricing constraints', 'not found', false]];
  rows.forEach(([n, c, ok], i) => {
    const yy = y + 36 + i * 38;
    s += ok ? `<path d="M${f(x + 2)} ${f(yy - 6)}l6 6l12 -13" fill="none" stroke="${T.ink}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>` : `<path d="M${f(x)} ${f(yy - 7)}H${f(x + 20)}" stroke="${T.accent}" stroke-width="2.6" stroke-linecap="round"/>`;
    s += tx(x + 34, yy, n, {size: 21, color: ok ? T.ink : T.accent});
    if (ok) s += tx(x + w, yy, c, {size: 19, color: T.muted, anchor: 'end', font: 'mono'});
  });
  s += tx(x, y + 36 + rows.length * 38 + 8, 'Not found. Who owns', {size: 19, color: T.accent, italic: true});
  s += tx(x, y + 36 + rows.length * 38 + 34, 'pricing constraints?', {size: 19, color: T.accent, italic: true});
  return s;
}

/** The risk grid: components × risk categories; filled = applies, hatched = off-taxonomy (routed to a person). */
function riskGrid(T, id, x, y, o = {}) {
  const tx = t(T), cols = ['Fraud', 'Access', 'Audit', 'Data', 'Ops'], rows = ['Bulk action', 'Approver roles', 'Limits', 'Notify'];
  const cw = o.cw ?? 54, rh = o.rh ?? 40, lx = o.lx ?? 150;
  let s = '';
  cols.forEach((c, j) => { s += tx(x + lx + j * cw + cw / 2, y - 8, c, {size: 16, color: T.muted, anchor: 'middle', weight: 600}); });
  const on = {'0,0': 'fill', '0,2': 'fill', '1,1': 'fill', '2,3': 'hatch', '3,4': 'none'};
  rows.forEach((r, i) => {
    s += tx(x, y + i * rh + rh * 0.66, r, {size: 18});
    cols.forEach((_, j) => {
      const k = on[`${i},${j}`], cx = x + lx + j * cw + 5, cy = y + i * rh + 5;
      s += `<rect x="${f(cx)}" y="${f(cy)}" width="${cw - 10}" height="${rh - 10}" rx="5" fill="${k === 'fill' ? T.ink : k === 'hatch' ? `url(#${id}-hatch)` : 'none'}" stroke="${k === 'hatch' ? T.accent : T.faint}" stroke-width="1.6"/>`;
    });
  });
  s += tx(x + lx, y + rows.length * rh + 22, 'filled: applies · hatched: new, routed to Alex', {size: 15, color: T.muted});
  return s;
}

/** The spec page: numbered requirements, mitigations arriving as new numbered lines, one OPEN marker. */
function specPage(T, x, y, w, h0, o = {}) {
  const tx = t(T), fold = 26, h = Math.max(h0, 88 + ((o.n ?? 7) + (o.open ?? 2)) * 24 + 6);
  let s = `<path d="M${f(x)} ${f(y)}H${f(x + w - fold)}L${f(x + w)} ${f(y + fold)}V${f(y + h)}H${f(x)}Z" fill="${T.paper}" stroke="${T.ink}" stroke-width="2"/><path d="M${f(x + w - fold)} ${f(y)}V${f(y + fold)}H${f(x + w)}" fill="none" stroke="${T.ink}" stroke-width="2"/>`;
  s += tx(x + 18, y + 34, o.title ?? 'Intent spec', {size: 19, weight: 600});
  s += tx(x + 18, y + 58, o.version ?? 'v2 · draft', {size: 14, color: T.muted, font: 'mono'});
  const n = o.n ?? 7, mit = o.mitigations ?? 0, open = o.open ?? 2;
  for (let i = 0; i < n; i++) {
    const yy = y + 88 + i * 24, isMit = i >= n - mit;
    s += tx(x + 18, yy, `R${i + 1}`, {size: 14, font: 'mono', color: isMit ? T.accent : T.muted});
    s += `<path d="M${f(x + 52)} ${f(yy - 5)}H${f(x + w - 24 - (i % 3) * 22)}" stroke="${isMit ? T.accent : T.faint}" stroke-width="3" stroke-linecap="round"/>`;
  }
  for (let i = 0; i < open; i++) s += pill(T, x + 52, y + 88 + (n + i) * 24 - 16, 'OPEN', {size: 12, tone: 'accent'});
  return s;
}

/** Top bar (ledger): project, visibility, members, day, cost. */
function topBar(T, id, st) {
  const tx = t(T), st_ = STATES[st];
  let s = `<path d="M0 72H${S}" stroke="${T.hair}" stroke-width="2"/>`;
  s += tx(40, 46, 'Helm', {size: 24, weight: 700, font: 'serif'});
  s += tx(126, 46, 'Bulk invoice approval', {size: 24, weight: 600});
  s += pill(T, 400, 24, 'private to project', {size: 14, tone: 'faint', font: 'sans'});
  st_.members.forEach((m, i) => { s += m === 'S' ? person(T, 628 + i * 40, 56, {s: 0.72}) : `<circle cx="${f(628 + i * 40)}" cy="${f(44)}" r="15" fill="${T.paper}" stroke="${T.ink}" stroke-width="2"/>` + tx(628 + i * 40, 50, m, {size: 15, anchor: 'middle', weight: 600}); });
  s += tx(820, 46, st_.day, {size: 18, color: T.muted, font: 'mono'});
  s += meter(T, 900, 34, 6, st === 1 ? 1 : st === 2 ? 3 : 4, {cw: 18, g: 4, h: 12});
  s += tx(1040, 46, '$', {size: 16, color: T.muted, anchor: 'end', font: 'mono'});
  return s;
}

/** Left rail (ledger): the project's typed artifact slots with state glyphs and counts. */
function rail(T, st) {
  const tx = t(T), st_ = STATES[st];
  let s = `<path d="M250 72V${S}" stroke="${T.hair}" stroke-width="2"/>`;
  s += tx(40, 118, 'Project', {size: 16, color: T.muted, weight: 600, ls: 1.4});
  SLOTS.forEach((n, i) => {
    const y = 160 + i * 52, state = st_.slots[i];
    s += glyph(T, 52, y - 8, state, {r: 7});
    s += tx(76, y, n, {size: 21, color: state === 'idle' ? T.muted : T.ink, weight: state === 'needs' ? 600 : 500});
    if (st_.counts[i]) s += tx(236, y, st_.counts[i], {size: 15, color: T.muted, anchor: 'end', font: 'mono'});
  });
  s += `<path d="M40 500H214" stroke="${T.hair}" stroke-width="2"/>`;
  s += tx(40, 538, 'Personas', {size: 16, color: T.muted, weight: 600, ls: 1.4});
  const per = [['R', 'Researcher'], ['D', 'Dependencies'], ['S', 'Shaper'], ['A', 'Risk advisor'], ['C', 'Checker']];
  const doneBy = {1: [], 2: ['R', 'D'], 3: ['R', 'D', 'S', 'A', 'C']};
  const activeBy = {1: ['R', 'D'], 2: ['S', 'A'], 3: []};
  per.forEach(([l, n], i) => {
    const y = 586 + i * 50, d = doneBy[st].includes(l), a = activeBy[st].includes(l);
    s += agent(T, 56, y - 8, l, {r: 15, done: d, op: d || a ? 1 : 0.4});
    s += tx(86, y, n, {size: 21, color: d || a ? T.ink : T.muted});
  });
  s += `<path d="M40 860H214" stroke="${T.hair}" stroke-width="2"/>`;
  s += tx(40, 898, 'Sources', {size: 16, color: T.muted, weight: 600, ls: 1.4});
  s += tx(40, 936, 'Tickets · Calls · Specs', {size: 18});
  s += tx(40, 968, 'Personal sources', {size: 18, color: T.muted});
  s += pill(T, 176, 950, 'off', {size: 13, tone: 'faint', font: 'sans'});
  s += tx(40, 1016, 'runs as Sam', {size: 17, color: T.muted, font: 'mono'});
  return s;
}

// Ledger layout -----------------------------------------------------------------------------------------------------------
export function ledger(T, id, st) {
  const tx = t(T);
  let s = topBar(T, id, st) + rail(T, st);
  s += `<path d="M780 72V${S}" stroke="${T.hair}" stroke-width="2"/>`;
  const cx = 290, cw = 460;
  if (st === 1) {
    s += threadCard(T, id, cx, 110, cw, 130, 'human', 'Sam · PM', 'Approve invoices in bulk, for finance.', ['Finance approvers act on many invoices at once.'], {accent: true});
    // Fan-out from Sam to Researcher and Dependency Mapper.
    s += line(`M${cx + 34} 240C${cx + 34} 270 ${cx + 60} 262 ${cx + 60} 282`, {stroke: T.ink, arrow: `${id}-ar`});
    s += line(`M${cx + 34} 240C${cx + 34} 300 ${cx + 60} 440 ${cx + 60} 462`, {stroke: T.ink, arrow: `${id}-ar`});
    s += threadCard(T, id, cx, 286, cw, 150, 'R', 'Researcher', 'Reading the record.', ['41 tickets · 6 calls · 2 prior specs', 'Filing evidence notes with quote links.']);
    s += threadCard(T, id, cx, 466, cw, 150, 'D', 'Dependency mapper', 'Mapping what this touches.', ['Approvals · Ledger API · Notifications', 'Owners from the service catalogue.']);
    s += wash(T, id, cx, 650, cw, 150, {});
    s += tx(cx + 24, 690, 'The project was made from one line.', {size: 20, color: T.muted});
    s += tx(cx + 24, 722, 'Owner: Sam. Reviewers: not yet named.', {size: 20, color: T.muted});
    s += tx(cx + 24, 754, 'Typed slots wait on the left; agents fill them.', {size: 20, color: T.muted});
    s += tx(cx + 24, 786, 'Nothing here is visible outside the project.', {size: 20, color: T.muted});
    s += provenance(T, 820, 118, 220);
    s += tx(820, 420, 'Connectors', {size: 16, color: T.muted, weight: 600, ls: 1.4});
    ['Tickets', 'Calls', 'Specs', 'Catalogue'].forEach((c, i) => { s += pill(T, 820 + (i % 2) * 120, 440 + Math.floor(i / 2) * 44, c, {size: 15, font: 'sans'}); });
  }
  if (st === 2) {
    s += threadCard(T, id, cx, 110, cw, 176, 'S', 'Shaper', 'Which approver roles may act in bulk?', ['From tickets #4412, #4480: finance leads only.']);
    s += pill(T, cx + 70, 236, 'confirm', {size: 15, tone: 'accent', font: 'sans'});
    s += pill(T, cx + 190, 236, 'correct', {size: 15, tone: 'faint', font: 'sans'});
    s += tx(cx + 70, 320, 'Completeness', {size: 17, color: T.muted, weight: 600});
    s += meter(T, cx + 70, 334, 12, 9, {cw: 16, g: 4, h: 14});
    s += tx(cx + 70, 378, '9 of 12 against the shaping standard', {size: 16, color: T.muted});
    s += specPage(T, cx + 316, 300, 144, 230, {n: 7, mitigations: 2, open: 1, version: 'v2 · draft'});
    s += threadCard(T, id, cx, 604, cw, 330, 'A', 'Risk advisor', 'Two risks apply. One is new.', []);
    s += riskGrid(T, id, cx + 24, 714, {cw: 52, rh: 38, lx: 140});
    s += tx(cx + 24, 964, 'Mitigations R6, R7 added to the spec.', {size: 18, color: T.muted});
    // The right panel: what asks you.
    s += tx(820, 118, 'Asks you', {size: 16, color: T.accent, weight: 600, ls: 1.4});
    s += card(T, 820, 134, 220, 196, {accent: true});
    s += person(T, 850, 188, {ring: true});
    s += tx(896, 166, 'Accept', {size: 18, weight: 600}); s += tx(896, 190, 'residual risk', {size: 18, weight: 600});
    s += tx(836, 236, 'Bulk limit 50 per run,', {size: 18, color: T.muted});
    s += tx(836, 262, 'or approver workload.', {size: 18, color: T.muted});
    s += pill(T, 836, 284, 'accept', {size: 15, tone: 'accent', filled: true, font: 'sans'});
    s += pill(T, 926, 284, 'change', {size: 15, tone: 'faint', font: 'sans'});
    s += tx(820, 380, 'Routed to a person', {size: 16, color: T.muted, weight: 600, ls: 1.4});
    s += card(T, 820, 396, 220, 92, {faint: true});
    s += `<rect x="836" y="414" width="26" height="26" rx="5" fill="url(#${id}-hatch)" stroke="${T.accent}" stroke-width="1.6"/>`;
    s += tx(874, 432, 'Limits × Data', {size: 18});
    s += tx(836, 470, 'new → Alex (risk)', {size: 17, color: T.muted, font: 'mono'});
    s += tx(820, 540, 'Decisions so far', {size: 16, color: T.muted, weight: 600, ls: 1.4});
    ['Roles: finance leads', 'Scope: under policy'].forEach((d, i) => { s += glyph(T, 828, 574 + i * 34 - 7, 'done', {r: 5}); s += tx(846, 574 + i * 34, d, {size: 17}); });
  }
  if (st === 3) {
    s += threadCard(T, id, cx, 110, cw, 206, 'C', 'Checker', 'Three findings against the standard.', [], {done: true});
    const fnd = [['R3 cites no source', 'fixed'], ['R5 and R6 conflict on limits', 'fixed'], ['No rollback requirement', 'overridden']];
    fnd.forEach(([n, r], i) => {
      const y = 200 + i * 34;
      s += glyph(T, cx + 78, y - 7, r === 'overridden' ? 'needs' : 'done', {r: 6});
      s += tx(cx + 96, y, n, {size: 18, color: r === 'overridden' ? T.ink : T.muted});
      if (r === 'overridden') { s += `<path d="M${f(cx + 94)} ${f(y - 6)}H${f(cx + 300)}" stroke="${T.ink}" stroke-width="2" stroke-linecap="round"/>`; s += pill(T, cx + 318, y - 18, 'Sam: out of scope', {size: 13, tone: 'accent', font: 'sans'}); }
    });
    s += tx(cx, 360, 'Sign-offs on v4', {size: 16, color: T.muted, weight: 600, ls: 1.4});
    [['P', 'Priya', 'feasibility'], ['J', 'Jo', 'usability'], ['A', 'Alex', 'risk']].forEach(([l, n, r], i) => {
      const y = 396 + i * 40;
      s += `<circle cx="${f(cx + 14)}" cy="${f(y - 8)}" r="14" fill="${T.paper}" stroke="${T.ink}" stroke-width="2"/>` + tx(cx + 14, y - 2, l, {size: 14, anchor: 'middle', weight: 600});
      s += tx(cx + 40, y, `${n} · ${r}`, {size: 19});
      s += `<path d="M${f(cx + 300)} ${f(y - 8)}l6 6l12 -13" fill="none" stroke="${T.ink}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>`;
      s += tx(cx + 340, y, 'v4', {size: 15, color: T.muted, font: 'mono'});
    });
    s += person(T, cx + 14, 536, {s: 0.8}); s += tx(cx + 40, 528, 'Sam · ratified', {size: 19, weight: 600});
    s += pill(T, cx + 200, 508, 'ratify', {size: 15, tone: 'accent', filled: true, font: 'sans'});
    // Hand-off packet.
    s += card(T, cx, 580, cw, 190, {});
    s += tx(cx + 24, 616, 'Hand-off packet', {size: 20, weight: 600});
    s += tx(cx + 24, 648, 'spec v4 · 6 evidence · 3 decisions · 4 dependencies', {size: 17, color: T.muted});
    { let px = cx + 24; for (const [n, c] of [['spec', 'v4'], ['evidence', '6'], ['decisions', '3'], ['deps', '4'], ['tickets', '5']]) { const w = `${n} ${c}`.length * 12 * 0.62 + 24; s += pill(T, px, 672, `${n} ${c}`, {size: 12, w}); px += w + 8; } }
    s += line(`M${cx + 24} 736H${cx + 180}`, {stroke: T.ink, arrow: `${id}-ar`});
    s += tx(cx + 196, 742, 'to engineering or a coding agent', {size: 17, color: T.muted});
    s += tx(cx + 24, 800, 'Decision record filed. The shaping standard', {size: 18, color: T.muted});
    s += tx(cx + 24, 828, 'has a proposed revision from this run.', {size: 18, color: T.muted});
    s += pill(T, cx + 24, 848, 'approve hand-off', {size: 15, tone: 'accent', font: 'sans'});
    // Right: identity badge, viewer re-check, audit, phone.
    s += tx(820, 118, 'Identity', {size: 16, color: T.muted, weight: 600, ls: 1.4});
    s += tx(820, 150, 'runs as Sam', {size: 18, font: 'mono'});
    s += tx(820, 178, 'viewers re-checked', {size: 18, font: 'mono'});
    s += card(T, 820, 200, 220, 72, {faint: true});
    s += `<rect x="836" y="216" width="188" height="40" rx="6" fill="url(#${id}-grey)" stroke="${T.faint}" stroke-width="1.4"/>`;
    s += tx(930, 242, 'not visible to Alex', {size: 15, color: T.muted, anchor: 'middle'});
    s += tx(820, 310, 'Audit', {size: 16, color: T.muted, weight: 600, ls: 1.4});
    [['allow', 'read tickets · R'], ['ask', 'accept risk · Sam'], ['allow', 'override 3 · Sam'], ['deny', 'publish transcript'], ['allow', 'sign off v4 · Alex']].forEach(([k, w], i) => {
      const y = 334 + i * 44;
      s += pill(T, 820, y, k, {size: 13, tone: k === 'ask' ? 'accent' : 'faint', w: 64});
      s += tx(892, y + 20, w, {size: 15, font: 'mono'});
    });
    s += tx(820, 600, '2 days later, from a phone', {size: 17, color: T.muted, italic: true});
    s += phone(T, 860, 620, 180, 380, '');
    s += tx(950, 680, 'Bulk invoice', {size: 15, anchor: 'middle', weight: 600});
    s += lines(T, 884, 706, 130, 6, {dy: 16});
    s += agent(T, 896, 830, 'C', {r: 12, done: true}); s += lines(T, 918, 826, 96, 2, {dy: 14});
    s += person(T, 896, 900, {s: 0.6}); s += lines(T, 918, 890, 96, 2, {dy: 14});
    s += pill(T, 884, 940, 'ratify', {size: 12, tone: 'accent', filled: true, font: 'sans'});
  }
  return s;
}

// Board layout ------------------------------------------------------------------------------------------------------------
export function board(T, id, st) {
  const tx = t(T), st_ = STATES[st];
  let s = '';
  // The persistent project card, top left: title, slots as glyphs, members.
  s += card(T, 60, 60, 420, 150, {});
  s += tx(84, 100, 'Bulk invoice approval', {size: 24, weight: 600, font: 'serif'});
  s += tx(84, 130, `private to project · ${st_.day}`, {size: 17, color: T.muted, font: 'mono'});
  SLOTS.forEach((n, i) => { s += glyph(T, 92 + i * 64, 166, st_.slots[i], {r: 7}); s += tx(92 + i * 64, 196, n.slice(0, 5), {size: 13, color: T.muted, anchor: 'middle'}); });
  st_.members.forEach((m, i) => { const mx = 456 - i * 34; s += m === 'S' ? person(T, mx, 136, {s: 0.72}) : `<circle cx="${f(mx)}" cy="${f(124)}" r="15" fill="${T.paper}" stroke="${T.ink}" stroke-width="2"/>` + tx(mx, 130, m, {size: 15, anchor: 'middle', weight: 600}); });
  // The human, left, one actor for the whole film.
  const hx = 120, hy = 520;
  s += person(T, hx, hy, {s: 1.5, ring: st === 2});
  s += tx(hx, hy + 44, 'Sam', {size: 20, anchor: 'middle', weight: 600});
  s += tx(hx, hy + 70, 'product', {size: 16, anchor: 'middle', color: T.muted});
  const fan = (ax, ay, letter, name, done) => line(`M${hx + 40} ${hy - 20}C${(hx + ax) / 2} ${hy - 20} ${(hx + ax) / 2} ${ay} ${ax - 30} ${ay}`, {stroke: T.ink, arrow: `${id}-ar`}) + agent(T, ax, ay, letter, {r: 24, done}) + tx(ax, ay + 50, name, {size: 16, anchor: 'middle', color: T.muted});
  if (st === 1) {
    s += tx(60, 290, 'Let finance approvers approve invoices in bulk.', {size: 28, font: 'serif', italic: true});
    s += fan(330, 400, 'R', 'Researcher', false);
    s += fan(330, 640, 'D', 'Dependencies', false);
    s += line(`M360 400H560`, {stroke: T.faint, sw: 2, dash: '6 6'}); s += line(`M360 640H560`, {stroke: T.faint, sw: 2, dash: '6 6'});
    for (let i = 0; i < 6; i++) { const x = 600 + (i % 3) * 64, y = 350 + Math.floor(i / 3) * 90; s += `<path d="M${x} ${y}H${x + 44}L${x + 54} ${y + 10}V${y + 68}H${x}Z" fill="${T.paper}" stroke="${T.ink}" stroke-width="1.8"/>` + lines(T, x + 8, y + 22, 36, 3, {dy: 12, sw: 2.4}); }
    s += tx(600, 470, 'evidence · quote links', {size: 16, color: T.muted});
    [['Approvals service', 'team payments'], ['Ledger API', 'team core'], ['Notifications', 'team comms']].forEach(([n, o], i) => { s += rect(600, 600 + i * 50, 300, 38, {stroke: T.ink, sw: 1.8, r: 6}); s += tx(614, 626 + i * 50, n, {size: 17}); s += tx(888, 626 + i * 50, o, {size: 14, color: T.muted, anchor: 'end', font: 'mono'}); });
    s += provenance(T, 600, 800, 300);
    s += tx(60, 1000, 'Personal sources: off · nothing visible outside the project', {size: 17, color: T.muted});
  }
  if (st === 2) {
    s += fan(330, 400, 'S', 'Shaper', false);
    s += fan(330, 700, 'A', 'Risk advisor', false);
    s += line(`M360 400H560`, {stroke: T.faint, sw: 2, dash: '6 6'});
    s += tx(600, 300, 'Which approver roles', {size: 24, weight: 600}); s += tx(600, 330, 'may act in bulk?', {size: 24, weight: 600});
    s += tx(600, 362, 'from tickets #4412, #4480:', {size: 16, color: T.muted, font: 'mono'}); s += tx(600, 384, 'finance leads only', {size: 16, color: T.muted, font: 'mono'});
    s += pill(T, 600, 400, 'confirm', {size: 15, tone: 'accent', font: 'sans'}); s += pill(T, 720, 400, 'correct', {size: 15, tone: 'faint', font: 'sans'});
    s += tx(600, 480, 'Completeness · 9 of 12', {size: 16, color: T.muted, weight: 600, ls: 1.2});
    s += meter(T, 600, 492, 12, 9, {cw: 18, g: 4, h: 14});
    s += specPage(T, 880, 280, 150, 220, {n: 7, mitigations: 2, open: 1, version: 'v2 · draft'});
    s += riskGrid(T, id, 600, 700, {cw: 54, rh: 40, lx: 150});
    s += line(`M360 700C460 700 500 760 560 760`, {stroke: T.faint, sw: 2, dash: '6 6'});
    // The human's decision in the accent.
    s += card(T, 60, 760, 440, 150, {accent: true});
    s += tx(84, 800, 'Accept residual risk?', {size: 22, weight: 600});
    s += tx(84, 832, 'Bulk limit 50 per run, or approver workload.', {size: 18, color: T.muted});
    s += pill(T, 84, 858, 'accept', {size: 15, tone: 'accent', filled: true, font: 'sans'}); s += pill(T, 176, 858, 'change', {size: 15, tone: 'faint', font: 'sans'});
    s += tx(60, 1000, 'Shaper and Risk advisor run without Sam; Sam answers, resolves, accepts.', {size: 17, color: T.muted});
  }
  if (st === 3) {
    s += fan(330, 330, 'C', 'Checker', true);
    [['P', 'Priya', 480], ['J', 'Jo', 620], ['A', 'Alex', 760]].forEach(([l, n, y]) => {
      s += line(`M${hx + 40} ${hy - 20}C240 ${hy - 20} 240 ${y} 300 ${y}`, {stroke: T.faint, sw: 2});
      s += `<circle cx="330" cy="${y}" r="22" fill="${T.paper}" stroke="${T.ink}" stroke-width="2.2"/>` + tx(330, y + 7, l, {size: 19, anchor: 'middle', weight: 600});
      s += tx(330, y + 48, n, {size: 16, anchor: 'middle', color: T.muted});
      s += `<path d="M372 ${y - 8}l6 6l12 -13" fill="none" stroke="${T.ink}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>` + tx(400, y + 6, 'signed v4', {size: 15, font: 'mono', color: T.muted});
    });
    s += tx(600, 300, 'Three findings', {size: 22, weight: 600});
    [['R3 cites no source', false], ['R5 and R6 conflict on limits', false], ['No rollback requirement', true]].forEach(([n, ov], i) => {
      const y = 340 + i * 34; s += glyph(T, 608, y - 7, ov ? 'needs' : 'done', {r: 6}); s += tx(626, y, n, {size: 18, color: T.muted});
      if (ov) { s += `<path d="M624 ${y - 6}H836" stroke="${T.ink}" stroke-width="2" stroke-linecap="round"/>`; s += pill(T, 850, y - 18, 'Sam: out of scope', {size: 13, tone: 'accent', font: 'sans'}); }
    });
    s += specPage(T, 600, 460, 150, 200, {n: 7, mitigations: 2, open: 0, version: 'v4 · ratified', title: 'Intent spec'});
    s += tx(780, 500, 'Hand-off packet', {size: 20, weight: 600});
    [['spec', 'v4'], ['evidence', '6'], ['decisions', '3'], ['deps', '4'], ['tickets', '5 draft']].forEach(([n, c], i) => { s += pill(T, 780 + (i % 2) * 130, 520 + Math.floor(i / 2) * 40, `${n} ${c}`, {size: 13}); });
    s += line(`M780 660H980`, {stroke: T.ink, arrow: `${id}-ar`}); s += tx(780, 696, 'to engineering or a coding agent', {size: 16, color: T.muted});
    s += tx(600, 760, 'Audit', {size: 16, color: T.muted, weight: 600, ls: 1.2});
    [['allow', 'read tickets · R'], ['ask', 'accept risk · Sam'], ['allow', 'override 3 · Sam'], ['deny', 'publish transcript']].forEach(([k, w], i) => { const y = 776 + i * 40; s += pill(T, 600, y, k, {size: 13, tone: k === 'ask' ? 'accent' : 'faint', w: 64}); s += tx(672, y + 20, w, {size: 15, font: 'mono'}); });
    s += phone(T, 880, 740, 150, 300, '');
    s += lines(T, 900, 790, 110, 8, {dy: 16}); s += pill(T, 900, 980, 'ratify', {size: 12, tone: 'accent', filled: true, font: 'sans'});
    s += tx(1030, 1062, '2 days later, from a phone', {size: 15, color: T.muted, italic: true, anchor: 'end'});
    s += tx(60, 1000, 'runs as Sam · viewers re-checked', {size: 17, color: T.muted, font: 'mono'});
  }
  return s;
}
