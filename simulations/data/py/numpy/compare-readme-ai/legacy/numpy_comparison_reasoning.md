# NumPy README Comparison: Paper Tool (README-Gen) vs readme-ai

**Evaluator Perspective:** Senior Computer Science Scientist — Documentation Quality Assessment

**Methodology:** This comparison applies the evaluation framework from *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis* (Andrade & Ribeiro, UERJ), including Completeness (§4.4.1), Correctness (§4.4.2), and ATORAK Adherence (§4.4.3), to compare the paper's generated READMEs against the output of [readme-ai](https://github.com/eli64s/readme-ai).

---

## Selection of Best and Worst Paper-Generated READMEs

All three paper-generated READMEs (data1.md, data2.md, data3.md) scored 100 on ATORAK adherence and completeness. Differentiation comes from the Correctness metric (§4.4.2).

### Best: data1.md

**Rationale:**
- **Correctness score: 93.33** (tied with data2.md, both highest)
- **Most comprehensive API Reference**: 19 documented API elements — includes `numpy.fft.fft`, `numpy.fft.ifft`, `numpy.ma.masked_array`, `np.empty`, and all reduction ufuncs (`np.sum`, `np.prod`, `np.min`, `np.max`) — broadest sub-module coverage of the three
- **Most domain concepts**: 7 concepts explicitly defined (ndarray, Broadcasting, ufuncs, Linear Algebra, Random Sampling, Fourier Transforms, Masked Arrays)
- **Most usage patterns**: 6 distinct patterns (importing, creating arrays, operations/broadcasting, ufuncs, linear algebra, random sampling)
- **Only README to document `numpy.ma` (Masked Arrays)** — a significant but often overlooked NumPy sub-module
- **Only README to document `np.empty`** — important creation function for performance-critical code

### Worst: data3.md

**Rationale:**
- **Correctness score: 90.00** (lowest of the three, 3.33 points below data1 and data2)
- **Installation section scored 60** (vs 80 for data1 and data2) — two criteria failed:
  - V2=0: Source build commands (`pip install cython; pip install .`) are incomplete; numpy 2.x requires `meson-python` and `ninja` as build dependencies, causing the commands to fail on clean environments
  - V3=0: Unresolved dependency errors confirmed during execution of source build instructions
