# Axios — ATORAK Adherence Evaluation

**Methodology:** Section 4.4.3 of *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis* (Andrade & Ribeiro, UERJ).

**Theory of Robust API Knowledge (ATORAK)** [Thayer et al. 2021] defines three Knowledge Elements that a robust API document must communicate:

- **KD — Domain Concepts:** Conceptual vocabulary, entities, and relationships that define the problem domain the API operates in.
- **KE — Execution Facts:** Concrete, verifiable facts about how the API behaves at runtime — commands, parameters, return values, environment requirements, installation steps.
- **KU — Usage Patterns:** Recurring, purposeful combinations of API calls that solve real problems, including the *what*, *how*, and *why* of usage.

Each element is binary: Ki ∈ {0, 1}. The adherence score per README is:

```
Kpercentage = (KD + KE + KU) / 3 × 100
```

The final score across the three generated READMEs is:

```
Kavg = (K1 + K2 + K3) / 3
```

---

## Ground Truth Reference

- Tool: **axios** — promise-based HTTP client for JavaScript (npm package)
- Repository: https://github.com/axios/axios
- Domain: HTTP communication, REST API consumption, asynchronous JavaScript
- Core domain entities: HTTP Request, HTTP Response, Promise, Interceptor, CancelToken, Adapter, Configuration, Instance
- Core execution facts: `axios(config)`, `axios.get()`, `axios.post()`, `axios.put()`, `axios.delete()`, `axios.patch()`, `axios.create()`, `axios.interceptors.request.use()`, `axios.interceptors.response.use()`, `axios.CancelToken`, `axios.isCancel()`, response object fields (`data`, `status`, `statusText`, `headers`, `config`, `request`)
- License: MIT

---

## data1.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

The README must correctly represent the conceptual vocabulary and entities of the axios domain.

**Evidence in data1.md:**

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **HTTP Requests** — "Communication initiated by the client to a server, specifying methods like GET, POST, PUT, DELETE, etc." ✅ Correct definition; accurately identifies the core communication mechanism.
- **Promises** — "Asynchronous operations that represent eventual completion or failure of an asynchronous task." ✅ Correct; matches the JavaScript Promise specification and how axios uses it.
- **Interceptors** — "Functions that Axios provides to process requests or responses before they are handled by `.then` or `.catch`." ✅ Correct; accurately describes the middleware-like interception mechanism.
- **Cancellation Tokens** — "Mechanism allowing to cancel HTTP requests." ✅ Correct; the CancelToken pattern is a real axios concept.
- **Adapters** — "Platform-specific implementations for sending HTTP requests (XHR for browsers, HTTP module for Node.js)." ✅ Correct; accurately describes the adapter abstraction that enables axios to work in both environments.
- **Configuration Options** — "Settings that customize request behavior such as headers, timeouts, base URLs, and more." ✅ Correct; the config object is central to axios usage.

The overview also correctly describes axios as a "promise-based HTTP client for JavaScript that works both in the browser and in Node.js environments" — this matches the official npm description verbatim.

**Assessment:** data1.md correctly and completely represents the domain concepts of axios. All six listed entities are accurately defined using terminology consistent with the official axios documentation. The domain is correctly identified as HTTP communication / REST API consumption. The conceptual vocabulary (Interceptors, CancelToken, Adapters, Promise API) matches the axios source terminology.

**KD = 1** ✅

---

#### KE — Execution Facts

The README must correctly represent concrete, verifiable runtime facts: commands, parameters, environment requirements, installation steps, and behavioral descriptions.

**Evidence in data1.md:**

*Installation facts:*
- `npm install axios` — correct and executable. ✅
- `yarn add axios` — correct and executable. ✅
- "Axios works in all modern browsers and Node.js." — accurate environment requirement. ✅

