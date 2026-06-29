# notes-cli — ATORAK Adherence Evaluation

**Methodology:** Section 4.4.3 of *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis*.

**Theory of Robust API Knowledge (ATORAK)** [Thayer et al. 2021] defines three Knowledge Elements that a robust API document must communicate:

- **KD — Domain Concepts:** The fundamental entities and abstractions that define the problem domain addressed by the software. Manifested through class names, variable names, data models, and terminology used in documentation.
- **KE — Execution Facts:** How the software behaves during execution — function inputs/outputs, return types, dependencies, side effects, configuration requirements, and runtime constraints.
- **KU — Usage Patterns:** Typical ways in which the software is intended to be used, expressed through code examples, test cases, tutorials, and build/deployment pipelines. Support learning by demonstration.

Each element is binary: Ki ∈ {0, 1}. The adherence score per README is:

```
Kpercentage = (KD + KE + KU) / 3 × 100
```

The final score across the three generated READMEs is:

```
Kavg = (K1 + K2 + K3) / 3
```

> **Scope:** This evaluation assesses only **completeness** — whether each Knowledge Element is present in the README. Correctness of the content is out of scope per the task definition.

---

## Ground Truth Reference

- Tool: **notes-cli** — lightweight command-line note-taking tool (Go)
- Repository: https://github.com/rhysd/notes-cli
- Domain: CLI note management, plain text files, terminal workflows
- Core domain entities: Notes (plain text files), Tags, Note Directory, Editor Integration, Indexing, Search, Metadata
- Core execution facts: `notes new <title>`, `notes list`, `notes search <query>`, `notes open <title>`, `notes index`, `notes edit [note-name]`, `notes show [note-name]`, `notes delete <title>`, env vars `NOTES_DIR`, `EDITOR`
- License: MIT

---

## data1.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

The README must represent the fundamental entities and abstractions that define the notes-cli domain.

**Evidence in data1.md:**

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **Notes** — "Plain text files representing pieces of information or thoughts, typically stored in a directory structure." ✅ Correctly identifies the core entity of the domain.
- **Tags** — "Keywords or labels attached to notes to categorize and retrieve them easily." ✅ Correctly defines the tagging abstraction.
- **Indexing** — "Creating an efficient search index over notes for rapid text and tag-based querying." ✅ Correctly identifies indexing as a domain concept.
- **Commands** — "The CLI interface exposes commands for creating, listing, searching, and organizing notes." ✅ Correctly identifies the command-based interaction model.
- **Editor Integration** — "Uses the user's environment editor (e.g., `vim`, `nano`) for editing notes." ✅ Correctly identifies the editor integration concept.
- **Note Directory** — "A designated folder containing all note files." ✅ Correctly identifies the storage abstraction.

The overview also correctly describes notes-cli as a "fast and lightweight command-line note-taking tool designed to help users quickly create, manage, and search plain text notes."

**Assessment:** data1.md contains a dedicated "Domain Concepts" subsection in the Overview with six clearly defined entities. All six entities are relevant to the notes-cli domain and correctly named. The conceptual vocabulary (Notes, Tags, Indexing, Editor Integration, Note Directory) matches the tool's actual domain. KD is fully satisfied.

**KD = 1** ✅

---

#### KE — Execution Facts

The README must represent concrete, verifiable facts about how notes-cli behaves at runtime — commands, parameters, environment requirements, installation steps, and behavioral descriptions.

**Evidence in data1.md:**

*Installation facts:*
- Prerequisites: Go 1.12+, Unix-like OS. ✅ Dependency declared.
- `git clone https://github.com/rhysd/notes-cli.git && cd notes-cli && go build` — build from source. ✅
- `mv notes-cli /usr/local/bin/` — installation to PATH. ✅
- Download from GitHub releases page. ✅

*Environment variables:*
- `NOTES_DIR` — "Path to the notes directory (default: `~/notes`)." ✅
- `EDITOR` — "Text editor to open notes (default: `vim`)." ✅

*API Reference (CLI Commands) — 5 commands documented:*
- `notes new <title>` — parameters: `<title>` (string); behavior: opens `$EDITOR`, saves to notes directory. ✅
- `notes list` — output: titles with creation/modification timestamps. ✅
- `notes search <query>` — parameters: `<query>` (text or `#tag`); returns: list sorted by relevance/recency. ✅
- `notes open <title>` — parameters: `<title>`. ✅
- `notes index` — purpose: precomputes search index; runs automatically on create/edit. ✅

