# notes-cli — README-AI Correctness Evaluation

Tool: **README-AI** v0.6.0rc1 (`gpt-4.1-mini-2025-04-14`).
File evaluated: `compare-readme-ai/notes_readme_readmeai.md` (single README).
Project: **notes-cli** (`shell/notes-cli`, low-popularity Go project).

## Cross-checked ground-truth sources

Same locally-established ground truth as the README-Gen evaluation:
cloned repo `/tmp/notescli-gt` (official `README.md`, `go.mod` with `go 1.19`,
`LICENSE.txt` = MIT, `cmd_*.go`), and the locally built binary
(`go build ./cmd/notes` → `notes`; `--help` output). Key facts: real
executable is `notes`; repo root is a **library** package (so root `go build`
produces no binary); real commands are `new/list/categories/tags/save/config/
selfupdate`; env vars are `NOTES_CLI_*` (no `NOTES_DIR`); notes are `.md`.

Executed installation evidence: `git clone …; cd notes-cli; go build` at the
repo root exits 0 but produces **no executable** (repo root is `package notes`,
not `package main`). Executed testing snippet: `go test ./...` **FAILS**
(`--- FAIL: TestSelfupdateUpdateToLatest`, needs network), and the documented
build/usage strings contain unresolved placeholders.

---

## Structural note (rule 7)

The `## Overview` heading in this README is **empty**. Per ground rule 7, the
**Features** table and **Project Index** file-summaries are the only carriers of
overview/purpose information, so they are evaluated under the Overview section
and cited explicitly below.

## Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 exact match | 1 | `# NOTES-CLI` = repo name `notes-cli` (case only). |
| 2 not different project | 1 | All content is about this repo. |
| 3 no hallucinated terms | 1 | Plain project name. |

**T = 3/3 = 100%.**

## Overview (O) — evaluated on the Features table + Project Index (rule 7)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality correct | 1 | "CLI tool written in Go … File-based note management"; file summaries describe creating, listing, tagging, saving notes. |
| 2 supported by artifacts | 1 | Matches real `cmd_new.go`, `cmd_list.go`, `cmd_tags.go`, `cmd_save.go`. |
| 3 no unsupported features | 0 | Claims **"OAuth2 library hints at secure authentication flows"** and **"Shell integration scripts for bash, fish, and bat shells"** — OAuth2/protobuf are indirect deps of the self-update lib (not user features), and **`bat` is not a shell**. These describe unsupported features. |
| 4 correct domain | 1 | Note-taking CLI correctly identified. |
| 5 terminology matches repo | 1 | Uses notes, categories, tags, save/Git, editor, pager — all repo vocabulary. |

**O = 4/5 = 80%.**

## Installation (I) — executed
Documented path: `git clone https://github.com/rhysd/notes-cli`, `cd notes-cli`,
`go build`. Prerequisites: "Go" + "Go modules" (no version stated).
| Rule | Verdict | Evidence |
|---|---|---|
| 1 deps declared | 1 | Go + Go modules declared; transitive deps auto-resolved. |
| 2 commands execute unmodified | 1 | `git clone`, `cd`, `go build` all run (exit 0). |
| 3 no unresolved dep errors | 1 | `go build` resolves all modules cleanly. |
| 4 env requirements correct | 1 | No Go version is claimed, so there is no incorrect version claim to fail against `go.mod`. |
| 5 produces expected artifact | 0 | `go build` at repo root produces **no executable** (root is a library package) — no runnable `notes`/`notes-cli` artifact results. |

**I = 4/5 = 80%.**

## Usage and Examples (U) — executed
| # | Snippet | Executes? | Match | E_i |
|---|---|---|---|---|
| 1 | `go run {entrypoint}` (Usage) | no | Unresolved placeholder `{entrypoint}` → fails execution rule (ground rule 6). | 0 |
| 2 | `go test ./...` (Testing) | no | `go test ./...` **FAILS** (`TestSelfupdateUpdateToLatest`); description contains unresolved `{__test_framework__}` placeholder; also this is a test command, not a tool-usage example. | 0 |

No actual `notes` usage examples exist anywhere in the README.
**U = 0/2 = 0%.**

## API Reference (A)
There is **no API Reference section** — no commands, flags, functions, or
endpoints are documented with parameters (the Project Index lists source files
with prose summaries, not an API surface). Number of documented API elements
**n = 0** → section absent.

**A = 0%** (per ground rule 8, a missing section scores 0).

## License (L)
The License section reads: *"Notes-cli is protected under the [LICENSE]
(https://choosealicense.com/licenses) License … refer to the [LICENSE]
(https://choosealicense.com/licenses/) file."*
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo LICENSE | 0 | Repo is **MIT**; the README never names MIT — it is an unfilled generic template linking to choosealicense.com. |
| 2 valid identifier | 0 | No license identifier is provided ("[LICENSE] License" is not a valid SPDX id). |
| 3 no conflicting info | 1 | No two statements conflict (generic text + repo license badge; no direct contradiction). |

**L = 1/3 = 33.33%.**

---

## Final scores (README-AI)

**C_R = (T + O + I + U + A + L)/6 = (100 + 80 + 80 + 0 + 0 + 33.33)/6 =
293.33/6 = 48.89%.**

| readme | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| notes_readme_readmeai.md | 100 | 80 | 80 | 0 | 0 | 33.33 | 48.89 |
| **average** | 100 | 80 | 80 | 0 | 0 | 33.33 | **48.89** |

Single-README evaluation: the `average` row equals the README row. ✓
