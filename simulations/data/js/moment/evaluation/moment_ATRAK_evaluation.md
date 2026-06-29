# Moment.js — ATORAK Adherence Evaluation

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

- Tool: **moment** — JavaScript date/time parsing, manipulation, and formatting library (npm package)
- Repository: https://github.com/moment/moment
- Domain: date and time handling, parsing, formatting, localization, durations
- Core domain entities: Moment object, Duration, Locale, Parsing, Formatting, Manipulation, Relative Time, UTC/Timezone, Validation
- Core execution facts: `moment()`, `moment(String, String)`, `moment.utc()`, `moment.duration()`, `.format()`, `.add()`, `.subtract()`, `.diff()`, `.fromNow()`, `.isBefore()`, `.isAfter()`, `.isSame()`, `.isValid()`, `.locale()`, `.startOf()`, `.endOf()`
- License: MIT

---

## data1.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

The README must correctly represent the conceptual vocabulary and entities of the moment.js domain.

**Evidence in data1.md:**

The "Overview" section lists the following domain concepts inline as bullet points:

- **Date and Time Representations** — "Moments encapsulate a point in time with support for time zones and locales." ✅ Correct; the Moment object as a point-in-time encapsulation is the central abstraction.
- **Parsing** — "Convert date/time strings into Moment objects using flexible formats or heuristics." ✅ Correct; accurately describes both format-based and heuristic parsing.
- **Formatting** — "Convert Moment objects to strings with specified formats or localized outputs." ✅ Correct.
- **Manipulation** — "Add, subtract, set, or query parts of a date/time (e.g., day, month, year, hour)." ✅ Correct; enumerates the manipulation operations.
- **Comparison** — "Compare moments for equality, order, or duration differences." ✅ Correct.
- **Durations and Intervals** — "Represent spans of time, perform arithmetic, and format them." ✅ Correct; Duration is a distinct concept from Moment.
- **Localization** — "Support for various locales and languages for formatting and parsing." ✅ Correct.

The overview also correctly describes Moment.js as a library for "parsing, validating, manipulating, and displaying dates and times in JavaScript" and mentions "abstracting away many of JavaScript's native Date pitfalls" — accurate characterization.

**Assessment:** data1.md correctly represents the domain concepts of moment.js. All seven listed entities are accurately defined. The domain is correctly identified as date/time handling. Notably, it does not explicitly list Relative Time or Validation as named concepts, but Comparison covers the comparison domain and Parsing implicitly covers validation. The coverage is sufficient to satisfy KD.

**KD = 1** ✅

---

#### KE — Execution Facts

The README must correctly represent concrete, verifiable runtime facts: commands, parameters, environment requirements, installation steps, and behavioral descriptions.

**Evidence in data1.md:**

*Installation facts:*
- `npm install moment` — correct and executable. ✅
- `yarn add moment` — correct and executable. ✅
- CDN script tag with `cdnjs.cloudflare.com` URL — correct for browser usage. ✅
- "Moment.js works in Node.js and all modern browsers." — accurate environment requirement. ✅

*API Reference facts:*
- `moment(input, format, strict)` — documents `input` (string|Date|Moment|number|array), `format` (string|string[]), `strict` (boolean). ✅ All parameter types are correct.
- `moment().format(formatString)` — documents `formatString` as optional, returns formatted string. ✅ Correct; omitting format defaults to ISO 8601.
- `moment().add(amount, unit)` — documents `amount` (number) and `unit` (string) with examples of valid units. ✅ Correct signature.
- `moment().subtract(amount, unit)` — "Parameters identical to `.add()`." ✅ Correct.
- `moment().isBefore(momentInput, unit)` — documents `momentInput` and optional `unit` granularity, returns boolean. ✅ Correct.
- `moment().isSame(momentInput, unit)` — "Parameters identical to `.isBefore()`." ✅ Correct.
- `moment.duration(input, unit)` — documents `input` (number|object|string) and optional `unit`. ✅ Correct.
- Duration methods: `.humanize()`, `.asMilliseconds()`, `.asSeconds()`, `.asMinutes()`, `.asHours()`, `.asDays()` — all real methods. ✅
- `moment.locale(localeName)` and `moment().locale(localeName)` — both static and instance forms documented. ✅

