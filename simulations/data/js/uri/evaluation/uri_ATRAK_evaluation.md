# lil-uri — ATORAK Adherence Evaluation

**Methodology:** Section 4.4.3 of *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis* (Andrade, UERJ).

**Theory of Robust API Knowledge (ATORAK)** [Thayer et al. 2021] defines three Knowledge Elements that a robust API document must communicate:

- **KD — Domain Concepts:** Conceptual vocabulary, entities, and relationships that define the problem domain the API operates in.
- **KE — Execution Facts:** Concrete facts about how the API behaves — commands, parameters, return values, environment requirements, installation steps.
- **KU — Usage Patterns:** Recurring, purposeful combinations of API calls that solve real problems, including the *what*, *how*, and *why* of usage.

Each element is binary: Ki ∈ {0, 1} — **1 if the knowledge element is present and communicated, 0 if absent**. This evaluation does not assess factual correctness (that is §4.4.2). It assesses whether each type of knowledge is communicated at all.

The adherence score per README is:

```
Kpercentage = (KD + KE + KU) / 3 × 100
```

The final score across the three generated READMEs is:

```
Kavg = (K1 + K2 + K3) / 3
```

---

## Ground Truth Reference

- Tool: **lil-uri** — minimalistic JavaScript URI parser and builder
- Repository: https://github.com/lil-js/uri
- Domain: URI parsing, manipulation, and serialization (RFC 3986)

---

## data1.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

The README must communicate conceptual vocabulary, entities, and relationships of the problem domain.

**Evidence in data1.md:**

The Overview section contains an explicit "Domain Concepts" subsection that lists and defines:

- **URI Structure** — scheme, authority (user info, host, port), path, query, fragment.
- **Parsing** — breaking down raw URI strings into structured components.
- **Serialization** — composing URI components back into valid URI strings.
- **Query Parameter Manipulation** — adding, updating, and removing query parameters.
- **Normalization** — adjusting URI parts according to standard rules.

The overview prose also introduces the RFC 3986 specification as the conceptual foundation and explains the relationship between URI components and web/network applications.

**Assessment:** The README explicitly communicates the domain vocabulary (scheme, authority, path, query, fragment), the core entities (URI, its components), and the relationships between them (a URI is composed of components; the library abstracts their complexity). The knowledge element KD is present and communicated.

**KD = 1** ✅

---

#### KE — Execution Facts

The README must communicate concrete facts about how the API behaves — installation commands, parameters, return values, environment requirements.

**Evidence in data1.md:**

*Installation:*
- `npm install @lil-js/uri` and `yarn add @lil-js/uri` — installation commands are provided.
- Environment requirement stated: "works in both Node.js and browser environments."

*API Reference section* documents:
- Constructor: `new URI(uriString: string)` with parameter type and description.
- Properties: `scheme`, `userinfo`, `host`, `port`, `path`, `query`, `fragment` — each with type (string) and description.
- Methods: `addQuery(key: string, value: string): void`, `setQuery(key: string, value: string): void`, `removeQuery(key: string): void`, `normalize(): void`, `toString(): string` — each with parameter names, types, return types, and behavioral descriptions.

**Assessment:** The README communicates concrete facts about how the API behaves: how to install it, what environment it runs in, what the constructor accepts, what properties exist and their types, what methods exist with their parameters and return values. The knowledge element KE is present and communicated.

**KE = 1** ✅

---

#### KU — Usage Patterns

The README must communicate recurring, purposeful combinations of API calls that solve real problems, with *what*, *how*, and *why*.

**Evidence in data1.md:**

The "Usage and Examples" section presents four named patterns:

1. **Basic Usage: Parsing a URI** — constructs a URI object and reads all components. *What*: parse a URI and access its parts. *How*: `new URI(url)` then read properties. *Why*: decompose a URI for programmatic use.
2. **Manipulating Query Parameters** — uses `addQuery`, `setQuery`, `removeQuery` in sequence. *What*: modify query parameters. *How*: call mutation methods. *Why*: update URIs without manual string manipulation.
3. **Serializing URI Back to String** — modifies path and fragment then calls `toString()`. *What*: reconstruct a URI after modification. *How*: assign properties, call `toString()`. *Why*: produce a valid URI string from modified components.
4. **Normalizing a URI** — calls `normalize()` then `toString()`. *What*: normalize a URI. *How*: call `normalize()`. *Why*: ensure URI conformance to standard rules.

