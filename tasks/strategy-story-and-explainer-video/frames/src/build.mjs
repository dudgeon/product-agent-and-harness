// Builds the Helm reference frames: three looks × three key states → ../*.svg and ../png/*.png (headless Chrome).
import {writeFileSync, mkdirSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
import {dirname, join, resolve} from 'node:path';
import {fileURLToPath} from 'node:url';
import {THEMES, svg} from './lib.mjs';
import {ledger, board} from './frames.mjs';

const here = dirname(fileURLToPath(import.meta.url)), out = resolve(here, '..');
mkdirSync(join(out, 'png'), {recursive: true});
const LOOKS = {A: ['ledger', 'paper'], B: ['board', 'paper'], C: ['ledger', 'plate']};
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const png = process.argv.includes('--png');
for (const [look, [layout, theme]] of Object.entries(LOOKS)) for (const st of [1, 2, 3]) {
  const T = THEMES[theme], id = `h${look}${st}`;
  const body = layout === 'ledger' ? ledger(T, id, st) : board(T, id, st);
  const file = join(out, `${look}-s${st}.svg`);
  writeFileSync(file, svg(T, id, body));
  if (png) execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--window-size=1080,1080', `--screenshot=${join(out, 'png', `${look}-s${st}.png`)}`, `file://${file}`], {stdio: 'ignore'});
  console.log('wrote', file);
}
