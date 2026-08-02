# Axios — README-Gen Correctness Evaluation

Tool: **README-Gen** (structured ATRAK-grounded prompting, `gpt-4.1-mini-2025-04-14`).
Files evaluated in order: `data1.md`, `data2.md`, `data3.md`.

## Cross-checked sources
- Installed artifact: `axios@1.18.1` (npm registry) in an isolated project `/tmp/eval-axios`; source build `axios@1.19.0` from `git clone --depth 1 https://github.com/axios/axios`.
- Node introspection of the installed package (`typeof` on the public surface, interceptor return value, `CancelToken.source()`, `isCancel`).
- Official docs: <https://axios-http.com/docs/intro> and the API reference pages.
- GitHub repository & README: <https://github.com/axios/axios> (default branch `v1.x`, `LICENSE` present, license shown as **MIT**).
- The GitHub README table of contents links **CancelToken** to the anchor `#canceltoken-deprecated`, and the Cancellation docs describe `CancelToken` as **deprecated** in favour of `AbortController`.

## Ground-truth API surface (node introspection, `/tmp/eval-axios`)
```
axios            -> function
axios.get/post/put/delete/patch -> function
axios.create     -> function (returns instance function)
axios.CancelToken-> function ; CancelToken.source -> function  [DEPRECATED per docs]
axios.isCancel   -> function (returns boolean)
axios.interceptors.request.use / response.use -> function (returns numeric id, observed 0)
axios.defaults   -> object
```
No `engines` field in `package.json` (checked: `require('axios/package.json').engines === undefined`). License field = `MIT`.

## Snippet execution environment
Each snippet written to a file and run with `node` (imports added where missing = permitted, recorded). Placeholder domains such as `https://api.example.com/...` are ordinary illustrative example URLs (not template placeholders like `{url}`), so ground rule 6 does not apply; they resolve to `ENOTFOUND`. A snippet **fails rule 4** only when it raises an *unhandled* exception (no `.catch`/`try`), which Node surfaces as `UnhandledPromiseRejection` with a non-zero exit code.

---

## README 1 — `data1.md`

### Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo/official name | 1 | Title `# Axios` == repo `axios/axios` |
| 2 not a different project | 1 | Content is about axios HTTP client |
| 3 no hallucinated terminology | 1 | All terms (HTTP client, interceptors) are axios terms |

**T = (3/3)×100 = 100**

### Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality correct | 1 | "promise-based HTTP client … browser and Node.js" matches docs |
| 2 supported by artifacts | 1 | HTTP client verified via installed package |
| 3 no unsupported features | 1 | Interceptors, cancellation tokens, adapters, JSON transform all real |
| 4 correct domain | 1 | HTTP client domain correct |
| 5 terminology matches | 1 | Matches repo vocabulary |

**O = (5/5)×100 = 100**

### Installation (I) — executed
Documented paths: `npm install axios`, `yarn add axios`.
| Rule | Verdict | Evidence |
|---|---|---|
| 1 dependencies declared | 1 | `axios` named; transitive deps auto-resolved by npm/yarn |
| 2 commands execute unmodified | 1 | `npm install axios` exit 0; `yarn add axios` exit 0 (`/tmp/eval-axios-yarn`) |
| 3 no unresolved dependency errors | 1 | npm "found 0 vulnerabilities"; yarn "Done in 0.92s" |
| 4 env requirements correct | 1 | "modern browsers and Node.js"; no version claim; no `engines` field to contradict |
| 5 produces expected artifact | 1 | `require('axios')` resolves to v1.18.1 (importable module) |

**I = (5/5)×100 = 100**

### Usage and Examples (U) — executed (k = 7)
| # | Snippet | Exec | Unhandled exc? | Output match | E_i |
|---|---|---|---|---|---|
| 1 | Basic GET (`.catch`) | runs, exit 0 | no (ENOTFOUND caught) | no output documented | 1 |
| 2 | POST JSON (`.catch`) | runs, exit 0 | no | n/a | 1 |
| 3 | async/await (`try/catch`) | runs, exit 0 | no | n/a | 1 |
| 4 | Set default config (no request) | runs, exit 0 | no | prints defaults | 1 |
| 5 | Create instance (`.then`, **no `.catch`**) | exit 1 | **YES — UnhandledPromiseRejection AxiosError** | — | 0 |
| 6 | Interceptors logging (no request) | runs, exit 0 | no | registers | 1 |
| 7 | Cancel request (`.catch`, CancelToken) | runs, exit 0 | no | "Request canceled …" | 1 |

**U = (6/7)×100 = 85.71**

### API Reference (A) — n = 8
| Element | Exists | Names/params | Types | Returns | Behaviour | Not deprecated | A_i |
|---|---|---|---|---|---|---|---|
| `axios(config)` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `axios.get(url[,config])` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `axios.post(url[,data[,config]])` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `axios.create([config])` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `axios.interceptors.request.use` | 1 | 1 | 1 | 1 (numeric id) | 1 | 1 | 1 |
| `axios.interceptors.response.use` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| `axios.CancelToken` | 1 | 1 | 1 | 1 | 1 | **0 (deprecated, documented as current)** | 0 |
| `axios.isCancel(value)` | 1 | 1 | 1 | 1 (boolean) | 1 | 1 | 1 |

