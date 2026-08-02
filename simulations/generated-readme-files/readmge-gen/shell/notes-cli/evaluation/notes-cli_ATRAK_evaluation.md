# notes-cli — README-Gen ATRAK Evaluation

ATRAK assesses **presence, not correctness**. An element is present (1) when
the README offers evaluable content for it, even if that content is factually
wrong. It is absent (0) only when the carrying section is empty/missing, is a
bare name-only list, or consists solely of unresolved placeholders.

## Ground Truth Reference

| Field | Value |
|---|---|
| Project | notes-cli |
| Repository | <https://github.com/rhysd/notes-cli> |
| Domain | Command-line (terminal) note-taking / knowledge management tool (Go) |
| Core domain entities | Notes (Markdown files), Categories (each note belongs to exactly one; nestable with `/`), Tags (`- Tags:` metadata line), Home directory (`$NOTES_CLI_HOME`, XDG data dir default), Templates (`.template.md`), Git-backed save |
| Core execution facts | Install via release binary or `go install github.com/rhysd/notes-cli/cmd/notes` (Go 1.19 per go.mod, 1.16+ per README); executable is `notes`; subcommands `new`/`list`(`ls`)/`categories`(`cats`)/`tags`/`save`/`config`/`selfupdate`; env vars `NOTES_CLI_HOME`, `NOTES_CLI_EDITOR`(+`EDITOR` fallback), `NOTES_CLI_GIT`, `NOTES_CLI_PAGER`; built with kingpin.v2; MIT license |
| Core usage patterns | `notes new <category> <filename> [tags]`; `notes list [-f/-o/-c/-t/-s/-e/-r]`; pipe `notes list` into grep/ag/fzf/peco; `notes save` to commit; `notes config` to inspect settings |

Sources cross-checked: cloned repo `/tmp/notescli-gt` (official `README.md`,
`go.mod`, `LICENSE.txt`, `cmd_*.go`), and the locally built binary
`/tmp/notesbin --help` / `new --help` / `list --help`.

---

## README 1 — `data1.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1** | "### Domain Concepts" defines Notes, Tags, Indexing, Commands, Editor Integration, Note Directory — each with an explanatory sentence (not a bare list). |
| **K_E Execution Facts** | **1** | Prerequisites (Go 1.12+, Unix-like OS), install steps (release binary, `go build`, `mv`), env vars `NOTES_DIR`/`EDITOR`, per-command behaviors and outputs. |
| **K_U Usage Patterns** | **1** | Multiple runnable command examples with what/how/why: `notes new`, `notes list`, `notes search`, `notes open`, `notes index`, tagging, plus a Best Practices section. |

**K(data1) = (1+1+1)/3 = 100%.** (Content is largely hallucinated — e.g.
`search`/`open`/`index` — but that is penalised in correctness, not here.)

## README 2 — `data2.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1** | Defines Notes Directory, Note Files, Note Metadata, Search & Filter, Note Actions with descriptions. |
| **K_E Execution Facts** | **1** | Prerequisites (Go 1.16+), build-from-source and prebuilt-binary install, `NOTES_DIR` env, command semantics, sample output blocks. |
| **K_U Usage Patterns** | **1** | Command examples with descriptions and an output example: `new`, `list`, `search`, `open`, `delete`; Common Options. |

**K(data2) = (1+1+1)/3 = 100%.**

## README 3 — `data3.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1** | Defines Notes as Files, Note Searching, Note Editing, Tagging, Listing/Filtering, Metadata with explanatory text. |
| **K_E Execution Facts** | **1** | Install via binaries / Homebrew / source (Go 1.13+), env config (`NOTES_DIR`, `$EDITOR`, `#` tags), command structure `notes [command] [flags]`. |
| **K_U Usage Patterns** | **1** | Command examples + a dedicated "Sample Workflows" section (`edit`, `search`, `list -t`, `show`) with what/how/why narration. |

**K(data3) = (1+1+1)/3 = 100%.**

---

## ATRAK summary (README-Gen)

| readme | K_D | K_E | K_U | atrak_score |
|---|---|---|---|---|
| data1.md | 1 | 1 | 1 | 100 |
| data2.md | 1 | 1 | 1 | 100 |
| data3.md | 1 | 1 | 1 | 100 |
| **average** | 1 | 1 | 1 | **100** |

All three generations carry all three knowledge elements with substantive
(if partly hallucinated) content, so ATRAK presence is uniformly 100%.