Each pattern has a named heading, a code snippet, and inline comments showing expected output. The *what* and *how* are explicitly communicated; the *why* is implied by the section headings and context.

**Assessment:** The README communicates four distinct usage patterns, each representing a purposeful combination of API calls that solves a real problem. The knowledge element KU is present and communicated.

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

The Overview section contains an explicit "Domain Concepts" subsection listing:

- **URI Components** — scheme (protocol), host, port, path, query parameters, fragment.
- **Parsing** — transforming a URI string into an object representation.
- **Serialization** — converting the URI object back into a valid URI string.
- **Manipulation** — modifying individual parts of the URI.
- **Normalization** — handling encoding and decoding of URI components.

The overview prose explicitly references RFC 3986 as the conceptual foundation and describes the library's purpose as decomposing, modifying, and recomposing URIs.

**Assessment:** The README communicates the domain vocabulary (scheme, authority, path, query, fragment), the core entities (URI and its components), and the relationships between them. The knowledge element KD is present and communicated.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data2.md:**

*Installation:*
- `npm install lil-uri` and `yarn add lil-uri` — installation commands provided.
- Environment requirement: "Node.js or browser environments supporting ES modules."

*API Reference section* documents:
- `uri(input?: string | URI): URI` — factory function with optional parameter type, return type, and behavioral description (parses, clones, or returns empty URI).
- URI Object Properties: `scheme`, `userinfo`, `host`, `port`, `path`, `search`, `hash` — each with type and description.
- `toString(): string` — with behavioral description.
- `query` Map-like interface — `get`, `set`, `delete`, `has`, `keys`, `values`, `entries` — each with parameter types and return types.

**Assessment:** The README communicates concrete facts about installation, environment, the factory function signature, all component property types, the serialization method, and the query interface with its full method signatures. The knowledge element KE is present and communicated.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data2.md:**

The "Usage and Examples" section presents three named patterns:

1. **Basic Parsing and Serialization** — `uri(url)` to parse, modify components, then `toString()`. *What*: parse a URI, modify it, serialize back. *How*: factory function, property assignment, `toString()`. *Why*: fundamental URI manipulation workflow.
2. **Accessing Query Parameters** — `u.query.get()`, `u.query.set()`, then `u.toString()`. *What*: read and write query parameters. *How*: Map-like query interface. *Why*: common need in web development.
3. **Creating a URI from Components** — `uri()` with no args, assign properties, `u.query.set()`, `u.toString()`. *What*: build a URI from scratch. *How*: empty factory, assign parts, serialize. *Why*: construct URIs programmatically without string concatenation.

Each pattern has a named heading, a code snippet, and inline comments showing expected output.

**Assessment:** The README communicates three distinct usage patterns covering the core URI manipulation workflows. The knowledge element KU is present and communicated.

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

The Overview section contains an explicit "Domain Concepts" subsection listing:

- **URI Components** — scheme, authority, path, query, fragment per RFC 3986.
- **Parsing** — extracting individual components from URI strings.
- **Formatting** — reconstructing URI strings from component parts.
- **Relative URI Resolution** — combining base URIs with relative references.
- **Query Handling** — parsing and serializing query parameters as key-value pairs.
- **Encoding & Decoding** — properly encoding reserved characters to maintain URI validity.

The overview prose explicitly references RFC 3986 and describes the library as abstracting URI syntax complexity.

**Assessment:** The README communicates the domain vocabulary (scheme, authority, path, query, fragment), the core entities (URI and its components), and the relationships between them. The knowledge element KD is present and communicated.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data3.md:**

*Installation:*
- `npm install @lil-js/uri` — installation command provided.
- Environment requirement: "modern JavaScript environments including Node.js and web browsers via bundlers."

