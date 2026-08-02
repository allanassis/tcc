# notes-cli — README-Gen Correctness Evaluation

Tool: **README-Gen** (`gpt-4.1-mini-2025-04-14`, ATRAK-grounded prompting).
Project: **notes-cli** (`shell/notes-cli`, low-popularity Go project).
READMEs evaluated in order: `data1.md`, `data2.md`, `data3.md`.

## Cross-checked ground-truth sources

All factual checks were made against the real repository, cloned shallow and
built locally on this host (Go 1.23.3, macOS/arm64):

- Repo: <https://github.com/rhysd/notes-cli> (cloned to `/tmp/notescli-gt`).
- `README.md` (official) — install method, subcommands, env vars, note format.
- `go.mod` — `module github.com/rhysd/notes-cli`, **`go 1.19`** directive; CLI
  built with `gopkg.in/alecthomas/kingpin.v2`.
- `LICENSE.txt` — first line `the MIT License`, `Copyright (c) 2018 rhysd`.
- Built binary: `go build -o /tmp/notesbin ./cmd/notes` (exit 0) → real
  executable is named **`notes`** (from `cmd/notes`, not the repo root).
- Real CLI surface captured from `/tmp/notesbin --help`, `new --help`,
  `list --help`:
  - Commands: `new <category> <filename> [<tags>]`, `list`/`ls`
    (`-f/--full`, `-c/--category`, `-t/--tag`, `-r/--relative`, `-o/--oneline`,
    `-s/--sort`, `-e/--edit`), `categories`/`cats`, `tags [<category>]`,
    `save`, `config [<name>]`, `selfupdate`.
    Global: `--no-color`, `-A/--color-always`, `--version`, `--help`,
    `--help-man`, `--completion-script-bash`.
  - Env vars (from official README + `config.go`): `NOTES_CLI_HOME`
    (default XDG data dir, macOS `~/.local/share/notes-cli`),
    `NOTES_CLI_EDITOR` (fallback `EDITOR`), `NOTES_CLI_GIT`, `NOTES_CLI_PAGER`.
    **There is no `NOTES_DIR` and no `~/notes` default.**
  - Notes are **Markdown (`.md`)** files organised under **category**
    directories; tags live in a `- Tags:` metadata line (not `#hashtags`).
- Verified **absent** commands by executing them against `/tmp/notesbin`:
  `search`, `open`, `edit`, `show`, `delete`, `index` → all return
  `notes: error: expected command but got "<x>"`.
- Homebrew tap check: `curl` on `https://github.com/rhysd/homebrew-tap` → **HTTP
  404** (tap does not exist); `brew install rhysd/tap/notes-cli` fails to tap.
- Releases page `https://github.com/rhysd/notes-cli/releases` → HTTP 200 (real).

### Executed installation evidence (shared)

| Test | Command (as documented) | Result |
|---|---|---|
| A | `git clone …; cd notes-cli; go build` | exit 0 but **produces no executable** — repo root is a library package (`package notes`); neither `notes` nor `notes-cli` binary appears. |
| A | `mv notes-cli /usr/local/bin/` (data1) | `mv: rename notes-cli … No such file or directory`, exit 1. |
| B | `make build` (data3) | `make: *** No rule to make target 'build'` — **no Makefile** in repo. |
| C | `brew install rhysd/tap/notes-cli` (data3) | Fails — tap `rhysd/homebrew-tap` is HTTP 404. |
| — | Correct method `go build ./cmd/notes` | exit 0, produces working `notes` binary (used as the reference for usage/API execution). |

---

## README 1 — `data1.md`

### Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 exact match | 1 | Title `notes-cli` = repo name. |
| 2 not different project | 1 | Describes the note-taking CLI. |
| 3 no hallucinated terms | 1 | Plain project name. |

**T = 3/3 = 100%.**

### Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality correct | 1 | "command-line note-taking tool … create, manage, and search" — create/manage is the real purpose. |
| 2 supported by artifacts | 1 | `new`/`list` exist (cmd_new.go, cmd_list.go). |
| 3 no unsupported features | 0 | Domain Concepts claim **"Indexing: Creating an efficient search index over notes"** — notes-cli has **no index feature**; search is delegated to external `grep`/`ag`/`rg`. |
| 4 correct domain | 1 | Note-taking CLI. |
| 5 terminology matches repo | 0 | Introduces non-repo term **"Indexing"** and omits the central concept **"category"**; uses "Note Directory" instead of home/category. |

**O = 3/5 = 60%.**

### Installation (I) — executed
| Rule | Verdict | Evidence |
|---|---|---|
| 1 deps declared | 1 | Go 1.12+, Unix-like OS declared. |
| 2 commands execute unmodified | 0 | `mv notes-cli /usr/local/bin/` fails (exit 1) — no such file (Test A). |
| 3 no unresolved dep errors | 1 | `go build` resolves modules (exit 0). |
| 4 env requirements correct | 0 | Claims **Go 1.12+**; authoritative `go.mod` declares **`go 1.19`** (official README says 1.16+). 1.12 is incorrect. |
| 5 produces expected artifact | 0 | `go build` at repo root yields **no `notes-cli` executable** (Test A). |

