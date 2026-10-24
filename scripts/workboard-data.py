#!/usr/bin/env python3
"""Build workboard.json: one row per task, for the Workboard dashboard."""
import json, re, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/dudgeon/product-agent-and-harness/blob/main/"
EXPL = Path("/Users/geoff/claude-home/explainers")

def fm(t):
    m = re.match(r"---\n(.*?)\n---\n", t, re.S); d = {}
    for l in (m.group(1).splitlines() if m else []):
        if ":" in l and not l.startswith(" "):
            k, v = l.split(":", 1); d[k.strip()] = v.strip()
    return d

# Worker table from DIRECTOR.md: task slug -> (worker, model, state)
workers = {}
for line in (ROOT / "DIRECTOR.md").read_text().splitlines():
    if line.startswith("| ") and "](tasks/" in line:
        cells = [c.strip() for c in line.strip("|").split("|")]
        for slug in re.findall(r"\(tasks/([a-z0-9-]+)\.md\)", cells[4]):
            workers.setdefault(slug, (cells[0], cells[3], cells[5]))

def kind(slug, title):
    if slug.endswith("-film") or "film" in slug or "video" in slug: return "Film"
    if slug.startswith("competitive-teardown"): return "Teardown"
    if slug.startswith("research-"): return "Research"
    if slug in ("user-story-mapping",): return "Design"
    return "Phase"

FILMS = {"strategy-story-and-explainer-video": "04-product-agent-harness", "pm-agents-evidence-film": "05-pm-agents-evidence",
         "ramp-glass-film": "06-ramp-glass-teardown", "runtime-patterns-film": "07-runtime-patterns",
         "intent-shaping-options-film": "08-intent-shaping-options", "stripe-teardown-film": "09-stripe-teardown"}

# Stage shown on the board. Keep in step with DIRECTOR.md (director updates it on each change).
STAGE = {
 "research-product-agent-and-harness": "Done, to review", "competitive-teardown-ramp-glass": "Done, to review",
 "research-pm-agents-jobs-to-be-done": "Done, to review", "research-agent-runtime-patterns-taxonomy": "Done, to review",
 "user-story-mapping": "Done, to review", "competitive-teardown-shopify-river": "Done, to review",
 "competitive-teardown-stripe-knowledge-agents": "Done, to review", "research-runtime-patterns-follow-up-round": "Done, to review",
 "research-lennys-newsletter-archive": "Done, to review", "research-department-of-product-knowledge-series": "Done, to review",
 "research-claude-resources-articles": "Done, to review",
 "strategy-story-and-explainer-video": "In flight", "pm-agents-evidence-film": "Waiting for GPU",
 "ramp-glass-film": "Waiting for GPU", "runtime-patterns-film": "Waiting for GPU",
 "intent-shaping-options-film": "Waiting for GPU", "stripe-teardown-film": "In flight",
 "competitive-teardowns": "Suggested", "define-concepts-strategy-deck": "Suggested", "prototypes-define-dimensions": "Suggested",
 "explainer-video-style": "Dropped",
}
rows = []
for p in sorted((ROOT / "tasks").glob("*.md")):
    slug = p.stem; t = p.read_text(); f = fm(t)
    prog = [l[2:].strip() for l in t.split("## Progress", 1)[-1].splitlines() if l.startswith("- 20")]
    links = [{"label": "Task note", "url": REPO + f"tasks/{slug}.md"}]
    folder = ROOT / "tasks" / slug
    if folder.is_dir():
        for q in sorted(folder.rglob("*")):
            if q.is_file() and q.suffix in (".md", ".html") and not q.name.startswith("."):
                links.append({"label": str(q.relative_to(folder)), "url": REPO + str(q.relative_to(ROOT))})
    arts = sorted(set(re.findall(r"https://claude\.ai/(?:code/)?artifact/[A-Za-z0-9-]+", t + "".join(
        q.read_text(errors="ignore") for q in folder.rglob("*.md")) if folder.is_dir() else t)))
    if slug in FILMS:
        pj = EXPL / "projects" / FILMS[slug]
        if pj.is_dir():
            for q in sorted(pj.glob("*.md")):
                arts += re.findall(r"https://claude\.ai/(?:code/)?artifact/[A-Za-z0-9-]+", q.read_text(errors="ignore"))
    for a in dict.fromkeys(arts):
        links.append({"label": "Claude artifact", "url": a})
    w = workers.get(slug, ("", "", ""))
    status = f.get("status", "?")
    if status == "in-progress": status = "active"
    rows.append({
        "task": slug, "title": f.get("title", slug), "kind": kind(slug, f.get("title", "")),
        "status": status, "stage": STAGE.get(slug, status.capitalize()), "worker": w[0], "model": w[1] or f.get("model", ""),
        "workerState": re.sub(r"\[[^\]]*\]\([^)]*\)", "", w[2]).strip(),
        "doneWhen": f.get("done_when", ""), "latest": prog[-1] if prog else "",
        "steps": len(prog), "film": FILMS.get(slug, ""),
        "links": json.dumps(links),
    })
out = ROOT / "workboard.json"
out.write_text(json.dumps(rows, indent=1))
print(len(rows), "tasks ->", out, datetime.datetime.now().isoformat(timespec="seconds"))