*API Reference facts (8 elements with parameters):*
- `axios(config)` — documents `url`, `method`, `baseURL`, `headers`, `params`, `data`, `timeout`, `responseType` — all are real config keys. ✅
- `axios.get(url[, config])` — correct signature, returns Promise. ✅
- `axios.post(url[, data[, config]])` — correct signature, returns Promise. ✅
- `axios.create([config])` — correct signature, returns new Axios instance. ✅
- `axios.interceptors.request.use(onFulfilled[, onRejected])` — correct signature, returns interceptor ID. ✅
- `axios.interceptors.response.use(onFulfilled[, onRejected])` — correct signature, returns interceptor ID. ✅
- `axios.CancelToken` — correctly described as a class for creating cancellation tokens. ✅
- `axios.isCancel(value)` — correct signature, returns Boolean. ✅

*Behavioral descriptions:*
- "Returns a Promise that resolves to a response object" — correct for all request methods. ✅
- "Interceptor ID" as return value for `interceptors.use()` — correct (numeric ID used for ejection). ✅
- Default configuration via `axios.defaults.baseURL`, `axios.defaults.headers.common`, `axios.defaults.timeout` — all real properties. ✅

**Assessment:** All documented execution facts are correct and verifiable. Installation commands are executable. All 8 API elements exist in axios with correct parameter names, types, and behavioral descriptions. The config object keys are accurate. No hallucinated commands or incorrect parameter types.

**KE = 1** ✅

---

#### KU — Usage Patterns

The README must present recurring, purposeful combinations of API calls that solve real problems, communicating *what* the pattern does, *how* to execute it, and *why* it is useful.

**Evidence in data1.md:**

The "Usage and Examples" section presents the following patterns:

1. **Basic GET Request** — `axios.get(url).then(r => console.log(r.data)).catch(...)`: Shows the fundamental request-response pattern. *What*: fetch data from an endpoint. *How*: `axios.get` with promise chaining. *Why*: simplest way to retrieve data. ✅
2. **POST Request with JSON Data** — `axios.post(url, {name, email}).then(...).catch(...)`: Shows how to send data to a server. *What*: create a resource. *How*: `axios.post` with a data object. *Why*: standard REST resource creation pattern. ✅
3. **Using Async/Await** — `async function fetchData() { const response = await axios.get(url); }`: Shows the modern async/await pattern. *What*: fetch data using async syntax. *How*: `await axios.get` inside try/catch. *Why*: cleaner alternative to promise chaining. ✅
4. **Setting Default Configuration** — `axios.defaults.baseURL`, `axios.defaults.headers.common`, `axios.defaults.timeout`: Shows how to configure axios globally. *What*: set defaults for all requests. *How*: assign to `axios.defaults`. *Why*: avoids repeating configuration in every request. ✅
5. **Creating an Axios Instance** — `axios.create({baseURL, timeout, headers})` then `apiClient.get('/posts')`: Shows the instance factory pattern. *What*: create a pre-configured client. *How*: `axios.create` with config, then use instance methods. *Why*: enables multiple clients with different base configurations. ✅
6. **Interceptors for Logging** — `axios.interceptors.request.use(fn, fn)` + `axios.interceptors.response.use(fn, fn)`: Shows the interceptor pattern. *What*: intercept and transform requests/responses. *How*: register handlers via `interceptors.use`. *Why*: centralized logging, auth token injection, error handling. ✅
7. **Canceling a Request** — `CancelToken.source()` → `axios.get(url, {cancelToken})` → `source.cancel()` → `axios.isCancel()`: Shows the full cancellation lifecycle. *What*: abort an in-flight request. *How*: create token, attach to request, call cancel. *Why*: prevents stale responses in UI components. ✅

**Assessment:** data1.md presents seven distinct usage patterns covering the most important axios workflows. Each pattern is a meaningful combination of API calls that solves a real problem. The *what* and *how* are clearly communicated through code and prose. The *why* is implied by section headings and contextual descriptions. The patterns progress from simple to advanced, covering the full spectrum of axios usage. This fully satisfies the KU criterion.

**KU = 1** ✅

---

### data1.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data1.md ATORAK Score: 100**

---

## data2.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

