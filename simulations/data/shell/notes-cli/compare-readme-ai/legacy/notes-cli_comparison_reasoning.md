# notes-cli README Comparison: Paper Tool (README-Gen) vs readme-ai

**Evaluator Perspective:** Senior Computer Science Scientist — Documentation Quality Assessment

**Methodology:** This comparison applies the evaluation framework from *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis* (Andrade & Ribeiro, UERJ), including Completeness (§4.4.1), Correctness (§4.4.2), and ATORAK Adherence (§4.4.3), to compare the paper's generated READMEs against the output of [readme-ai](https://github.com/eli64s/readme-ai).

---

## Selection of Best and Worst Paper-Generated READMEs

The correctness scores for notes-cli are:
- data1.md: CR = 50.00 (T:100, O:40, I:20, U:20, A:20, L:100)
- data2.md: CR = 50.00 (T:100, O:40, I:40, U:0, A:20, L:100)
- data3.md: CR = 48.75 (T:100, O:40, I:0, U:40, A:12.5, L:100)

All three scored 100 on ATORAK adherence and completeness. Selection is based on correctness scores and qualitative differentiation.

### Best: data1.md

**Rationale:**
- **Tied for highest correctness score** (50.00), balanced performance across all sections
- **Uses the correct binary name** (`notes`) throughout all examples — data2.md incorrectly uses `notes-cli` as the binary, which breaks every usage example
- **Most balanced coverage**: Scores >0 in all sections (I:20, U:20, A:20), unlike data2.md (U:0) or data3.md (I:0)
- **Correct `notes list` command**: The one usage example that works (`notes list`) uses the right binary name
- **Clear, structured API Reference**: 5 documented commands with parameters and behavioral descriptions
- **Consistent presentation**: Professional, well-organized documentation structure throughout

### Worst: data3.md

**Rationale:**
- **Lowest overall correctness score** (48.75)
- **Completely incorrect installation section** (I:0): Fabricates a Homebrew formula (`brew install rhysd/tap/notes-cli`) that doesn't exist; references a non-existent `Makefile`; states wrong Go version minimum (1.13 vs real 1.16)
- **Lowest API Reference score** (12.5): Documents only 4 commands, and introduces hallucinated flags (`-r/--recent` for `list`)
- **Hallucinated commands**: `notes edit`, `notes show`, and `notes search` don't exist in the real tool
- **Most misleading for new users**: The Homebrew install command would fail immediately, creating a frustrating first experience

---

## readme-ai Output Analysis (notes_readme_readmeai.md)

### Structure and Format

The readme-ai output differs fundamentally in approach and structure from the paper tool:

| Aspect | Paper Tool (README-Gen) | readme-ai |
|--------|------------------------|-----------|
| Primary focus | Developer-facing API/CLI documentation | Repository/project overview for contributors |
| Structure | Overview → Installation → Usage → API Reference → License | Overview → Features → Project Structure → Getting Started → Contributing |
| Content depth | CLI command documentation with parameters and examples | High-level architectural file-by-file descriptions |
| Code examples | Multiple command-line snippets demonstrating workflows | Only `git clone`, `go build`, `go test ./...` |
| API Reference | Complete CLI command documentation with parameters | Absent |
| Domain concepts | Explicitly defined (Notes, Tags, Indexing, etc.) | Implicitly described in Features table |
| Target audience | End-users wanting to use notes-cli | Contributors/maintainers exploring the codebase |
| Correctness of claims | Hallucinated commands but correct project identity | Mostly avoids specific claims; some incorrect inferences |

### Detailed Assessment

#### KD — Domain Concepts

**readme-ai:** The Features table mentions "CLI tool written in Go", "Modular command structure using kingpin.v2", "File-based note management leveraging filesystem conventions", and "Single binary distribution with embedded update mechanism". These are architectural observations about the codebase, not domain concept definitions.

The tool correctly identifies:
- Go as the language ✅
- kingpin.v2 for CLI parsing ✅
- go-github-selfupdate for self-update ✅
- File-based note management ✅
- Shell completions for bash, fish, and zsh ✅

