# lil-uri README Correctness Evaluation

**Methodology:** Section 4.4.2 of *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis* (Andrade, UERJ).

**Documentation Sources Cross-checked:**
- Official npm package: `npm install lil-uri` → v0.3.1 (installed at `/tmp/uri-test/node_modules/lil-uri/`)
- Source code: `/tmp/uri-test/node_modules/lil-uri/uri.js`
- Official README: `/tmp/uri-test/node_modules/lil-uri/README.md`
- LICENSE file: `/tmp/uri-test/node_modules/lil-uri/LICENSE` (MIT, confirmed)
- Live execution via `node -e` for all code snippets and API element verifications
- GitHub repository: https://github.com/lil-js/uri

**Key ground-truth facts established before evaluation:**
- Correct package name on npm: `lil-uri` (NOT `@lil-js/uri`)
- Real API: `uri()` factory function returning a `URI` instance with **chainable methods** (not direct properties)
- Real property names: `protocol` (not `scheme`), `auth` (not `userinfo`), `hash` (not `fragment`), `search` (not `query` string)
- `query()` returns a plain object `{key: value}` — NOT a Map-like interface
- Methods on URI prototype: `protocol`, `host`, `hostname`, `port`, `auth`, `user`, `password`, `path`, `search`, `query`, `hash`, `get`, `build`, `toString`, `valueOf`, `parse`
- Static exports: `uri.VERSION`, `uri.isURL`, `uri.is`, `uri.URI`
- **Non-existent methods:** `addQuery`, `setQuery`, `removeQuery`, `normalize`, `parse` (as standalone export), `format`, `resolve`, `parseQuery`, `formatQuery`
- License: MIT (confirmed via LICENSE file)

---

## Scoring Formula (from TCC §4.4.2)

Each section uses binary criteria Vᵢ ∈ {0,1}. Section scores are percentages. Final score:

```
CR = (T + O + I + U + A + L) / 6
```

---

## data1.md Evaluation

### Step-by-step Reasoning

**Project Title (T)**

The README title is `# lil-js/uri`.

Criteria:
1. Title exactly matches repository/official name → The npm package is `lil-uri`; the GitHub repo is `lil-js/uri`. The title `lil-js/uri` matches the GitHub repository path but not the npm package name. The official project name as documented in the package is `lil-uri`. The title uses the GitHub org/repo format which is a valid representation of the project identity. ✅ V1=1
2. Title does not describe a different project → Correct, it refers to the URI library. ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucination in the title itself. ✅ V3=1

**T = (1+1+1)/3 × 100 = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → "minimalist JavaScript URI library designed to parse, manipulate, and serialize URIs" — accurate per official README ("URI parser and builder with semantic API"). ✅ V1=1
2. Described functionality supported by repository artifacts → Parsing, serialization, query manipulation, normalization — parsing and serialization are real. However, `normalize()` is described as a feature but does NOT exist in the source code (verified: `typeof u.normalize === 'undefined'`). ❌ V2=0
3. Overview does not describe unsupported features → Normalization is described as a domain concept but `normalize()` does not exist in the library. ❌ V3=0
4. Correctly identifies software domain → URI parsing/manipulation — correct. ✅ V4=1
5. Terminology matches repository terminology → Uses "scheme", "authority", "userinfo", "fragment" — these are RFC 3986 terms but the library uses `protocol`, `auth`, `hash` internally. The overview-level terminology is acceptable as conceptual framing. ✅ V5=1

**O = (1+0+0+1+1)/5 × 100 = 60**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → Only the package itself needed. ✅ V1=1
2. Installation commands execute without modification → `npm install @lil-js/uri` — **FAILS**. The correct package name is `lil-uri`. `@lil-js/uri` returns 404 on npm (verified: `npm error 404 The requested resource '@lil-js/uri@*' could not be found`). `yarn add @lil-js/uri` would also fail. ❌ V2=0
3. No unresolved dependency errors → The install command itself fails with 404. ❌ V3=0
4. Documented environment requirements correct → "works in both Node.js and browser environments" — accurate per official README. ✅ V4=1
5. Installation produces expected executable artifact → Cannot produce artifact since install fails. ❌ V5=0

**I = (1+0+0+1+0)/5 × 100 = 40**

