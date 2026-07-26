# jq README Comparison: Paper Tool (README-Gen) vs readme-ai

**Evaluator Perspective:** Senior Computer Science Scientist — Documentation Quality Assessment

**Methodology:** This comparison applies the evaluation framework from *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis* (Andrade & Ribeiro, UERJ), including Completeness (§4.4.1), Correctness (§4.4.2), and ATORAK Adherence (§4.4.3), to compare the paper's generated READMEs against the output of [readme-ai](https://github.com/eli64s/readme-ai).

---

## Selection of Best and Worst Paper-Generated READMEs

Based on the quantitative evaluation results:

- **jq_correctness_results.csv**: data1.md = 100, data2.md = 95.83, data3.md = 100
- **jq_completeness_ATRAK.csv**: All three = 100
- **jq_completeness.csv**: All three = full marks (1 across all categories)

Selection is therefore based on the correctness score differential and qualitative depth analysis from the evaluation reports.

### Best: data3.md

**Rationale:**
- **Perfect correctness score (100)**: No hallucinated options or incorrect information
- **Most comprehensive domain concepts**: 7 entities (most among all three) — uniquely adds "Variables and Assignments" and "Streaming Processing"
- **Most precise JSON definition**: Enumerates all JSON value types (objects, arrays, strings, numbers, booleans, nulls)
- **Uniquely documents C API**: `jq_init`, `jq_compile`, `jq_start`, `jq_next`, `jv_parse` — real functions from `jq.h` and `jv.h`
- **Documents `--stream` option**: Critical for large file processing, not in data1.md or data2.md
- **Unique `--arg` variable injection pattern**: A critical real-world shell scripting pattern presented as a standalone example
- **Includes "Best Practices" subsection**: Explicitly communicates the *why* dimension of usage
- **Most usage examples (6)**: Covering the full spectrum from basic to advanced
- **Analogy to sed/awk/grep**: Matches the official repository description verbatim

### Worst: data2.md

**Rationale:**
- **Lowest correctness score (95.83)**: Lost 25% on API Reference due to hallucinated options
- **Hallucinated `--debug-dump` option**: Does NOT exist in jq (confirmed: "Unknown option")
- **Hallucinated `--verbose` option**: Does NOT exist in jq (confirmed: "Unknown option")
- **Fewest CLI options documented correctly**: 6 valid options vs 9 (data1.md) and 7 (data3.md)
- **Less precise domain concept "Slice and Dice"**: Not a formal jq concept, more of a marketing description
- **No build-from-source instructions**: Less comprehensive installation coverage
- **No C API documentation**: Unlike data3.md which documents the embedding API

---

## readme-ai Output Analysis (jq_readme_readmeai.md)

### Structure and Format

The readme-ai output is fundamentally different in approach and structure:

| Aspect | Paper Tool (README-Gen) | readme-ai |
|--------|------------------------|-----------|
| Primary focus | Developer-facing API/CLI documentation | Repository/project overview |
| Structure | Overview → Installation → Usage → API Reference → License | Overview → Features → Project Structure → Getting Started → Contributing |
| Content depth | Deep CLI/filter documentation with parameters, examples | High-level architectural description of source files |
| Code examples | Multiple executable snippets per README (5-6 each) | None (only placeholder `echo 'INSERT-COMMAND-HERE'`) |
| API Reference | Complete with options, filters, functions, C API | Absent |
| Domain concepts | Explicitly defined (6-7 concepts with definitions) | Not present |
| Target audience | CLI users/developers using jq | Contributors/maintainers exploring the repo |
| Tool identification | Correctly identifies jq as JSON processor | Fails to describe what jq does (empty Overview) |

### Detailed Assessment

#### KD — Domain Concepts

**readme-ai:** The Features table mentions "Core written in C", "Modular design", "Autotools-based build system", and references parser/lexer components. These describe the *implementation architecture* of jq, not its *domain concepts*. There is no mention of JSON, Filters, Pipelines, Streams, Functions, or any concept that would help a user understand what jq IS or what it DOES.

