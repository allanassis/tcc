# ATRAK Evaluation — README-Gen (project: git-cli)

> ATRAK is a **presence-only** assessment (Thayer et al. 2021). Content that is
> factually wrong or hallucinated still counts as present; factual accuracy is
> scored under Correctness and is not double-counted here. An element is **absent
> (0)** only when: the carrying section is empty/missing; the only candidate is a
> bare name-only list; or the only candidate is unresolved template placeholders.

## Ground Truth Reference
- **Project:** Git
- **Repository:** https://github.com/git/git
- **Domain:** distributed version control system (source-code history management)
- **Core domain entities:** repository, commit, branch, merge, remote, index
  (staging area), working directory, HEAD, tag.
- **Core execution facts:** installed via package managers/source; CLI commands
  (`git init/add/commit/clone/push/pull/log/merge/checkout/reset`); requires a
  repository context; `git --version` reports the build; distributed under GPL v2.
- **Core usage patterns:** init/clone → stage (`add`) → `commit` → branch/merge →
  push/pull; inspect history via `log`/`diff`.

---

## README 1 — data1.md
- **K_D (Domain Concepts):** dedicated "Domain Concepts" glossary defines
  repository, commit, branch, merge, remote, index, working directory, checkout,
  tag — each with an explanatory definition (not a bare list). **Present = 1**
- **K_E (Execution Facts):** Installation (brew/apt/dnf/installer), `git --version`,
  CLI command synopses with parameters, `.git` metadata behavior. **Present = 1**
- **K_U (Usage Patterns):** worked examples for init/clone/status/add/commit/push,
  branching+merging, log/diff, undo. **Present = 1**
- **K = (1+1+1)/3 = 100%**

## README 2 — data2.md
- **K_D:** "Domain Concepts" glossary (repository, commit, branch, merge, index,
  remote, working directory) with definitions + "snapshots over differences,
  immutable history." **Present = 1**
- **K_E:** Installation across Linux/macOS/Windows, identity config, CLI command
  reference with parameters and behavior notes (three-way merge, `origin`). **1**
- **K_U:** end-to-end workflow examples (config → init → clone → add → commit →
  branch/merge → remote add → push/pull → log). **Present = 1**
- **K = (1+1+1)/3 = 100%**

## README 3 — data3.md
- **K_D:** "Core Domain Concepts" glossary (repository, commit, branch, merge,
  remote, index, working directory, HEAD, tag) with definitions + rebasing,
  cherry-picking, submodules, hooks. **Present = 1**
- **K_E:** Installation (apt/brew/installer/choco), CLI command reference with
  options, reset modes (soft/mixed/hard). **Present = 1**
- **K_U:** Usage section + dedicated "Examples" section with runnable multi-step
  workflows (init+README commit; clone+checkout maint; merge; push). **Present = 1**
- **K = (1+1+1)/3 = 100%**

---

## ATRAK averages (over 3 READMEs)
- domain_concepts = 1.00, execution_facts = 1.00, usage_patterns = 1.00
- **ATRAK average = 100%**
