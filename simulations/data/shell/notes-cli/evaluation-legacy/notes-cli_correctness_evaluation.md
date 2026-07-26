# notes-cli README Correctness Evaluation

**Methodology:** Section 4.4.2 of *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis* (Andrade & Ribeiro, UERJ).

**Documentation Sources Cross-checked:**
- Official GitHub repository: https://github.com/rhysd/notes-cli
- GitHub API: https://api.github.com/repos/rhysd/notes-cli — confirms language: Go, name: notes-cli, 260 stars
- Official README: https://raw.githubusercontent.com/rhysd/notes-cli/master/README.md — confirms subcommands, usage, environment variables
- LICENSE file: https://raw.githubusercontent.com/rhysd/notes-cli/master/LICENSE.txt — confirms MIT License (Copyright 2018 rhysd)
- `cmd.go`: confirms subcommands: `new`, `list` (alias `ls`), `categories` (alias `cats`), `tags`, `save`, `config`, `selfupdate`
- `cmd_new.go`: confirms `notes new <category> <filename> [<tags>]` with `--no-inline-input` and `--no-edit` flags
- `cmd_list.go`: confirms `notes list` with flags `--full/-f`, `--category/-c`, `--tag/-t`, `--relative/-r`, `--oneline/-o`, `--sort/-s`, `--edit/-e`
- `cmd_save.go`: confirms `notes save` with `--message/-m` flag
- `cmd_tags.go`: confirms `notes tags [category]`
- `cmd_categories.go`: confirms `notes categories` (alias `cats`)
- `cmd_config.go`: confirms `notes config [name]` (name: home, git, editor)
- `cmd_selfupdate.go`: confirms `notes selfupdate` with `--dry/-d` flag
- `config.go`: confirms env vars: `$NOTES_CLI_HOME`, `$NOTES_CLI_EDITOR`, `$NOTES_CLI_GIT`, `$NOTES_CLI_PAGER`, `$XDG_DATA_HOME`, `$EDITOR`, `$PAGER`
- Default home: `~/.local/share/notes-cli` (XDG data dir), NOT `~/notes`
- Installation: `go install github.com/rhysd/notes-cli/cmd/notes` or download binary from GitHub releases

**Key Ground Truth Facts:**
- Language: **Go**
- Binary name: **notes**
- Tool: CLI note-taking tool for markdown notes organized by category
- License: **MIT License** (LICENSE.txt)
- Installation: download binary from releases or `go install github.com/rhysd/notes-cli/cmd/notes`
- Subcommands: `new`, `list`/`ls`, `categories`/`cats`, `tags`, `save`, `config`, `selfupdate`
- `notes new <category> <filename> [<tags>]` — requires category AND filename (not just a title)
- Notes are **markdown** files (`.md`), NOT plain text
- Home directory env var: `$NOTES_CLI_HOME` (NOT `$NOTES_DIR`)
- Default home: `~/.local/share/notes-cli` (NOT `~/notes`)
- Editor env var: `$NOTES_CLI_EDITOR` (fallback `$EDITOR`)
- There is NO `search` subcommand — searching is done via external tools (`grep`, `ag`, `rg`) piped with `notes list`
- There is NO `open` subcommand — opening is done via `notes list --edit` or piping to editor
- There is NO `delete` subcommand — deletion is done via `rm`
- There is NO `show` subcommand
- There is NO `index` subcommand
- There is NO `edit` subcommand (editing is via `notes new` or `notes list --edit`)
- There is NO tag search with `#` prefix syntax built into the tool
- There is NO Homebrew formula (not confirmed in official README)

---

## Scoring Formula (from TCC §4.4.2)

Each section uses binary criteria Vᵢ ∈ {0,1}. Section scores are percentages. Final score:

```
CR = (T + O + I + U + A + L) / 6
```

---

## data1.md Evaluation

### Step-by-step Reasoning

**data1.md claims:** notes-cli is a "fast and lightweight command-line note-taking tool" for plain text notes with commands: `notes new`, `notes list`, `notes search`, `notes open`, `notes index`. Uses `NOTES_DIR` env var with default `~/notes`. License: MIT.

---

**Project Title (T)**

Criteria:
1. Title exactly matches repository/official name → "notes-cli" matches the official repository name. ✅ V1=1
2. Title does not describe a different project → Correct project. ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucinated terms. ✅ V3=1