- **Fewest API elements**: 13 documented elements (vs 19 for data1 and 16 for data2)
- **Does not document FFT or Masked Arrays modules** — narrower sub-module coverage
- **5 usage patterns** (fewer than data1's 6)
- Note: data3.md has the most detailed `numpy.array()` signature (full parameter documentation) and uniquely documents `numpy.add`/`numpy.subtract`, but these strengths do not compensate for the installation failures and narrower coverage

---

## readme-ai Output Analysis (numpy_readme_readmeai.md)

### Structure and Format

The readme-ai output is fundamentally different in approach and structure:

| Aspect | Paper Tool (README-Gen) | readme-ai |
|--------|------------------------|-----------|
| Primary focus | Developer-facing API documentation | Repository/project overview |
| Structure | Overview → Installation → Usage → API Reference → License | Overview → Features → Project Structure → Getting Started → Contributing |
| Content depth | Deep API-level documentation with parameters, returns, examples | High-level architectural description of source files |
| Code examples | Multiple executable snippets per README | None (only template placeholders: `python {entrypoint}`) |
| API Reference | Complete with parameters, types, return values | Absent |
| Domain concepts | Explicitly defined (6-7 concepts with definitions) | Implicitly mentioned in Features table |
| Target audience | API consumers/developers using the library | Contributors/maintainers exploring the repo |
| File size | ~150-200 lines of focused content | ~8,900+ lines (mostly project structure and file descriptions) |

### Detailed Assessment

#### KD — Domain Concepts

**readme-ai:** The Features table mentions "Multi-dimensional array objects, numerical operations, linear algebra, Fourier transforms, random sampling" and references "Multiple RNG implementations". These are correct but presented as feature bullet points in a table, not as domain concepts with definitions. No conceptual vocabulary is explicitly taught to the reader — there is no explanation of what an ndarray IS, what Broadcasting MEANS, or what a ufunc DOES.

**Verdict:** Domain concepts are *listed* but not *communicated* in the ATORAK sense. A developer reading this Features table would not learn the conceptual vocabulary needed to work with NumPy effectively.

**KD = 0** (does not satisfy ATORAK's requirement for conceptual vocabulary communication)

#### KE — Execution Facts

**readme-ai:**
- Installation section provides `git clone` + `conda env create -f environment.yml` or `pip install -r requirements/test_requirements.txt, ...` — this is the **developer/contributor** installation path, not the standard consumer path (`pip install numpy`)
- The pip install command lists **all internal requirements files** (test, typing, build, CI, etc.) as if they were user dependencies — this is **incorrect** for library consumers
- Usage section contains unresolved template variables: `python {entrypoint}` and `conda activate {venv}` — **broken placeholders**
- Testing section references `{__test_framework__}` — a **template placeholder that was not resolved**
- A cmake section says `echo 'INSERT-INSTALL-COMMAND-HERE'` — another **unresolved placeholder**
- No API method signatures, parameters, return types, or behavioral descriptions anywhere
- No environment requirements (Python version) documented from the consumer perspective

**Verdict:** Execution facts are either incorrect (developer build path instead of consumer install), broken (unresolved template variables), or absent (no API signatures, no function parameters, no return types).

**KE = 0** (fails to provide correct, verifiable runtime facts for API consumers)

#### KU — Usage Patterns

**readme-ai:** No code examples demonstrating how to USE numpy as a library. The Getting Started section only shows how to clone and build the repository from source. No array creation, broadcasting, ufunc, linear algebra, or random sampling patterns. The "Usage" section contains only broken template placeholders (`python {entrypoint}`).

**Verdict:** Zero usage patterns for API consumers.

**KU = 0** (no purposeful combinations of API calls solving real problems)

---

## Comparative Analysis: Best Paper README (data1.md) vs readme-ai

| Criterion | data1.md (Best) | readme-ai | Winner |
|-----------|----------------|-----------|--------|
| **Project Title** | "NumPy" — correct, matches official name | "NUMPY" — uppercase, stylistic deviation from official branding | data1.md |
| **Overview** | Complete description of NumPy's purpose, domain, and capabilities | Empty (the Overview section has no content) | data1.md |
| **Domain Concepts** | 7 concepts with accurate definitions (ndarray, Broadcasting, ufuncs, linalg, random, fft, masked arrays) | Implicit mentions in Features table, no definitions | data1.md |
| **Installation** | `pip install numpy` / `conda install numpy` — correct consumer path | `git clone` + `conda env create -f environment.yml` — contributor path with all dev requirements | data1.md |
| **Usage Examples** | 6 executable code snippets covering core patterns (array creation, broadcasting, ufuncs, linalg, random) | None (only `python {entrypoint}` which is a broken placeholder) | data1.md |
| **API Reference** | 19 elements with parameter documentation across 6 sub-modules (core, linalg, random, fft, ma, ufuncs) | Absent | data1.md |
| **License** | BSD 3-Clause — correct, links to GitHub LICENSE.txt | Links to generic choosealicense.com, does not identify the actual license type | data1.md |
| **Project Structure** | Not included | Comprehensive file tree with ~8000+ lines of file summaries | readme-ai |
| **Contributing Guide** | Not included | Full contributing workflow with fork/clone/branch/commit/PR steps | readme-ai |
| **Build System Details** | Not included | Meson build configuration, pyproject.toml, environment.yml described | readme-ai |
| **CI/CD Information** | Not included | CI workflow descriptions, sanitizer suppressions documented | readme-ai |
| **Visual Presentation** | Clean markdown, no badges | Badges (license, last-commit, languages), logo, styled HTML tables | readme-ai |

### Summary

data1.md is overwhelmingly superior for its intended purpose: **teaching developers how to use the NumPy library**. It provides everything an API consumer needs — installation, concepts, examples, and comprehensive API reference documentation across all major sub-modules — all verified as correct (minus the floating-point edge case and Python version inaccuracy).

readme-ai excels at a fundamentally different task: **documenting the repository structure for contributors**. It provides exhaustive file-by-file descriptions of the source code (8,900+ lines), build tooling details, CI configuration, and contributing workflows that data1.md does not attempt.

---

## Comparative Analysis: Worst Paper README (data3.md) vs readme-ai

| Criterion | data3.md (Worst) | readme-ai | Winner |
|-----------|-----------------|-----------|--------|
| **Project Title** | "NumPy" — correct | "NUMPY" — uppercase deviation | data3.md |
| **Overview** | Complete, accurate description with ecosystem context (SciPy, Pandas, scikit-learn) | Empty section | data3.md |
| **Domain Concepts** | 6 concepts with precise definitions (most precise ndarray definition: "homogeneous array of fixed-size items") | Implicit mentions only | data3.md |
| **Installation** | Correct consumer commands + source build (though source build is incomplete for numpy 2.x) | Incorrect: lists all dev requirements files, broken template placeholders | data3.md |
| **Usage Examples** | 5 executable code snippets (array creation, broadcasting, ufuncs, linalg, random) | None (broken placeholders only) | data3.md |
| **API Reference** | 13 elements with full parameter documentation (most detailed `numpy.array` signature of all three) | Absent | data3.md |
| **License** | BSD 3-Clause — correct | Generic choosealicense.com link, wrong | data3.md |
| **Project Structure** | Not included | Comprehensive (8,900+ lines) | readme-ai |
| **Contributing Guide** | Not included | Full workflow with steps | readme-ai |
| **Source Build Detail** | Provides source build commands (incomplete for numpy 2.x) | Provides `git clone` + environment setup (developer-focused) | Tie (both have issues) |

### Summary

Even the "worst" paper-generated README (data3.md) significantly outperforms readme-ai for API documentation purposes. While data3.md has known issues with its source build instructions (causing its score to drop to 90.00), it still provides:
- 5 working code examples (readme-ai provides 0)
- 13 documented API elements with parameters and types (readme-ai provides 0)
- 6 defined domain concepts with precise definitions (readme-ai provides 0 formal definitions)
- Correct consumer installation instructions (readme-ai provides incorrect/broken ones)
- The most detailed `numpy.array()` signature documentation of all three READMEs

---

## Scoring Summary

### Correctness Scoring (§4.4.2)

**data1.md (Best):**
- Title: 100, Overview: 100, Installation: 80, Usage: 80, API: 100, License: 100
- **CR = 93.33**

**data3.md (Worst):**
- Title: 100, Overview: 100, Installation: 60, Usage: 80, API: 100, License: 100
- **CR = 90.00**

**readme-ai:**
- Title: 80 (uppercase deviation, but recognizable)
- Overview: 0 (section is completely empty)
- Installation: 20 (provides commands that execute but are wrong path for consumers; lists all dev requirements; has broken cmake placeholder; no correct consumer install documented)
- Usage: 0 (only broken template placeholders; no executable code examples)
- API: 0 (absent entirely)
- License: 25 (mentions license exists but links to generic choosealicense.com; does not identify BSD 3-Clause)
- **CR = (80 + 0 + 20 + 0 + 0 + 25) / 6 = 20.83**

### ATORAK Scoring (§4.4.3)

| README | KD | KE | KU | ATORAK Score |
|--------|----|----|----|----|
| data1.md (best) | 1 | 1 | 1 | 100 |
| data3.md (worst) | 1 | 1 | 1 | 100 |
| readme-ai | 0 | 0 | 0 | 0 |

### Completeness Scoring (§4.4.1)

| README | Project Title | Overview | Installation | Usage & Examples | API Reference | License | Core Functionality |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| data1.md (best) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| data3.md (worst) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| readme-ai | 1 | 0 | 1 | 0 | 0 | 1 | 0 |

---

## Conclusion

The two tools serve fundamentally different purposes and should not be considered interchangeable:

1. **README-Gen (paper tool)**: Generates **API consumer documentation** — teaches developers how to install, configure, and use the NumPy library with correct code examples, comprehensive API references, and explicit domain concept definitions.

2. **readme-ai**: Generates **repository overview documentation** — describes the project's file structure, build tooling, CI/CD configuration, and contributing workflow for potential contributors or maintainers. Its output for NumPy is 8,900+ lines, dominated by a Project Index that describes every source file in the repository.

For the specific evaluation criteria defined by the paper (Completeness, Correctness, ATORAK Adherence), README-Gen produces categorically superior output because it directly addresses the knowledge elements that API consumers need. readme-ai does not attempt to generate API-level documentation and thus scores 0 on all three ATORAK knowledge elements.

### Critical Issues with readme-ai Output for NumPy:

1. **Empty Overview section** — the most critical section for a README has no content
2. **Unresolved template placeholders** — `{entrypoint}`, `{venv}`, `{__test_framework__}`, `INSERT-INSTALL-COMMAND-HERE` appear verbatim
3. **Incorrect consumer path** — instructs users to clone the repo and install all dev requirements instead of `pip install numpy`
4. **No API documentation whatsoever** — for a library, this is the most important section
5. **No code examples** — no demonstration of actual NumPy usage
6. **Massive, unfocused output** — 8,900+ lines with the vast majority being file-by-file project structure descriptions of limited utility to library consumers
7. **Generic license link** — links to choosealicense.com instead of identifying BSD 3-Clause

### Where readme-ai adds value:

1. **Project structure visualization** — comprehensive file tree
2. **Source file descriptions** — explains the purpose of individual source files
3. **Contributing workflow** — standardized fork/clone/branch/commit/PR guide
4. **Build system documentation** — describes meson, pyproject.toml, and CI configuration
5. **Visual badges** — license, last-commit, language stats at a glance

An ideal README would combine README-Gen's API-focused content with readme-ai's structural/contributor documentation, creating a comprehensive document that serves both library consumers and potential contributors.