**Assessment:** data1.md provides concrete execution facts across all required dimensions: installation commands, environment variable requirements with defaults, and a dedicated "API Reference (CLI Commands)" section documenting 5 commands with parameters and behavioral descriptions. KE is fully satisfied.

**KE = 1** ✅

---

#### KU — Usage Patterns

The README must present recurring, purposeful combinations of API calls that solve real problems, communicating *what*, *how*, and *why*.

**Evidence in data1.md:**

The "Usage and Examples" section presents the following patterns:

1. **Setting the Notes Directory** — `export NOTES_DIR=~/my_notes`: *What*: configure storage location. *How*: set env var. *Why*: customize where notes are stored. ✅
2. **Create a new note** — `notes new "My first note"`: *What*: create a note. *How*: `notes new` with title argument. *Why*: opens editor to enter content. ✅
3. **List all notes** — `notes list`: *What*: see all notes. *How*: `notes list`. ✅
4. **Search notes by text** — `notes search "meeting notes"`: *What*: find notes by content. *How*: `notes search` with query. ✅
5. **Search using tags** — `notes search "#todo"`: *What*: find notes by tag. *How*: prefix query with `#`. ✅
6. **Open an existing note** — `notes open "My first note"`: *What*: edit an existing note. *How*: `notes open` with title. ✅
7. **Indexing notes** — `notes index`: *What*: update search index. *How*: run `notes index`. *Why*: ensures up-to-date search results when notes are manipulated externally. ✅

**Assessment:** data1.md presents seven distinct usage patterns covering the full notes-cli workflow. Each pattern includes a code snippet and a prose explanation. The patterns progress from configuration to creation, listing, searching, and maintenance. The *what* and *how* are clearly communicated. The *why* is present in several patterns (e.g., indexing for up-to-date results, tags for categorization). KU is fully satisfied.

**KU = 1** ✅

---

### data1.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data1.md ATORAK Score: 100**

---

## data2.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

**Evidence in data2.md:**

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **Notes Directory** — "A folder where all notes are stored as individual text files." ✅ Correctly identifies the storage container abstraction.
- **Note Files** — "Plain text files representing individual notes, typically with `.txt` or user-defined extensions." ✅ Correctly identifies the core entity.
- **Note Metadata** — "Basic metadata such as creation time and modification time associated with each note file." ✅ Correctly identifies metadata as a domain concept.
- **Search & Filter** — "Mechanisms to quickly find notes by keywords or patterns." ✅ Correctly identifies search as a domain abstraction.
- **Note Actions** — "Creating new notes, listing notes, opening existing notes in an editor, and deleting notes." ✅ Correctly identifies the action vocabulary of the domain.

**Assessment:** data2.md contains a dedicated "Domain Concepts" subsection with five clearly defined entities. The entities cover the core domain vocabulary: storage (Notes Directory, Note Files), metadata, search, and actions. Notably, this README does not explicitly list "Tags" or "Indexing" as domain concepts (unlike data1.md and data3.md), but it does mention tags implicitly in the search description. The five listed concepts are sufficient to represent the domain conceptual space. KD is satisfied.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data2.md:**

*Installation facts:*
- Prerequisites: Go 1.16+. ✅
- `git clone ... && go build` — build from source. ✅
- Prebuilt binaries from GitHub releases. ✅

*Environment variables:*
- `NOTES_DIR` — "If not set, it uses `~/notes`." ✅
- `$EDITOR` or `vi` as default editor. ✅

*API Reference — 5 commands documented:*
- `new <title>` — creates note, opens in editor, handles overwrite prompt. ✅
- `list` — lists all note files with filenames. ✅
- `search <keyword>` — searches all notes, outputs matching files. ✅
- `open <title>` — opens note in editor, prompts on multiple matches. ✅
- `delete <title>` — deletes note, asks for confirmation. ✅

*Common Options:*
- `-h, --help` — show help. ✅
- `--version` — show version. ✅

**Assessment:** data2.md provides concrete execution facts: installation steps with prerequisites, environment variable requirements with defaults, and a dedicated "API Reference" section documenting 5 commands with parameters and behavioral descriptions. It additionally documents common options (`--help`, `--version`). KE is fully satisfied.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data2.md:**