**T = (1+1+1)/3 × 100 = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → "fast and lightweight command-line note-taking tool designed to help users quickly create, manage, and search plain text notes" — partially correct. It IS a CLI note-taking tool, but notes are **markdown** files, not "plain text notes." The tool description is close but not precise. Partially correct. ✅ V1=1
2. Described functionality supported by repository artifacts → "Notes", "Tags", "Commands", "Editor Integration", "Note Directory" — these concepts exist in the real tool. However, "Indexing" does NOT exist. ❌ V2=0
3. Overview does not describe unsupported features → "Indexing: Creating an efficient search index over notes for rapid text and tag-based querying" — this feature does NOT exist. The real tool relies on external grep tools for searching. ❌ V3=0
4. Correctly identifies software domain → "note-taking tool... integrates smoothly into terminal workflows" — correct domain. ✅ V4=1
5. Terminology matches repository terminology → "Notes", "Tags", "Editor Integration" match. However, "Indexing", "Note Directory" (real term is "home") don't match. Partial. ❌ V5=0

**O = (1+0+0+1+0)/5 × 100 = 40**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → States "Go (version 1.12+ for building from source)" — Go is correct (though real minimum is 1.16). ✅ V1=1
2. Installation commands execute without modification → `git clone https://github.com/rhysd/notes-cli.git && cd notes-cli && go build` — this would work but produces `notes-cli` binary, not `notes`. The official method is `go install github.com/rhysd/notes-cli/cmd/notes`. The build command is partially correct but produces wrong binary name. ❌ V2=0
3. No unresolved dependency errors → `go build` at repo root would build the library, not the command. The actual command is in `cmd/notes/`. ❌ V3=0
4. Documented environment requirements correct → "Go (version 1.12+)" — real minimum is 1.16 per README. Minor inaccuracy. ❌ V4=0
5. Installation produces expected executable artifact → `go build` at root does not produce the `notes` binary. The correct path is `cmd/notes/`. ❌ V5=0

**I = (1+0+0+0+0)/5 × 100 = 20**

---

**Usage and Examples (U)**

Snippets evaluated (k=5):

| # | Snippet | Execution Result | Score |
|---|---------|-----------------|-------|
| E1 | `export NOTES_DIR=~/my_notes` | Wrong env var. Real var is `NOTES_CLI_HOME`. ❌ | 0 |
| E2 | `notes new "My first note"` | Wrong syntax. Real syntax is `notes new <category> <filename> [<tags>]` — requires both category and filename, not just a title. ❌ | 0 |
| E3 | `notes list` | This command exists and works. ✅ | 1 |
| E4 | `notes search "meeting notes"` | `search` subcommand does NOT exist. ❌ | 0 |
| E5 | `notes open "My first note"` | `open` subcommand does NOT exist. ❌ | 0 |

**U = 1/5 × 100 = 20**

---

**API Reference (A)**

Documented API elements (n=5 commands): `notes new <title>`, `notes list`, `notes search <query>`, `notes open <title>`, `notes index`.