---

**Usage and Examples (U)**

Snippets evaluated (k=4):

| # | Snippet | Execution Result | Score |
|---|---------|-----------------|-------|
| E1 | `import URI from "@lil-js/uri"` then `new URI(url)` accessing `uri.scheme`, `uri.userinfo`, `uri.host`, `uri.port`, `uri.path`, `uri.query`, `uri.fragment` | **FAILS**: (a) wrong package name `@lil-js/uri`; (b) `uri.scheme` is `undefined` (real: `u.parts.protocol` or `u.protocol()`); (c) `uri.userinfo` is `undefined` (real: `u.parts.auth`); (d) `uri.host` is a function not a string; (e) `uri.fragment` is `undefined` (real: `u.parts.hash`). Verified via `node -e`. | 0 |
| E2 | `uri.addQuery(key, value)`, `uri.setQuery(key, value)`, `uri.removeQuery(key)` | **FAILS**: None of these methods exist on URI prototype. Verified: `typeof u.addQuery === 'undefined'`. | 0 |
| E3 | `uri.path = '/newpath'; uri.fragment = 'top'; uri.toString()` | **FAILS**: Direct property assignment does not work — `path` is a method, assigning to it shadows the method but does not update `parts`. `toString()` returns original URI unchanged. Verified via `node -e`. | 0 |
| E4 | `uri.normalize()` | **FAILS**: `normalize` does not exist on URI prototype. Verified: `typeof u.normalize === 'undefined'`. | 0 |

**U = 0/4 × 100 = 0**

---

**API Reference (A)**

Documented API elements (n=12):

