# Axios — README-Gen ATRAK Evaluation (presence, not correctness)

ATRAK assesses **presence** of three Knowledge Elements [Thayer et al. 2021]. Hallucinated or
incorrect content still counts as present; an element is absent (0) only when the carrying
section is empty/missing, is a bare name-only list, or consists solely of unresolved placeholders.

## Ground Truth Reference
- **Project:** axios
- **Repository:** https://github.com/axios/axios (default branch `v1.x`)
- **Domain:** Promise-based HTTP client for the browser and Node.js
- **Core domain entities:** HTTP requests/responses, Promises, interceptors, request config,
  cancellation (CancelToken/AbortController), adapters (XHR/http/fetch), response schema.
- **Core execution facts:** install via `npm install axios` / `yarn add axios`; import via
  `require`/`import`; returns a Promise resolving to a response object; config options
  (url, method, baseURL, headers, params, data, timeout, responseType); no `engines` constraint.
- **Core usage patterns:** GET/POST/async-await requests, instance creation, interceptors,
  request cancellation.

---

## README 1 — `data1.md`
| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | 1 | "### Domain Concepts" defines HTTP Requests, Promises, Interceptors, Cancellation Tokens, Adapters, Configuration Options — each with an explanatory sentence (not bare names). |
| **K_E Execution Facts** | 1 | Installation commands, config-option list with types (url/method/baseURL/headers/params/data/timeout/responseType), documented Promise return values. |
| **K_U Usage Patterns** | 1 | Seven runnable code examples (GET, POST, async/await, defaults, instance, interceptors, cancellation) with what/how narration. |

**K(data1) = (1+1+1)/3 × 100 = 100**

## README 2 — `data2.md`
| Element | Verdict | Evidence |
|---|---|---|
| **K_D** | 1 | "### Domain Concepts" defines HTTP Requests, Promises, Interceptors, Request Configurations, Response Objects, Cancellation, Adapter — with explanations. |
| **K_E** | 1 | Install commands; request-config option list with types incl. `cancelToken`; Promise resolve/reject semantics. |
| **K_U** | 1 | Six runnable examples (GET, POST, headers+params, async/await, interceptors, cancellation). |

**K(data2) = 100**

## README 3 — `data3.md`
| Element | Verdict | Evidence |
|---|---|---|
| **K_D** | 1 | Bulleted domain concepts (HTTP Requests/Responses, Interceptors, Cancellation, Request Configuration, Promise API, Adapters) each with a definition. |
| **K_E** | 1 | Install commands; config options with types; Response Object schema (data/status/statusText/headers/config/request); Promise return. |
| **K_U** | 1 | Six runnable examples incl. `axios({...})` config form, async/await, cancellation, interceptors. |

**K(data3) = 100**

---

## Summary
| readme | K_D | K_E | K_U | atrak_score |
|---|---|---|---|---|
| data1.md | 1 | 1 | 1 | 100 |
| data2.md | 1 | 1 | 1 | 100 |
| data3.md | 1 | 1 | 1 | 100 |
| **average** | 1 | 1 | 1 | **100** |

Average-row check: each column mean = 1; atrak mean = (100+100+100)/3 = 100. Consistent.
