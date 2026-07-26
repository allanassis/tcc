# Axios — README-AI ATRAK Evaluation (presence, not correctness)

Presence of the three Knowledge Elements [Thayer et al. 2021]. Incorrect/hallucinated content
still counts as present; absent (0) only for empty/missing sections, bare name-only lists, or
sections consisting solely of unresolved placeholders.

## Ground Truth Reference
- **Project:** axios
- **Repository:** https://github.com/axios/axios (default branch `v1.x`)
- **Domain:** Promise-based HTTP client for the browser and Node.js
- **Core domain entities:** HTTP requests/responses, Promises, interceptors, adapters
  (XHR/http/fetch), cancellation, request config, response schema.
- **Core execution facts:** install (`npm install axios`); build from source (`npm install`,
  `npm start`, `npm test`); returns Promises; config options; no `engines` constraint.
- **Core usage patterns:** GET/POST/async-await requests, instances, interceptors, cancellation.

File: `compare-readme-ai/axios_readme_readmeai.md` (single README).

---

## Evidence & verdicts
| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | 1 | The Features table defines conceptual/architectural entities with explanations — "Promise-based HTTP client", "Interceptor pattern for request/response manipulation", "Modular adapter system (XHR, HTTP)", "Config-driven request customization". The Project-Index file summaries further explain cancellation, adapters, interceptors, headers. These are definitions, not a bare name-only list. |
| **K_E Execution Facts** | 1 | Prerequisites (JavaScript, Npm); installation steps (`git clone`, `cd`, `npm install`); run/test commands (`npm start`, `npm test`); project structure and build/CI tooling (Rollup, Vitest). Runtime/build facts present. |
| **K_U Usage Patterns** | 1 | A Usage section (`npm start`) and Testing section (`npm test`) give how-to-run commands; Contributing gives a git workflow; Project-Index entries narrate how example files apply axios (GET/POST/upload/abort). Evaluable usage content present. |

**K = (1+1+1)/3 × 100 = 100**

---

## Summary
| readme | K_D | K_E | K_U | atrak_score |
|---|---|---|---|---|
| axios_readme_readmeai.md | 1 | 1 | 1 | 100 |
| **average** | 1 | 1 | 1 | **100** |

Single README ⇒ average row equals the row. Consistent.
