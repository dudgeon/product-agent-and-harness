#!/usr/bin/env python3
"""git clean filter: drop third-party "## Full text" sections from source notes.

The public repo keeps each note's summary, short quotes and source_url; the
verbatim text of third-party videos, posts and articles stays local only.
"""
import re
import sys

text = sys.stdin.read()
out = re.sub(
    r"(^## Full text[^\n]*\n)(.*?)(?=^## |\Z)",
    r"\1\n_Full text omitted from the public repository; see `source_url` for the original._\n\n",
    text, flags=re.S | re.M)
sys.stdout.write(out)
