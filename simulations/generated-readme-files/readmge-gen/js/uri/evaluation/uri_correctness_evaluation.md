# Correctness Evaluation — README-Gen (project `uri` / lil-js/uri)

Tool: README-Gen. READMEs evaluated in order: `data1.md`, `data2.md`, `data3.md`.

## Ground Truth (cross-checked sources)

- Repository (shallow clone): https://github.com/lil-js/uri → `/tmp/eval-uri-clone`
- `package.json`: `name: "lil-uri"`, `version: 0.3.1`, `license: MIT`, `main: ./uri.js`, **no `engines` field**, devDeps chai/mocha/uglify-js, dep terser.
- `bower.json`: `name: "lil-uri"`.
- `LICENSE`: MIT © Tomas Aparicio and contributors.
- `uri.js` (real API surface, UMD/CommonJS module; internal `VERSION = '0.2.2'`):
  - Factory `uri([uriString])` → returns a `URI` instance. `uri.URI` (constructor), `uri.VERSION`, `uri.is` = `uri.isURL` = `isURL(str)` → boolean.
  - Chainable instance accessors (getter with no arg, setter returning `this` with arg): `protocol`, `host`, `hostname`, `port`, `auth`, `user`, `password`, `path`, `search`, `query` (getter returns parsed object; setter takes object), `hash`; plus `get(name)`, `parse(uri)`, `build()`/`toString()`/`valueOf()`.
  - **No** `scheme`/`userinfo`/`fragment` data properties, **no** `addQuery`/`setQuery`/`removeQuery`/`normalize`, **no** named exports `parse`/`format`/`resolve`/`parseQuery`/`formatQuery`, **no** Map-like `query.get/set/...`.
- npm registry checks: `npm view lil-uri version` → `0.3.1` (exists); `npm view @lil-js/uri` → **404 Not Found** (does not exist). `npm/yarn` install + `node` snippet execution in `/tmp/eval-uri`.

Execution environment: node v24.12.0, npm 11.6.2, yarn 1.22.22.

---

## README 1 — `data1.md`

Title: `# lil-js/uri`. Uses package `@lil-js/uri`, a `URI` class with `.scheme/.userinfo/...` properties and `addQuery/setQuery/removeQuery/normalize` methods.

### Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo/official name | 1 | `lil-js/uri` is the GitHub repository slug. |
| 2 not a different project | 1 | Correctly the URI project. |
| 3 no hallucinated terms | 1 | No invented terminology. |

**T = 3/3 = 100%**

### Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality correct | 1 | "parse, manipulate, and serialize URIs" — matches. |
| 2 supported by artifacts | 1 | Parse/build exist in `uri.js`. |
| 3 no unsupported features | 0 | Domain Concepts list claims "Query Parameter Manipulation: Adding, updating, and removing query parameters" and "Normalization: Adjusting URI parts according to standard rules" — no such per-parameter add/update/remove nor a normalize capability exists. |
| 4 correct domain | 1 | URI library — correct. |
| 5 terminology matches repo | 0 | Uses `scheme`/`authority`/`userinfo`/`fragment`; repo terminology is `protocol`/`auth`/`hash`. |

**O = 3/5 = 60%**

### Installation (I) — executed
Documented paths: `npm install @lil-js/uri`, `yarn add @lil-js/uri`.

| Rule | Verdict | Evidence |
|---|---|---|
| 1 deps declared | 1 | Declares the package + "Node.js and browser". |
| 2 commands execute unmodified | 0 | `npm install @lil-js/uri` → **E404 Not Found**; `yarn add @lil-js/uri` → **registry Not found**. |
| 3 no unresolved dependency errors | 0 | 404 = unresolved dependency (package does not exist). |
| 4 env requirements correct | 1 | "Node.js and browser" is correct for the real package; no false version claim (no `engines`). |
| 5 expected artifact produced | 0 | Nothing installs; no artifact. |

**I = 2/5 = 40%**

### Usage and Examples (U) — executed
All snippets `import URI from "@lil-js/uri"` (nonexistent package); tested API behavior against real source.