| # | Element | Exists | Names Correct | Params Correct | Returns Correct | Behavior Correct | Not Deprecated | Score |
|---|---------|--------|--------------|----------------|-----------------|-----------------|----------------|-------|
| A1 | `URI` class (constructor) | ✅ (via `uri.URI`) | ❌ (accessed as `new URI()` from default import — wrong import path) | ✅ | ✅ | ❌ | ✅ | 0 |
| A2 | `scheme` property (string) | ❌ (real: `protocol()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A3 | `userinfo` property (string) | ❌ (real: `auth()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A4 | `host` property (string) | ❌ (real: `host()` method returning string) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A5 | `port` property (string) | ❌ (real: `port()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A6 | `path` property (string) | ❌ (real: `path()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A7 | `query` property (raw string) | ❌ (real: `query()` returns plain object) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A8 | `fragment` property (string) | ❌ (real: `hash()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A9 | `addQuery(key, value): void` | ❌ (does not exist) | ❌ | ❌ | ❌ | ❌ | N/A | 0 |
| A10 | `setQuery(key, value): void` | ❌ (does not exist) | ❌ | ❌ | ❌ | ❌ | N/A | 0 |
| A11 | `removeQuery(key): void` | ❌ (does not exist) | ❌ | ❌ | ❌ | ❌ | N/A | 0 |
| A12 | `normalize(): void` | ❌ (does not exist) | ❌ | ❌ | ❌ | ❌ | N/A | 0 |

Only `toString(): string` is correctly documented (implicitly present in examples). However, it is not listed as a standalone API element in the reference section.

**A = 0/12 × 100 = 0**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → README states "MIT License" — confirmed MIT via `/tmp/uri-test/node_modules/lil-uri/LICENSE`. ✅ V1=1
2. License identifier is valid → "MIT" is a valid SPDX identifier. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

**L = (1+1+1)/3 × 100 = 100**

---

### data1.md Final Score

```
CR = (100 + 60 + 40 + 0 + 0 + 100) / 6 = 300 / 6 = 50.00
```

**data1.md scores 50.00.** The title and license are correct. The overview partially describes real functionality but introduces the non-existent `normalize()` feature. The installation command uses the wrong npm package name (`@lil-js/uri` instead of `lil-uri`), causing complete install failure. All four usage snippets fail at runtime because the README documents a completely fabricated API (class-based with direct properties `scheme`, `userinfo`, `fragment`, and methods `addQuery`, `setQuery`, `removeQuery`, `normalize`) that does not match the real chainable method-based API. The API Reference documents 12 elements, none of which correctly represent the actual library interface.

---

## data2.md Evaluation

### Step-by-step Reasoning

**Project Title (T)**

The README title is `# lil-uri`.

Criteria:
1. Title exactly matches repository/official name → `lil-uri` is the exact npm package name. ✅ V1=1
2. Title does not describe a different project → Correct. ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucination. ✅ V3=1

**T = (1+1+1)/3 × 100 = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → "minimalistic and efficient JavaScript library focused on parsing and manipulating URI strings" — accurate. ✅ V1=1
2. Described functionality supported by repository artifacts → Parsing, serialization, manipulation, normalization listed. Normalization is mentioned as a domain concept but `normalize()` does not exist. ❌ V2=0
3. Overview does not describe unsupported features → "Normalization: Handling encoding and decoding of URI components" — the library does decode via `decodeURIComponent` internally, but there is no explicit normalization API. This is borderline; the description is vague enough to be considered a description of internal behavior rather than a public API feature. ✅ V3=1
4. Correctly identifies software domain → URI parsing/manipulation — correct. ✅ V4=1
5. Terminology matches repository terminology → Uses "scheme", "authority", "path", "query", "fragment" — RFC 3986 terms used in overview context. The library's own README uses these terms conceptually. ✅ V5=1

**O = (1+0+1+1+1)/5 × 100 = 80**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → Only `lil-uri` needed. ✅ V1=1
2. Installation commands execute without modification → `npm install lil-uri` — **SUCCEEDS** (verified: v0.3.1 installed). `yarn add lil-uri` — valid command. ✅ V2=1
3. No unresolved dependency errors → Clean install confirmed (0 vulnerabilities). ✅ V3=1
4. Documented environment requirements correct → "Node.js or browser environments supporting ES modules" — accurate per official README. ✅ V4=1
5. Installation produces expected executable artifact → `require('lil-uri')` works post-install (verified). ✅ V5=1

**I = (1+1+1+1+1)/5 × 100 = 100**

---

**Usage and Examples (U)**

Snippets evaluated (k=3):

| # | Snippet | Execution Result | Score |
|---|---------|-----------------|-------|
| E1 | `import uri from 'lil-uri'`; `const parsed = uri(url)`; `console.log(parsed)` showing `{scheme, userinfo, host, port, path, search, hash}` | **PARTIALLY FAILS**: `uri(url)` works and returns a URI object. However, `console.log(parsed)` does NOT output `{scheme, userinfo, host, port, path, search, hash}` — it outputs a URI object with methods. `parsed.scheme` is `undefined`; `parsed.userinfo` is `undefined`. The documented output object shape is wrong. Then `parsed.path = '/new/path'` does not work (direct assignment does not update internal state). Verified via `node -e`. | 0 |
| E2 | `u.query.get('foo')` and `u.query.set('baz', '3')` | **FAILS**: `u.query()` returns a plain object `{foo:'1', bar:'2'}`, not a Map. `u.query.get` is `undefined`. `u.query.set` is `undefined`. Verified via `node -e`. | 0 |
| E3 | `uri()` then `u.scheme = 'http'`, `u.host = 'example.org'`, `u.path = '/index.html'`, `u.query.set('id', '123')` | **FAILS**: Direct property assignment does not work. `u.query.set` does not exist. Real API: `uri().protocol('http').host('example.org').path('/index.html').query({id:'123'}).build()`. Verified via `node -e`. | 0 |

**U = 0/3 × 100 = 0**

---

**API Reference (A)**

Documented API elements (n=10):

| # | Element | Exists | Names Correct | Params Correct | Returns Correct | Behavior Correct | Not Deprecated | Score |
|---|---------|--------|--------------|----------------|-----------------|-----------------|----------------|-------|
| A1 | `uri(input?: string \| URI): URI` | ✅ | ✅ | ✅ (optional string) | ✅ (URI object) | ✅ | ✅ | 1 |
| A2 | `scheme` property (string) | ❌ (real: `protocol()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A3 | `userinfo` property (string\|undefined) | ❌ (real: `auth()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A4 | `host` property (string\|undefined) | ❌ (real: `host()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A5 | `port` property (string\|undefined) | ❌ (real: `port()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A6 | `path` property (string) | ❌ (real: `path()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A7 | `search` property (string) | ❌ (real: `search()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A8 | `hash` property (string) | ❌ (real: `hash()` method) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |
| A9 | `toString(): string` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 1 |
| A10 | `query` Map-like interface with `get`, `set`, `delete`, `has`, `keys`, `values`, `entries` | ❌ (`query()` returns plain object, no Map methods) | ❌ | ❌ | ❌ | ❌ | ✅ | 0 |

2 out of 10 elements pass all criteria.

**A = 2/10 × 100 = 20**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → README states "MIT License" — confirmed MIT. ✅ V1=1
2. License identifier is valid → "MIT" is valid SPDX. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

**L = (1+1+1)/3 × 100 = 100**

---

### data2.md Final Score

```
CR = (100 + 80 + 100 + 0 + 20 + 100) / 6 = 400 / 6 = 66.67
```

**data2.md scores 66.67.** The title is correct (`lil-uri`), installation commands work correctly (`npm install lil-uri`), and the license is accurate. The overview is mostly correct but mentions normalization as a feature. The API Reference correctly identifies the `uri()` factory function and `toString()` but documents all URI component accessors as direct properties instead of chainable methods, and fabricates a Map-like query interface that does not exist. All usage snippets fail because they rely on the non-existent property-based and Map-based API.

---

## data3.md Evaluation

### Step-by-step Reasoning

**Project Title (T)**

The README title is `# lil-uri`.

Criteria:
1. Title exactly matches repository/official name → `lil-uri` is the exact npm package name. ✅ V1=1
2. Title does not describe a different project → Correct. ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucination. ✅ V3=1

**T = (1+1+1)/3 × 100 = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → "minimalistic JavaScript library designed to provide a simple and efficient API for parsing, constructing, and manipulating URI components" — accurate. ✅ V1=1
2. Described functionality supported by repository artifacts → Parsing, formatting, relative URI resolution, query handling, encoding/decoding listed. `resolve()` does not exist. Encoding/decoding is internal only. ❌ V2=0
3. Overview does not describe unsupported features → "Relative URI Resolution: Combining base URIs with relative references" — `resolve()` does not exist in the library. ❌ V3=0
4. Correctly identifies software domain → URI parsing/manipulation — correct. ✅ V4=1
5. Terminology matches repository terminology → Uses RFC 3986 terms at overview level — acceptable. ✅ V5=1

**O = (1+0+0+1+1)/5 × 100 = 60**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → Only the package itself. ✅ V1=1
2. Installation commands execute without modification → `npm install @lil-js/uri` — **FAILS**. Wrong package name. Correct is `lil-uri`. Verified: npm 404 error. ❌ V2=0
3. No unresolved dependency errors → Install fails with 404. ❌ V3=0
4. Documented environment requirements correct → "modern JavaScript environments including Node.js and web browsers via bundlers" — accurate. ✅ V4=1
5. Installation produces expected executable artifact → Cannot produce artifact since install fails. ❌ V5=0

**I = (1+0+0+1+0)/5 × 100 = 40**

---

**Usage and Examples (U)**

Snippets evaluated (k=4):

| # | Snippet | Execution Result | Score |
|---|---------|-----------------|-------|
| E1 | `import { parse } from '@lil-js/uri'`; `parse(url)` returning `{scheme, userinfo, host, port, path, query, fragment}` | **FAILS**: (a) wrong package name; (b) `parse` is not a named export — `uri.parse` is `undefined` (verified). The real `parse` is an instance method on URI prototype, not a standalone export. | 0 |
| E2 | `import { format } from '@lil-js/uri'`; `format(components)` | **FAILS**: `format` does not exist as an export. Verified: `uri.format === undefined`. | 0 |
| E3 | `import { resolve } from '@lil-js/uri'`; `resolve(base, relative)` | **FAILS**: `resolve` does not exist. Verified: `uri.resolve === undefined`. | 0 |
| E4 | `import { parseQuery, formatQuery } from '@lil-js/uri'`; `parseQuery(queryString)`, `formatQuery(params)` | **FAILS**: Neither `parseQuery` nor `formatQuery` exist. Verified: both `undefined`. | 0 |

**U = 0/4 × 100 = 0**

---

**API Reference (A)**

Documented API elements (n=5):

| # | Element | Exists | Names Correct | Params Correct | Returns Correct | Behavior Correct | Not Deprecated | Score |
|---|---------|--------|--------------|----------------|-----------------|-----------------|----------------|-------|
| A1 | `parse(uri: string): UriComponents` | ❌ (does not exist as standalone export; `uri.parse` is `undefined`) | ❌ | ❌ | ❌ | ❌ | N/A | 0 |
| A2 | `format(components: UriComponents): string` | ❌ (does not exist; `uri.format` is `undefined`) | ❌ | ❌ | ❌ | ❌ | N/A | 0 |
| A3 | `resolve(base: string, relative: string): string` | ❌ (does not exist; `uri.resolve` is `undefined`) | ❌ | ❌ | ❌ | ❌ | N/A | 0 |
| A4 | `parseQuery(query: string): Record<string, string>` | ❌ (does not exist; `uri.parseQuery` is `undefined`) | ❌ | ❌ | ❌ | ❌ | N/A | 0 |
| A5 | `formatQuery(params: Record<string, string>): string` | ❌ (does not exist; `uri.formatQuery` is `undefined`) | ❌ | ❌ | ❌ | ❌ | N/A | 0 |

**A = 0/5 × 100 = 0**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → README states "MIT License" — confirmed MIT. ✅ V1=1
2. License identifier is valid → "MIT" is valid SPDX. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

**L = (1+1+1)/3 × 100 = 100**

---

### data3.md Final Score

```
CR = (100 + 60 + 40 + 0 + 0 + 100) / 6 = 300 / 6 = 50.00
```

**data3.md scores 50.00.** The title and license are correct. The overview introduces non-existent features (relative URI resolution). The installation command uses the wrong package name (`@lil-js/uri`). All four usage snippets fail because the README documents a completely fabricated functional API (`parse`, `format`, `resolve`, `parseQuery`, `formatQuery` as named exports) that does not exist in the library. The API Reference documents 5 elements, none of which exist in the actual package.

---

## Summary: All Three lil-uri READMEs

| README | T | O | I | U | A | L | CR |
|--------|---|---|---|---|---|---|-----|
| data1.md | 100 | 60 | 40 | 0 | 0 | 100 | **50.00** |
| data2.md | 100 | 80 | 100 | 0 | 20 | 100 | **66.67** |
| data3.md | 100 | 60 | 40 | 0 | 0 | 100 | **50.00** |
| **Average** | **100** | **66.67** | **60** | **0** | **6.67** | **100** | **55.56** |

### Final Average Score (Equation 2 from TCC)

```
Score_avg = (50.00 + 66.67 + 50.00) / 3 = 55.56
```

---

## Analysis and Observations

**Why scores are low:**

`lil-uri` is a small, older library (v0.3.1) with a chainable, accessor-based API that is unusual compared to modern JavaScript libraries. The LLM consistently hallucinated APIs that do not exist:

- **data1.md** invented a class-based API with direct properties (`scheme`, `userinfo`, `fragment`) and mutation methods (`addQuery`, `setQuery`, `removeQuery`, `normalize`) — none of which exist.
- **data2.md** invented a property-based API and a Map-like query interface — the real API uses chainable methods and returns plain objects.
- **data3.md** invented a functional API with named exports (`parse`, `format`, `resolve`, `parseQuery`, `formatQuery`) — none of which exist.

**What all three got right:**
- Title (data2 and data3 use the correct npm name `lil-uri`; data1 uses the GitHub path `lil-js/uri`)
- License (MIT — consistently correct)
- High-level purpose description (URI parsing and manipulation)
- data2 correctly identified the `uri()` factory function and `toString()`

**What all three got wrong:**
- Usage snippets: 0% across all three — every single code example fails at runtime
- API Reference: heavily hallucinated in all three cases
- Installation: data1 and data3 use wrong package name `@lil-js/uri`; only data2 uses correct `lil-uri`

**Root cause:** The LLM appears to have generated APIs based on patterns from similar URI libraries (e.g., the `URI.js` library which does have `scheme`, `fragment`, `addQuery` etc.) rather than the actual `lil-uri` source code. This is a classic hallucination pattern where the model conflates similar-sounding libraries.
