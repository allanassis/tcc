# ATRAK Evaluation — README-Gen (project `uri` / lil-js/uri)

> ATRAK is **presence-only**: hallucinated or factually incorrect content still
> counts as present. An element is absent (0) only for an empty/missing section,
> a bare name-only list, or unresolved placeholders. Factual accuracy is scored
> in the correctness dimension, not here.

## Ground Truth Reference
- **Project:** lil-uri (npm/bower package `lil-uri`; GitHub repo `lil-js/uri`).
- **Repository:** https://github.com/lil-js/uri
- **Domain:** URI/URL parsing and building in JavaScript (Node + browser).
- **Core domain entities:** URI and its components — protocol/scheme, host, hostname, port, auth (user/password), path, search/query, hash/fragment.
- **Core execution facts:** UMD/CommonJS module (`require('lil-uri')` / global `lil.uri`); factory `uri(str)` returns a chainable `URI` instance; accessors get/set components; `build()`/`toString()` serialize; `uri.is/isURL` validate; MIT license; no `engines` requirement.
- **Core usage patterns:** parse a URL string then read components; chain accessors to build a URL; read the query object.

---

## README 1 — `data1.md`
| Element | Verdict | Evidence |
|---|---|---|
| K_D Domain Concepts | **1** | Dedicated "Domain Concepts" list with definitions (URI Structure, Parsing, Serialization, Query Parameter Manipulation, Normalization) — explanatory prose, not a bare name list. |
| K_E Execution Facts | **1** | Installation commands, environment ("Node.js and browser"), constructor input, property/return descriptions, method signatures. |
| K_U Usage Patterns | **1** | Four runnable code examples (parse, manipulate query, serialize, normalize) with expected outputs and narrative. |

**K = 3/3 = 100%**

## README 2 — `data2.md`
| Element | Verdict | Evidence |
|---|---|---|
| K_D Domain Concepts | **1** | "Domain Concepts" list with definitions (URI Components, Parsing, Serialization, Manipulation, Normalization). |
| K_E Execution Facts | **1** | npm/yarn install, environment claim, factory return type, property/method descriptions, query interface signatures. |
| K_U Usage Patterns | **1** | Three code examples (parse+serialize, query access, build from components) with documented outputs. |

**K = 3/3 = 100%**

## README 3 — `data3.md`
| Element | Verdict | Evidence |
|---|---|---|
| K_D Domain Concepts | **1** | "Domain Concepts" list with definitions (URI Components, Parsing, Formatting, Relative URI Resolution, Query Handling, Encoding & Decoding). |
| K_E Execution Facts | **1** | Install command, environment support, function signatures with parameter/return descriptions. |
| K_U Usage Patterns | **1** | Four code examples (parse, format, resolve, query parse/format) with outputs. |

**K = 3/3 = 100%**

---

## Summary & averages
| readme | K_D | K_E | K_U | ATRAK |
|---|---|---|---|---|
| data1.md | 1 | 1 | 1 | 100 |
| data2.md | 1 | 1 | 1 | 100 |
| data3.md | 1 | 1 | 1 | 100 |
| **average** | 1 | 1 | 1 | **100** |

All three READMEs provide substantive (if partly hallucinated) domain, execution, and usage content, so all K elements are present. Averages verified consistent.

## Cross-checked sources
Cloned repo `/tmp/eval-uri-clone` (`uri.js`, `package.json`, `bower.json`, `LICENSE`, `README.md`); npm registry (`lil-uri`, `@lil-js/uri`).