| # | Snippet | Executes | Output match | E_i | Evidence |
|---|---|---|---|---|---|
| 1 | Basic parse (`new URI`, `.scheme`…) | No | No | 0 | Import fails (404); against real src `.scheme`/`.userinfo` → `undefined`, `.host` is a function. |
| 2 | `addQuery/setQuery/removeQuery` | No | No | 0 | `u.addQuery` is `undefined` → TypeError. |
| 3 | `uri.path=…; toString()` | No | No | 0 | Import fails; property-set does not affect real serialization. |
| 4 | `uri.normalize()` | No | No | 0 | `normalize` does not exist → TypeError. |

**U = 0/4 = 0%**

### API Reference (A)
Documented function/class/method elements (data properties excluded per rubric scope).

| Element | Exists | Names | Types | Return | Behavior | Not-deprecated | A_i |
|---|---|---|---|---|---|---|---|
| `URI` class (`new URI(str)`) | 1 (`uri.URI`) | 1 | 1 | 1 | 0 (parses to `.parts.*`, not `.scheme`/`.userinfo`) | 1 | 0 |
| `addQuery(key,value)` | 0 | — | — | — | — | — | 0 |
| `setQuery(key,value)` | 0 | — | — | — | — | — | 0 |
| `removeQuery(key)` | 0 | — | — | — | — | — | 0 |
| `normalize()` | 0 | — | — | — | — | — | 0 |
| `toString()` | 1 | 1 | 1 | 1 | 1 (serializes) | 1 | 1 |

n=6, Σ=1. **A = 1/6 = 16.67%**

### License (L)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo LICENSE | 1 | States MIT; repo LICENSE is MIT. |
| 2 valid identifier | 1 | `MIT` valid SPDX. |
| 3 no conflicting info | 1 | Single consistent statement. |

**L = 3/3 = 100%**

### C_R (data1) = (100 + 60 + 40 + 0 + 16.67 + 100)/6 = **52.78%**

---

## README 2 — `data2.md`

Title `# lil-uri`. Uses **correct** package `lil-uri`; `import uri from "lil-uri"`; factory `uri(input)`; expects `.scheme/.userinfo` props and a Map-like `query` (`.get/.set/.delete/...`).

### Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches name | 1 | `lil-uri` = exact npm/bower package name. |
| 2 not different project | 1 | Correct. |
| 3 no hallucinated terms | 1 | Correct. |

**T = 100%**

### Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality | 1 | Parse/manipulate URIs — matches. |
| 2 supported by artifacts | 1 | Parse/build exist. |
| 3 no unsupported features | 1 | "Manipulation: changing query params or path" and "Normalization: encoding/decoding" — the lib does set path/query (object) and internally decodes; no explicit unsupported method claimed in overview. |
| 4 correct domain | 1 | URI library. |
| 5 terminology matches repo | 0 | `scheme`/`authority`/`fragment` vs repo `protocol`/`auth`/`hash`. |

**O = 4/5 = 80%**

### Installation (I) — executed
Documented paths: `npm install lil-uri`, `yarn add lil-uri`.

| Rule | Verdict | Evidence |
|---|---|---|
| 1 deps declared | 1 | Package + node/browser stated. |
| 2 commands execute unmodified | 1 | `npm install lil-uri` → "added 12 packages"; `yarn add lil-uri` → "success Saved". |
| 3 no unresolved dependency errors | 1 | "found 0 vulnerabilities"; no errors. |
| 4 env requirements correct | 1 | No false version claim (no `engines`); ESM import works via CJS interop. |
| 5 expected artifact produced | 1 | `node_modules/lil-uri/uri.js` present after both installs. |

**I = 5/5 = 100%**

### Usage and Examples (U) — executed

| # | Snippet | Executes | Output match | E_i | Evidence |
|---|---|---|---|---|---|
| 1 | parse + `console.log(parsed)` object + set `.path/.search` + `toString()` | Partial | No | 0 | `parsed.scheme` → `undefined`, `.host` is a function; documented plain object output not produced; property-set does not change serialization. |
| 2 | `u.query.get("foo")` / `.set` | No | No | 0 | **`u.query.get is not a function`** (query is a method returning a plain object). |
| 3 | `uri()` + `u.scheme=…` + `u.query.set(...)` | No | No | 0 | **`u.query.set is not a function`**. |

**U = 0/3 = 0%**

### API Reference (A)

