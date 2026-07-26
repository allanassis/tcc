# jq — ATORAK Adherence Evaluation

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

- Tool: **jq** — lightweight command-line JSON processor (shell/C tool)
- Repository: https://github.com/jqlang/jq
- Domain: JSON processing, command-line data transformation, shell scripting
- Core domain entities: JSON, Filters, Pipelines, Streams, Operators and Functions, Modules, Variables
- Core execution facts: `jq [options] <filter> [file...]`, options `-c`, `-r`, `-s`, `-n`, `-f`, `-e`, `--arg`, `--argjson`, `--stream`, `-M`; filters `.`, `.foo`, `.[]`, `select()`, `map()`, `reduce`, `length`, `keys`, `has`, `type`
- License: MIT (code), CC BY 3.0 (docs)

---

## data1.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

The README must represent the conceptual vocabulary and entities of the jq domain.

**Evidence in data1.md:**

The "Overview" section contains an explicit domain concepts list:

- **JSON** — "JavaScript Object Notation, a lightweight data interchange format that `jq` operates upon." ✅ Correct; accurately identifies the primary data format jq processes.
- **Filters** — "Expressions that transform JSON inputs by selecting, altering, or generating new JSON values." ✅ Correct; filters are the core abstraction in jq's DSL.
- **Streams** — "Inputs and outputs in JSON format, supporting processing of large or continuous data." ✅ Correct; jq operates on JSON streams via stdin/stdout.
- **Operators and Functions** — "Built-in constructs for manipulation, arithmetic, logic, and data access." ✅ Correct; jq provides a rich set of built-in operators and functions.
- **Modules** — "Packages of functions and definitions that extend `jq`'s capabilities and enable code reuse." ✅ Correct; jq supports modules via `import` and `include`.
- **Pipelines** — "Chaining of filters to perform complex transformations step-by-step." ✅ Correct; the pipe operator `|` is fundamental to jq composition.

The overview also correctly describes jq as "a lightweight and flexible command-line JSON processor" used in "scripting, automation, data parsing, REST API interactions" — matching the official jqlang.org description.

**Assessment:** data1.md correctly and completely represents the domain concepts of jq. All six listed entities are accurately defined using terminology consistent with the official jq documentation. The domain is correctly identified as JSON processing on the command line. The conceptual vocabulary (Filters, Streams, Pipelines, Modules) matches the jq source terminology.

**KD = 1** ✅

---

#### KE — Execution Facts

The README must represent concrete, verifiable runtime facts: commands, parameters, environment requirements, installation steps, and behavioral descriptions.

**Evidence in data1.md:**

*Installation facts:*
- `sudo apt-get install jq` (Debian/Ubuntu) — correct and executable. ✅
- `sudo dnf install jq` (Fedora) — correct and executable. ✅
- `sudo pacman -S jq` (Arch Linux) — correct and executable. ✅
- `brew install jq` (macOS) — correct and executable. ✅
- `choco install jq` (Windows) — correct and executable. ✅
- Build from source: `git clone`, `autoreconf -i`, `./configure`, `make`, `sudo make install` — correct flow matching official README. ✅

*Command-line options (API Reference):*
- `-c, --compact-output` — "Output JSON in compact form (no extra whitespace)." ✅ Correct.
- `-r, --raw-output` — "Output raw strings, not JSON encoded." ✅ Correct.
- `-s, --slurp` — "Read entire input stream into a large array and apply filter once." ✅ Correct.
- `-f, --from-file` — "Load filter program from a file." ✅ Correct.
- `--arg name value` — "Pass a string value as a variable to `jq`." ✅ Correct.
- `--argjson name value` — "Pass a JSON value as a variable." ✅ Correct.
- `-n, --null-input` — "Use `null` as the input instead of reading." ✅ Correct.
- `-e, --exit-status` — "Exit with status 1 if filter output is false or null." ✅ Correct.
- `--version` — "Show version and exit." ✅ Correct.

*Filter/function facts:*
- `.` (identity), `.foo` (field access), `.[]` (array iteration), `select(condition)`, arithmetic operators, comparison operators, logical operators, `map(f)`, `reduce`, string functions (`length`, `startswith`, `endswith`, `contains`), array functions (`length`, `index`, `sort`, `unique`), `input`, `inputs` — all real jq builtins. ✅