However, it makes some incorrect inferences:
- "OAuth2 and protobuf dependencies suggest possible external API or config integrations" — these are transitive dependencies, not features ❌
- "No dedicated documentation files detected" — the real repo has a README.md ❌
- "No explicit test files or directories detected" — the repo has extensive `*_test.go` files visible in its own Project Structure section ❌ (contradicts itself)

**Verdict:** Domain concepts are *not communicated* in the ATORAK sense. The Features table describes code architecture, not the user-facing domain vocabulary (notes, categories, tags, saving to git). A user reading this would not learn what notes-cli does conceptually.

**KD = 0** (does not satisfy ATORAK's requirement for conceptual vocabulary teaching)

#### KE — Execution Facts

**readme-ai:**
- Installation: `git clone` + `go build` — this is partially correct but produces the wrong binary (builds at repo root, not `cmd/notes/`). The official installation is `go install github.com/rhysd/notes-cli/cmd/notes` or downloading from releases.
- Usage: `go run {entrypoint}` — a **template placeholder that was not resolved** ❌
- Testing: `go test ./...` — this is actually correct for running the test suite ✅
- Testing framework: `{__test_framework__}` — another **unresolved template placeholder** ❌
- No CLI command documentation whatsoever
- No environment variable documentation
- No subcommand listing

**Verdict:** Execution facts are either template placeholders (unresolved), partially incorrect (installation), or absent (no CLI commands documented). The one correct fact (`go test ./...`) is about development, not end-user operation.

**KE = 0** (fails to provide correct, verifiable runtime facts for CLI end-users)

#### KU — Usage Patterns

**readme-ai:** No code examples demonstrating how to USE notes-cli as an end-user. The Getting Started section only shows how to clone and build the repository. No `notes new`, `notes list`, `notes save`, or any subcommand usage whatsoever.

**Verdict:** Zero usage patterns for end-users of the tool.

**KU = 0** (no purposeful combinations of CLI commands solving real problems)

---

## Comparative Analysis: Best Paper README (data1.md) vs readme-ai

| Criterion | data1.md (Best) | readme-ai | Winner |
|-----------|----------------|-----------|--------|
| **Project Title** | "notes-cli" — correct, matches repo name | "NOTES-CLI" — uppercase stylistic deviation | data1.md |
| **Overview** | Describes functionality: "fast and lightweight command-line note-taking tool" | Empty (Overview section has no content) | data1.md |
| **Domain Concepts** | 6 concepts with definitions (Notes, Tags, Indexing, Commands, Editor Integration, Note Directory) | Implicit architectural descriptions only | data1.md |
| **Installation** | Partially correct: `go build` at root (wrong binary path) but correct releases link | Partially correct: same `go build` issue, has template placeholders | data1.md |
| **Usage Examples** | 7 code snippets covering full workflow (create, list, search, open, tag, index) | None (only `go run {entrypoint}` placeholder) | data1.md |
| **API Reference** | 5 commands with parameters and behavioral descriptions | Absent | data1.md |
| **License** | MIT — correct | Generic choosealicense.com link, not actual license | data1.md |
| **Project Structure** | Not included | Comprehensive file tree with file-by-file summaries | readme-ai |
| **Contributing Guide** | Not included | Full contributing workflow with steps | readme-ai |
| **CI/CD Information** | Not included | GitHub Actions CI workflow described | readme-ai |
| **Code Quality Insights** | Not included | Mentions go.mod, linting, Go ecosystem standards | readme-ai |
| **Shell Completions** | Not documented | Fish and Zsh completions documented in structure | readme-ai |
| **Visual Presentation** | Clean markdown, no badges | Badges (license, last-commit, language), logo, styled HTML | readme-ai |
| **Factual Accuracy** | Many hallucinated commands (search, open, index), wrong env vars | Avoids specific CLI claims; some incorrect inferences about OAuth2/protobuf | Mixed |

### Summary

data1.md is clearly superior for its intended purpose: **teaching users how to use notes-cli**. Despite hallucinating several commands (search, open, index) and getting the environment variable wrong (`NOTES_DIR` vs real `NOTES_CLI_HOME`), it provides a coherent mental model of a CLI note-taking tool with explicit domain concepts, concrete usage patterns, and a structured API reference.

readme-ai excels at **documenting the repository for contributors**: it provides a detailed project structure tree, per-file descriptions of source code purpose, CI/CD pipeline documentation, and a contributing guide. However, it completely fails to communicate what notes-cli does from an end-user perspective.

---

## Comparative Analysis: Worst Paper README (data3.md) vs readme-ai

| Criterion | data3.md (Worst) | readme-ai | Winner |
|-----------|-----------------|-----------|--------|
| **Project Title** | "notes-cli" — correct | "NOTES-CLI" — uppercase | data3.md |
| **Overview** | "simple and lightweight command-line tool for managing personal notes" — meaningful | Empty section | data3.md |
| **Domain Concepts** | 6 concepts with definitions (Notes as Files, Searching, Editing, Tagging, Listing, Metadata) | Implicit mentions in Features table | data3.md |
| **Installation** | Completely incorrect: fake Homebrew formula, non-existent Makefile | Partially correct: `git clone` + `go build` (wrong path but would compile something) | readme-ai |
| **Usage Examples** | 10 patterns including workflows (edit, search, list, show, tag filtering) | None (template placeholder only) | data3.md |
| **API Reference** | 4 commands with parameters and options documented | Absent | data3.md |
| **License** | MIT — correct | Generic link, not actual license file | data3.md |
| **Project Structure** | Not included | Comprehensive file tree | readme-ai |
| **Contributing Guide** | Not included | Full workflow | readme-ai |
| **Correctness of Installation** | 0/100 — fabricated Homebrew tap, no Makefile exists | Partial — `go build` at root compiles but wrong binary | readme-ai |
| **Command Correctness** | 12.5/100 — most commands don't exist (edit, show, search) | N/A — no commands documented | data3.md (at least attempts) |
| **Tag Documentation** | Documents `-t/--tag` flag (partially correct — flag exists on `list`) | Not documented | data3.md |

### Summary

data3.md, despite being the worst paper-generated README, still provides significantly more user-facing documentation than readme-ai. Its 10 usage patterns and 4 documented commands give a reader a (flawed but useful) mental model of what the tool does. The critical failure is in installation — a user following data3.md's Homebrew command would immediately fail.

readme-ai avoids this problem by not making specific CLI claims, but the tradeoff is that it provides zero guidance on how to actually use the tool. A user reading readme-ai would understand the code architecture but would have no idea how to run `notes new`, `notes list`, or any other subcommand.

Interestingly, for installation specifically, readme-ai is marginally better than data3.md: `go build` at the repo root would at least compile (producing a library, not the binary), while `brew install rhysd/tap/notes-cli` and `make build` would both fail outright.

---

## Scoring: readme-ai Under the Paper's Framework

### Completeness (§4.4.1)

| Section | Present? | Score |
|---------|----------|-------|
| Project Title | ✅ "NOTES-CLI" present | 1 |
| Overview | ❌ Section exists but is empty | 1 (section header present) |
| Installation | ✅ `git clone` + `go build` instructions provided | 1 |
| Usage and Examples | ❌ Only `go run {entrypoint}` placeholder | 0 |
| API Reference | ❌ Absent | 0 |
| License | ✅ License section present (generic link) | 1 |
| Core Functionality | ❌ No CLI commands or features described for end-users | 0 |

### Correctness (§4.4.2)

**Project Title (T):**
1. Title matches repository name → "NOTES-CLI" (uppercase but matches). ✅ V1=1
2. Does not describe a different project → Correct project. ✅ V2=1
3. No hallucinated terminology → Clean. ✅ V3=1

**T = 100**

**Overview (O):**
1. Primary functionality correctly described → Empty section. ❌ V1=0
2. Described functionality supported by artifacts → No claims made. N/A → ❌ V2=0
3. No unsupported features described → No claims (empty). ✅ V3=1
4. Correctly identifies software domain → Not stated. ❌ V4=0
5. Terminology matches repository → No terminology used. ❌ V5=0

**O = (0+0+1+0+0)/5 × 100 = 20**

**Installation (I):**
1. Dependencies declared → "Go" and "Go modules" listed. ✅ V1=1
2. Commands execute without modification → `git clone` + `go build` would compile at root, but doesn't produce the correct `notes` binary (need `cmd/notes/`). Partial. ❌ V2=0
3. No unresolved dependency errors → `go build` at root would succeed (builds the library). ✅ V3=1
4. Environment requirements correct → "Go" and "Go modules" — correct but no version specified. Partial. ❌ V4=0
5. Produces expected artifact → Does not produce the `notes` binary. ❌ V5=0

**I = (1+0+1+0+0)/5 × 100 = 40**

**Usage and Examples (U):**
- `go run {entrypoint}` — unresolved template placeholder, non-executable. ❌
- No other usage examples for end-users.

**U = 0/5 × 100 = 0**

**API Reference (A):**
- No API elements documented.

**A = 0**

**License (L):**
1. License matches → Links to generic choosealicense.com, not the actual MIT LICENSE.txt. The section text says "protected under the LICENSE License" — does not name MIT. ❌ V1=0
2. Valid identifier → No specific identifier given. ❌ V2=0
3. No conflicting info → Only one (vague) license mention. ✅ V3=1

**L = (0+0+1)/3 × 100 = 33.33**

**Final Correctness Score:**
```
CR = (100 + 20 + 40 + 0 + 0 + 33.33) / 6 = 32.22
```

### ATORAK Adherence (§4.4.3)

| Knowledge Element | Present? | Score |
|-------------------|----------|-------|
| KD — Domain Concepts | ❌ No user-facing domain vocabulary taught | 0 |
| KE — Execution Facts | ❌ No CLI commands, env vars, or runtime behavior | 0 |
| KU — Usage Patterns | ❌ No purposeful CLI usage demonstrations | 0 |

**ATORAK Score = 0**

---

## Final Comparative Summary

| Metric | data1.md (Best) | data3.md (Worst) | readme-ai |
|--------|----------------|-----------------|-----------|
| **Correctness (CR)** | 50.00 | 48.75 | 32.22 |
| **ATORAK Score** | 100 | 100 | 0 |
| **Completeness** | 7/7 sections | 7/7 sections | 4/7 sections |
| **Domain Concepts** | 6 defined | 6 defined | 0 formal definitions |
| **Usage Patterns** | 7 examples | 10 examples | 0 examples |
| **API Reference** | 5 commands | 4 commands | 0 commands |
| **Correct Installation** | Partial (20%) | Failed (0%) | Partial (40%) |
| **Project Structure** | Not included | Not included | Comprehensive |
| **Contributing Guide** | Not included | Not included | Full workflow |

---

## Conclusion

The comparison reveals two tools with fundamentally different objectives:

1. **README-Gen (paper tool)**: Generates **end-user CLI documentation** — teaches users how to install, configure, and use notes-cli with domain concepts, command examples, and API references. Its primary weakness is hallucination of non-existent commands and incorrect environment variables, but it consistently produces a coherent user-facing document.

2. **readme-ai**: Generates **repository overview documentation** — describes the project's file structure, build tooling, source code organization, and contributing workflow. Its primary weakness is the complete absence of end-user documentation (no CLI commands, no usage patterns, no domain concepts). Additionally, unresolved template placeholders (`{entrypoint}`, `{__test_framework__}`) indicate incomplete generation.

For the evaluation criteria defined by the paper (Completeness, Correctness, ATORAK Adherence), README-Gen produces superior output because it directly addresses the knowledge elements that CLI tool users need. Even the worst paper README (data3.md, CR=48.75) significantly outperforms readme-ai (CR=32.22) on correctness and dramatically outperforms on ATORAK (100 vs 0).

However, readme-ai provides complementary value:
- **Accurate project structure** showing all source files and their purposes
- **Correct identification of real dependencies** (kingpin.v2, go-github-selfupdate, go-colorable)
- **CI/CD documentation** describing the GitHub Actions workflow
- **Contributing workflow** useful for potential contributors
- **Shell completion documentation** (fish, zsh) visible in the project structure

The ideal README for notes-cli would combine README-Gen's user-facing documentation approach (with correctness improvements) with readme-ai's structural and contributor-facing content.