*API Reference section* documents five functions with full signatures:
- `parse(uri: string): UriComponents` — parameter name, type, return type, and description of all returned fields (`scheme`, `userinfo`, `host`, `port`, `path`, `query`, `fragment`).
- `format(components: UriComponents): string` — parameter name, type, return type, and behavioral description.
- `resolve(base: string, relative: string): string` — two parameter names and types, return type, and behavioral description.
- `parseQuery(query: string): Record<string, string>` — parameter name, type, return type, and behavioral description.
- `formatQuery(params: Record<string, string>): string` — parameter name, type, return type, and behavioral description.

**Assessment:** The README communicates concrete facts about installation, environment, and five API functions with their parameter names, types, return types, and behavioral descriptions. The knowledge element KE is present and communicated.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data3.md:**

The "Usage and Examples" section presents four named patterns:

1. **Parsing a URI** — `parse(url)` returning a components object. *What*: decompose a URI string into parts. *How*: call `parse()`, read fields from result. *Why*: access individual URI components programmatically.
2. **Formatting a URI** — `format(components)` from a plain object. *What*: build a URI string from parts. *How*: pass a components object to `format()`. *Why*: construct URIs without string concatenation.
3. **Resolving a Relative URI** — `resolve(base, relative)`. *What*: resolve a relative URI against a base. *How*: call `resolve()` with two strings. *Why*: handle relative links in web applications.
4. **Working with Query Parameters** — `parseQuery(queryString)` and `formatQuery(params)`. *What*: parse and serialize query strings. *How*: call `parseQuery` and `formatQuery`. *Why*: manipulate query parameters as structured objects.

Each pattern has a named heading, a code snippet, and inline comments showing expected output.

**Assessment:** The README communicates four distinct usage patterns, each representing a purposeful combination of API calls that solves a real problem. The knowledge element KU is present and communicated.

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

## Summary: All Three lil-uri READMEs — ATORAK Adherence

| README | KD (Domain Concepts) | KE (Execution Facts) | KU (Usage Patterns) | Kpercentage |
|--------|---------------------|---------------------|---------------------|-------------|
| data1.md | 1 | 1 | 1 | **100** |
| data2.md | 1 | 1 | 1 | **100** |
| data3.md | 1 | 1 | 1 | **100** |

### Final Average Score (Equation 16 from TCC §4.4.3)

```
Kavg = (100 + 100 + 100) / 3 = 100
```

**lil-uri ATORAK Average Score: 100**

---

## Analysis and Observations

**Why all three score 100 on ATORAK adherence:**

The ATORAK evaluation measures whether each type of knowledge is communicated — not whether the content is factually correct. All three READMEs consistently communicate all three knowledge elements across every generation.

**KD (Domain Concepts) — all three score 1:**
Every README includes an explicit "Domain Concepts" subsection in the Overview that names and defines the core URI entities (scheme, authority, path, query, fragment) and the primary operations (parsing, serialization, manipulation). The domain is correctly identified as URI handling per RFC 3986. The conceptual vocabulary is present and communicated in all three cases.

**KE (Execution Facts) — all three score 1:**
Every README provides an Installation section with commands and environment requirements, and an API Reference section with function/method signatures, parameter names, types, return types, and behavioral descriptions. The form of execution knowledge is present in all three — commands to run, parameters to pass, values to expect. Whether those facts are accurate is a §4.4.2 concern, not a §4.4.3 concern.

**KU (Usage Patterns) — all three score 1:**
Every README provides a "Usage and Examples" section with multiple named patterns, each containing a code snippet and inline comments showing expected output. Each pattern communicates *what* it does (via the heading), *how* to do it (via the code), and *why* it is useful (via context and comments). The form of usage knowledge is present in all three.

**Important distinction from §4.4.2 (Correctness):**
The correctness evaluation (§4.4.2) reveals that lil-uri scores poorly — 55.56 average — because the LLM hallucinated the API (wrong package names, non-existent methods, wrong property names). However, that finding is orthogonal to ATORAK adherence. The ATORAK framework asks: *does the README attempt to communicate domain concepts, execution facts, and usage patterns?* The answer is yes in all three cases. A README can fully adhere to the ATORAK structure while containing incorrect information — these are independent dimensions of documentation quality.