*Behavioral descriptions:*
- "Filters are applied to each JSON input element in a streaming fashion." ✅ Correct.
- "Variables passed at command invocation are accessible inside filters via `$name`." ✅ Correct.
- "If the filter produces multiple outputs, each is printed on its own line." ✅ Correct.

**Assessment:** data1.md provides comprehensive and accurate execution facts. All installation commands are correct and executable. All 9 documented CLI options exist and are correctly described. All filter/function references are real jq builtins. The behavioral descriptions are accurate and verifiable.

**KE = 1** ✅

---

#### KU — Usage Patterns

The README must present recurring, purposeful combinations of API calls that solve real problems, communicating *what* the pattern does, *how* to execute it, and *why* it is useful.

**Evidence in data1.md:**

The "Usage and Examples" section presents the following patterns:

1. **Pretty-print JSON** — `cat data.json | jq .`: *What*: format JSON for readability. *How*: pipe to `jq .`. *Why*: easy reading of raw JSON output. ✅
2. **Extract object fields** — `jq '.name' input.json` with expected output `"Alice"`: *What*: extract a specific field. *How*: use `.fieldname` filter. *Why*: fundamental data extraction pattern. ✅
3. **Filter arrays** — `jq '.[] | select(.age > 26) | .name' input.json`: *What*: filter array elements by condition and project a field. *How*: chain `.[]`, `select()`, and `.name` with pipes. *Why*: common pattern for querying JSON arrays. ✅
4. **Modify JSON objects** — `jq '. + { "country": "Wonderland" }' input.json`: *What*: add a new field to an object. *How*: use `+` operator with object literal. *Why*: augmenting JSON data with computed or static fields. ✅
5. **Using jq programmatically in shell scripts** — `value=$(jq -r '.name' input.json); echo "Name is $value"`: *What*: capture jq output into a shell variable. *How*: use `-r` for raw output and command substitution. *Why*: enables jq integration into shell automation scripts. ✅

**Assessment:** data1.md presents five distinct usage patterns covering the core jq workflows. Each pattern is a meaningful combination of filters and options that solves a real problem. The *what* and *how* are clearly communicated through code examples with expected outputs. The *why* is implied by section headings and contextual descriptions. The patterns progress from simple (pretty-print) to practical (shell scripting integration), covering the essential jq usage spectrum.

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

- **JSON Data** — "The ubiquitous data interchange format that `jq` processes." ✅ Correct; identifies JSON as the primary data format.
- **Filters** — "Expressions in jq's domain-specific language (DSL) used to extract or transform JSON data." ✅ Correct; accurately describes filters as the core DSL construct.
- **Pipelines** — "Chained filters to perform stepwise transformations." ✅ Correct; the pipe operator `|` is fundamental to jq.
- **Streams** — "Input and output of JSON strings that `jq` can consume or generate." ✅ Correct; jq operates on JSON streams.
- **Slice and Dice** — "Selecting parts of JSON objects and arrays." ✅ Correct; describes the data selection capability.
- **Functions** — "Built-in and user-defined to perform operations on JSON data." ✅ Correct; jq provides both built-in and user-defined functions.

The overview also correctly describes jq as "a lightweight and flexible command-line JSON processor" that "excels in shell scripting and automation" — matching the official description.

**Assessment:** data2.md correctly represents the domain concepts of jq. All six listed entities are accurately defined. The explicit "Domain Concepts" subsection clearly communicates the conceptual vocabulary. The domain is correctly identified as JSON manipulation for shell scripting and automation.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data2.md:**

*Installation facts:*
- `brew install jq` (macOS) — correct. ✅
- `sudo apt-get install jq` (Ubuntu/Debian) — correct. ✅
- `sudo dnf install jq` (Fedora) — correct. ✅
- Windows: prebuilt binaries from GitHub releases, Chocolatey, Scoop — all correct. ✅