**Evidence in data2.md:**

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **HTTP Requests** — "Axios models HTTP requests such as GET, POST, PUT, DELETE, PATCH, etc., to interact with web services." ✅ Correct; enumerates the HTTP methods axios supports.
- **Promises** — "Axios uses JavaScript Promises for asynchronous control flow, returning a promise that resolves with the HTTP response or rejects with an error." ✅ Correct; accurately describes the Promise-based return contract.
- **Interceptors** — "Functions that allow transformation or logging of requests/responses before they are handled." ✅ Correct; captures the transformation and logging use cases.
- **Request Configurations** — "Structured options describing how HTTP requests should be made, including headers, query params, timeouts, and more." ✅ Correct; the config object is the central abstraction in axios.
- **Response Objects** — "Structured data containing status, headers, and payload returned from an HTTP call." ✅ Correct; accurately describes the response object structure.
- **Cancellation** — "Ability to abort requests mid-flight using Cancel tokens." ✅ Correct; "mid-flight" is an accurate description of the cancellation mechanism.
- **Adapter** — "Internal abstraction enabling Axios to work in different environments (browser or Node.js) with interchangeable HTTP implementations." ✅ Correct; accurately describes the adapter pattern and its purpose.

The overview also correctly describes axios as "a popular promise-based HTTP client for JavaScript, designed to work both in the browser and in Node.js environments" and mentions "automatic JSON data transformation, cancellation, and timeout handling" — all real features.

**Assessment:** data2.md provides a comprehensive and accurate domain concept representation. All seven listed entities are correctly defined. Notably, it adds "Response Objects" as an explicit concept (not present in data1.md), which is a key domain entity in axios. The "Adapter" definition is the most precise of the three READMEs, correctly identifying it as an "internal abstraction" with "interchangeable HTTP implementations."

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data2.md:**

*Installation facts:*
- `npm install axios` — correct. ✅
- `yarn add axios` — correct. ✅
- "compatible with both browser and Node.js environments, with no additional setup required" — accurate. ✅

*API Reference facts (11 elements):*
- `axios(config)` — documents `url`, `method`, `baseURL`, `headers`, `params`, `data`, `timeout`, `responseType`, `cancelToken` — all real config keys; adds `cancelToken` not present in data1.md. ✅
- `axios.get(url[, config])` — correct signature. ✅
- `axios.post(url[, data[, config]])` — correct signature. ✅
- `axios.put(url[, data[, config]])` — correct; `typeof axios.put === 'function'` is verifiable. ✅
- `axios.delete(url[, config])` — correct; `typeof axios.delete === 'function'` is verifiable. ✅
- `axios.patch(url[, data[, config]])` — correct; `typeof axios.patch === 'function'` is verifiable. ✅
- `axios.create([config])` — correct signature, returns new Axios instance with custom config. ✅
- `axios.interceptors.request.use(onFulfilled, onRejected)` — correct; "Returns interceptor ID" is accurate. ✅
- `axios.interceptors.response.use(onFulfilled, onRejected)` — correct. ✅
- `axios.CancelToken` — correct; described as "Constructor for creating cancel tokens to abort requests." ✅
- `axios.isCancel(value)` — correct; "Checks if an error was caused by cancellation." ✅

**Assessment:** data2.md has the most comprehensive API Reference of the three READMEs, documenting 11 elements including `axios.put`, `axios.delete`, and `axios.patch` — all real methods. The `cancelToken` config key is also documented in the config object. All execution facts are correct and verifiable.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data2.md:**

The "Usage and Examples" section presents the following patterns:

1. **Basic GET Request** — `axios.get(url).then(r => console.log(r.data)).catch(...)`: Core fetch pattern. *What*: retrieve data. *How*: `axios.get` with promise chaining. ✅
2. **POST Request with JSON Payload** — `axios.post(url, {firstName, lastName}).then(...).catch(...)`: Resource creation pattern. *What*: send data to server. *How*: `axios.post` with payload object. ✅
3. **Request with Custom Headers and Query Parameters** — `axios.get(url, {params: {category, sort}, headers: {Authorization}})`: Shows parameterized requests. *What*: filter and authenticate a request. *How*: pass `params` and `headers` in config. *Why*: common pattern for authenticated, filtered API calls. ✅
4. **Using Async/Await** — `async function fetchData() { await axios.get(url) }`: Modern async pattern. *What*: fetch data with async syntax. *How*: `await` inside try/catch. ✅
5. **Using Interceptors** — Request interceptor adding auth token + response interceptor logging status: Shows the dual-interceptor pattern. *What*: centralize auth and logging. *How*: `interceptors.request.use` and `interceptors.response.use`. *Why*: avoids repeating auth logic in every request. ✅
6. **Cancelling Requests** — Full `CancelToken.source()` → attach → `source.cancel()` → `axios.isCancel()` flow: Complete cancellation lifecycle. *What*: abort an in-flight request. *How*: create token, attach, cancel, check. ✅

