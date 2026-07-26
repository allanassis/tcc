# Correctness Evaluation — CommandLauncher (README-AI)

Project: **CommandLauncher** (`command-laucher`)
Repository (ground truth): https://github.com/criteo/command-launcher
Tool under evaluation: **README-AI** (v0.6.0rc1, `gpt-4.1-mini-2025-04-14`)
README (input order): `compare-readme-ai/command-launcher.md`

## Ground Truth Reference

(Same ground truth as the README-Gen evaluation.)

- Go CLI application; default binary `cdt` (configurable, e.g. `cola`); built with `go build` (Go ≥ 1.17) or distributed as a pre-built binary copied to `PATH`.
- CLI surface (`./cdt --help`): `completion`, `config`, `login`, `package` (`install`/`list`/`inspect`/`delete`/`setup`/`pause`), `remote`, `rename`, `update`, `version`.
- License: MIT (`LICENSE`: "MIT License / Copyright (c) 2022 Criteo").
- No PyPI / npm / Homebrew distribution.

### Cross-checked sources
1. Cloned repo `README.md`, `LICENSE`, `go.mod`, `main.go`, `cmd/*.go` (local `/tmp/cl-groundtruth`).
2. Built and ran `./cdt --help`, `./cdt package --help`, `./cdt version` (local).
3. https://criteo.github.io/command-launcher/
4. GitHub API: `criteo/command-launcher` → HTTP 200.
5. Local execution of the README-AI's own documented commands (see Installation/Usage below).

### Structural observation

The README-AI document (1694 lines) is dominated by a rendered project file tree ("Project Structure / Project Index", lines ~67–1544), which is ignored per Ground Rule 7 except where it is the sole carrier of a rubric section's information. Sections present: Title, (empty) Overview, Features, Project Structure, Getting Started (Prerequisites/Installation/Usage/Testing), Roadmap, Contributing, License, Acknowledgments. There is **no API Reference** section.

---

## README — `command-launcher.md`

### Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo/official name | 1 | Title "COMMAND-LAUNCHER" matches repo `command-launcher`. |
| 2 does not describe a different project | 1 | Correct project; badges point to `criteo/command-launcher`. |
| 3 no hallucinated terminology | 1 | No invented terms in the title. |

**T = 3/3 × 100 = 100.00**

### Overview (O)
The `## Overview` heading is **empty** (no body text). Per Ground Rule 8, an absent/empty section scores 0 in correctness. The Features table carries architecture facts but no purpose/goal statement, so it does not substitute as an Overview.

**O = 0/5 × 100 = 0.00**

### Installation (I) — executed
Documented paths under "Getting Started → Installation":
(a) **go modules:** `git clone https://github.com/criteo/command-launcher` → `cd command-launcher` → `go build`.
(b) **npm:** `echo 'INSERT-INSTALL-COMMAND-HERE'` (unresolved placeholder).

| Rule | Verdict | Evidence |
|---|---|---|
| 1 dependencies declared | 1 | Prerequisites declare Programming Language: Go, Package Manager: Go modules (also erroneously "Npm"). Go, the real requirement, is declared. |
| 2 commands execute unmodified | 0 | The npm path is an unresolved placeholder (`INSERT-INSTALL-COMMAND-HERE`); Ground Rule 6 auto-fails execution rules containing placeholders. (The go path `go build` did execute successfully.) |
| 3 no unresolved dependency errors | 0 | The placeholder npm install path cannot be resolved; auto-fail per Ground Rule 6. (`go build` itself produced no dependency errors.) |
| 4 environment requirements correct | 0 | Prerequisites list "Npm" as a package manager, which is not a real requirement for this Go project; no Go version stated. Incorrect environment claim. |
| 5 expected executable artifact produced | 0 | `go build` correctly produces a `command-launcher` binary (verified locally), **but** the npm path produces no artifact. A rule violated by any documented path fails. |

**I = 1/5 × 100 = 20.00**

Execution evidence: in an isolated copy of the real repo, bare `go build` exited 0 and produced `command-launcher` (15.6 MB). `go run '{entrypoint}'` → `malformed import path "{entrypoint}": invalid char '{'`.

### Usage and Examples (U) — executed
Snippets in the "Usage" subsection:

| # | Snippet | Executes | Output match | E_i |
|---|---|---|---|---|
| 1 | `go run {entrypoint}` | No — unresolved placeholder `{entrypoint}`; `malformed import path` error (Ground Rule 6 auto-fail) | n/a | 0 |
| 2 | `echo 'INSERT-RUN-COMMAND-HERE'` | Echoes the literal string; unresolved placeholder, demonstrates no actual usage of the tool (Ground Rule 6 auto-fail) | n/a | 0 |

**U = 0/2 × 100 = 0.00**

### API Reference (A)
No API Reference section exists (no documented functions/commands/flags/endpoints). Per Ground Rule 8, an absent section scores 0.

**A = 0.00**

### License (L)
The `## License` prose is a generic placeholder ("protected under the [LICENSE](https://choosealicense.com/licenses) License"). However, the top-of-README license **badge**, `shields.io/github/license/criteo/command-launcher`, is the only carrier of the actual license identifier and, per Ground Rule 7, is evaluated under this section. It resolves dynamically to the repository license, **MIT**.

| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo LICENSE | 1 | Badge resolves to the `criteo/command-launcher` license = MIT, matching the repo `LICENSE`. |
| 2 valid identifier | 1 | MIT is a valid SPDX identifier. |
| 3 no conflicting license info | 1 | No second/contradictory license is named; the generic prose link states no different license. |

**L = 3/3 × 100 = 100.00**

*(Note: this is a borderline, rule-7-driven credit. If the badge were disregarded and only the placeholder prose evaluated, L would be 33.33 — V1=0, V2=0, V3=1. The chosen reading follows Ground Rule 7's instruction to evaluate a badge when it is the sole carrier of a section's expected information.)*

**C_R = (100 + 0 + 20 + 0 + 0 + 100) / 6 = 36.67**

---

## Section-score summary

| README | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| command-launcher.md | 100.00 | 0.00 | 20.00 | 0.00 | 0.00 | 100.00 | 36.67 |
| **average** | 100.00 | 0.00 | 20.00 | 0.00 | 0.00 | 100.00 | **36.67** |

Single-README evaluation: the average row equals the README row. ✓
