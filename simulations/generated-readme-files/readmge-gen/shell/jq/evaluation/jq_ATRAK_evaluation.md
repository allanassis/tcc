# jq — README-Gen ATRAK Evaluation

Adherence to the Theory of Robust API Knowledge (Thayer et al. 2021).
**Presence, not correctness** — content that is factually wrong still counts as
present. An element is absent (0) only when the carrying section is empty/
missing, is a bare name-only list, or is only unresolved placeholders.

`K = (K_D + K_E + K_U) / 3`

## Ground Truth Reference

- **Project:** jq
- **Repository:** https://github.com/jqlang/jq
- **Domain:** command-line JSON processing; jq is a filter language/tool for
  slicing, filtering, mapping and transforming JSON.
- **Core domain entities:** JSON values (objects, arrays, strings, numbers,
  booleans, null); filters; pipelines (`|`); generators/streams; builtin
  operators & functions; variables (`$x`); modules; assignment/path expressions.
- **Core execution facts:** reads JSON from stdin/files, writes newline-
  separated JSON to stdout; CLI flags (`-c -r -s -n -e --arg --argjson
  --stream …`); IEEE754 numbers; exit statuses; installable via package
  managers or autotools source build (oniguruma dependency for regex).
- **Usage patterns:** `jq '<filter>' file.json`; piping; `select`, `map`,
  variable binding, object construction.

Sources: repository, https://jqlang.org/manual/, `src/jq.h`, `src/jv.h`.

---

## README 1 — `data1.md`

- **K_D Domain Concepts — PRESENT (1):** the Overview defines JSON, Filters,
  Streams, Operators/Functions, Modules, Pipelines with explanatory sentences
  (not a bare name list).
- **K_E Execution Facts — PRESENT (1):** Installation steps, CLI flags with
  semantics, and an explicit "Execution Facts" subsection (streaming, `|`
  piping, `$name` variables, multi-output-per-line behaviour, program files).
- **K_U Usage Patterns — PRESENT (1):** five worked examples (pretty-print,
  field extraction, `select` filtering, object merge, shell-script capture)
  with what/how narration.

**K = (1+1+1)/3 × 100 = 100**

## README 2 — `data2.md`

- **K_D — PRESENT (1):** "Domain Concepts" list (JSON Data, Filters, Pipelines,
  Streams, Slice and Dice, Functions) each with a short definition.
- **K_E — PRESENT (1):** installation, CLI options with descriptions, a
  "Feedback and Debugging" subsection (exit codes, stderr), input/output model.
- **K_U — PRESENT (1):** four executed examples plus a "Filter Usage in
  Scripts" example.

**K = 100**

## README 3 — `data3.md`

- **K_D — PRESENT (1):** "Domain Concepts" (JSON Data, Filters, Pipelines/
  Composition, Streaming, Functions/Operators, Variables/Assignments, Modules)
  with definitions and a sed/awk/grep analogy.
- **K_E — PRESENT (1):** installation, CLI options, "Execution Facts" flag
  descriptions, and a "C API (General Facts)" subsection (`jq_init`,
  `jq_compile`, `jq_start`, `jq_next`, `jv_parse`).
- **K_U — PRESENT (1):** six worked examples plus a "Best Practices" list and a
  variables example.

**K = 100**

---

## Aggregate

| readme | K_D | K_E | K_U | atrak_score |
|---|---|---|---|---|
| data1.md | 1 | 1 | 1 | 100 |
| data2.md | 1 | 1 | 1 | 100 |
| data3.md | 1 | 1 | 1 | 100 |
| **average** | 1 | 1 | 1 | **100** |
