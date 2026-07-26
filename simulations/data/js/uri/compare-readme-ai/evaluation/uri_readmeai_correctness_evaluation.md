# Correctness Evaluation — README-AI (project `uri` / lil-js/uri)

Tool: README-AI. README evaluated: `compare-readme-ai/uri_readme_readmeai.md`.

## Ground Truth (cross-checked sources)
Same as the README-Gen evaluation. Key facts:
- npm/bower package `lil-uri` v0.3.1, MIT (© Tomas Aparicio), `main: ./uri.js`, no `engines`.
- `uri.js` real API: factory `uri(str)` → chainable `URI` instance; accessors `protocol/host/hostname/port/auth/user/password/path/search/query/hash`, `get`, `parse`, `build/toString/valueOf`; `uri.is/isURL`, `uri.URI`, `uri.VERSION`.
- Repo has **no** `start` script; `npm test` runs `make test` (terser + mocha).
- Sources: cloned repo `/tmp/eval-uri-clone`; executed clone + `npm install`/`npm start`/`npm test` in `/tmp/eval-uri-readmeai` (node v24.12.0, npm 11.6.2).

The README-AI document is a template-style README: header/badges, Overview, Features table, Project Structure, Getting Started (Prerequisites/Installation/Usage/Testing), Roadmap, Contributing, License, Acknowledgments. It contains **no API Reference** and its Installation/Usage rely on build-from-source with several unresolved placeholders.

---

## Project Title (T)
Title: `# URI`.
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo/official name | 1 | Repo folder name is `uri`; "URI" is the case-normalized repo name. |
| 2 not a different project | 1 | Correct project (lil-js/uri). |
| 3 no hallucinated terms | 1 | No invented terminology in title. |

**T = 3/3 = 100%**

## Overview (O)
"uri is a lightweight, chainable URI parser and builder … parse, validate, and construct URIs."
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality correct | 1 | Parse URIs — matches core functionality. |
| 2 supported by artifacts | 1 | Parse/build (chainable) and validate (`isURL`) all exist in `uri.js`. |
| 3 no unsupported features | 1 | Claims (chainable API, comprehensive parsing, validation, browser-based tests) are all real; remaining bullets are generic marketing. |
| 4 correct domain | 1 | URI/URL manipulation library. |
| 5 terminology matches repo | 1 | "chainable URI parser and builder" closely matches package.json description "Tiny URI parser and builder with chainable API". |

**O = 5/5 = 100%**

## Installation (I) — executed
Documented as build-from-source: `git clone https://github.com/lil-js/uri`, `cd uri`, then two install paths:
- **bower:** `echo 'INSERT-INSTALL-COMMAND-HERE'` (unresolved placeholder)
- **npm:** `npm install`

| Rule | Verdict | Evidence |
|---|---|---|
| 1 deps declared | 1 | Prerequisites list (JavaScript; Bower, Npm); `npm install` resolves the repo's declared devDeps. |
| 2 commands execute unmodified | 0 | The bower path is an **unresolved placeholder** (`INSERT-INSTALL-COMMAND-HERE`) — installs nothing. (`git clone` + `npm install` do work.) Ground-rule 6: placeholder auto-fails this execution rule; and any failing documented path fails the rule. |
| 3 no unresolved dependency errors | 1 | `npm install` in the fresh clone completed ("found 0 vulnerabilities"-class success; only `npm audit` advisories, no install errors). |
| 4 env requirements correct | 1 | No version claims to contradict authoritative metadata (no `engines`); JavaScript/npm are correct. |
| 5 expected artifact produced | 0 | The bower path (placeholder) produces no artifact; documented path fails. |

**I = 3/5 = 60%**

## Usage and Examples (U) — executed
Shell snippets under Usage/Testing (no library-usage code examples are provided):

| # | Snippet | Executes | Output match | E_i | Evidence |
|---|---|---|---|---|---|
| 1 | Usage (bower): `echo 'INSERT-RUN-COMMAND-HERE'` | No | No | 0 | Unresolved placeholder (ground-rule 6). |
| 2 | Usage (npm): `npm start` | No | No | 0 | Repo has no `start` script → `npm error … Did you mean npm star?`. |
| 3 | Testing (bower): `echo 'INSERT-TEST-COMMAND-HERE'` | No | No | 0 | Unresolved placeholder. |
| 4 | Testing (npm): `npm test` | Yes | n/a (no output documented) | 1 | Runs `make test` (terser + mocha), exits 0; matches "Run the test suite". (Surrounding prose still has an unresolved `{__test_framework__}` placeholder — noted as a caveat.) |

k=4, ΣE=1. **U = 1/4 = 25%**

## API Reference (A)
The README-AI document contains **no API Reference section** — no functions, classes, methods, parameters, or endpoints are documented (only a Features table and a file-tree Project Structure, which are outside the API-reference scope). Per ground-rule 8, a missing section scores 0.

**A = 0% (n=0, section absent)**

## License (L)
Text: "Uri is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file."
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo LICENSE | 0 | Repo is **MIT**; README never states MIT — only a generic "the LICENSE License" with a choosealicense.com link. |
| 2 valid identifier | 0 | "LICENSE" is not a valid SPDX identifier. |
| 3 no conflicting info | 1 | No two contradictory license names in the text. |

**L = 1/3 = 33.33%**

## C_R (README-AI) = (100 + 100 + 60 + 25 + 0 + 33.33)/6 = **53.06%**

---

## Section-score summary & average (single README ⇒ average = the row)
| readme | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| uri_readme_readmeai.md | 100 | 100 | 60 | 25 | 0 | 33.33 | 53.06 |
| **average** | 100 | 100 | 60 | 25 | 0 | 33.33 | **53.06** |

Average verified consistent.

## Cross-checked sources
- Cloned repo `/tmp/eval-uri-clone` (`uri.js`, `package.json`, `bower.json`, `LICENSE`).
- Executed clone + `npm install` + `npm start` + `npm test` in `/tmp/eval-uri-readmeai` (node v24.12.0, npm 11.6.2).