Rules passing = {1, 3} (module dependencies resolve cleanly on `go build`, so
rule 3 holds; the `mv` step, the 1.12 version claim, and the missing artifact
fail rules 2, 4, 5). **I = 2/5 = 40%.**

### Usage and Examples (U) — executed against `/tmp/notesbin`
| # | Snippet | Executes? | Output/behavior match | E_i |
|---|---|---|---|---|
| 1 | `export NOTES_DIR=~/my_notes` | yes (shell) | Tool ignores `NOTES_DIR` (real var is `NOTES_CLI_HOME`); does not change notes dir | 0 |
| 2 | `notes new "My first note"` | no | `error: required argument 'filename' not provided` (needs `<category> <filename>`) | 0 |
| 3 | `notes list` | yes | Documented "titles and creation dates"; real output is full file **paths** | 0 |
| 4 | `notes search "meeting notes"` | no | `error: expected command but got "search"` | 0 |
| 5 | `notes search "#todo"` | no | same — no `search` command | 0 |
| 6 | `notes open "My first note"` | no | `error: expected command but got "open"` | 0 |
| 7 | `notes index` | no | `error: expected command but got "index"` | 0 |

**U = 0/7 = 0%.**

### API Reference (A) — 6 rules per element
| Element | Exists? | Names/params | Behavior | A_i |
|---|---|---|---|---|
| `notes new <title>` | partial | param is `<category> <filename> [tags]`, not `<title>`; "defaults to vim" false | mismatch | 0 |
| `notes list` | yes | ok | claims titles+timestamps; real = paths | 0 |
| `notes search <query>` | **no** | — | — | 0 |
| `notes open <title>` | **no** | — | — | 0 |
| `notes index` | **no** | — | — | 0 |
| env `NOTES_DIR` | **no** | real is `NOTES_CLI_HOME` | — | 0 |
| env `EDITOR (default vim)` | fallback exists | "default vim" false; presented as primary | partial | 0 |

**A = 0/7 = 0%.**

### License (L)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo LICENSE | 1 | Repo `LICENSE.txt` = MIT. |
| 2 valid identifier | 1 | MIT is valid SPDX. |
| 3 no conflicting info | 1 | Single consistent MIT statement. |

**L = 3/3 = 100%.**

**C_R(data1) = (100 + 60 + 40 + 0 + 0 + 100)/6 = 300/6 = 50.00%.**

---

## README 2 — `data2.md`

### Project Title (T) — 100%
`notes-cli` matches repo; no different project; no hallucinated terms. **T = 100%.**

### Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality correct | 1 | "managing plain text notes … create, search, list, and open". |
| 2 supported by artifacts | 1 | create/list exist. |
| 3 no unsupported features | 0 | "Note Actions … and **deleting notes**" — no `delete` command exists. |
| 4 correct domain | 1 | Note-taking CLI. |
| 5 terminology matches repo | 0 | Claims note files are **`.txt`**; real notes are **`.md`**; omits "category". |

**O = 3/5 = 60%.**

### Installation (I) — executed
| Rule | Verdict | Evidence |
|---|---|---|
| 1 deps declared | 1 | Go 1.16+ declared. |
| 2 commands execute unmodified | 1 | `git clone`, `cd`, `go build` all run (exit 0). |
| 3 no unresolved dep errors | 1 | modules resolve. |
| 4 env requirements correct | 0 | Claims Go **1.16+**; `go.mod` authoritative minimum is **`go 1.19`**. |
| 5 produces expected artifact | 0 | Claims "produces an executable `notes-cli` in the current directory" — **false**, `go build` at root produces nothing (Test A). |

**I = 3/5 = 60%.**

### Usage and Examples (U) — executed
| # | Snippet | Executes? | Match | E_i |
|---|---|---|---|---|
| 1 | `export NOTES_DIR=~/my_notes` | yes | var ignored by tool | 0 |
| 2 | `notes-cli new "My First Note"` | no | binary `notes-cli` never built; also missing `<filename>` arg → error | 0 |
| 3 | `notes-cli list` | yes | documented output shows `.txt` filenames; real = `.md` full paths | 0 |
| 4 | `notes-cli search keyword` | no | no `search` command | 0 |
| 5 | `notes-cli open "Meeting Notes"` | no | no `open` command | 0 |
| 6 | `notes-cli delete "Project Ideas"` | no | no `delete` command | 0 |

**U = 0/6 = 0%.**

### API Reference (A)
| Element | Exists? | Verdict | A_i |
|---|---|---|---|
| `new <title>` | partial | param wrong (`category`+`filename`); overwrite-prompt behavior false | 0 |
| `list` | yes | claims "filenames"; real = full paths | 0 |
| `search <keyword>` | **no** | — | 0 |
| `open <title>` | **no** | — | 0 |
| `delete <title>` | **no** | — | 0 |
| `-h, --help` | **yes** | real global flag; shows help | 1 |
| `--version` | **yes** | real global flag; shows version | 1 |

