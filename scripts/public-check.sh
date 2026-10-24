#!/bin/sh
# Check what would be published: no do-not-name terms, no transcripts, no unstripped full text.
# Usage: scripts/public-check.sh   (checks the git index; run after `git add -A`)
cd "$(dirname "$0")/.." || exit 1
fail=0
if [ -f .public-check-terms ] && git grep --cached -niE -f .public-check-terms >/dev/null; then
  echo "FAIL: do-not-name term found:"; git grep --cached -nliE -f .public-check-terms; fail=1
fi
if git ls-files | grep -q '\.transcript\.md$'; then echo "FAIL: transcript tracked"; fail=1; fi
for f in $(git ls-files '*.md'); do
  git show ":$f" | python3 -c "
import sys,re
t=sys.stdin.read()
for m in re.finditer(r'^## Full text[^\n]*\n(.*?)(?=^## |\Z)',t,re.S|re.M):
    b=m.group(1).replace('_Full text omitted from the public repository; see \`source_url\` for the original._','').strip()
    if b: print('FAIL: unstripped full text in $f'); sys.exit(1)
" || fail=1
done
[ $fail = 0 ] && echo "public check: ok"
exit $fail
