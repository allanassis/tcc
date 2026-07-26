#!/usr/bin/env python3
"""Execute the comparison per simulations/readme-evaluation-comparison-prompt.md
with the parameters of simulations/tcc-run-manifest.md.
Consumes ONLY the standardized evaluation CSVs. Prints an audit trail."""
import csv, os, statistics, sys

BASE = "simulations/data"
OUT = "simulations/comparison"

# Manifest: package folder -> (project label, language, popularity, readmeai prefix)
PKGS = [
    ("js/axios", "axios", "JavaScript", "popular"),
    ("js/jquey", "jquey", "JavaScript", "popular"),
    ("js/moment", "moment", "JavaScript", "popular"),
    ("js/uri", "uri", "JavaScript", "low"),
    ("py/numpy", "numpy", "Python", "popular"),
    ("py/rich", "rich", "Python", "popular"),
    ("py/scikit-learn", "scikit-learn", "Python", "popular"),
    ("py/snakemd", "snakemd", "Python", "low"),
    ("shell/git-cli", "git-cli", "Shell", "popular"),
    ("shell/jq", "jq", "Shell", "popular"),
    ("shell/notes-cli", "notes-cli", "Shell", "low"),
    ("shell/command-laucher", "command-laucher", "Shell", "low"),
]
SEC = ["title_score", "overview_score", "installation_score", "usage_score", "api_score", "license_score", "correctness_score"]

def read_correctness(folder, prefix):
    rows = list(csv.DictReader(open(f"{folder}/{prefix}_correctness_results.csv")))
    runs = [r for r in rows if r["readme"] != "average"]
    return runs

def read_atrak(folder, prefix):
    rows = list(csv.DictReader(open(f"{folder}/{prefix}_completeness_ATRAK.csv")))
    return [r for r in rows if r["readme"] != "average"]

def read_completeness(folder, prefix):
    rows = list(csv.reader(open(f"{folder}/{prefix}_completeness.csv")))
    return [round(sum(float(v) for v in r) / len(r) * 100, 2) for r in rows[1:]]

def f(x):
    return round(float(x), 2)

results = {}  # pkg -> {tool -> {aggregation -> record}}
audit = []
for pkgpath, pkg, lang, pop in PKGS:
    folder = f"{BASE}/{pkgpath}"
    gen_runs = read_correctness(f"{folder}/evaluation", pkg)
    gen_atrak = read_atrak(f"{folder}/evaluation", pkg)
    gen_comp = read_completeness(f"{folder}/evaluation", pkg)
    ai_runs = read_correctness(f"{folder}/compare-readme-ai/evaluation", f"{pkg}_readmeai")
    ai_atrak = read_atrak(f"{folder}/compare-readme-ai/evaluation", f"{pkg}_readmeai")
    ai_comp = read_completeness(f"{folder}/compare-readme-ai/evaluation", f"{pkg}_readmeai")
    assert len(gen_runs) == 3 and len(ai_runs) == 1, f"{pkg}: run counts {len(gen_runs)}/{len(ai_runs)}"

    def rec(sections, comp, atrak):
        d = {c: f(sections[c]) for c in SEC}
        d["completeness_score"] = f(comp)
        d["atrak_score"] = f(atrak)
        return d

    # README-Gen aggregations
    corr = [float(r["correctness_score"]) for r in gen_runs]
    bi, wi = corr.index(max(corr)), corr.index(min(corr))
    mean_sections = {c: sum(float(r[c]) for r in gen_runs) / 3 for c in SEC}
    gen = {
        "mean": rec(mean_sections, sum(gen_comp) / 3, sum(float(a["atrak_score"]) for a in gen_atrak) / 3),
        "best": rec({c: float(gen_runs[bi][c]) for c in SEC}, gen_comp[bi], float(gen_atrak[bi]["atrak_score"])),
        "worst": rec({c: float(gen_runs[wi][c]) for c in SEC}, gen_comp[wi], float(gen_atrak[wi]["atrak_score"])),
    }
    ai = {"single": rec({c: float(ai_runs[0][c]) for c in SEC}, ai_comp[0], float(ai_atrak[0]["atrak_score"]))}
    results[pkg] = {"README-Gen": gen, "README-AI": ai, "lang": lang, "pop": pop}
    audit.append(f"{pkg}: gen runs corr={[f(c) for c in corr]} (best=run{bi+1}, worst=run{wi+1}), "
                 f"gen comp={gen_comp}, ai corr={f(ai_runs[0]['correctness_score'])}, ai comp={ai_comp[0]}")

    # Per-package comparison CSV
    out = f"{folder}/compare-readme-ai/{pkg}_standard_comparison.csv"
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["project", "tool", "aggregation", "completeness_score", "atrak_score"] + SEC + ["winner_correctness"])
        ai_c = ai["single"]["correctness_score"]
        for agg in ["mean", "best", "worst"]:
            r = gen[agg]
            winner = ""
            if agg == "mean":
                winner = "README-Gen" if r["correctness_score"] > ai_c else ("README-AI" if ai_c > r["correctness_score"] else "tie")
            w.writerow([pkg, "README-Gen", agg, r["completeness_score"], r["atrak_score"]] + [r[c] for c in SEC] + [winner])
        r = ai["single"]
        winner = "README-AI" if ai_c > gen["mean"]["correctness_score"] else ("README-Gen" if gen["mean"]["correctness_score"] > ai_c else "tie")
        w.writerow([pkg, "README-AI", "single", r["completeness_score"], r["atrak_score"]] + [r[c] for c in SEC] + [winner])