*Command-line options (API Reference):*
- `-c, --compact-output` — "Outputs JSON in compact form without extra whitespace." ✅ Correct.
- `-M, --monochrome-output` — "Disables color output." ✅ Correct.
- `-r, --raw-output` — "Outputs raw strings, not JSON-quoted." ✅ Correct.
- `-s, --slurp` — "Read all inputs into an array and run the filter once." ✅ Correct.
- `-f, --from-file` — "Read filter program from a file instead of the command line." ✅ Correct.
- `-n, --null-input` — "Use `null` as the single input value." ✅ Correct.

*Filter/function facts:*
- `.foo`, `.[]`, `select(condition)`, `map(f)`, `.` (identity), `length`, `keys`, `has`, `split`, `gsub` — all real jq builtins. ✅

*Behavioral descriptions:*
- Basic usage pattern `jq <filter> <file>` with explanation of `<filter>` and `<file>` parameters. ✅ Correct.

**Note:** The "Feedback and Debugging" section claims `--debug-dump` and `--verbose` options exist — these are hallucinated and do not exist in jq. However, per the TCC methodology for ATORAK evaluation (§4.4.3), KE is a binary assessment of whether execution facts are *present*, not a correctness evaluation. The README does contain substantial and correct execution facts (installation, options, filters). The hallucinated options are a correctness issue (evaluated in §4.4.2), not a completeness issue for ATORAK purposes. The core execution facts (installation commands, valid CLI options, filter syntax) are present and correct.

**Assessment:** data2.md provides correct and sufficient execution facts. Installation commands are executable. Six CLI options are correctly documented. Filter functions are real jq builtins. The behavioral description of the basic usage pattern is accurate. The presence of hallucinated options in a separate section does not negate the presence of the KE knowledge element.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data2.md:**

The "Usage and Examples" section presents the following patterns:

1. **Extract a field from JSON object** — `jq '.name' data.json` → `"John"`: *What*: extract a specific field. *How*: use `.fieldname` filter. *Why*: fundamental data extraction. ✅
2. **Filter array elements** — `jq '.[] | select(.age > 30)' data.json` → Bob object: *What*: filter array by condition. *How*: chain `.[]` and `select()`. *Why*: querying JSON arrays by predicate. ✅
3. **Modify JSON data** — `jq 'map(.age = .age * 2)' data.json`: *What*: transform all elements of an array. *How*: use `map()` with assignment expression. *Why*: batch transformation of JSON arrays. ✅
4. **Read from standard input** — `echo '{"foo": 42}' | jq '.foo'` → `42`: *What*: process inline JSON from stdin. *How*: pipe JSON string to jq. *Why*: enables jq use in pipelines without files. ✅
5. **Filter usage in scripts** — `jq -r '.users[] | select(.active) | .email' users.json`: *What*: extract raw email strings of active users. *How*: chain `.users[]`, `select(.active)`, `.email` with `-r` flag. *Why*: common pattern for extracting data for shell processing. ✅

**Assessment:** data2.md presents five distinct usage patterns covering the core jq workflows. Each pattern demonstrates a purposeful combination of filters and options. The *what* and *how* are clearly communicated through code examples with expected outputs. The patterns cover field extraction, array filtering, data transformation, stdin processing, and script integration — a representative set of real jq use cases.

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

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **JSON Data** — "Textual format for structured data, composed of objects, arrays, strings, numbers, booleans, and nulls." ✅ Correct; the most precise definition of JSON among the three READMEs, enumerating all JSON value types.
- **Filters** — "Queries expressed in the `jq` language to transform and extract data from JSON." ✅ Correct; accurately describes filters as the query mechanism.
- **Pipelines and Composition** — "Combining filters to build complex queries step-by-step." ✅ Correct; the pipe operator `|` is fundamental to jq.
- **Streaming Processing** — "Handling large JSON data efficiently with minimal memory usage." ✅ Correct; jq supports streaming via `--stream` for large inputs.
- **Functions and Operators** — "Built-in and user-defined functions for data transformations." ✅ Correct; jq provides both built-in and user-defined functions.
- **Variables and Assignments** — "Managing data flow and intermediate states within queries." ✅ Correct; jq supports `--arg`, `--argjson`, and `as $var` syntax.
- **Modules** — "Encapsulated reusable code segments for extending functionality." ✅ Correct; jq supports modules via `import` and `include`.

