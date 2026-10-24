// Helm reference frames: a small procedural SVG library. Plain strings, pure functions of their inputs (seeded noise only),
// so the same drawing can move into the film's Remotion scene. Square 1080 × 1080, the explainers' restrained look.
export const S = 1080;
export const f = (n) => (Math.round(n * 10) / 10).toString();
export const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

// Themes. `ledger` and `board` share the house paper palette; `plate` is a two-colour printed plate with halftone washes.
export const THEMES = {
  paper: {name: 'paper', paper: '#f3f0e8', ink: '#24221e', muted: '#8a857b', faint: '#d3cdc0', hair: '#e2ddd2', accent: '#c4673f', accentWash: '#f0dccf', wash: '#ebe6dc', serif: "Charter, 'Iowan Old Style', Georgia, serif", sans: "'Avenir Next', 'Helvetica Neue', sans-serif", mono: 'Menlo, monospace', halftone: false},
  plate: {name: 'plate', paper: '#eef0ee', ink: '#2a3645', muted: '#6d7a8a', faint: '#c5cdd6', hair: '#d4dae1', accent: '#c4673f', accentWash: '#f0dccf', wash: '#dde3e8', serif: "Charter, 'Iowan Old Style', Georgia, serif", sans: "'Avenir Next', 'Helvetica Neue', sans-serif", mono: 'Menlo, monospace', halftone: true},
};

export const defs = (T, id) => `<defs>
<marker id="${id}-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" stroke="${T.ink}" stroke-width="1.4"/></marker>
<marker id="${id}-ara" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" stroke="${T.accent}" stroke-width="1.4"/></marker>
<pattern id="${id}-hatch" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="9" height="9" fill="${T.accentWash}"/><path d="M0 0V9" stroke="${T.accent}" stroke-width="1.2" opacity="0.5"/></pattern>
<pattern id="${id}-grey" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0V8" stroke="${T.faint}" stroke-width="1.2"/></pattern>
<pattern id="${id}-dots" width="7" height="7" patternUnits="userSpaceOnUse"><circle cx="3.5" cy="3.5" r="1.25" fill="${T.ink}" opacity="0.18"/></pattern>
</defs>`;

export const text = (x, y, s, o = {}) => {
  const {size = 26, font = 'sans', color, anchor = 'start', weight = 500, italic = false, ls = 0.3, op = 1} = o;
  return `<text x="${f(x)}" y="${f(y)}" text-anchor="${anchor}" font-family="${o.T[font]}" font-size="${size}" font-weight="${weight}"${italic ? ' font-style="italic"' : ''} fill="${color ?? o.T.ink}" letter-spacing="${ls}" opacity="${op}">${esc(s)}</text>`;
};
export const rect = (x, y, w, h, o = {}) => `<rect x="${f(x)}" y="${f(y)}" width="${f(w)}" height="${f(h)}" rx="${o.r ?? 8}" fill="${o.fill ?? 'none'}" stroke="${o.stroke ?? 'none'}" stroke-width="${o.sw ?? 2}"${o.dash ? ` stroke-dasharray="${o.dash}"` : ''} opacity="${o.op ?? 1}"/>`;
export const line = (d, o = {}) => `<path d="${d}" fill="none" stroke="${o.stroke}" stroke-width="${o.sw ?? 2.2}" stroke-linecap="round" stroke-linejoin="round"${o.dash ? ` stroke-dasharray="${o.dash}"` : ''}${o.arrow ? ` marker-end="url(#${o.arrow})"` : ''} opacity="${o.op ?? 1}"/>`;

