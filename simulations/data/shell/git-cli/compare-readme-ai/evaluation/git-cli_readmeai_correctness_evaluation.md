# Correctness Evaluation — README-AI (project: git-cli)

README under evaluation: `compare-readme-ai/git_readme_readmeai.md`
Repository (ground truth): https://github.com/git/git
Core functionality: Create and manage commits
Installed artifact used for cross-check: `git version 2.55.0` (Homebrew, macOS).

## Methodology notes
- Same execution environment and cross-checked sources as the README-Gen
  evaluation (git-scm.com/docs, local `git help`, `COPYING`).
- Placeholder policy (rubric rule 6): `INSERT-…-HERE` and `{__test_framework__}`
  are unresolved template placeholders that automatically fail execution rules.
- Rule 7 (carrier content): the "## Overview" heading is **empty**. The
  **Features** table (outside the six rubric sections) is the only carrier of
  overview information (purpose, functionality, domain), so Overview is evaluated
  against the Features table content and this is stated explicitly.
- The ~3.2 MB file size is almost entirely the "Project Structure" file tree
  (ignored per rubric rule 7); evaluated content is the Overview, Features,
  Getting Started (Prerequisites/Installation/Usage/Testing), and License sections.

## Cross-checked sources
- https://github.com/git/git , `COPYING` (raw) → GNU GPL v2.
- https://git-scm.com/docs ; local `git help` (2.55.0).
- https://choosealicense.com/licenses → 200 (generic license-chooser page — the
  README's License links point here, not to git's actual license).

---

## Project Title (T) — 3 rules
Header renders "GIT".
- V1 matches repository name (`git`). **1**
- V2 does not describe a different project. **1**
- V3 no hallucinated terminology in the title. **1**
- **T = 3/3 = 100%**

## Overview (O) — 5 rules (evaluated via Features table, rule 7)
The "## Overview" section is empty; the Features table carries the overview
content. Relevant rows: "Version Control Model — Distributed version control
system enabling multiple repositories and offline work"; "Programming Language —
Primarily written in C"; plus content-addressable storage, DAG history, staging
area, packfiles, hooks, protocols — all genuine git characteristics.
- V1 primary functionality correctly described (distributed VCS). **1**
- V2 supported by repository artifacts. **1**
- V3 no unsupported features (all listed features are real git features). **1**
- V4 correct software domain (version control). **1**
- V5 terminology matches repository terminology. **1**
- **O = 5/5 = 100%**
  (Note: the Prerequisites section separately claims "Programming Language: Shell",
  contradicting the Features table's correct "C"; that defect is charged under
  Installation, below, not Overview.)

## Installation (I) — 5 rules (executed / validated)
Documented as a source build. Prerequisites: "Programming Language: Shell";
"Package Manager: Cargo, Autotools, Cmake". Steps: `git clone …/git/git` (real),
`cd git` (real), then per-manager install commands that are all
`❯ echo 'INSERT-INSTALL-COMMAND-HERE'`.
- V1 required dependencies declared — actual build deps (C compiler, `make`,
  zlib, curl, OpenSSL, gettext) are NOT declared; listed package managers are
  wrong for git. **0**
- V2 commands execute without modification — install commands are unresolved
  `INSERT-INSTALL-COMMAND-HERE` placeholders (rule 6). **0**
- V3 no unresolved dependency errors — cannot execute; deps not established. **0**
- V4 environment requirements correct — "Programming Language: Shell" is wrong
  (git is written in C); "Package Manager: Cargo, Autotools, Cmake" is wrong
  (git builds via `make`/autotools, not Cargo). **0**
- V5 expected executable artifact produced — placeholders produce no `git`
  binary. **0**
- **I = 0/5 = 0%**

## Usage and Examples (U) — snippets executed
The "### Usage" section contains 3 snippets, one per (bogus) package manager,
each identical: `echo 'INSERT-RUN-COMMAND-HERE'`.
| # | Snippet | Executes as usage of git | E_i |
|---|---|---|---|
| 1 | cargo: `echo 'INSERT-RUN-COMMAND-HERE'` | no — placeholder (rule 6) | 0 |
| 2 | autotools: `echo 'INSERT-RUN-COMMAND-HERE'` | no — placeholder | 0 |
| 3 | cmake: `echo 'INSERT-RUN-COMMAND-HERE'` | no — placeholder | 0 |
The "### Testing" snippets are likewise `INSERT-TEST-COMMAND-HERE` with the
literal placeholder `{__test_framework__}` in prose. No runnable usage example
exists (the `git clone`/`cd` lines are install steps; Contributing examples are a
contribution workflow, rule 7). **U = 0/3 = 0%**

## API Reference (A) — 6 rules per element
The README documents **no** API elements: there is no functions/commands/endpoints
reference with parameters. The Features table names capabilities but not API
elements with signatures. Section absent → **A = 0%** (ground rule 8).

## License (L) — 3 rules
Text: "Git is protected under the [LICENSE](https://choosealicense.com/licenses)
License. For more details, refer to the [LICENSE](…/licenses/) file." — the actual
license (GPL v2) is never named; links go to a generic license-chooser page.
- V1 documented license matches repo `COPYING` (GPL v2) — no, generic "LICENSE". **0**
- V2 license identifier valid — "LICENSE" is not a valid license identifier. **0**
- V3 no conflicting licensing information — only one (generic) mention; no
  internal conflict. **1**
- **L = 1/3 = 33.33%**

---

## Correctness score
**C_R = (100 + 100 + 0 + 0 + 0 + 33.33)/6 = 38.89%**

Single README → the `average` row equals this row.