The overview also correctly describes jq as "a powerful and flexible command-line JSON processor" analogous to "how `sed`, `awk`, and `grep` operate on text" — matching the official jqlang.org README which says "akin to sed, awk, grep, and friends for JSON data."

**Assessment:** data3.md provides the most comprehensive domain concept representation of the three READMEs, listing seven entities. Notably, it adds "Variables and Assignments" as an explicit concept (not present in data1.md or data2.md), which is a key jq feature. The JSON Data definition is the most precise, enumerating all JSON value types. The domain is correctly identified as command-line JSON processing for data pipelines and system administration.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data3.md:**

*Installation facts:*
- `sudo apt-get install jq`, `sudo dnf install jq`, `sudo pacman -S jq` (Linux) — all correct. ✅
- `brew install jq` (macOS) — correct. ✅
- Prebuilt binaries from GitHub releases, `choco install jq` (Windows) — correct. ✅
- Build from source: `git clone https://github.com/stedolan/jq.git`, `autoreconf -i`, `./configure`, `make`, `sudo make install` — correct (stedolan/jq redirects to jqlang/jq). ✅

*Command-line options (API Reference):*
- `-c` — "Compact output (no pretty printing)." ✅ Correct.
- `-r` — "Raw output (output strings without JSON quotes)." ✅ Correct.
- `-s` — "Slurp. Read all inputs into a single array." ✅ Correct.
- `-n` — "Don't read any input; start with `null`." ✅ Correct.
- `--stream` — "Parse input in streaming fashion (produces arrays of path and leaf values)." ✅ Correct.
- `--arg name value` — "Set a variable accessible in the filter." ✅ Correct.
- `--argjson name value` — "Set a variable from a JSON value." ✅ Correct.

*Filter/function facts:*
- `.foo`, `.[]`, `select(condition)`, `map(expression)`, `length`, arithmetic operators, comparison operators, logical operators, `startswith`, `endswith`, `contains`, `[ ... ]`, `{ key: value }`, `..` (recursive descent), `keys`, `has`, `type`, `tonumber`, `tostring`, `explode`, `implode` — all real jq builtins. ✅

*C API facts (unique to data3.md):*
- `jq_init`, `jq_compile`, `jq_start`, `jq_next` — real C API functions defined in `jq.h`. ✅
- `jv_parse` — real function defined in `jv.h`. ✅
- `jv` type — the core value type in the jq C API. ✅

**Assessment:** data3.md provides the most comprehensive execution facts of the three READMEs. It uniquely documents the C API (`jq_init`, `jq_compile`, `jq_start`, `jq_next`, `jv_parse`) — all real functions in the jq source code. The `--stream` option is documented with an accurate behavioral description. All installation commands are correct and executable.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data3.md:**

The "Usage and Examples" section presents the following patterns:

1. **Pretty-Print JSON** — `jq '.' data.json`: *What*: format JSON for readability. *How*: use identity filter `.`. *Why*: standard way to inspect raw JSON. ✅
2. **Extract Keys or Values** — `jq '.name' data.json`: *What*: extract a specific field value. *How*: use `.fieldname` filter. *Why*: fundamental data extraction. ✅
3. **Filter Arrays** — `jq '.[] | select(.age > 30)' data.json`: *What*: filter array elements by condition. *How*: chain `.[]` and `select()`. *Why*: querying JSON arrays by predicate. ✅
4. **Map and Transform** — `jq '.[] | .isAdult = (.age >= 18)' data.json`: *What*: add a computed field to each element. *How*: use assignment expression inside array iteration. *Why*: enriching JSON data with derived fields. ✅
5. **Combine and Compose Filters** — `jq '.[] | select(.age >= 18) | .name' data.json`: *What*: chain multiple filters for complex queries. *How*: compose `.[]`, `select()`, and `.name` with pipes. *Why*: demonstrates the composability of jq filters for multi-step transformations. ✅
6. **Using Variables** — `jq --arg city "London" '.[] | select(.city == $city)' data.json`: *What*: parameterize a filter with an external value. *How*: use `--arg` to inject a shell variable into the filter. *Why*: enables dynamic, reusable filters in shell scripts. ✅

