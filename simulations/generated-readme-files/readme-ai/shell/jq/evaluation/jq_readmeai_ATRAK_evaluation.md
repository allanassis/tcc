# jq — README-AI ATRAK Evaluation

Adherence to the Theory of Robust API Knowledge (Thayer et al. 2021).
**Presence, not correctness.** Absent (0) only when the carrying content is
empty/missing, a bare name-only list, or only unresolved placeholders.

`K = (K_D + K_E + K_U) / 3`

## Ground Truth Reference
- **Project:** jq
- **Repository:** https://github.com/jqlang/jq
- **Domain:** command-line JSON processing (a filter language for JSON).
- **Core domain entities:** JSON values, filters, pipelines, generators/
  streams, builtin operators & functions, variables, modules, assignment.
- **Core execution facts:** stdin/file input → newline-separated JSON stdout;
  CLI flags; IEEE754 numbers; exit codes; package-manager or autotools/source
  install (oniguruma for regex); written in portable C.
- **Usage patterns:** `jq '<filter>' file.json`, piping, `select`, `map`,
  variable binding.

Sources: repository, https://jqlang.org/manual/, Fedora package metadata.

---

## README-AI — `jq_readme_readmeai.md`

- **K_D Domain Concepts — PRESENT (1):** although `## Overview` is empty, the
  Features table and the Project-Index file summaries provide explanatory prose
  about the problem domain — e.g. "parsing JSON and jq expressions", and
  jq.1.prebuilt described as "transformation, querying, and manipulation of JSON
  data". This is more than a bare name-only list, so K_D is present (presence
  standard; accuracy is not judged here).

- **K_E Execution Facts — PRESENT (1):** the Prerequisites block (Package
  Manager: Autotools, Container Runtime: Docker), real Installation commands
  (`git clone …`, `cd jq`, `docker build -t jqlang/jq .`), and the Features
  "Architecture/Testing/Performance" rows provide evaluable runtime/build/
  dependency facts. (Some install/usage commands are placeholders, but genuine
  non-placeholder execution facts exist, so the element is present.)

- **K_U Usage Patterns — ABSENT (0):** the only content that demonstrates using
  jq (the Usage and Testing sections) consists entirely of unresolved template
  placeholders — `docker run -it {image_name}`, `echo 'INSERT-RUN-COMMAND-HERE'`,
  `{__test_framework__}`, `echo 'INSERT-TEST-COMMAND-HERE'`. Per the absence
  criterion ("only candidate content consists of unresolved template
  placeholders"), K_U is absent. (The Contributing git commands are a
  contribution workflow, not a demonstration of applying jq.)

**K = (1 + 1 + 0)/3 × 100 = 66.67**

---

## Aggregate (single README → average = the row)

| readme | K_D | K_E | K_U | atrak_score |
|---|---|---|---|---|
| jq_readme_readmeai.md | 1 | 1 | 0 | 66.67 |
| **average** | 1 | 1 | 0 | **66.67** |
