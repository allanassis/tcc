# ATRAK Evaluation — README-AI (project `uri` / lil-js/uri)

> ATRAK is **presence-only**: incorrect/hallucinated content still counts as
> present. Absent (0) only for empty/missing section, bare name-only list, or
> unresolved placeholders as the sole content.

## Ground Truth Reference
- **Project:** lil-uri (package `lil-uri`; repo `lil-js/uri`).
- **Repository:** https://github.com/lil-js/uri
- **Domain:** URI/URL parsing and building in JavaScript (Node + browser).
- **Core domain entities:** URI components — protocol/scheme, host, hostname, port, auth (user/password), path, search/query, hash/fragment.
- **Core execution facts:** UMD/CommonJS module; factory `uri(str)` → chainable `URI`; `build()/toString()` serialize; `uri.is/isURL` validate; MIT; no `engines`; test via `make test` (mocha/chai); deps mocha/chai/uglify-js/terser.
- **Core usage patterns:** clone/build workflow; parse then read components; chain accessors to build.

---

## README — `uri_readme_readmeai.md`

| Element | Verdict | Evidence |
|---|---|---|
| K_D Domain Concepts | **1** | Overview defines the tool as a "chainable URI parser and builder" and the Features table's **Details** column explains architecture/modularity/parsing of URI components (protocol, host, path, query, fragments) with descriptive prose — beyond a bare name list. |
| K_E Execution Facts | **1** | Prerequisites (JavaScript; Bower/Npm), Installation (clone + `npm install`), Testing (`npm test`), Project Structure file tree, and a Dependencies row (mocha, chai, uglify-js, terser) — concrete runtime/build facts. Some placeholders exist but substantial non-placeholder execution content remains. |
| K_U Usage Patterns | **1** | Getting Started demonstrates the applied workflow: `git clone`, `cd uri`, `npm install`, `npm start`, `npm test`, plus a Contributing walkthrough — evaluable usage content (even though `npm start` is wrong and some commands are placeholders). Not solely placeholders. |

**K = 3/3 = 100%**

---

## Summary & average (single README ⇒ average = the row)
| readme | K_D | K_E | K_U | ATRAK |
|---|---|---|---|---|
| uri_readme_readmeai.md | 1 | 1 | 1 | 100 |
| **average** | 1 | 1 | 1 | **100** |

Note: Under the correctness dimension the same content scores poorly (no API reference, placeholder installs, generic license); ATRAK measures only presence, so all three knowledge elements are present. Average verified consistent.

## Cross-checked sources
Cloned repo `/tmp/eval-uri-clone` (`uri.js`, `package.json`, `bower.json`, `LICENSE`); executed build/test in `/tmp/eval-uri-readmeai`.
