# Moment — README-AI Correctness Evaluation

Tool under evaluation: **README-AI** v0.6.0rc1 (`gpt-4.1-mini-2025-04-14`).
README: `compare-readme-ai/moment_readme_readmeai.md` (single file).

## Environment & Cross-Checked Sources

- **Isolated env:** `/tmp/eval-moment` and cloned source `/tmp/eval-moment/moment`.
- **Source-build install executed:** `git clone https://github.com/moment/moment` (exit 0) →
  `cd moment` → `npm install` (exit 0, dev deps resolved). `npm start` → **exit 1, "Missing script:
  start"**. `npm test` → **exit 0** (`grunt test` + typescript-test, "Done."). `package.json` scripts
  contain `test`, `eslint`, `coverage`, etc., but **no `start`**.
- **devDependencies introspection** (to check Features claims): rollup, uglify-js, grunt(+plugins),
  karma(+launchers), qunit, eslint, prettier, nyc, coveralls all present — Features tooling claims are
  accurate.
- **Repository LICENSE:** MIT (raw.githubusercontent.com/moment/moment/develop/LICENSE).
- **Official docs:** https://momentjs.com/docs/.

Document structure: `# MOMENT` title, **empty `## Overview`**, `## Features` table, `## Project
Structure` + `## Project Index` (auto-generated file tree/summaries), `## Getting Started`
(Prerequisites, Installation, Usage, Testing), Roadmap, Contributing, `## License`, Acknowledgments.
There is **no API Reference section**.

---

## Project Title (T)
Title = `# MOMENT`.
1. Matches repository name `moment` (case variant of the project name) — **1**
2. Not a different project — **1**
3. No hallucinated terminology — **1**
**T = 3/3 = 100%**

## Overview (O)
The `## Overview` section is **empty**. Per ground rule 7, the `## Features` table is the only carrier
of overview/functionality information, so it is evaluated here (stated explicitly). Features claims:
"Modular JavaScript design focused on date/time manipulation", "locale-aware formatting and parsing",
"zero external dependencies", ESLint/Prettier/TypeScript, QUnit/Karma testing, Rollup/UglifyJS bundling.
1. Primary functionality correctly described (date/time manipulation) — **1**
2. Supported by artifacts (verified in repo) — **1**
3. No unsupported features — all tooling/functionality claims verified against `devDependencies` and
   repo layout (rollup, grunt, karma, qunit, nyc, coveralls all present) — **1**
4. Domain correctly identified (JS date/time) — **1**
5. Terminology matches repository — **1**
**O = 5/5 = 100%**

## Installation (I) — executed
Documented paths under "Installation": (a) source build `git clone` + `cd moment` + **npm** `npm install`;
(b) **bower** `echo 'INSERT-INSTALL-COMMAND-HERE'`; (c) **composer** `echo 'INSERT-INSTALL-COMMAND-HERE'`.
Prerequisites: "JavaScript; Package Manager: Bower, Npm, Composer".

1. Required dependencies declared — Features states zero runtime deps + dev deps; npm path resolves
   via package.json — **1**
2. Commands execute without modification — the bower and composer steps are **unresolved placeholders**
   (`INSERT-INSTALL-COMMAND-HERE`); rubric rule 6 auto-fails execution rules → **0**
3. No unresolved dependency errors — `npm install` completed cleanly (exit 0) — **1**
4. Environment requirements correct — no version claim made; `engines=node:*` so nothing false — **1**
5. Produces expected executable artifact — npm path yields a usable tree, but the bower/composer
   documented paths produce **no artifact** (placeholders); a rule violated by any documented path
   fails → **0**
**I = 3/5 = 60%**

## Usage and Examples (U) — executed (k = 3)

| # | Snippet | Executes | Result | E_i |
|---|---|---|---|---|
| npm | `npm start` | ran | **exit 1 — "Missing script: start"** | 0 |
| bower | `echo 'INSERT-RUN-COMMAND-HERE'` | placeholder | unresolved placeholder (rule 6 auto-fail) | 0 |
| composer | `echo 'INSERT-RUN-COMMAND-HERE'` | placeholder | unresolved placeholder (rule 6 auto-fail) | 0 |

No moment API usage examples are present; the "Usage" section only lists generic run commands.
**U = 0/3 = 0%**

## API Reference (A)
The README has **no API Reference section** and documents **no functions, classes, methods, or
parameters** (the Project Index summarizes files in prose only). n = 0 documented elements; per ground
rule 8 a missing section scores 0. **A = 0%**

## License (L)
Text: "Moment is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more
details, refer to the [LICENSE](https://choosealicense.com/licenses/) file."
1. Matches repo LICENSE — repo is **MIT**, README does **not** name MIT (generic "LICENSE" +
   choosealicense.com link) → does not match → **0**
2. License identifier valid — "LICENSE" is not a valid SPDX identifier → **0**
3. No conflicting licensing info — no second/contradictory license stated in text → **1**
**L = 1/3 = 33.33%**

## Correctness Score
**C_R = (100 + 100 + 60 + 0 + 0 + 33.33) / 6 = 293.33 / 6 = 48.89%**

---

## Summary

| README | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| moment_readme_readmeai.md | 100 | 100 | 60 | 0 | 0 | 33.33 | 48.89 |
| **average** | 100 | 100 | 60 | 0 | 0 | 33.33 | **48.89** |
