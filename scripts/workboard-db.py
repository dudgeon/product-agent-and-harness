#!/usr/bin/env python3
"""Build the Review board's documents: tasks/<slug> and docs/<slug>--<n>, one JSON file each, under an out dir.

Usage: python3 scripts/workboard-db.py <out-dir>
"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/dudgeon/product-agent-and-harness/blob/main/"
EXPL = Path("/Users/geoff/claude-home/explainers")
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)

# Worker sessions: app sessions open in the Claude app; background ones are attached from a terminal.
APP = lambda sid: {"kind": "app", "id": sid, "link": f"claude://claude.ai/epitaxy/{sid}"}
RC = {"36a0d56f": "https://claude.ai/code/session_01TYrCTxTPCphJh23xGnarV2", "db172d7f": "https://claude.ai/code/session_01LmQEayPXyVyaGhrMWD7xJL",
      "2c0b10cc": "https://claude.ai/code/session_01Nr5DsHCZhcJKX6LSudXnjn", "d6d48790": "https://claude.ai/code/session_01JtkQS4zfweTzmB27xQLbqX",
      "6058ba84": "https://claude.ai/code/session_01V2Np7vJRfWhWV3KRfQregP", "3d45fbd1": "https://claude.ai/code/session_01HwoRhRcgdY5PBNZbt8Yg1W",
      "0bd16627": "https://claude.ai/code/session_01RBtdYJ4dEa5inMmJwfHsVe", "343d6311": "https://claude.ai/code/session_01A2TsUmicGNkKURfBSNxGQQ", "85993db5": "https://claude.ai/code/session_01F2D6G24G9xFAoLAG1fAWF5", "762dd35c": "https://claude.ai/code/session_015Nc54pXhjrkX3EZq2YRo4e"}
BG = lambda name, jid, state="": {"kind": "bg", "id": jid, "name": name, "url": RC.get(jid, ""), "attach": f"claude attach {jid}", "note": state}
SESS = {
 "research-product-agent-and-harness": APP("local_8a840fd4-9a6b-4127-b4cc-1a5745fb6fff"),
 "intent-shaping-options-film": APP("local_8a840fd4-9a6b-4127-b4cc-1a5745fb6fff"),
 "competitive-teardown-ramp-glass": APP("local_dabad5f3-9c2e-4de2-a436-011942aa0ba0"),
 "ramp-glass-film": APP("local_dabad5f3-9c2e-4de2-a436-011942aa0ba0"),
 "research-pm-agents-jobs-to-be-done": APP("local_84be37e8-1851-4195-9cb6-21c6f8b3ce5b"),
 "pm-agents-evidence-film": APP("local_84be37e8-1851-4195-9cb6-21c6f8b3ce5b"),
 "research-agent-runtime-patterns-taxonomy": APP("local_2ee18572-3463-43af-b06d-0ee8b5960ba9"),
 "runtime-patterns-film": APP("local_2ee18572-3463-43af-b06d-0ee8b5960ba9"),
 "user-story-mapping": APP("local_8ebd568e-df86-4849-8b4a-81ae6863d7ca"),
 "competitive-teardown-shopify-river": BG("teardown-shopify-river", "36a0d56f"),
 "competitive-teardown-stripe-knowledge-agents": BG("teardown-stripe-agents", "3d45fbd1"),
 "stripe-teardown-film": BG("teardown-stripe-agents", "3d45fbd1"),
 "research-runtime-patterns-follow-up-round": BG("research-follow-up-round", "a36bf408", "stopped; results merged by the director"),
 "strategy-story-and-explainer-video": BG("story-and-film", "0bd16627"),
 "research-lennys-newsletter-archive": BG("sweep-lennys", "db172d7f"),
 "research-department-of-product-knowledge-series": BG("sweep-dept-of-product", "2c0b10cc"),
 "research-claude-resources-articles": BG("ingest-claude-resources", "d6d48790"),
 "project-readme": BG("project-readme", "6058ba84"),
 "pdlc-cross-ecosystem-map": BG("pdlc-cross-ecosystem", "343d6311"),
 "research-airbnb-spotify-product-practices": BG("research-airbnb-spotify", "85993db5"),
 "research-block-product-practices": BG("research-block", "762dd35c"),
}
MODEL = {"strategy-story-and-explainer-video": "Fable 5.1"}
FILMS = {"strategy-story-and-explainer-video": "04-product-agent-harness", "pm-agents-evidence-film": "05-pm-agents-evidence",
         "ramp-glass-film": "06-ramp-glass-teardown", "runtime-patterns-film": "07-runtime-patterns",
         "intent-shaping-options-film": "08-intent-shaping-options", "stripe-teardown-film": "09-stripe-teardown"}
# Stage, kept in step with DIRECTOR.md by the director.
STAGE = json.loads((ROOT / "scripts" / "workboard-stages.json").read_text())
PRIMARY = re.compile(r"^(00-[^/]*|01-synthesis|README|INDEX|audit-2026-10-24|02-prototype-design|01-story)\.md$")

def fm(t):
    m = re.match(r"---\n(.*?)\n---\n", t, re.S); d = {}
    for l in (m.group(1).splitlines() if m else []):
        if ":" in l and not l.startswith(" "):
            k, v = l.split(":", 1); d[k.strip()] = v.strip()
    return d

def kind(slug):
    if "film" in slug or "video" in slug: return "Film"
    if slug.startswith("competitive-teardown"): return "Teardown"
    if slug.startswith("research-"): return "Research"
    if slug == "user-story-mapping": return "Design"
    return "Phase"

n_docs = 0
for p in sorted((ROOT / "tasks").glob("*.md")):
    slug = p.stem; t = p.read_text(); f = fm(t)
    prog = [l[2:].strip() for l in t.split("## Progress", 1)[-1].splitlines() if l.startswith("- 20")]
    folder = ROOT / "tasks" / slug
    files = sorted(q for q in folder.rglob("*") if q.is_file() and q.suffix in (".md", ".html")) if folder.is_dir() else []
    if slug == "research-runtime-patterns-follow-up-round":
        files = sorted((ROOT / "tasks/research-agent-runtime-patterns-taxonomy").glob("followup-*.md"))
    docs = [("Task note", f"tasks/{slug}.md", t)]
    for q in files:
        if q.suffix == ".md" and (PRIMARY.match(q.name) or q.name.startswith("followup-")) and q.stat().st_size < 200_000:
            docs.append((q.name, str(q.relative_to(ROOT)), q.read_text()))
    if slug in FILMS:
        pj = EXPL / "projects" / FILMS[slug]
        for name in ("review-note.md", "script-doc.md", "README.md"):
            q = pj / name
            if q.exists() and q.stat().st_size < 200_000:
                docs.append((f"{FILMS[slug]}/{name}", f"explainers/projects/{FILMS[slug]}/{name} (local only)", q.read_text()))
    links = [{"label": q.name if q.parent == folder else str(q.relative_to(ROOT / "tasks")), "url": REPO + str(q.relative_to(ROOT))} for q in files]
    blob = t + "".join(d[2] for d in docs)
    for a in dict.fromkeys(re.findall(r"https://claude\.ai/(?:code/)?artifact/[A-Za-z0-9-]+", blob)):
        links.append({"label": "Claude artifact", "url": a})
    doc_ids = []
    for i, (label, path, text) in enumerate(docs):
        did = f"{slug}--{i}"
        json.dump({"task": slug, "label": label, "path": path, "github": REPO + path if "local only" not in path else "", "text": text, "order": i},
                  open(out / f"docs__{did}.json", "w"))
        doc_ids.append({"id": did, "label": label}); n_docs += 1
    stage = STAGE.get(slug, f.get("status", "?").capitalize())
    json.dump({
        "title": f.get("title", slug), "kind": kind(slug), "stage": stage,
        "needsReview": stage == "Done, to review", "session": SESS.get(slug),
        "model": MODEL.get(slug, f.get("model", "") .replace("claude-opus-5-5", "Opus 5.5").replace("claude-fable-5-1", "Fable 5.1") or "Opus 5.5"),
        "doneWhen": f.get("done_when", ""), "latest": prog[-1] if prog else "", "steps": len(prog),
        "noteUrl": REPO + f"tasks/{slug}.md", "docs": doc_ids, "links": links,
    }, open(out / f"tasks__{slug}.json", "w"))
print("tasks:", len(list((ROOT / 'tasks').glob('*.md'))), "docs:", n_docs)