# Aggregate summary
os.makedirs(OUT, exist_ok=True)
def mean(vals):
    return round(sum(vals) / len(vals), 2)

def group_rows(w, scope, members_by_name):
    for name, members in members_by_name.items():
        for tool, agg in [("README-Gen", "mean"), ("README-AI", "single")]:
            recs = [results[p][tool][agg] for p in members]
            w.writerow([scope, name, tool,
                        mean([r["completeness_score"] for r in recs]),
                        mean([r["atrak_score"] for r in recs]),
                        mean([r["correctness_score"] for r in recs]), "", ""])

with open(f"{OUT}/summary_readme_gen_vs_readme_ai.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["scope", "name", "tool", "completeness_score", "atrak_score", "correctness_score", "correctness_std", "wins"])
    for pkg in [p[1] for p in PKGS]:
        g, a = results[pkg]["README-Gen"]["mean"], results[pkg]["README-AI"]["single"]
        winner = "README-Gen" if g["correctness_score"] > a["correctness_score"] else ("README-AI" if a["correctness_score"] > g["correctness_score"] else "tie")
        w.writerow(["project", pkg, "README-Gen", g["completeness_score"], g["atrak_score"], g["correctness_score"], "", winner])
        w.writerow(["project", pkg, "README-AI", a["completeness_score"], a["atrak_score"], a["correctness_score"], "", winner])
    allp = [p[1] for p in PKGS]
    for tool, agg in [("README-Gen", "mean"), ("README-AI", "single")]:
        recs = [results[p][tool][agg] for p in allp]
        corr = [r["correctness_score"] for r in recs]
        w.writerow(["overall", "all", tool, mean([r["completeness_score"] for r in recs]),
                    mean([r["atrak_score"] for r in recs]), mean(corr), round(statistics.pstdev(corr), 2), ""])
    group_rows(w, "popularity", {
        "popular": [p[1] for p in PKGS if p[3] == "popular"],
        "low": [p[1] for p in PKGS if p[3] == "low"]})
    group_rows(w, "language", {
        lang: [p[1] for p in PKGS if p[2] == lang] for lang in ["JavaScript", "Python", "Shell"]})
    for agg, label in [("mean", "vs_gen_mean"), ("worst", "vs_gen_worst")]:
        gw = sum(1 for p in allp if results[p]["README-Gen"][agg]["correctness_score"] > results[p]["README-AI"]["single"]["correctness_score"])
        aw = sum(1 for p in allp if results[p]["README-AI"]["single"]["correctness_score"] > results[p]["README-Gen"][agg]["correctness_score"])
        w.writerow(["win_count", label, "README-Gen", "", "", "", "", gw])
        w.writerow(["win_count", label, "README-AI", "", "", "", "", aw])

print("AUDIT TRAIL")
for a in audit:
    print(" ", a)
print("\nSUMMARY")
for line in open(f"{OUT}/summary_readme_gen_vs_readme_ai.csv"):
    print(" ", line.rstrip())