**Assessment:** All documented execution facts are correct and verifiable. Installation commands are executable. The API Reference covers 7 core methods with correct parameter names, types, and return values. Duration methods are correctly listed. No hallucinated commands or incorrect parameter types. The coverage is solid though it omits `.diff()`, `.fromNow()`, `.isValid()`, and `.startOf()` — but what is documented is accurate.

**KE = 1** ✅

---

#### KU — Usage Patterns

The README must present recurring, purposeful combinations of API calls that solve real problems, communicating *what* the pattern does, *how* to execute it, and *why* it is useful.

**Evidence in data1.md:**

The "Usage and Examples" section presents the following patterns:

1. **Creating Moments (current time)** — `moment()` → `.format()`: *What*: get current date/time. *How*: call `moment()` then `.format()`. *Why*: simplest entry point. ✅
2. **Creating from a date string** — `moment("1990-12-25", "YYYY-MM-DD")` → `.format("MMMM Do, YYYY")`: *What*: parse a specific date. *How*: pass string and format token. *Why*: demonstrates format-based parsing. ✅
3. **Parsing with Custom Formats** — `moment(dateStr, "DD/MM/YYYY HH:mm")` → `.format()`: *What*: parse non-ISO date strings. *How*: provide custom format string. *Why*: real-world dates rarely come in ISO format. ✅
4. **Add 7 days** — `moment().add(7, "days")` → `.format()`: *What*: advance a date. *How*: `.add(amount, unit)`. ✅
5. **Subtract 3 months** — `moment().subtract(3, "months")` → `.format()`: *What*: go back in time. *How*: `.subtract(amount, unit)`. ✅
6. **Set specific units** — `moment().month(0).date(1)`: *What*: set to a specific date. *How*: chain setter calls. ✅
7. **isBefore comparison** — `date1.isBefore(date2)`: *What*: compare two dates. *How*: `.isBefore()`. ✅
8. **isSame with granularity** — `date1.isSame(date2, "day")`: *What*: compare at day granularity. *How*: `.isSame(date, unit)`. ✅
9. **Duration humanize** — `moment.duration({hours: 2, minutes: 15}).humanize()`: *What*: create and describe a duration. *How*: `moment.duration()` → `.humanize()`. ✅
10. **Duration diff** — `moment.duration(end.diff(start)).asMinutes()`: *What*: compute elapsed time. *How*: `.diff()` inside `moment.duration()`. ✅

**Assessment:** data1.md presents ten distinct usage patterns covering the full spectrum of moment.js usage. Each pattern is a meaningful combination of API calls. The *what* and *how* are clearly communicated through code and prose. The *why* is implied by section headings and contextual descriptions. This fully satisfies the KU criterion.

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

- **Date and Time Parsing** — "Converting strings or other representations into date objects." ✅ Correct.
- **Date and Time Manipulation** — "Adding, subtracting, or adjusting units of time (years, months, days, hours, etc.)." ✅ Correct.
- **Formatting** — "Displaying dates and times in user-friendly or standardized string formats." ✅ Correct.
- **Localization** — "Supporting multiple languages and locale-specific date/time formats." ✅ Correct.
- **Time Zones** — "Handling timezone offsets and conversions." ✅ Correct; explicitly names Time Zones as a distinct concept.
- **Relative Time** — "Expressing time differences in human-readable form (e.g., '2 days ago')." ✅ Correct; data2.md is the only README to explicitly name Relative Time as a domain concept.
- **Durations** — "Representing spans of time rather than specific dates." ✅ Correct; correctly distinguishes Duration from Moment.

The overview also correctly describes Moment.js as providing "an intuitive and consistent API that enhances JavaScript's native Date object capabilities."