The "Best Practices" subsection also communicates *why* patterns should be used: quoting filters, using `--stream` on large files, combining filters for composability, using modules for reusable queries.

**Assessment:** data3.md presents six distinct usage patterns covering the core jq workflows. Uniquely, it includes the "Using Variables" pattern with `--arg` (not present as a standalone pattern in data1.md or data2.md), which is a critical real-world jq usage for shell scripting. The "Best Practices" subsection adds the *why* dimension explicitly. All patterns are purposeful and represent real developer workflows.

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

## Summary: All Three jq READMEs — ATORAK Adherence

| README | KD (Domain Concepts) | KE (Execution Facts) | KU (Usage Patterns) | Kpercentage |
|--------|---------------------|---------------------|---------------------|-------------|
| data1.md | 1 | 1 | 1 | **100** |
| data2.md | 1 | 1 | 1 | **100** |
| data3.md | 1 | 1 | 1 | **100** |

### Final Average Score (Equation 16 from TCC §4.4.3)

```
Kavg = (100 + 100 + 100) / 3 = 100
```

**jq ATORAK Average Score: 100**

---

## Analysis and Observations

**Why all three score 100 on ATORAK adherence:**

jq (`jqlang/jq`) is a high-popularity tool (34k+ stars) with extensive public documentation, a dedicated website (jqlang.org), and widespread usage in tutorials, blog posts, and Stack Overflow answers. This matches the TCC's classification: high-popularity tool with extensive public documentation.

**KD (Domain Concepts) — all three score 1:**
All three READMEs include an explicit domain concepts section in the Overview, listing and correctly defining the core jq entities. data1.md defines 6 concepts (JSON, Filters, Streams, Operators and Functions, Modules, Pipelines). data2.md defines 6 concepts with an explicit "Domain Concepts" subsection, adding "Slice and Dice" as a distinct concept. data3.md defines 7 concepts — the most comprehensive — adding "Variables and Assignments" as an explicit entity and providing the most precise JSON Data definition (enumerating all JSON value types).

**KE (Execution Facts) — all three score 1:**
All three READMEs provide correct, executable installation commands for multiple platforms (Linux, macOS, Windows, build from source), correct CLI option documentation with accurate behavioral descriptions, and correct filter/function references. data1.md documents 9 CLI options (the most among the three). data3.md uniquely documents the C API (`jq_init`, `jq_compile`, `jq_start`, `jq_next`, `jv_parse`) and the `--stream` option. data2.md adds `-M/--monochrome-output` and Windows Scoop installation. Note: data2.md contains hallucinated options (`--debug-dump`, `--verbose`) in a "Feedback and Debugging" section — these are correctness issues (§4.4.2) but do not negate the presence of the KE knowledge element for ATORAK completeness purposes.

**KU (Usage Patterns) — all three score 1:**
All three READMEs present multiple named usage patterns covering the core jq workflows (field extraction, array filtering, data transformation, stdin processing, shell scripting integration). data1.md uniquely demonstrates the object modification pattern (`jq '. + {...}'`) and shell variable capture. data2.md adds the `map()` transformation pattern. data3.md uniquely demonstrates the `--arg` variable injection pattern and includes a "Best Practices" subsection that explicitly communicates the *why* dimension.

**Qualitative differences (not affecting binary ATORAK score):**
- data1.md: Most complete CLI option coverage (9 options), includes build-from-source instructions, shell scripting integration pattern.
- data2.md: Adds `-M/--monochrome-output`, Windows Scoop installation, `map()` transformation pattern. Contains hallucinated `--debug-dump` and `--verbose` options (correctness issue only).
- data3.md: Most comprehensive domain concepts (7 entities), uniquely documents C API, `--stream` option, `--arg` variable pattern, and "Best Practices" subsection.

**This result is consistent with the TCC's hypothesis** that high-popularity tools with extensive public documentation are the easiest case for LLM-based README generation. jq's ubiquity in LLM training data ensures that all three knowledge elements are naturally and correctly present in every generated README.