**Assessment:** data2.md presents six distinct usage patterns. Notably, it adds the "Request with Custom Headers and Query Parameters" pattern (not in data1.md), which is a very common real-world axios usage. The interceptor example is more realistic than data1.md, showing auth token injection as the *why*. All patterns are purposeful and represent real developer workflows.

**KU = 1** ✅

---

### data2.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data2.md ATORAK Score: 100**

---

## data3.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

**Evidence in data3.md:**

The "Overview" section presents domain concepts inline (not as a dedicated subsection, but as a bulleted list):

- **HTTP Requests and Responses** — "Standard mechanisms of sending requests to and receiving responses from servers." ✅ Correct; pairs request and response as a unified concept.
- **Interceptors** — "Middleware-like hooks to transform requests or responses before they are handled by then or catch." ✅ Correct; the "middleware-like" analogy is accurate and helpful.
- **Cancellation** — "Ability to cancel requests using Cancel Tokens." ✅ Correct.
- **Request Configuration** — "Defining headers, parameters, timeouts, and other request-specific settings." ✅ Correct.
- **Promise API** — "Enabling asynchronous request handling with modern JavaScript Promises." ✅ Correct.
- **Adapters** — "Abstraction to support HTTP calls in different environments (e.g., XHR in browsers, http module in Node.js)." ✅ Correct; explicitly names XHR and the http module.

The overview also states: "Axios is widely used for its ease of use, robust feature set, and ability to work seamlessly both in client-side and server-side JavaScript environments." — Accurate characterization.

**Assessment:** data3.md correctly represents the domain concepts of axios. All six listed entities are accurately defined. The "middleware-like hooks" description for interceptors is the most intuitive of the three READMEs. The explicit naming of XHR and the http module in the Adapters definition adds precision. The domain is correctly identified as HTTP communication for both client-side and server-side JavaScript.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data3.md:**

*Installation facts:*
- `npm install axios` — correct. ✅
- `yarn add axios` — correct. ✅
- "supports all modern browsers and Node.js environments" — accurate. ✅

*API Reference facts — Axios Instance Methods (8 elements):*
- `axios(config)` — documents `url`, `method`, `baseURL`, `headers`, `params`, `data`, `timeout`, `responseType`, `cancelToken` — all real config keys. ✅
- `axios.get(url[, config])` — correct. ✅
- `axios.post(url[, data[, config]])` — correct. ✅
- `axios.put(url[, data[, config]])` — correct. ✅
- `axios.delete(url[, config])` — correct. ✅
- `axios.create([config])` — correct. ✅
- `axios.CancelToken` — correct. ✅
- `axios.isCancel(value)` — "Returns `true` if the provided value is a cancellation error." ✅ Correct behavioral description.

*Response Object fields (unique to data3.md):*
- `data` — "The response body provided by the server." ✅
- `status` — "HTTP status code of the response." ✅
- `statusText` — "HTTP status message." ✅
- `headers` — "Headers from the response." ✅
- `config` — "The original request configuration." ✅
- `request` — "The request object." ✅

All six response object fields are real properties of the axios response object, verifiable via `Object.keys(response)` after a live request.

*Interceptors:*
- `axios.interceptors.request.use(onFulfilled[, onRejected])` — correct. ✅
- `axios.interceptors.response.use(onFulfilled[, onRejected])` — correct. ✅

**Assessment:** data3.md is the only README to explicitly document the Response Object fields (`data`, `status`, `statusText`, `headers`, `config`, `request`) — all of which are real and verifiable. This is a significant execution fact that developers need to know. All other documented facts are also correct. The API Reference is comprehensive and accurate.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data3.md:**

The "Usage and Examples" section presents the following patterns:

1. **Basic GET Request** — `axios.get(url).then(r => console.log(r.data)).catch(...)`: Core fetch pattern. ✅
2. **POST Request with Data** — `axios.post(url, {firstName, lastName}).then(...).catch(...)`: Resource creation pattern. ✅
3. **Setting Request Headers and Configurations** — `axios({method, url, headers: {Authorization}, timeout, params: {id}})`: Shows the full config object form. *What*: make a fully configured request. *How*: pass a config object directly to `axios()`. *Why*: useful when all options need to be specified explicitly. ✅ This is the only README to demonstrate the `axios(config)` object form as a usage pattern.
4. **Using Async/Await Pattern** — `async function fetchData() { await axios.get(url) }`: Modern async pattern. ✅
5. **Request Cancellation** — Full `CancelToken.source()` → attach → `source.cancel()` → `axios.isCancel()` flow. ✅
6. **Using Interceptors** — Request interceptor (log before send) + response interceptor (log on receive): Shows the dual-interceptor pattern with comments explaining the 2xx status code behavior. ✅

**Assessment:** data3.md presents six distinct usage patterns. Uniquely, it demonstrates the `axios(config)` object form as a standalone pattern (pattern 3), which is a real and important usage pattern not highlighted in the other READMEs. The interceptor example includes comments about the 2xx status code trigger condition, adding precision. All patterns are purposeful and represent real developer workflows.

**KU = 1** ✅

---

### data3.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data3.md ATORAK Score: 100**

---

## Summary: All Three axios READMEs — ATORAK Adherence

| README | KD (Domain Concepts) | KE (Execution Facts) | KU (Usage Patterns) | Kpercentage |
|--------|---------------------|---------------------|---------------------|-------------|
| data1.md | 1 | 1 | 1 | **100** |
| data2.md | 1 | 1 | 1 | **100** |
| data3.md | 1 | 1 | 1 | **100** |

### Final Average Score (Equation 16 from TCC §4.4.3)

```
Kavg = (100 + 100 + 100) / 3 = 100
```

**axios ATORAK Average Score: 100**

---

## Analysis and Observations

**Why all three score 100 on ATORAK adherence:**

Axios is one of the most widely used JavaScript libraries, with extensive public documentation, tutorials, and examples in LLM training data. The model correctly identified all three knowledge elements in every generated README.

**KD (Domain Concepts) — all three score 1:**
All three READMEs include an explicit domain concepts section in the Overview, listing and correctly defining the core axios entities. data1.md defines 6 concepts (HTTP Requests, Promises, Interceptors, Cancellation Tokens, Adapters, Configuration Options). data2.md defines 7 concepts, adding Response Objects as an explicit entity. data3.md defines 6 concepts with the most precise Adapters definition (explicitly naming XHR and the http module).

**KE (Execution Facts) — all three score 1:**
All three READMEs provide correct, executable installation commands, correct API Reference sections with accurate parameter names and behavioral descriptions, and correct environment requirements. data2.md is the most complete, documenting 11 API elements including `axios.put`, `axios.delete`, and `axios.patch`. data3.md uniquely documents the Response Object fields (`data`, `status`, `statusText`, `headers`, `config`, `request`).

**KU (Usage Patterns) — all three score 1:**
All three READMEs present multiple named usage patterns covering the core axios workflows (GET, POST, async/await, interceptors, cancellation). data1.md adds the `axios.defaults` configuration pattern and the `axios.create` instance factory pattern. data2.md adds the custom headers + query parameters pattern. data3.md uniquely demonstrates the `axios(config)` object form as a standalone pattern.

**Qualitative differences (not affecting binary ATORAK score):**
- data1.md: Most structured, 7 usage patterns, 8 API elements, includes `axios.defaults` and `axios.create` patterns.
- data2.md: Most complete API coverage, 11 API elements, 6 usage patterns, adds `axios.put/delete/patch`.
- data3.md: Uniquely documents Response Object fields and the `axios(config)` object form; 6 usage patterns, 10 API elements.

**This result is consistent with the TCC's hypothesis** that high-popularity libraries with extensive public documentation are the easiest case for LLM-based README generation. Axios's ubiquity in LLM training data ensures that all three knowledge elements are naturally and correctly present in every generated README.