**A = 2/7 = 28.57%.**

### License (L) — 100%
MIT matches repo; valid; no conflict. **L = 100%.**

**C_R(data2) = (100 + 60 + 60 + 0 + 28.57 + 100)/6 = 348.57/6 = 58.10%.**

---

## README 3 — `data3.md`

### Project Title (T) — 100%
`notes-cli` matches. **T = 100%.**

### Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality correct | 1 | "managing and manipulating personal notes … searching, and organizing". |
| 2 supported by artifacts | 1 | create(`new`)/`list`/`tags` exist. |
| 3 no unsupported features | 0 | "Note Searching … fast search engine supporting regex" (no `search` cmd); `edit`/`show` commands; tagging via inline `#` (real tags = `- Tags:` metadata). |
| 4 correct domain | 1 | Note-taking CLI. |
| 5 terminology matches repo | 0 | "tags recognized as words prefixed with `#`" contradicts repo; omits "category". |

**O = 3/5 = 60%.**

### Installation (I) — executed (three documented paths)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 deps declared | 1 | Go 1.13+ declared for source path. |
| 2 commands execute unmodified | 0 | `brew install rhysd/tap/notes-cli` fails (tap 404, Test C); `make build` fails (no Makefile, Test B). |
| 3 no unresolved dep errors | 0 | Homebrew tap unresolvable; `make build` "no rule to make target". |
| 4 env requirements correct | 0 | Claims Go **1.13+**; `go.mod` minimum is **`go 1.19`**. |
| 5 produces expected artifact | 0 | `make build && ./notes` never yields a binary (Test B); brew path yields nothing (Test C). |

**I = 1/5 = 20%.**

### Usage and Examples (U) — executed
| # | Snippet | Executes? | Match | E_i |
|---|---|---|---|---|
| 1 | `notes edit mynote` | no | `error: expected command but got "edit"` | 0 |
| 2 | `notes search keyword` | no | no `search` command | 0 |
| 3 | `notes search -t tagname` | no | no `search` command | 0 |
| 4 | `notes list` | yes | described "by modification time"; real default sort = created | 0 |
| 5 | `notes list -t tagname` | **yes** | real `-t/--tag` filters list by tag; matches description | **1** |
| 6 | `notes show mynote` | no | `error: expected command but got "show"` | 0 |
| 7 | `notes edit "project-ideas"` | no | no `edit` command | 0 |
| 8 | `notes search meeting` | no | no `search` command | 0 |
| 9 | `notes list -t todo` | **yes** | valid; filters by tag `todo` (exit 0) | **1** |
| 10 | `notes show project-ideas` | no | no `show` command | 0 |

**U = 2/10 = 20%.**

### API Reference (A)
| Element | Exists? | Verdict | A_i |
|---|---|---|---|
| `notes edit [note-name]` | **no** | — | 0 |
| `notes search [pattern]` (`-t/--tag`) | **no** | — | 0 |
| `notes list` (`-t/--tag`, `-r/--recent`) | yes | `-t` correct but **`-r/--recent` wrong** (real `-r` = `--relative`; recent-sort is `-s modified`) → param names fail | 0 |
| `notes show [note-name]` | **no** | — | 0 |
| env `NOTES_DIR` | **no** | real is `NOTES_CLI_HOME` | 0 |
| env `$EDITOR` | yes | `EDITOR` is a real (fallback) editor var; setting it opens editor | 1 |
| tags via `#` in content | **no** | real tags are `- Tags:` metadata field | 0 |

**A = 1/7 = 14.29%.**

### License (L) — 100%
MIT matches repo; valid; no conflict. **L = 100%.**

**C_R(data3) = (100 + 60 + 20 + 20 + 14.29 + 100)/6 = 314.29/6 = 52.38%.**

---

## Final scores (README-Gen)

Installation is scored per-rule after executing every documented path in
isolated `/tmp` dirs. Rule 3 ("no unresolved dependency errors") passes for
data1/data2 because `go build` resolves all modules; it fails for data3 because
the `rhysd/tap/notes-cli` Homebrew formula cannot be resolved (tap HTTP 404).

| readme | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| data1.md | 100 | 60 | 40 | 0 | 0 | 100 | 50.00 |
| data2.md | 100 | 60 | 60 | 0 | 28.57 | 100 | 58.10 |
| data3.md | 100 | 60 | 20 | 20 | 14.29 | 100 | 52.38 |
| **average** | 100 | 60 | 40.00 | 6.67 | 14.29 | 100 | **53.49** |

Average consistency check: (100 + 60 + 40.00 + 6.67 + 14.29 + 100)/6 = 53.49 =
mean of the three per-README C_R values (50.00, 58.10, 52.38). ✓