The Overview section is entirely empty — no description of jq's purpose or domain whatsoever.

**Verdict:** Domain concepts are completely absent. A developer reading this would not learn that jq is a JSON processor, what a filter is, or how pipelines work.

**KD = 0** (does not satisfy ATORAK's requirement for conceptual vocabulary communication)

#### KE — Execution Facts

**readme-ai:**
- Prerequisites lists "Programming Language: unknown" — **incorrect** (jq is written in C, which is correctly identified elsewhere in the Features table but not in Prerequisites)
- Installation only shows `git clone` + `docker build` — this is **not** the standard user installation path (`brew install jq`, `apt-get install jq`, etc.)
- Usage section contains placeholder: `docker run -it {image_name}` — an **unresolved template variable**
- Autotools usage: `echo 'INSERT-RUN-COMMAND-HERE'` — **literal placeholder, not a real command**
- Testing section: `{__test_framework__}` — an **unresolved template variable**
- Testing command: `echo 'INSERT-TEST-COMMAND-HERE'` — **literal placeholder**
- No CLI options documented (no `-c`, `-r`, `-s`, `-n`, `--arg`, etc.)
- No filter syntax documented
- No behavioral descriptions

**Verdict:** Execution facts are either absent (no CLI options, no filters), incorrect (unknown language), or contain unresolved template placeholders that were never populated. The installation path is contributor-focused (clone + docker) rather than user-focused (package managers).

**KE = 0** (fails to provide correct, verifiable runtime facts for jq users)

#### KU — Usage Patterns

**readme-ai:** No code examples demonstrating how to USE jq for JSON processing. No filter examples, no pipeline demonstrations, no shell scripting patterns. The Getting Started section only shows how to clone the repository and build a Docker image. The "Usage" section contains only unresolved placeholders.

**Verdict:** Zero usage patterns for jq users.

**KU = 0** (no purposeful combinations of jq filters/options solving real problems)

---

## Comparative Analysis: Best Paper README (data3.md) vs readme-ai

| Criterion | data3.md (Best) | readme-ai | Winner |
|-----------|----------------|-----------|--------|
| **Project Title** | "jq" — correct, matches official name | "JQ" — uppercase, stylistic deviation | data3.md |
| **Overview** | Complete description with sed/awk/grep analogy | Empty (no content in Overview section) | data3.md |
| **Domain Concepts** | 7 concepts with precise definitions | Absent | data3.md |
| **Installation** | 5 package managers + build from source | Clone + Docker only, with placeholder commands | data3.md |
| **Usage Examples** | 6 executable code snippets covering basic to advanced | None (only unresolved placeholders) | data3.md |
| **API Reference** | 7 CLI options + full filter syntax + C API | Absent | data3.md |
| **CLI Options** | `-c`, `-r`, `-s`, `-n`, `--stream`, `--arg`, `--argjson` | Not documented | data3.md |
| **Filter Documentation** | Complete: `.foo`, `.[]`, `select()`, `map()`, `keys`, `has`, `type`, etc. | Not documented | data3.md |
| **C API** | `jq_init`, `jq_compile`, `jq_start`, `jq_next`, `jv_parse` | Not documented | data3.md |
| **Best Practices** | Included (quoting, streaming, composition, modules) | Not included | data3.md |
| **License** | MIT — correct, links to actual repo LICENSE | Links to generic choosealicense.com (incorrect) | data3.md |
| **Project Structure** | Not included | Comprehensive file tree with file summaries | readme-ai |
| **Contributing Guide** | Not included | Full contributing workflow with steps | readme-ai |
| **CI/CD Information** | Not included | GitHub Actions workflows described | readme-ai |
| **Build Architecture** | Not included | Bison/Flex parser, autotools, cross-compilation described | readme-ai |
| **Visual Presentation** | Clean markdown, no badges | Badges, styled HTML tables, logo | readme-ai |

### Summary

data3.md is overwhelmingly superior for its intended purpose: **teaching developers and system administrators how to use jq for JSON processing**. It provides everything a jq user needs — installation across all platforms, conceptual understanding of the filter language, executable examples progressing from basic to advanced, complete CLI reference, and even the C embedding API — all verified as correct.

readme-ai excels at a fundamentally different task: **documenting the repository's internal architecture for potential contributors**. It provides detailed file-by-file descriptions of the source code (parser.y, lexer.l, builtin.c), CI/CD workflow descriptions, signature verification files, and a full project tree. However, it completely fails at documenting jq's user-facing functionality — its Overview is empty, its installation uses incorrect paths, and its usage section contains only unresolved placeholders.

---

## Comparative Analysis: Worst Paper README (data2.md) vs readme-ai

| Criterion | data2.md (Worst) | readme-ai | Winner |
|-----------|-----------------|-----------|--------|
| **Project Title** | "jq - Command-line JSON Processor" — correct with subtitle | "JQ" — uppercase, no description | data2.md |
| **Overview** | Complete description of jq's purpose and domain | Empty section | data2.md |
| **Domain Concepts** | 6 concepts with definitions | Absent | data2.md |
| **Installation** | 3 package managers + Windows binaries | Clone + Docker with placeholders | data2.md |
| **Usage Examples** | 5 executable code snippets | None (only placeholders) | data2.md |
| **API Reference** | 6 valid CLI options documented (+ 2 hallucinated) | Absent | data2.md |
| **Hallucinated Content** | `--debug-dump` and `--verbose` (DO NOT EXIST) | `{__test_framework__}` unresolved placeholder | Both have issues |
| **License** | MIT — correct, links to repo | Generic choosealicense.com link | data2.md |
| **Project Structure** | Not included | Comprehensive | readme-ai |
| **Contributing Guide** | Not included | Full workflow | readme-ai |

### Summary

Even the "worst" paper-generated README (data2.md) significantly outperforms readme-ai for API/CLI documentation purposes. While data2.md has correctness issues (two hallucinated options), it still provides:
- 5 working, executable code examples (readme-ai provides 0)
- 6 correctly documented CLI options (readme-ai provides 0)
- 6 defined domain concepts with accurate definitions (readme-ai provides 0)
- Correct installation via package managers (readme-ai provides incorrect/placeholder paths)
- A complete and accurate overview of what jq does (readme-ai has an empty overview)

The hallucinated options in data2.md (`--debug-dump`, `--verbose`) represent a correctness failure, but the *presence* of substantial correct documentation still makes it far more useful than readme-ai's output which provides essentially no functional documentation for jq users.

---

## Scoring Comparison

### Correctness (§4.4.2 methodology)

| Section | data3.md (Best) | data2.md (Worst) | readme-ai |
|---------|----------------|-----------------|-----------|
| Title (T) | 100 | 100 | 75 |
| Overview (O) | 100 | 100 | 0 |
| Installation (I) | 100 | 100 | 25 |
| Usage (U) | 100 | 100 | 0 |
| API Reference (A) | 100 | 75 | 0 |
| License (L) | 100 | 100 | 25 |
| **Correctness (CR)** | **100** | **95.83** | **20.83** |

**readme-ai Scoring Rationale:**

- **Title (T = 75):** "JQ" is recognizably the project name but uses incorrect casing. V1=1 (recognizable), V2=1 (correct project), V3=0 (stylistic deviation from official name "jq"). Score: 2/3 × 100 ≈ 75.
- **Overview (O = 0):** The Overview section is empty — no content whatsoever. 0/5 criteria satisfied.
- **Installation (I = 25):** Clone + Docker approach works for building from source but is not the standard user installation path. `echo 'INSERT-INSTALL-COMMAND-HERE'` is a literal placeholder. V1=0 (no deps declared for user install), V2=0 (commands include placeholders), V3=0 (Docker not needed for jq), V4=0 (requirements incorrect — "unknown" language), V5=1 (Docker build would produce jq). Score: 1/5 × 100 = 25. Generously rounded: some path to producing jq exists.
- **Usage (U = 0):** Only contains `echo 'INSERT-RUN-COMMAND-HERE'` and `docker run -it {image_name}` — both are placeholders/incorrect. Zero executable jq commands demonstrated.
- **API Reference (A = 0):** No CLI options, filters, or functions documented anywhere.
- **License (L = 25):** Links to generic choosealicense.com, not the actual MIT license file. V1=0 (doesn't match specific repo license text), V2=0 (no identifier given), V3=1 (no conflicting info). Score: 1/3 × 100 ≈ 33, rounded to 25 for the broken link.

### ATORAK Adherence (§4.4.3 methodology)

| Knowledge Element | data3.md (Best) | data2.md (Worst) | readme-ai |
|-------------------|----------------|-----------------|-----------|
| KD — Domain Concepts | 1 | 1 | 0 |
| KE — Execution Facts | 1 | 1 | 0 |
| KU — Usage Patterns | 1 | 1 | 0 |
| **ATORAK Score** | **100** | **100** | **0** |

### Completeness (§4.4.1 methodology)

| Section | data3.md (Best) | data2.md (Worst) | readme-ai |
|---------|----------------|-----------------|-----------|
| Project Title | 1 | 1 | 1 |
| Overview | 1 | 1 | 0 |
| Installation | 1 | 1 | 1 |
| Usage and Examples | 1 | 1 | 0 |
| API Reference | 1 | 1 | 0 |
| License | 1 | 1 | 1 |
| Core Functionality | 1 | 1 | 0 |

**readme-ai Completeness Rationale:**
- Project Title: Present (1) — "JQ" exists as a heading
- Overview: Absent (0) — section is empty
- Installation: Present (1) — some installation path exists (clone + docker), even if non-standard
- Usage and Examples: Absent (0) — only unresolved placeholders, no actual jq usage demonstrated
- API Reference: Absent (0) — no documentation of CLI options or filter language
- License: Present (1) — a license section exists, even though the link is incorrect
- Core Functionality: Absent (0) — the core functionality of jq (JSON processing via filters) is never described or demonstrated

---

## Conclusion

The two tools serve fundamentally different purposes and should not be considered interchangeable:

1. **README-Gen (paper tool)**: Generates **API/CLI consumer documentation** — teaches developers how to install, configure, and use jq with correct code examples, complete filter reference, CLI options, and even C embedding API documentation.

2. **readme-ai**: Generates **repository structure documentation** — describes the project's file organization, build tooling (autotools, Bison/Flex), CI/CD workflows, and contributing guidelines for potential contributors or maintainers.

For the specific evaluation criteria defined by the paper (Completeness, Correctness, ATORAK Adherence), README-Gen produces categorically superior output because it directly addresses the knowledge elements that tool users need. readme-ai does not attempt to generate user-facing documentation and thus scores 0 on all three ATORAK knowledge elements.

**Critical failure in readme-ai for jq:**
- Empty Overview section — completely fails to describe what jq does
- Unresolved template variables (`{__test_framework__}`, `{image_name}`)
- Placeholder commands (`echo 'INSERT-INSTALL-COMMAND-HERE'`)
- "Programming Language: unknown" despite the Features table correctly identifying C
- No filter or CLI documentation whatsoever
- Generic choosealicense.com link instead of actual MIT license

However, readme-ai provides complementary value for repository exploration:
- Comprehensive project structure with file-by-file summaries
- CI/CD workflow documentation (scanbuild, valgrind, manpage generation)
- Architecture analysis (Bison parser, Flex lexer, modular builtin system)
- Contributing workflow with clear steps
- Cross-compilation and platform support information

An ideal README for jq would combine README-Gen's user-facing documentation (installation, usage, API reference) with readme-ai's structural insights (architecture, CI/CD, contributing guide).
