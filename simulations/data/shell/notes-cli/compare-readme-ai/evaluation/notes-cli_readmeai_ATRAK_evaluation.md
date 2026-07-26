# notes-cli — README-AI ATRAK Evaluation

ATRAK assesses **presence, not correctness**. Present (1) when the README
provides evaluable content for the element; absent (0) only when the carrying
section is empty/missing, is a bare name-only list, or is only unresolved
placeholders.

File: `compare-readme-ai/notes_readme_readmeai.md`.

## Ground Truth Reference

| Field | Value |
|---|---|
| Project | notes-cli |
| Repository | <https://github.com/rhysd/notes-cli> |
| Domain | Command-line (terminal) note-taking / knowledge management tool (Go) |
| Core domain entities | Notes (Markdown files), Categories, Tags (`- Tags:` metadata), Home dir (`$NOTES_CLI_HOME`), Templates, Git-backed save |
| Core execution facts | Install via release binary or `go install github.com/rhysd/notes-cli/cmd/notes` (Go 1.19 per go.mod); executable `notes`; subcommands new/list/categories/tags/save/config/selfupdate; env `NOTES_CLI_*`; kingpin.v2; MIT |
| Core usage patterns | `notes new <category> <filename> [tags]`; `notes list [flags]`; pipe into grep/fzf; `notes save`; `notes config` |

Sources: cloned repo `/tmp/notescli-gt` (`README.md`, `go.mod`, `LICENSE.txt`,
`cmd_*.go`) and built binary `/tmp/notesbin --help`.

---

## Per-element verdicts

| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1** | The **Features** table and **Project Index** provide substantive, defined descriptions of the domain: note management, categories, tags, editor integration, Git save, pager, self-update — with explanatory prose (not a bare name-only list). |
| **K_E Execution Facts** | **1** | Prerequisites (Go, Go modules), installation steps (`git clone`/`cd`/`go build`), a Testing section (`go test ./...`), dependency/CI facts, and config-path descriptions (home, git, editor, pager) in the file summaries. |
| **K_U Usage Patterns** | **0** | The only Usage carrier is `go run {entrypoint}` — an **unresolved template placeholder** — and the Testing snippet embeds `{__test_framework__}`. Per the ATRAK placeholder rule, placeholder-only content is not evaluable. No actual `notes` usage examples/tutorials (what/how/why of applying the tool) appear anywhere. |

**K = (1 + 1 + 0)/3 = 66.67%.**

---

## ATRAK summary (README-AI)

| readme | K_D | K_E | K_U | atrak_score |
|---|---|---|---|---|
| notes_readme_readmeai.md | 1 | 1 | 0 | 66.67 |
| **average** | 1 | 1 | 0 | **66.67** |

Single-README evaluation: the `average` row equals the README row. ✓
