# lil-uri README Comparison: Paper Tool (README-Gen) vs readme-ai

**Evaluator Perspective:** Senior Computer Science Scientist — Documentation Quality Assessment

**Methodology:** This comparison applies the evaluation framework from *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis* (Andrade & Ribeiro, UERJ), including Completeness (§4.4.1), Correctness (§4.4.2), and ATORAK Adherence (§4.4.3), to compare the paper's generated READMEs against the output of [readme-ai](https://github.com/eli64s/readme-ai).

---

## Selection of Best and Worst Paper-Generated READMEs

The three paper-generated READMEs scored identically on ATORAK (100 each) and Completeness (all sections present), but diverged significantly on Correctness:

| README | Correctness Score (CR) |
|--------|----------------------|
| data1.md | 50.00 |
| data2.md | 66.67 |
| data3.md | 50.00 |

### Best: data2.md

**Rationale:**
- **Correct package name**: Uses `lil-uri` (the actual npm package name) — data1 and data3 use the non-existent `@lil-js/uri`
- **Installation commands work**: `npm install lil-uri` succeeds (verified via npm)
- **Correctly identifies the factory function**: Documents `uri(input?: string | URI): URI` which is the real entry point
- **Correctly documents `toString()`**: This method exists and functions as described
- **Highest correctness score (66.67)**: 2 out of 10 API elements pass all correctness criteria
- **Overview most accurate**: Scores 80 on Overview (highest among the three), avoids claiming non-existent features as standalone APIs

### Worst: data1.md

**Rationale:**
- **Wrong package name**: Uses `@lil-js/uri` which returns 404 on npm — installation completely fails
- **Wrong project title**: Uses `lil-js/uri` (GitHub org/repo path format) instead of `lil-uri`
- **Completely fabricated class-based API**: Documents `new URI(uriString)` as a constructor — the real API uses a `uri()` factory function
- **All 12 documented API elements are incorrect**: Invents `addQuery`, `setQuery`, `removeQuery`, `normalize` methods — none exist
- **All 4 usage snippets fail at runtime**: 0% execution success
- **Lowest correctness score (50.00)**: Tied with data3 but uses wrong title format
- **Most misleading API paradigm**: Invents a class-based property model (`uri.scheme`, `uri.userinfo`, `uri.fragment`) that conflates lil-uri with unrelated libraries like URI.js

---

## readme-ai Output Analysis (uri_readme_readmeai.md)

### Structure and Format

The readme-ai output follows a fundamentally different philosophy:

| Aspect | Paper Tool (README-Gen) | readme-ai |
|--------|------------------------|-----------|
| Primary focus | Developer-facing API documentation | Repository/project overview |
| Structure | Overview → Installation → Usage → API Reference → License | Overview → Features → Project Structure → Getting Started → Contributing |
| Content depth | Deep API-level documentation with parameters, returns, examples | High-level architectural description of source files |
| Code examples | Multiple executable snippets per README | None (only `git clone`, `npm install`, `npm start`) |
| API Reference | Complete with parameters, types, return values | Absent |
| Domain concepts | Explicitly defined (5-6 concepts) | Implicitly mentioned in Features table |
| Target audience | API consumers/developers using the library | Contributors/maintainers exploring the repo |

### Detailed Assessment

#### KD — Domain Concepts

**readme-ai:** The Overview section mentions "URI parser and builder designed to simplify URL manipulation" and the Features table references "Chainable API", "Comprehensive Parsing", "Modular" architecture. These are correct high-level characterizations. However, no explicit domain vocabulary is taught — there is no explanation of what URI components are (scheme, host, path, query, fragment), no reference to RFC 3986, and no conceptual framework for understanding the problem domain.

**Verdict:** The readme-ai output *references* URI handling concepts in marketing language but does not *communicate* them in the ATORAK sense. A developer reading this would know the library handles URIs but would not learn the domain vocabulary necessary to use it effectively.

