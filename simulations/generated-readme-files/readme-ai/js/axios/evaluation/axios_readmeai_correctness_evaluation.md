# Axios — README-AI Correctness Evaluation

Tool: **README-AI** v0.6.0rc1 (`gpt-4.1-mini-2025-04-14`).
File evaluated: `compare-readme-ai/axios_readme_readmeai.md` (single README).

## Cross-checked sources
- Installed/built artifact: `axios@1.18.1` (registry) and `axios@1.19.0` (source build from
  `git clone --depth 1 https://github.com/axios/axios` into `/tmp/axios-src`).
- Repo `package.json` scripts (from the source build): confirmed a real `start`
  (`node ./sandbox/server.js`) and `test` (`vitest run`) script exist.
- Official docs <https://axios-http.com/docs/intro>; GitHub repo/README (branch `v1.x`, MIT).

## Executed installation / usage path (the README's documented path)
| Command | Result | Evidence |
|---|---|---|
| `git clone https://github.com/axios/axios` | exit 0 | shallow clone succeeded |
| `cd axios` | ok | — |
| `npm install` (from source) | exit 0 | dev deps installed; "3 high severity vulnerabilities" but **no dependency-resolution errors** |
| `npm start` (Usage) | server up | `> node ./sandbox/server.js` → "Listening on localhost:3000..." (held 8s, killed) |
| `npm test` (Testing) | framework launches | `vitest run` executes unit tests; killed at 30s (long suite) |

## Structural note
The README's substantive content is a Features table + a large Project-Index file tree.
Per ground rule 7, that content is used as the carrier for sections whose own heading is empty
(Overview) or generic.

---

## Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo/official name | 1 | `# AXIOS` == `axios` (case only) |
| 2 not a different project | 1 | Content is axios |
| 3 no hallucinated terminology | 1 | Title is just the name |

**T = 100**

## Overview (O)
The `## Overview` heading is **empty**; the immediately-following **Features** table is the only
carrier (ground rule 7) and is evaluated here.
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality correct | 1 | Features/Architecture: "Promise-based HTTP client … browser & Node.js" |
| 2 supported by artifacts | 1 | Verified against installed package |
| 3 no unsupported features | 1 | User-facing claims (interceptors, adapters, cancellation, config-driven) are real |
| 4 correct domain | 1 | HTTP client |
| 5 terminology matches repo | 1 | promise/interceptor/adapter vocabulary matches |

**O = 100** (carried entirely by the Features table; the Overview section itself is empty).

## Installation (I) — executed
| Rule | Verdict | Evidence |
|---|---|---|
| 1 dependencies declared | 1 | Prereqs (JS, npm); build deps in `package.json`, resolved by `npm install` |
| 2 commands execute unmodified | 1 | clone/cd/`npm install` all exit 0 |
| 3 no unresolved dependency errors | 1 | install completed; vulnerabilities ≠ resolution errors |
| 4 env requirements correct | 1 | "JavaScript / Npm"; no version claim; axios declares no `engines` → nothing false |
| 5 produces expected artifact | 1 | Build completes; documented `npm start` yields a runnable server (localhost:3000) |

**I = 100** (note: the from-source framing is unusual for a library, but every documented command executes).

## Usage and Examples (U) — executed (k = 2)
| # | Snippet | Exec | Notes | E_i |
|---|---|---|---|---|
| 1 | `npm start` | server starts | matches "Run the project" | 1 |
| 2 | `npm test` | vitest runs | description says "Axios uses the **{__test_framework__}** test framework" — **unresolved placeholder** ⇒ ground rule 6 fails the execution-related rule | 0 |

**U = (1/2)×100 = 50**

## API Reference (A)
The README contains **no** documented functions/classes/methods/endpoints with parameters — the
Project Index describes files, not an API. The section is absent ⇒ ground rule 8.

**A = 0** (n = 0 documented elements; section lacking).

## License (L)
Text: *"Axios is protected under the [LICENSE](https://choosealicense.com/licenses) License … refer to the [LICENSE](https://choosealicense.com/licenses/) file."*
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo LICENSE | 0 | Repo is **MIT**; README names no license (generic "LICENSE", links to choosealicense.com listing) — does not match/identify MIT |
| 2 valid identifier | 0 | "LICENSE" is not a valid SPDX identifier |
| 3 no conflicting info | 1 | No second, contradictory license name stated (top badge renders MIT dynamically; text is vague, not contradictory) |

**L = (1/3)×100 = 33.33**

---

## Section-score summary
| readme | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| axios_readme_readmeai.md | 100 | 100 | 100 | 50 | 0 | 33.33 | 63.89 |
| **average** | 100 | 100 | 100 | 50 | 0 | 33.33 | **63.89** |

C_R = (100+100+100+50+0+33.33)/6 = 63.89. Single README ⇒ average row equals the row.