/** An agent: the house hexagon with a centre dot; a letter names the persona. Hollow while working, filled when done. */
export const agent = (T, x, y, letter, o = {}) => {
  const r = o.r ?? 22, done = o.done ?? false, col = o.color ?? T.ink;
  const pts = Array.from({length: 6}, (_, i) => `${f(x + r * Math.cos((Math.PI / 3) * i + Math.PI / 6))} ${f(y + r * Math.sin((Math.PI / 3) * i + Math.PI / 6))}`).join('L');
  return `<g opacity="${o.op ?? 1}"><path d="M${pts}Z" fill="${done ? col : T.paper}" stroke="${col}" stroke-width="2.4" stroke-linejoin="round"/>` +
    (letter ? `<text x="${f(x)}" y="${f(y + r * 0.36)}" text-anchor="middle" font-family="${T.sans}" font-weight="600" font-size="${r * 0.95}" fill="${done ? T.paper : col}">${letter}</text>` : `<circle cx="${f(x)}" cy="${f(y)}" r="${r * 0.22}" fill="${col}"/>`) + `</g>`;
};
/** A person, head and shoulders; the human in the product role is always drawn in the accent. */
export const person = (T, x, y, o = {}) => {
  const col = o.color ?? T.accent, s = o.s ?? 1;
  return `<g opacity="${o.op ?? 1}" transform="translate(${f(x)} ${f(y)}) scale(${s})"><circle cx="0" cy="-30" r="11" fill="${T.paper}" stroke="${col}" stroke-width="2.6"${o.dash ? ' stroke-dasharray="4 4"' : ''}/><path d="M-20 0Q-20 -14 0 -14Q20 -14 20 0" fill="none" stroke="${col}" stroke-width="2.6" stroke-linecap="round"${o.dash ? ' stroke-dasharray="4 4"' : ''}/>${o.ring ? `<circle cx="0" cy="-14" r="34" fill="none" stroke="${col}" stroke-width="1.6" opacity="0.55"/>` : ''}</g>`;
};
/** A state glyph: hollow circle (working), filled circle (done), dash (idle), diamond (review), accent dot (needs you). */
export const glyph = (T, x, y, state, o = {}) => {
  const r = o.r ?? 7;
  if (state === 'done') return `<circle cx="${f(x)}" cy="${f(y)}" r="${r}" fill="${T.ink}"/>`;
  if (state === 'working') return `<circle cx="${f(x)}" cy="${f(y)}" r="${r}" fill="none" stroke="${T.ink}" stroke-width="2"/>`;
  if (state === 'idle') return `<path d="M${f(x - r)} ${f(y)}H${f(x + r)}" stroke="${T.faint}" stroke-width="2.4" stroke-linecap="round"/>`;
  if (state === 'needs') return `<circle cx="${f(x)}" cy="${f(y)}" r="${r}" fill="${T.accent}"/>`;
  if (state === 'review') return `<path d="M${f(x)} ${f(y - r)}L${f(x + r)} ${f(y)}L${f(x)} ${f(y + r)}L${f(x - r)} ${f(y)}Z" fill="${T.ink}"/>`;
  return '';
};
/** Lines of text as marks (a page's body). */
export const lines = (T, x, y, w, n, o = {}) => Array.from({length: n}, (_, k) => `<path d="M${f(x)} ${f(y + k * (o.dy ?? 14))}H${f(x + w * (k % 3 === 2 ? 0.6 : k % 2 ? 0.82 : 1))}" stroke="${o.color ?? T.faint}" stroke-width="${o.sw ?? 3}" stroke-linecap="round" opacity="${o.op ?? 1}"/>`).join('');
/** A pill: small mono label in a hairline capsule; `tone` ink | accent | faint. */
export const pill = (T, x, y, s, o = {}) => {
  const size = o.size ?? 17, w = o.w ?? s.length * size * 0.62 + 24, h = size + 14;
  const col = o.tone === 'accent' ? T.accent : o.tone === 'faint' ? T.muted : T.ink;
  const fill = o.filled ? col : T.paper;
  return `<g opacity="${o.op ?? 1}"><rect x="${f(x)}" y="${f(y)}" width="${f(w)}" height="${h}" rx="${h / 2}" fill="${fill}" stroke="${col}" stroke-width="1.6"/><text x="${f(x + w / 2)}" y="${f(y + size + 4.5)}" text-anchor="middle" font-family="${o.font === 'sans' ? T.sans : T.mono}" font-size="${size}" fill="${o.filled ? T.paper : col}">${esc(s)}</text></g>`;
};
/** A meter: cells that fill, never numbers that spin. */
export const meter = (T, x, y, n, k, o = {}) => {
  const cw = o.cw ?? 22, g = o.g ?? 6, h = o.h ?? 14;
  return Array.from({length: n}, (_, i) => `<rect x="${f(x + i * (cw + g))}" y="${f(y)}" width="${cw}" height="${h}" rx="3" fill="${i < k ? (o.color ?? T.ink) : 'none'}" stroke="${i < k ? (o.color ?? T.ink) : T.faint}" stroke-width="1.6"/>`).join('');
};
/** A phone frame. */
export const phone = (T, x, y, w, h, inner) => `<g><rect x="${f(x)}" y="${f(y)}" width="${f(w)}" height="${f(h)}" rx="26" fill="${T.paper}" stroke="${T.ink}" stroke-width="2.6"/><rect x="${f(x + 10)}" y="${f(y + 10)}" width="${f(w - 20)}" height="${f(h - 20)}" rx="18" fill="none" stroke="${T.faint}" stroke-width="1.4"/><path d="M${f(x + w / 2 - 22)} ${f(y + 24)}H${f(x + w / 2 + 22)}" stroke="${T.faint}" stroke-width="3" stroke-linecap="round"/>${inner}</g>`;
/** A halftone wash field (plate theme) or a flat wash (paper). */
export const wash = (T, id, x, y, w, h, o = {}) => T.halftone ? `<rect x="${f(x)}" y="${f(y)}" width="${f(w)}" height="${f(h)}" rx="${o.r ?? 10}" fill="url(#${id}-dots)"/>` : `<rect x="${f(x)}" y="${f(y)}" width="${f(w)}" height="${f(h)}" rx="${o.r ?? 10}" fill="${o.fill ?? T.wash}"/>`;

export const svg = (T, id, body, o = {}) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${S} ${S}" width="${o.w ?? S}" height="${o.h ?? S}">${defs(T, id)}<rect width="${S}" height="${S}" fill="${T.paper}"/>${body}</svg>`;