**A = (7/8)×100 = 87.5**

### License (L)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo LICENSE | 1 | "MIT License" == repo MIT |
| 2 valid identifier | 1 | MIT is a valid SPDX id |
| 3 no conflicting info | 1 | Single consistent MIT statement (link uses `master`; not a licence conflict) |

**L = (3/3)×100 = 100**

**C_R(data1) = (100+100+100+85.71+87.5+100)/6 = 95.54**

---

## README 2 — `data2.md`

### Project Title (T) = 100
`# Axios`; correct, no hallucination.

### Overview (O) = 100
All 5 rules pass. Adds "Response Objects" and "Adapter" concepts — all accurate axios terminology; no unsupported features.

### Installation (I) = 100 — executed
Documented `npm install axios` and `yarn add axios`; both executed as above. "compatible with both browser and Node.js … no additional setup" — correct; no version claim vs. absent `engines`.

### Usage and Examples (U) — executed (k = 6)
| # | Snippet | Exec | Unhandled exc? | E_i |
|---|---|---|---|---|
| 1 | Basic GET (`.catch`) | exit 0 | no | 1 |
| 2 | POST JSON (`.catch`) | exit 0 | no | 1 |
| 3 | Custom headers + params (`.then`, **no `.catch`**) | exit 1 | **YES — UnhandledPromiseRejection** | 0 |
| 4 | async/await (`try/catch`) | exit 0 | no | 1 |
| 5 | Interceptors (no request) | exit 0 | no | 1 |
| 6 | Cancelling (`.catch`, CancelToken) | exit 0 | no ("Request canceled …") | 1 |

**U = (5/6)×100 = 83.33**

### API Reference (A) — n = 11
Elements: `axios(config)`, `axios.get`, `axios.post`, `axios.put`, `axios.delete`, `axios.patch`, `axios.create`, `axios.interceptors.request.use`, `axios.interceptors.response.use`, `axios.CancelToken`, `axios.isCancel`.
- All exist and match implementation (put/delete/patch verified `typeof === 'function'`).
- `axios.CancelToken` → A_i = 0 (deprecated, documented as current). All others A_i = 1.

**A = (10/11)×100 = 90.91**

### License (L) = 100
"MIT License", link uses `main`; valid, no conflict.

**C_R(data2) = (100+100+100+83.33+90.91+100)/6 = 95.71**

---

## README 3 — `data3.md`

### Project Title (T) = 100
`# Axios`; correct.

### Overview (O) = 100
HTTP requests/responses, interceptors, cancellation, request config, Promise API, adapters — all accurate.

### Installation (I) = 100 — executed
Documented `npm install axios` and `yarn add axios`; both executed successfully.

### Usage and Examples (U) — executed (k = 6)
| # | Snippet | Exec | Unhandled exc? | E_i |
|---|---|---|---|---|
| 1 | Basic GET (`.catch`) | exit 0 | no | 1 |
| 2 | POST (`.catch`) | exit 0 | no | 1 |
| 3 | `axios({method,url,headers,timeout,params})` (`.catch`) | exit 0 | no | 1 |
| 4 | async/await (`try/catch`) | exit 0 | no | 1 |
| 5 | Cancellation (`.then`+`.catch`, CancelToken) | exit 0 | no ("Request canceled …") | 1 |
| 6 | Interceptors (no request) | exit 0 | no | 1 |

**U = (6/6)×100 = 100**

### API Reference (A) — n = 11
Elements: `axios(config)`, `axios.get`, `axios.post`, `axios.put`, `axios.delete`, `axios.create`, `axios.CancelToken`, `axios.isCancel`, Response Object schema (`data/status/statusText/headers/config/request` — all verified real), `axios.interceptors.request.use`, `axios.interceptors.response.use`.
- `axios.CancelToken` → A_i = 0 (deprecated). All others A_i = 1.

**A = (10/11)×100 = 90.91**

### License (L) = 100
"MIT License"; link uses `master`; valid, no conflict.

**C_R(data3) = (100+100+100+100+90.91+100)/6 = 98.48**

---

## Section-score summary
| readme | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| data1.md | 100 | 100 | 100 | 85.71 | 87.5 | 100 | 95.54 |
| data2.md | 100 | 100 | 100 | 83.33 | 90.91 | 100 | 95.71 |
| data3.md | 100 | 100 | 100 | 100 | 90.91 | 100 | 98.48 |
| **average** | 100 | 100 | 100 | 89.68 | 89.77 | 100 | **96.58** |

Average-row check: usage (85.71+83.33+100)/3 = 89.68; api (87.5+90.91+90.91)/3 = 89.77; C_R (95.54+95.71+98.48)/3 = 96.58. Consistent.