| Element | Exists | Names | Types | Return | Behavior | Not-deprecated | A_i |
|---|---|---|---|---|---|---|---|
| `uri(input?: string\|URI): URI` | 1 | 1 | partial | partial | 0 (string parse works, but "clones an existing URI object" is unsupported → returns empty parts) | 1 | 0 |
| `toString(): string` | 1 | 1 | 1 | 1 | 1 (serializes) | 1 | 1 |
| `query` Map-like (`get/set/delete/has/keys/values/entries`) | 0 | — | — | — | — | — | 0 |

n=3, Σ=1. **A = 1/3 = 33.33%**

### License (L)
MIT stated; matches repo; valid; no conflict. **L = 100%**

### C_R (data2) = (100 + 80 + 100 + 0 + 33.33 + 100)/6 = **68.89%**

---

## README 3 — `data3.md`

Title `# lil-uri`. Uses package `@lil-js/uri` (nonexistent) and **named exports** `parse`, `format`, `resolve`, `parseQuery`, `formatQuery`.

### Project Title (T)
Matches package name `lil-uri`; not different; no hallucination. **T = 3/3 = 100%**

### Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality | 1 | Parsing/constructing URIs — matches. |
| 2 supported by artifacts | 1 | Parse/build exist. |
| 3 no unsupported features | 0 | Claims "Relative URI Resolution: Combining base URIs with relative references" — no resolve capability exists. |
| 4 correct domain | 1 | URI library. |
| 5 terminology matches repo | 0 | `scheme`/`fragment`/`authentication` vs repo `protocol`/`hash`/`auth`. |

**O = 3/5 = 60%**

### Installation (I) — executed
Documented path: `npm install @lil-js/uri`.

| Rule | Verdict | Evidence |
|---|---|---|
| 1 deps declared | 1 | Declares package + node/browser/bundlers. |
| 2 commands execute unmodified | 0 | `npm install @lil-js/uri` → **E404**. |
| 3 no unresolved dependency errors | 0 | 404 — package does not exist. |
| 4 env requirements correct | 1 | No false version claim. |
| 5 expected artifact produced | 0 | Nothing installs. |

**I = 2/5 = 40%**

### Usage and Examples (U) — executed
All snippets `import { … } from "@lil-js/uri"` with named exports.

| # | Snippet | Executes | Output match | E_i | Evidence |
|---|---|---|---|---|---|
| 1 | `parse(url)` | No | No | 0 | Package 404; named export absent. Against real src: `SyntaxError: Named export not found`. |
| 2 | `format(components)` | No | No | 0 | `format` does not exist. |
| 3 | `resolve(base, relative)` | No | No | 0 | `resolve` does not exist. |
| 4 | `parseQuery`/`formatQuery` | No | No | 0 | Neither export exists. |

**U = 0/4 = 0%**

### API Reference (A)

| Element | Exists | A_i |
|---|---|---|
| `parse(uri: string): UriComponents` | 0 (only `URI.prototype.parse`, not a standalone export) | 0 |
| `format(components): string` | 0 | 0 |
| `resolve(base, relative): string` | 0 | 0 |
| `parseQuery(query): Record` | 0 | 0 |
| `formatQuery(params): string` | 0 | 0 |

n=5, Σ=0. **A = 0/5 = 0%**

### License (L)
MIT stated; matches; valid; no conflict. **L = 100%**

### C_R (data3) = (100 + 60 + 40 + 0 + 0 + 100)/6 = **50.00%**

---

## Section-score summary & averages

| readme | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| data1.md | 100 | 60 | 40 | 0 | 16.67 | 100 | 52.78 |
| data2.md | 100 | 80 | 100 | 0 | 33.33 | 100 | 68.89 |
| data3.md | 100 | 60 | 40 | 0 | 0 | 100 | 50.00 |
| **average** | 100 | 66.67 | 60 | 0 | 16.67 | 100 | **57.22** |

Averages verified arithmetically consistent with per-README rows.

## Cross-checked sources
- Cloned repo `/tmp/eval-uri-clone`: `package.json`, `bower.json`, `LICENSE`, `uri.js`, `README.md`.
- npm registry: `npm view lil-uri` (0.3.1, exists), `npm view @lil-js/uri` (404).
- Executed installs/snippets in `/tmp/eval-uri`, `/tmp/eval-uri-yarn` (node v24.12.0, npm 11.6.2, yarn 1.22.22).