**Assessment:** data2.md provides the most structured and complete domain concept representation of the three READMEs. All seven listed entities are accurately defined. Notably, it explicitly names Relative Time and Time Zones as distinct concepts — both are real and important moment.js domain entities not explicitly named in data1.md.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data2.md:**

*Installation facts:*
- `npm install moment` — correct. ✅
- `yarn add moment` — correct. ✅
- CDN script tag with `cdn.jsdelivr.net` URL — correct. ✅

*API Reference facts:*
- `moment(input, format, strict)` — documents all three parameters with correct types. ✅
- `.format(string)` — optional format string, defaults to ISO 8601. ✅ Includes a concrete example: `moment().format('YYYY-MM-DD')`.
- `.add(Number, String)` — correct signature with valid unit examples. ✅
- `.subtract(Number, String)` — correct. ✅
- `.startOf(String)` — documents unit parameter (`'year'`, `'month'`, `'day'`, `'hour'`). ✅ data2.md is the only README to include `.startOf()` in the API Reference.
- `.diff(Moment, String, Boolean)` — documents all three parameters including the floating-point boolean. ✅ Correct and complete signature.
- `.fromNow(Boolean)` — documents the optional boolean suffix parameter. ✅ Correct.
- `.locale(String)` — documents both get and set behavior. ✅
- `moment.locale([localeCode])` — static form documented. ✅
- `moment.duration(input, unit)` — correct. ✅

**Assessment:** data2.md has the most complete API Reference of the three READMEs. It uniquely documents `.startOf()` and `.diff()` with full parameter details including the floating-point boolean. `.fromNow()` is also explicitly documented. All execution facts are correct and verifiable.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data2.md:**

The "Usage and Examples" section presents the following patterns:

1. **Creating Moment Objects (current + specific + custom format)** — Three creation variants in one block: `moment()`, `moment('1990-12-25')`, `moment('12-25-1990', 'MM-DD-YYYY')`. *What*: create moments in different ways. *How*: three constructor forms. ✅
2. **Manipulating Dates** — `.add(7, 'days')`, `.subtract(1, 'month')`, `.startOf('day')`, `.startOf('month')`, `.startOf('year')`: *What*: adjust dates. *How*: chained manipulation methods. ✅ Uniquely demonstrates `.startOf()`.
3. **Formatting Dates** — `.format('MMMM Do YYYY, h:mm:ss a')`, `.format('ddd, hA')`, `.toISOString()`: *What*: display dates in various formats. *How*: format tokens and `.toISOString()`. ✅
4. **Relative Time** — `moment().subtract(10, 'days').fromNow()` → "10 days ago"; `moment().add(5, 'hours').fromNow()` → "in 5 hours": *What*: express time relative to now. *How*: `.fromNow()`. *Why*: human-readable time display. ✅ Only README to demonstrate `.fromNow()` as a named pattern.
5. **Duration and Difference** — `moment.duration(end.diff(start)).asDays()`, `.months()`, `moment.duration(2, 'hours').humanize()`: *What*: compute and describe time spans. *How*: `.diff()` + `moment.duration()`. ✅
6. **Localization** — `moment.locale('fr')` → `.format('LL')` → `moment.locale('en')`: *What*: format dates in a different language. *How*: set locale globally, format, reset. *Why*: internationalization. ✅

**Assessment:** data2.md presents six distinct usage patterns. It uniquely demonstrates `.fromNow()` as a named "Relative Time" pattern and `.startOf()` in the manipulation block. The localization pattern shows a complete locale switch-and-reset workflow. All patterns are purposeful and represent real developer workflows.

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

The "Overview" section contains an explicit "Main Domain Concepts" subsection listing:

- **Date and Time Manipulation** — "Work with JavaScript dates easily including addition, subtraction, and comparison." ✅ Correct.
- **Parsing and Formatting** — "Parse dates from strings and format dates to readable strings in many locales." ✅ Correct; combines parsing and formatting as one concept.
- **Time Zones and UTC** — "Support for UTC mode and localized time zones." ✅ Correct; explicitly names UTC mode.
- **Relative Time** — "Express time differences like '3 hours ago' or 'in 2 days.'" ✅ Correct; includes concrete examples.
- **Localization (i18n)** — "Moment.js supports multiple languages and regional settings." ✅ Correct; explicitly labels it as i18n.
- **Durations** — "Represent time spans independent of date/time." ✅ Correct; the "independent of date/time" distinction is accurate.
- **Validation** — "Check if dates are valid or invalid." ✅ Correct; data3.md is the only README to explicitly name Validation as a domain concept.

The overview also correctly describes Moment.js as helping "accurately and consistently handle any date/time related operations, greatly easing cross-browser inconsistencies and complexity of native Date API."

**Assessment:** data3.md provides the most complete domain concept list of the three READMEs. It uniquely names Validation as an explicit domain concept, which is a real and important moment.js feature (`.isValid()`). All seven listed entities are accurately defined. The explicit mention of UTC mode and i18n labeling adds precision.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data3.md:**

*Installation facts:*
- `npm install moment` — correct. ✅
- `yarn add moment` — correct. ✅
- CDN script tag with `cdn.jsdelivr.net` URL — correct. ✅

*API Reference facts (grouped by category):*

Creating Moments:
- `moment()` — current date/time. ✅
- `moment(String, String)` — parse with format. ✅
- `moment.utc()` — UTC mode. ✅ data3.md is the only README to document `moment.utc()` in the API Reference.

Formatting:
- `.format([String])` — optional format, defaults to ISO 8601. ✅

Parsing:
- `moment(String)` — ISO8601 or RFC2822. ✅
- `moment(String, String[, Boolean])` — with strict parsing boolean. ✅

Manipulation:
- `.add(Number, String)` — with full unit list including `'milliseconds'`. ✅
- `.subtract(Number, String)` — same units. ✅

Query & Validation:
- `.isValid()` — returns boolean. ✅ Only README to document `.isValid()` in the API Reference.
- `.isBefore(Moment|String[, String])` — correct signature. ✅
- `.isAfter(Moment|String[, String])` — correct. ✅ Only README to document `.isAfter()`.

Relative Time:
- `.fromNow(Boolean)` — with suffix behavior. ✅
- `.toNow(Boolean)` — correct. ✅ Only README to document `.toNow()`.
- `.from(Moment|String[, Boolean])` — relative from another moment. ✅

Duration:
- `moment.duration(Number|String|Object, String)` — correct. ✅
- `.asMinutes()`, `.asHours()`, `.asSeconds()` etc. — correct. ✅

Timezone & UTC:
- `.utc()` — converts to UTC mode. ✅
- `.local()` — converts back to local. ✅

**Assessment:** data3.md has the most comprehensive API Reference of the three READMEs. It uniquely documents `moment.utc()`, `.isValid()`, `.isAfter()`, `.toNow()`, `.from()`, `.utc()`, and `.local()` — all real and verifiable methods. All execution facts are correct.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data3.md:**

The "Usage and Examples" section presents the following patterns:

1. **Creating a Moment Object** — `moment()` and `moment("1990-12-25")` with `.format()`: *What*: create moments. *How*: constructor forms. ✅
2. **Parsing Different Formats** — `moment("12-25-1990", "MM-DD-YYYY")` → `.format("YYYY-MM-DD")`: *What*: parse custom format. *How*: format string argument. ✅
3. **Manipulating Dates** — `.add(1, "days")`, `.add(1, "months")`, `.subtract(2, "hours")`: *What*: adjust dates. *How*: `.add()` and `.subtract()`. ✅
4. **Displaying Relative Time** — `moment().add(3, "days").fromNow()` → "in 3 days"; `moment().subtract(5, "minutes").fromNow()` → "5 minutes ago": *What*: human-readable relative time. *How*: `.fromNow()`. *Why*: user-facing time display. ✅
5. **Working with UTC and Timezones** — `moment.utc()` → `.format()` → `.local()` → `.format()`: *What*: work in UTC and convert to local. *How*: `moment.utc()` then `.local()`. *Why*: timezone-safe operations. ✅ Only README to demonstrate this pattern.
6. **Validating Dates** — `moment("2023-02-28", "YYYY-MM-DD", true).isValid()` → true; `moment("2023-02-30", ...).isValid()` → false: *What*: check date validity. *How*: strict parsing + `.isValid()`. *Why*: prevent invalid date processing. ✅ Only README to demonstrate validation as a pattern.
7. **Durations and Time Spans** — `moment.duration(2, "hours").asMinutes()` → 120; `moment("2023-12-25").diff(moment("2023-12-24"), "hours")` → 24: *What*: compute time spans. *How*: `moment.duration()` and `.diff()`. ✅

**Assessment:** data3.md presents seven distinct usage patterns. It uniquely demonstrates the UTC/timezone conversion pattern and the date validation pattern — both real and important moment.js workflows. The validation example with strict parsing (`true` as third argument) is particularly precise. All patterns are purposeful and represent real developer workflows.

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

## Summary: All Three moment READMEs — ATORAK Adherence

| README | KD (Domain Concepts) | KE (Execution Facts) | KU (Usage Patterns) | Kpercentage |
|--------|---------------------|---------------------|---------------------|-------------|
| data1.md | 1 | 1 | 1 | **100** |
| data2.md | 1 | 1 | 1 | **100** |
| data3.md | 1 | 1 | 1 | **100** |

### Final Average Score (Equation 16 from TCC §4.4.3)

```
Kavg = (100 + 100 + 100) / 3 = 100
```

**moment ATORAK Average Score: 100**

---

## Analysis and Observations

**Why all three score 100 on ATORAK adherence:**

Moment.js is one of the most downloaded JavaScript libraries of all time, with extensive public documentation, tutorials, and examples in LLM training data. The model correctly identified all three knowledge elements in every generated README.

**KD (Domain Concepts) — all three score 1:**
All three READMEs include a domain concepts section in the Overview. data1.md lists 7 concepts inline. data2.md provides the most structured subsection with 7 named concepts, uniquely naming Relative Time explicitly. data3.md provides the most complete list, uniquely naming Validation as a domain concept and explicitly labeling Localization as i18n.

**KE (Execution Facts) — all three score 1:**
All three READMEs provide correct, executable installation commands, correct API Reference sections with accurate parameter names and behavioral descriptions. data2.md uniquely documents `.startOf()` and `.diff()` with full parameter details. data3.md is the most comprehensive, uniquely documenting `moment.utc()`, `.isValid()`, `.isAfter()`, `.toNow()`, `.from()`, `.utc()`, and `.local()`.

**KU (Usage Patterns) — all three score 1:**
All three READMEs present multiple named usage patterns covering the core moment.js workflows. data1.md covers 10 patterns including setter chaining. data2.md uniquely demonstrates `.fromNow()` as a named Relative Time pattern and `.startOf()` in manipulation. data3.md uniquely demonstrates the UTC/timezone conversion pattern and the date validation pattern with strict parsing.

**Qualitative differences (not affecting binary ATORAK score):**
- data1.md: Broadest usage coverage (10 patterns), 9 API elements, includes setter chaining and duration diff.
- data2.md: Most structured domain concepts, 10 API elements, uniquely documents `.startOf()` and `.diff()` with full signatures.
- data3.md: Most comprehensive API Reference (15+ elements), 7 usage patterns, uniquely documents validation, UTC, `.isAfter()`, `.toNow()`.

**This result is consistent with the TCC's hypothesis** that high-popularity libraries with extensive public documentation are the easiest case for LLM-based README generation. Moment.js's ubiquity in LLM training data ensures that all three knowledge elements are naturally and correctly present in every generated README.