**KD = 0** (does not satisfy ATORAK's requirement for conceptual vocabulary communication)

---

#### KE — Execution Facts

**readme-ai:**
- Installation section provides `git clone` + `npm install` — this is for building from source, NOT for consuming the library (`npm install lil-uri` is the correct consumer path)
- Bower install section shows `echo 'INSERT-INSTALL-COMMAND-HERE'` — **an unresolved template placeholder**
- Usage section says `npm start` — lil-uri is a library, not an application; this command is contextually incorrect for library consumers
- Testing section references `{__test_framework__}` — **another unresolved template placeholder**
- No API method signatures, parameters, return types, or behavioral descriptions
- No environment requirements from the consumer perspective

**Verdict:** Execution facts are either incorrect (npm start for a library), incomplete (no API signatures), or broken (unresolved template variables). The readme-ai tool clearly failed to resolve its template placeholders for this project.

**KE = 0** (fails to provide correct, verifiable runtime facts for API consumers)

---

#### KU — Usage Patterns

**readme-ai:** No code examples demonstrating how to USE lil-uri as a library. The Getting Started section only shows how to clone and build the repository. No parsing, manipulation, or serialization patterns are demonstrated.

**Verdict:** Zero usage patterns for API consumers.

**KU = 0** (no purposeful combinations of API calls solving real problems)

---

## Comparative Analysis: Best Paper README (data2.md) vs readme-ai

| Criterion | data2.md (Best) | readme-ai | Winner |
|-----------|----------------|-----------|--------|
| **Project Title** | "lil-uri" — correct npm package name | "URI" — shortened, omits the actual package name | data2.md |
| **Overview** | Describes functionality, RFC 3986, domain concepts | Marketing-oriented overview with emoji bullets | data2.md |
| **Domain Concepts** | 5 concepts with accurate definitions | Implicit mentions in Features table, no definitions | data2.md |
| **Installation** | `npm install lil-uri` — correct consumer path ✅ | `git clone` + `npm install` — contributor path, not consumer | data2.md |
| **Usage Examples** | 3 executable code snippets covering parsing, query, and construction | None (only `npm start` which is incorrect for a library) | data2.md |
| **API Reference** | 10 elements (2 correct: `uri()` factory, `toString()`) | Absent | data2.md |
| **License** | MIT — correct, links to GitHub LICENSE file | Links to generic choosealicense.com, not the actual license | data2.md |
| **Project Structure** | Not included | Comprehensive file tree with file-by-file summaries | readme-ai |
| **Contributing Guide** | Not included | Full contributing workflow with steps | readme-ai |
| **Visual Presentation** | Clean markdown, no badges | Badges, logo, styled HTML tables | readme-ai |
| **Template Completeness** | Fully rendered, no placeholders | Contains unresolved placeholders (`{__test_framework__}`, `INSERT-*-HERE`) | data2.md |

### Summary

data2.md is substantially superior for its intended purpose: **teaching developers how to use the lil-uri library**. Despite its correctness issues (hallucinated property-based API, fabricated Map-like query interface), it still provides:
- The correct package name and installation command
- A correct description of the library's purpose
- Code examples that demonstrate the intended workflow (even if they fail at runtime due to wrong API shape)
- Two correctly documented API elements (`uri()` factory and `toString()`)

readme-ai excels at a fundamentally different task: **documenting repository structure for contributors**. However, for this particular project, readme-ai's output is notably poor — it contains multiple unresolved template placeholders and provides no functional usage information whatsoever.

---

## Comparative Analysis: Worst Paper README (data1.md) vs readme-ai

| Criterion | data1.md (Worst) | readme-ai | Winner |
|-----------|-----------------|-----------|--------|
| **Project Title** | "lil-js/uri" — GitHub path, not npm name | "URI" — shortened | Tie (both imprecise) |
| **Overview** | Complete description with domain concepts | Marketing overview without substance | data1.md |
| **Domain Concepts** | 5 concepts with definitions | No formal definitions | data1.md |
| **Installation** | `npm install @lil-js/uri` — **FAILS** (wrong package) | `git clone` + `npm install` — wrong approach | Tie (both fail) |
| **Usage Examples** | 4 code snippets (all fail at runtime) | None | data1.md |
| **API Reference** | 12 elements documented (all incorrect) | Absent | data1.md* |
| **License** | MIT — correct | Generic link, incorrect | data1.md |
| **Project Structure** | Not included | Comprehensive | readme-ai |
| **Contributing Guide** | Not included | Full workflow | readme-ai |
| **Template Quality** | Complete, no placeholders | Unresolved placeholders | data1.md |

*\*Note: data1.md's API Reference is present but entirely hallucinated (0 correct elements). However, having a structured API reference — even an incorrect one — communicates the FORM of API documentation to the reader, which is more useful as a starting point than complete absence.*

### Summary

Even the worst paper-generated README (data1.md) provides more value for API documentation purposes than readme-ai, despite its severe correctness problems:
- data1.md gives developers a (wrong but structured) mental model of the library's API
- data1.md provides 4 code examples showing intended usage patterns (even though they fail)
- data1.md formally defines domain concepts (even though property names are incorrect)
- readme-ai provides no API documentation, no usage examples, and leaves template placeholders unresolved

However, data1.md is particularly dangerous because its installation command uses a non-existent package name (`@lil-js/uri`) — a developer following these instructions would get a 404 error immediately. In this narrow sense, readme-ai's `git clone` approach at least successfully clones the real repository.

---

## Conclusion

The two tools serve fundamentally different purposes:

1. **README-Gen (paper tool)**: Generates **API consumer documentation** — attempts to teach developers how to install, configure, and use a library with code examples and API references. For lil-uri, the output suffers from significant hallucination problems (the LLM confused it with similar libraries like URI.js), but the documentation *structure* and *intent* are correct.

2. **readme-ai**: Generates **repository overview documentation** — describes project files, build tooling, and contributing workflow. For lil-uri, the output is particularly weak: unresolved template variables, no consumer-facing information, and incorrect usage commands.

### Key Findings

| Metric | data2.md (Best) | data1.md (Worst) | readme-ai |
|--------|----------------|-----------------|-----------|
| Correctness Score | 66.67 | 50.00 | ~16.67* |
| ATORAK Adherence | 100 | 100 | 0 |
| Completeness (all sections) | 7/7 | 7/7 | 3/7** |
| Working installation | ✅ Yes | ❌ No | ❌ No (contributor path only) |
| API Reference present | ✅ Yes (2/10 correct) | ✅ Yes (0/12 correct) | ❌ No |
| Usage examples present | ✅ Yes (0/3 execute) | ✅ Yes (0/4 execute) | ❌ No |
| Template fully resolved | ✅ Yes | ✅ Yes | ❌ No |

*\*Estimated readme-ai correctness: Title (100), Overview (0 — no substance), Installation (25 — clone works but wrong approach), Usage (0), API (0), License (25 — wrong link). CR = (100+0+25+0+0+25)/6 ≈ 25.00*

*\*\*Completeness for readme-ai: Title (✅), Overview (✅), Installation (partial), Usage (❌), API Reference (❌), License (✅), Core Functionality (❌)*

### Practical Recommendation

For the lil-uri project specifically, **neither tool produces fully usable documentation**:
- README-Gen's output requires correctness fixes (wrong property names, non-existent methods) but has the right structure
- readme-ai's output would need to be entirely rewritten to include any API documentation

An ideal workflow would use README-Gen's structure with manual correctness verification, supplemented by readme-ai's project structure overview for contributor documentation.