The "Usage and Examples" section presents the following patterns:

1. **Setting Notes Directory** — `export NOTES_DIR=~/my_notes`: *What*: configure storage. *How*: set env var. ✅
2. **Creating a New Note** — `notes-cli new "My First Note"`: *What*: create a note. *How*: `notes-cli new` with title. *Why*: opens editor, creates file. ✅ Includes output example showing the created filename.
3. **Listing Notes** — `notes-cli list`: *What*: see all notes. *How*: `notes-cli list`. Includes example output. ✅
4. **Searching Notes** — `notes-cli search keyword`: *What*: find notes by keyword. *How*: `notes-cli search`. ✅
5. **Opening a Note** — `notes-cli open "Meeting Notes"`: *What*: edit existing note. *How*: `notes-cli open`. *Why*: prompts on multiple matches. ✅
6. **Deleting a Note** — `notes-cli delete "Project Ideas"`: *What*: remove a note. *How*: `notes-cli delete`. ✅

**Assessment:** data2.md presents six distinct usage patterns covering the full notes-cli workflow. Each pattern includes a code snippet. Notably, data2.md includes an output example for the `list` command, which adds concreteness. The delete pattern is unique to this README among the three. The *what* and *how* are clearly communicated for all patterns. KU is fully satisfied.

**KU = 1** ✅

---

### data2.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data2.md ATORAK Score: 100**

---

## data3.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

**Evidence in data3.md:**

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **Notes as Files** — "Individual notes are stored as plain text files in a user-specified directory." ✅ Correctly identifies the core entity and its storage model.
- **Note Searching** — "Supports searching notes by keywords or tags." ✅ Correctly identifies search as a domain concept.
- **Note Editing** — "Launches the user's preferred terminal editor to create or modify notes." ✅ Correctly identifies editor integration as a domain concept.
- **Tagging** — "Enables categorizing notes with tags for easier retrieval." ✅ Correctly identifies tagging as a domain concept.
- **Note Listing and Filtering** — "Lists notes with optional filters such as by recent activity or tags." ✅ Correctly identifies listing/filtering as a domain concept.
- **Metadata** — "Notes can include metadata such as creation date and tags inside the file content." ✅ Correctly identifies metadata as a domain concept.

**Assessment:** data3.md contains a dedicated "Domain Concepts" subsection with six clearly defined entities. The entities cover the full domain vocabulary: storage model (Notes as Files), search, editing, tagging, listing/filtering, and metadata. This is the most complete domain concept representation of the three READMEs, explicitly naming both "Tagging" and "Metadata" as separate concepts. KD is fully satisfied.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data3.md:**

*Installation facts:*
- Prerequisites: Go 1.13+. ✅
- `brew install rhysd/tap/notes-cli` — Homebrew installation (unique to this README). ✅
- `git clone ... && make build` — build from source. ✅
- Prebuilt binaries from GitHub releases. ✅

*Environment variables:*
- `NOTES_DIR` — "Default location is `~/notes`." ✅
- `$EDITOR` — editor selection. ✅
- Tags recognized as words prefixed with `#`. ✅

*API Reference — 4 commands documented:*
- `notes edit [note-name]` — opens in `$EDITOR`, creates if not exists. ✅
- `notes search [pattern]` — parameters: `pattern` (string), `-t/--tag` (optional); supports regex. ✅
- `notes list` — options: `-t/--tag`, `-r/--recent`. ✅
- `notes show [note-name]` — prints note content to terminal. ✅

**Assessment:** data3.md provides concrete execution facts: three installation methods (Homebrew, prebuilt binaries, source), environment variable requirements, and a dedicated "API Reference" section documenting 4 commands with parameters, options, and behavioral descriptions. Notably, it documents the `-t/--tag` and `-r/--recent` flags for `list` and `search`, and explicitly states regex support for search. KE is fully satisfied.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data3.md:**

The "Usage and Examples" section presents the following patterns, including a dedicated "Sample Workflows" subsection:

1. **Create or Edit a Note** — `notes edit mynote`: *What*: create or update a note. *How*: `notes edit`. *Why*: if note doesn't exist, a new file is created. ✅
2. **Search Notes by text** — `notes search keyword`: *What*: find notes by content. *How*: `notes search`. ✅
3. **Search Notes by tag** — `notes search -t tagname`: *What*: find notes by tag. *How*: `notes search -t`. ✅
4. **List Notes** — `notes list`: *What*: see all notes. *How*: `notes list`. ✅
5. **List Notes by tag** — `notes list -t tagname`: *What*: filter notes by tag. *How*: `notes list -t`. ✅
6. **Show Note Content** — `notes show mynote`: *What*: display note in terminal. *How*: `notes show`. ✅

*Sample Workflows (composite patterns):*
7. **Add a new note** — `notes edit "project-ideas"` with editor interaction. *What*: full note creation workflow. *How*: edit → write → save. ✅
8. **Search notes containing "meeting"** — `notes search meeting`. ✅
9. **List notes tagged as "todo"** — `notes list -t todo`. ✅
10. **View the content of a note** — `notes show project-ideas`. ✅

**Assessment:** data3.md presents the richest usage pattern coverage of the three READMEs. It includes both individual command examples and a dedicated "Sample Workflows" section with four composite patterns. The tag-based filtering patterns (`-t tagname`) are unique to this README and represent important real-world usage. The *what* and *how* are clearly communicated for all patterns. KU is fully satisfied.

**KU = 1** ✅

---

### data3.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data3.md ATORAK Score: 100**

---

## Summary: All Three notes-cli READMEs — ATORAK Adherence

| README | KD (Domain Concepts) | KE (Execution Facts) | KU (Usage Patterns) | Kpercentage |
|--------|---------------------|---------------------|---------------------|-------------|
| data1.md | 1 | 1 | 1 | **100** |
| data2.md | 1 | 1 | 1 | **100** |
| data3.md | 1 | 1 | 1 | **100** |

### Final Average Score (Equation 16 from TCC §4.4.3)

```
Kavg = (100 + 100 + 100) / 3 = 100
```

**notes-cli ATORAK Average Score: 100**

---

## Analysis and Observations

**Why all three score 100 on ATORAK adherence:**

notes-cli is a Go-based CLI tool with a well-defined and narrow domain (plain text note management). The tool's domain concepts, execution facts, and usage patterns are straightforward and consistently represented across all three generated READMEs.

**KD (Domain Concepts) — all three score 1:**
All three READMEs include an explicit "Domain Concepts" subsection in the Overview. data1.md defines 6 concepts (Notes, Tags, Indexing, Commands, Editor Integration, Note Directory). data2.md defines 5 concepts (Notes Directory, Note Files, Note Metadata, Search & Filter, Note Actions). data3.md defines 6 concepts (Notes as Files, Note Searching, Note Editing, Tagging, Note Listing and Filtering, Metadata). Each README correctly identifies the core entities of the notes-cli domain.

**KE (Execution Facts) — all three score 1:**
All three READMEs provide installation instructions with prerequisites, environment variable documentation (`NOTES_DIR`, `EDITOR`), and a dedicated API Reference section documenting CLI commands with parameters and behavioral descriptions. data3.md uniquely documents the Homebrew installation method and the `-t/--tag` and `-r/--recent` flags. data2.md uniquely documents the `delete` command and `--version`/`--help` options.

**KU (Usage Patterns) — all three score 1:**
All three READMEs present multiple named usage patterns with code snippets covering the core notes-cli workflows (create, list, search, open/edit). data1.md covers 7 patterns including tag-based search and manual indexing. data2.md covers 6 patterns including note deletion. data3.md covers 10 patterns including a dedicated "Sample Workflows" section with composite patterns and tag-based filtering.

**Qualitative differences (not affecting binary ATORAK score):**
- data1.md: Most structured API Reference with explicit parameter types and behavioral descriptions; includes `notes index` command.
- data2.md: Only README to document `delete` command and `--help`/`--version` options; includes output example for `list`.
- data3.md: Richest usage pattern coverage with Sample Workflows section; only README to document Homebrew installation and tag/recent flags for `list` and `search`.

**This result is consistent with the TCC's hypothesis** that tools with a clear, narrow domain and well-defined CLI interface are reliably documented by LLM-based README generation. The notes-cli domain is simple enough that all three knowledge elements are naturally and correctly present in every generated README.