| # | Element | Exists | Names Correct | Params Correct | Behavior Correct | Not Deprecated |
|---|---------|--------|--------------|----------------|-----------------|----------------|
| A1 | `notes new <title>` | Partially — `new` exists but signature is wrong | ❌ params wrong (real: `<category> <filename> [<tags>]`) | ❌ | ❌ behavior wrong (doesn't just take a title) | ✅ |
| A2 | `notes list` | ✅ | ✅ | ✅ | ✅ "Lists all notes" — correct | ✅ |
| A3 | `notes search <query>` | ❌ Does NOT exist | ❌ | ❌ | ❌ | N/A |
| A4 | `notes open <title>` | ❌ Does NOT exist | ❌ | ❌ | ❌ | N/A |
| A5 | `notes index` | ❌ Does NOT exist | ❌ | ❌ | ❌ | N/A |

Environment variables: `NOTES_DIR` — WRONG (real: `NOTES_CLI_HOME`). `EDITOR` — partially correct (real primary is `NOTES_CLI_EDITOR`, fallback `EDITOR`).

Scoring: 1 fully correct out of 5 commands. `notes new` exists but with completely wrong parameters, counting as incorrect.

**A = 1/5 × 100 = 20**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → "MIT License" — confirmed MIT via LICENSE.txt. ✅ V1=1
2. License identifier is valid → "MIT" is a valid SPDX identifier. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

**L = (1+1+1)/3 × 100 = 100**

---

### data1.md Final Score

```
CR = (100 + 40 + 20 + 20 + 20 + 100) / 6 = 50.00
```

---

## data2.md Evaluation

### Step-by-step Reasoning

**data2.md claims:** notes-cli is a "command-line tool designed for managing plain text notes" with commands: `notes-cli new`, `notes-cli list`, `notes-cli search`, `notes-cli open`, `notes-cli delete`. Uses `NOTES_DIR` env var with default `~/notes`. License: MIT.

---

**Project Title (T)**

Criteria:
1. Title exactly matches repository/official name → "notes-cli" matches. ✅ V1=1
2. Title does not describe a different project → Correct project. ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucinated terms. ✅ V3=1

**T = (1+1+1)/3 × 100 = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → "command-line tool designed for managing plain text notes efficiently directly from the terminal" — partially correct. It IS a CLI note tool, but notes are markdown, not "plain text." Close enough conceptually. ✅ V1=1
2. Described functionality supported by repository artifacts → "Notes Directory", "Note Files", "Note Metadata", "Note Actions" — these concepts broadly exist. However, "Note Files" described as ".txt or user-defined extensions" is wrong (they are `.md`). ❌ V2=0
3. Overview does not describe unsupported features → "Deleting notes" is listed as a feature — there is no `delete` command (users use `rm`). ❌ V3=0
4. Correctly identifies software domain → "keyboard-driven workflow and plain text note-taking" — correct domain. ✅ V4=1
5. Terminology matches repository terminology → "Notes Directory" (real: "home"), "Note Files" (real: notes/markdown files). Partial mismatch. ❌ V5=0

**O = (1+0+0+1+0)/5 × 100 = 40**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → "Go programming environment (version 1.16 or higher recommended)" — correct. ✅ V1=1
2. Installation commands execute without modification → `git clone ... && cd notes-cli && go build` — same issue as data1: builds at root, not `cmd/notes/`. Does not produce the correct `notes` binary. ❌ V2=0
3. No unresolved dependency errors → `go build` at root won't produce the command binary. ❌ V3=0
4. Documented environment requirements correct → "Go 1.16 or higher" — correct. ✅ V4=1
5. Installation produces expected executable artifact → Produces `notes-cli` not `notes`. ❌ V5=0

**I = (1+0+0+1+0)/5 × 100 = 40**

---

**Usage and Examples (U)**

Snippets evaluated (k=5):

| # | Snippet | Execution Result | Score |
|---|---------|-----------------|-------|
| E1 | `export NOTES_DIR=~/my_notes` | Wrong env var. Real: `NOTES_CLI_HOME`. ❌ | 0 |
| E2 | `notes-cli new "My First Note"` | Wrong binary name (`notes` not `notes-cli`) AND wrong syntax (real: `notes new <category> <filename> [<tags>]`). ❌ | 0 |
| E3 | `notes-cli list` | Wrong binary name. Real binary is `notes`. ❌ | 0 |
| E4 | `notes-cli search keyword` | Wrong binary name AND `search` does not exist. ❌ | 0 |
| E5 | `notes-cli delete "Project Ideas"` | Wrong binary name AND `delete` does not exist. ❌ | 0 |

**U = 0/5 × 100 = 0**

---

**API Reference (A)**

Documented API elements (n=5 commands): `new <title>`, `list`, `search <keyword>`, `open <title>`, `delete <title>`.

| # | Element | Exists | Names Correct | Params Correct | Behavior Correct | Not Deprecated |
|---|---------|--------|--------------|----------------|-----------------|----------------|
| A1 | `new <title>` | Partially — `new` exists but params wrong | ❌ (real: `<category> <filename> [<tags>]`) | ❌ | ❌ | ✅ |
| A2 | `list` | ✅ | ✅ | ✅ | ✅ | ✅ |
| A3 | `search <keyword>` | ❌ Does NOT exist | ❌ | ❌ | ❌ | N/A |
| A4 | `open <title>` | ❌ Does NOT exist | ❌ | ❌ | ❌ | N/A |
| A5 | `delete <title>` | ❌ Does NOT exist | ❌ | ❌ | ❌ | N/A |

Common options: `-h, --help` ✅ exists. `--version` ✅ exists.

Scoring: 1 fully correct out of 5 commands.

**A = 1/5 × 100 = 20**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → "MIT License" — confirmed. ✅ V1=1
2. License identifier is valid → "MIT" is valid. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

LICENSE link: `https://github.com/rhysd/notes-cli/blob/master/LICENSE` — close but actual file is `LICENSE.txt`. Minor URL inaccuracy but license type is correct.

**L = (1+1+1)/3 × 100 = 100**

---

### data2.md Final Score

```
CR = (100 + 40 + 40 + 0 + 20 + 100) / 6 = 50.00
```

---

## data3.md Evaluation

### Step-by-step Reasoning

**data3.md claims:** notes-cli is a "simple and lightweight command-line tool for managing and manipulating personal notes stored as plain text files" with commands: `notes edit`, `notes search`, `notes list`, `notes show`. Includes Homebrew install `brew install rhysd/tap/notes-cli`. Uses `NOTES_DIR` env var. License: MIT.

---

**Project Title (T)**

Criteria:
1. Title exactly matches repository/official name → "notes-cli" matches. ✅ V1=1
2. Title does not describe a different project → Correct project. ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucinated terms. ✅ V3=1

**T = (1+1+1)/3 × 100 = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → "simple and lightweight command-line tool for managing and manipulating personal notes stored as plain text files" — partially correct. It IS a CLI note tool, but notes are markdown, not "plain text." ✅ V1=1
2. Described functionality supported by repository artifacts → "Notes as Files", "Note Searching", "Note Editing", "Tagging", "Note Listing and Filtering", "Metadata" — most concepts exist. Searching is done via external tools, not built-in. Tagging exists in note metadata. ❌ V2=0
3. Overview does not describe unsupported features → "Supports searching notes by keywords or tags" as a built-in feature — searching is NOT built-in, it's done via external tools. ❌ V3=0
4. Correctly identifies software domain → "note-taking domain by treating notes as lightweight text files and providing commands for common workflows" — correct domain. ✅ V4=1
5. Terminology matches repository terminology → "Tagging", "Metadata" match. "Note Searching" as built-in doesn't match. Partial. ❌ V5=0

**O = (1+0+0+1+0)/5 × 100 = 40**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → "Go 1.13 or later installed" — close (real minimum is 1.16). ❌ V1=0
2. Installation commands execute without modification → `brew install rhysd/tap/notes-cli` — this Homebrew tap is NOT documented in the official README and likely does not exist. `git clone ... && cd notes-cli && make build` — there is no Makefile in the repository (checked: no `Makefile` in repo contents). ❌ V2=0
3. No unresolved dependency errors → `make build` would fail (no Makefile). ❌ V3=0
4. Documented environment requirements correct → "Go 1.13 or later" — wrong minimum version. ❌ V4=0
5. Installation produces expected executable artifact → `make build` would fail. Binary download from releases is mentioned and correct conceptually. Partial. ❌ V5=0

**I = (0+0+0+0+0)/5 × 100 = 0**

---

**Usage and Examples (U)**

Snippets evaluated (k=5):

| # | Snippet | Execution Result | Score |
|---|---------|-----------------|-------|
| E1 | `notes edit mynote` | `edit` subcommand does NOT exist. Real command for creating/editing is `notes new <category> <filename>` or `notes list --edit`. ❌ | 0 |
| E2 | `notes search keyword` | `search` subcommand does NOT exist. ❌ | 0 |
| E3 | `notes list` | This command exists and works. ✅ | 1 |
| E4 | `notes list -t tagname` | The `-t` flag exists for filtering by tag. ✅ | 1 |
| E5 | `notes show mynote` | `show` subcommand does NOT exist. ❌ | 0 |

**U = 2/5 × 100 = 40**

---

**API Reference (A)**

Documented API elements (n=4 commands): `notes edit [note-name]`, `notes search [pattern]`, `notes list`, `notes show [note-name]`.

| # | Element | Exists | Names Correct | Params Correct | Behavior Correct | Not Deprecated |
|---|---------|--------|--------------|----------------|-----------------|----------------|
| A1 | `notes edit [note-name]` | ❌ Does NOT exist | ❌ | ❌ | ❌ | N/A |
| A2 | `notes search [pattern]` with `-t/--tag` | ❌ Does NOT exist | ❌ | ❌ | ❌ | N/A |
| A3 | `notes list` with `-t/--tag` and `-r/--recent` | Partially — `list` exists, `-t/--tag` exists, but `-r/--recent` does NOT exist (real sort flag is `--sort/-s modified`) | ✅ exists | ❌ `-r/--recent` wrong | ❌ partial | ✅ |
| A4 | `notes show [note-name]` | ❌ Does NOT exist | ❌ | ❌ | ❌ | N/A |

Environment: `NOTES_DIR` — WRONG (real: `NOTES_CLI_HOME`). `$EDITOR` — partially correct (real primary: `$NOTES_CLI_EDITOR`). "Tags are recognized as words prefixed with `#`" — tags are actually defined in note metadata header, not by `#` prefix in content.

Scoring: `notes list` partially correct (exists with some correct flags but `-r/--recent` is hallucinated). Counting as 0.5. Others are non-existent.

**A = 0.5/4 × 100 = 12.5**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → "MIT License" — confirmed. ✅ V1=1
2. License identifier is valid → "MIT" is valid. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

LICENSE link: `https://github.com/rhysd/notes-cli/blob/master/LICENSE` — actual file is `LICENSE.txt`, minor URL inaccuracy but type is correct.

**L = (1+1+1)/3 × 100 = 100**

---

### data3.md Final Score

```
CR = (100 + 40 + 0 + 40 + 12.5 + 100) / 6 = 48.75
```

---

## Summary: All Three notes-cli READMEs

| README | T | O | I | U | A | L | CR |
|--------|---|---|---|---|---|---|-----|
| data1.md | 100 | 40 | 20 | 20 | 20 | 100 | **50.00** |
| data2.md | 100 | 40 | 40 | 0 | 20 | 100 | **50.00** |
| data3.md | 100 | 40 | 0 | 40 | 12.5 | 100 | **48.75** |
| **Average** | **100** | **40** | **20** | **20** | **17.5** | **100** | **49.58** |

### Final Average Score (Equation 2 from TCC)

```
Score_avg = (50.00 + 50.00 + 48.75) / 3 = 49.58
```

---

## Analysis and Observations

**Why scores are around 50:**

`notes-cli` (`rhysd/notes-cli`) is a moderate-low popularity repository (260 stars) with a detailed README but a unique CLI design that differs from typical note-taking tools. The LLM partially understood the tool's purpose but hallucinated many commands and details.

The LLM failed on this repository because:

1. **Hallucinated subcommands:** All three READMEs invented commands that do not exist (`search`, `open`, `delete`, `edit`, `show`, `index`). The real tool deliberately delegates searching to external tools like `grep`, `ag`, `rg` piped with `notes list`. This is a core design philosophy the LLM missed.

2. **Wrong `new` command syntax:** All three READMEs described `notes new <title>` or `notes new "title"`. The real syntax is `notes new <category> <filename> [<tags>]` — requiring both a category and filename as separate arguments. This is a fundamental misunderstanding of the tool's category-based organization.

3. **Wrong environment variables:** All three READMEs used `NOTES_DIR` with default `~/notes`. The real env var is `NOTES_CLI_HOME` with default `~/.local/share/notes-cli` (XDG data directory). This is a significant factual error.

4. **Wrong binary name (data2.md):** data2.md used `notes-cli` as the binary name. The actual binary is `notes`.

5. **Wrong file format:** All three described notes as "plain text files" or `.txt` files. The real tool creates **markdown** (`.md`) files with structured metadata headers.

6. **Hallucinated installation methods:** data3.md invented a Homebrew formula and a `make build` command that don't exist. data1.md and data2.md's `go build` at repo root doesn't produce the correct binary.

**What the LLM got right:**
- Project name and general domain (CLI note-taking)
- License type (MIT)
- `notes list` command exists in all three
- General concept of tags and editor integration
- Go as the implementation language

**Root cause:** The LLM appears to have conflated `notes-cli` with generic note-taking CLI patterns (like `notes.sh` or similar tools) that have `search`, `open`, `delete` commands. The real `notes-cli` has a Unix philosophy design where it provides minimal built-in commands and relies on composability with external tools. This design pattern is unusual enough that the LLM defaulted to more common note-taking CLI patterns.

**This result validates the TCC's hypothesis** that moderate-popularity repositories with unique design patterns can still challenge LLM-based README generation, as the model may substitute common patterns from similar tools rather than accurately reflecting the specific tool's actual interface.
