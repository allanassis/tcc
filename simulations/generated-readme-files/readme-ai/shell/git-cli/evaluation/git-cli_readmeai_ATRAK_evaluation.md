# ATRAK Evaluation — README-AI (project: git-cli)

README under evaluation: `compare-readme-ai/git_readme_readmeai.md`

> ATRAK is a **presence-only** assessment. Hallucinated or incorrect content still
> counts as present; accuracy is scored under Correctness and not double-counted.
> An element is absent (0) only when its carrying content is empty/missing, is a
> bare name-only list, or consists solely of unresolved template placeholders.

## Ground Truth Reference
- **Project:** Git
- **Repository:** https://github.com/git/git
- **Domain:** distributed version control system.
- **Core domain entities:** repository, commit, branch, merge, remote, index
  (staging area), working directory, HEAD, tag.
- **Core execution facts:** built from source (C, `make`/autotools) or installed
  via package managers; CLI subcommands; requires a repository context;
  distributed under GPL v2.
- **Core usage patterns:** clone/init → add → commit → branch/merge → push/pull.

---

## K_D — Domain Concepts — **Present = 1**
The **Features** table provides defined domain/architecture concepts with
explanations, not a bare name list: "Version Control Model — Distributed version
control system…", "Data Storage — content-addressable filesystem storing objects
(blobs, trees, commits, tags)", "Commit History — DAG structure… supporting
rebasing", "Staging Area (Index) — intermediate area to prepare commits",
"Packfiles", "Hooks System", "Protocols Supported". Each row carries a
descriptive definition → evaluable domain knowledge is present.

## K_E — Execution Facts — **Present = 1**
Beyond the `INSERT-…-HERE` placeholders there is real execution-fact content:
Prerequisites list a programming language and package managers; Getting Started
gives runnable `git clone https://github.com/git/git` and `cd git` steps; the
Features table states runtime facts (transport protocols HTTP/SSH/Git/local,
cross-platform support, build system, signed commits/tags). The candidate content
is therefore NOT solely placeholders → present. (Correctness of these facts, e.g.
"Programming Language: Shell", is penalized under Correctness, not here.)

## K_U — Usage Patterns — **Present = 1**
Although the dedicated Usage section is placeholder-only, the README elsewhere
demonstrates how git is applied with concrete commands: the Installation steps
show `git clone …`/`cd git`, and the Contributing walkthrough demonstrates a full
usage sequence — `git clone`, `git checkout -b new-feature-x`,
`git commit -m '…'`, `git push origin new-feature-x`. These are real code
demonstrations of applying the tool → usage-pattern knowledge is present.

---

## ATRAK score
**K = (K_D + K_E + K_U)/3 = (1 + 1 + 1)/3 = 100%**

Single README → the `average` row equals this row.
