# Moment — README-Gen Correctness Evaluation

Tool under evaluation: **README-Gen** (structured ATRAK-grounded prompting, `gpt-4.1-mini-2025-04-14`).
READMEs: `data1.md`, `data2.md`, `data3.md` (evaluated in this order).

## Environment & Cross-Checked Sources

- **Isolated execution env:** `/tmp/eval-moment` (`npm init -y`, `npm install moment`).
  Installed **moment 2.30.1**; `engines = {"node":"*"}`; runtime `dependencies = undefined`
  (zero); `license = "MIT"` (from `node_modules/moment/package.json`). Node v24.12.0, npm 11.6.2.
- **Repository:** https://github.com/moment/moment — `LICENSE` fetched from
  `raw.githubusercontent.com/moment/moment/develop/LICENSE` → **MIT License** text ("Permission is
  hereby granted, free of charge ... THE SOFTWARE IS PROVIDED 'AS IS'").
- **Official docs:** https://momentjs.com/docs/ — confirmed: moments are **mutable**; `add`/`subtract`/
  `startOf` mutate & return the same moment for chaining; `add(Number, String)`, `subtract(Number, String)`,
  `startOf(String)`, `diff(Moment, String, Boolean)`, `fromNow(Boolean)`, `toNow(Boolean)`,
  `from(...)`, `format([String])` (defaults to ISO 8601), `isBefore/isSame/isAfter(moment, [unit])`,
  `isValid()`, `moment.utc()`, `.utc()`, `.local()`, `moment.duration(...)`, duration `humanize()`/`asX()`,
  `moment.locale(String)` (global) and `moment().locale(String)` (instance).
- **API introspection:** `node -e` `typeof` checks against the installed package — every documented
  element resolved to `function` (see API tables below).
- **Install-path checks:** `npm install moment` (exit 0), `yarn add moment` (yarn 1.22.22, resolves
  `moment@2.30.1`, exit 0), and all three documented CDN URLs return **HTTP 200**.

Time-dependent outputs: the harness ran on 2026-07-25. Per the evaluation rule, a documented
example output that is **format-illustrative** (e.g. a sample date) counts as matching when the actual
output has the same shape. Coincidentally the run day was a Saturday, so `ddd` → `Sat` matched literally.

---

## README 1 — `data1.md`

### Project Title (T)
Title = `# Moment.js`.
1. Matches officially documented project name "Moment.js" (repo `moment/moment`) — **1**
2. Does not describe a different project — **1**
3. No hallucinated terminology — **1**
**T = 3/3 = 100%**

### Overview (O)
Text: "parsing, validating, manipulating, and displaying dates and times ... time zones and locales ...
durations ... localization."
1. Primary functionality correctly described (parse/validate/manipulate/display dates) — **1**
2. Supported by artifacts (all verified in installed package) — **1**
3. No unsupported features — moment core provides UTC mode + `utcOffset` (offset-based zone handling)
   and full locale support; claims are supported — **1**
4. Domain correctly identified (JS date/time library) — **1**
5. Terminology matches repo (Moment, parse, format, duration, locale) — **1**
**O = 5/5 = 100%**

### Installation (I) — executed
Documented paths: `npm install moment`, `yarn add moment`, CDN
`cdnjs.cloudflare.com/.../2.29.4/moment.min.js`. README states "works in Node.js and all modern browsers."
1. Required dependencies declared — moment has **zero runtime deps**; nothing missing — **1**
2. Commands execute without modification — `npm install moment` exit 0; `yarn add moment` exit 0;
   CDN URL HTTP 200 — **1**
3. No unresolved dependency errors — clean install, `found 0 vulnerabilities` — **1**
4. Environment requirements correct — no version claim made; installed `engines=node:*` → "Node.js and
   modern browsers" is accurate — **1**
5. Produces expected executable artifact — `require('moment')` works; CDN serves a valid build — **1**
**I = 5/5 = 100%**

### Usage and Examples (U) — executed (k = 10)

| # | Snippet | Executes | Output match | E_i |
|---|---|---|---|---|
| d1-s1 | `moment().format()` | yes | `2026-07-25T22:54:04-03:00` — ISO 8601 (format-illustrative) ✓ | 1 |
| d1-s2 | `moment("1990-12-25","YYYY-MM-DD").format("MMMM Do, YYYY")` | yes | `December 25th, 1990` (exact) ✓ | 1 |
| d1-s3 | `moment("31/01/2024 15:30","DD/MM/YYYY HH:mm").format()` | yes | `2024-01-31T15:30:00-03:00` — parsed ISO ✓ | 1 |
| d1-s4 | `moment().add(7,"days").format("YYYY-MM-DD")` | yes | `2026-08-01` (no fixed output documented) ✓ | 1 |
| d1-s5 | `moment().subtract(3,"months").format("YYYY-MM-DD")` | yes | `2026-04-25` ✓ | 1 |
| d1-s6 | `moment().month(0).date(1).format("YYYY-MM-DD")` | yes | `2026-01-01` — "Jan 1 of current year" ✓ | 1 |
| d1-s7 | `date1.isBefore(date2)` | yes | `true` (documented `true`) ✓ | 1 |
| d1-s8 | `date1.isSame(date2,"day")` | yes | `true` (documented `true`) ✓ | 1 |
| d1-s9 | `moment.duration({hours:2,minutes:15}).humanize()` | yes | `2 hours` (documented `"2 hours"`) ✓ | 1 |
| d1-s10 | `moment.duration(end.diff(start)).asMinutes()` | yes | `150` (documented `150`) ✓ | 1 |

All 10 snippets satisfy rules 1–5 (execute, imports documented via `require("moment")`, output matches,
no exceptions, behavior matches text). **U = 10/10 = 100%**

### API Reference (A) — verified against installed package + momentjs.com/docs

| Element | Exists | Names/params | Types | Return | Behavior | Not deprecated | A_i |
|---|---|---|---|---|---|---|---|
| `moment(input, format, strict)` | yes | ✓ | ✓ | Moment ✓ | ✓ | ✓ | 1 |
| `moment().format(formatString)` | yes | ✓ | ✓ | string ✓ | ✓ | ✓ | 1 |
| `moment().add(amount, unit)` | yes | ✓ | ✓ | mutated Moment ✓ | ✓ | ✓ | 1 |
| `moment().subtract(amount, unit)` | yes | ✓ | ✓ | mutated Moment ✓ | ✓ | ✓ | 1 |
| `moment().isBefore(momentInput, unit)` | yes | ✓ | ✓ | boolean ✓ | ✓ | ✓ | 1 |
| `moment().isSame(momentInput, unit)` | yes | ✓ | ✓ | boolean ✓ | ✓ | ✓ | 1 |
| `moment.duration(input, unit)` | yes | ✓ | ✓ | Duration ✓ | ✓ | ✓ | 1 |
| Duration methods `.humanize()/.asMilliseconds()/.asSeconds()/.asMinutes()/.asHours()/.asDays()` | yes | ✓ | ✓ | string/number ✓ | ✓ | ✓ | 1 |
| Localization `moment.locale()` / `moment().locale()` | yes | ✓ | ✓ | ✓ | ✓ | ✓ | 1 |

**A = 9/9 = 100%**

### License (L)
1. Documented MIT matches repo `LICENSE` (MIT) — **1**
2. `MIT` is a valid SPDX identifier — **1**
3. No conflicting licensing info — **1**
**L = 3/3 = 100%**

**C_R(data1) = (100+100+100+100+100+100)/6 = 100%**

---

## README 2 — `data2.md`

### Project Title (T) — `# Moment.js`: matches, not different, no hallucination → **T = 100%**

### Overview (O)
Adds "Time Zones: Handling timezone offsets and conversions", "Relative Time", "Durations".
1. Functionality correct — **1**; 2. Supported — **1**; 3. No unsupported features (offset handling,
relative time, durations all in core) — **1**; 4. Domain correct — **1**; 5. Terminology matches — **1**.
**O = 100%**

### Installation (I) — executed
Paths: `npm install moment` (exit 0), `yarn add moment` (exit 0), CDN
`cdn.jsdelivr.net/npm/moment@2.29.4/moment.min.js` (HTTP 200). Same verification as data1.
Rules 1–5 all pass. **I = 100%**

### Usage and Examples (U) — executed (k = 6)

| # | Snippet block | Executes | Output match | E_i |
|---|---|---|---|---|
| d2-s1 | create now / birthday / `moment('12-25-1990','MM-DD-YYYY')` | yes | `December 25th, 1990`, `1990-12-25` ✓ | 1 |
| d2-s2 | manipulate `m.add(7,'days')` / `subtract(1,'month')` / `startOf(...)` | yes | runs; behavior matches text (mutable `m`, documented outputs are generic) ✓ | 1 |
| d2-s3 | format `'MMMM Do YYYY, h:mm:ss a'` / `'ddd, hA'` / `toISOString()` | yes | `July 25th 2026, 10:54:04 pm`, `Sat, 10PM` — format-illustrative ✓ | 1 |
| d2-s4 | relative `subtract(10,'days').fromNow()` / `add(5,'hours').fromNow()` | yes | `10 days ago`, `in 5 hours` (exact) ✓ | 1 |
| d2-s5 | duration `end.diff(start)` → `asDays()`/`months()`; `duration(2,'hours').humanize()` | yes | `91`, `2`, `2 hours` (generic comments) ✓ | 1 |
| d2-s6 | localization `moment.locale('fr'); format('LL')` | yes | `25 juillet 2026` — French locale ✓ | 1 |

**U = 6/6 = 100%**

### API Reference (A)

| Element | Exists | Signature/params | Return | Behavior | Not deprecated | A_i |
|---|---|---|---|---|---|---|
| `moment(input, format, strict)` | yes | ✓ | Moment ✓ | ✓ | ✓ | 1 |
| `.format(string)` (default ISO 8601) | yes | ✓ | string ✓ | ✓ | ✓ | 1 |
| `.add(Number, String)` (chaining) | yes | ✓ | same moment ✓ | ✓ | ✓ | 1 |
| `.subtract(Number, String)` | yes | ✓ | same moment ✓ | ✓ | ✓ | 1 |
| `.startOf(String)` | yes | ✓ | same moment ✓ | ✓ | ✓ | 1 |
| `.diff(Moment, String, Boolean)` | yes | ✓ | number (float if 3rd=true) ✓ | ✓ | ✓ | 1 |
| `.fromNow(Boolean)` | yes | ✓ | string ✓ | ✓ | ✓ | 1 |
| `.locale(String)` (get/set) | yes | ✓ | moment/string ✓ | ✓ | ✓ | 1 |
| `moment.locale([localeCode])` | yes | ✓ | ✓ | ✓ | ✓ | 1 |
| `moment.duration(input, unit)` | yes | ✓ | Duration ✓ | ✓ | ✓ | 1 |

**A = 10/10 = 100%**

### License (L) — MIT matches repo, valid identifier, no conflict → **L = 100%**

**C_R(data2) = 100%**

---

## README 3 — `data3.md`

### Project Title (T) — `# Moment.js`: matches → **T = 100%**

### Overview (O)
Adds "Time Zones and UTC (UTC mode)", "Validation". 1–5 all pass (UTC mode, validation `isValid`,
relative time, durations all verified in core). **O = 100%**

### Installation (I) — executed
Paths: `npm install moment` (exit 0), `yarn add moment` (exit 0), CDN
`cdn.jsdelivr.net/npm/moment@2.29.4/min/moment.min.js` (HTTP 200). Rules 1–5 pass. **I = 100%**

### Usage and Examples (U) — executed (k = 7)

| # | Snippet block | Executes | Output match | E_i |
|---|---|---|---|---|
| d3-s1 | create now / `moment("1990-12-25").format("MMMM Do, YYYY")` | yes | `December 25th, 1990` ✓ | 1 |
| d3-s2 | parse `moment("12-25-1990","MM-DD-YYYY").format("YYYY-MM-DD")` | yes | `1990-12-25` (documented) ✓ | 1 |
| d3-s3 | manipulate add days/months, subtract hours | yes | `2026-07-26`, `2026-08-25`, `20:54` ✓ | 1 |
| d3-s4 | relative `add(3,'days').fromNow()` / `subtract(5,'minutes').fromNow()` | yes | `in 3 days`, `5 minutes ago` (exact) ✓ | 1 |
| d3-s5 | `moment.utc()` / `.local()` | yes | `2026-07-26T01:54:04Z`, local ISO ✓ | 1 |
| d3-s6 | validate strict `isValid()` | yes | `true`, `false` (documented) ✓ | 1 |
| d3-s7 | `moment.duration(2,'hours').asMinutes()` / `diff(...,'hours')` | yes | `120`, `24` (documented) ✓ | 1 |

**U = 7/7 = 100%**

### API Reference (A)

| Element | Exists | Signature | Behavior | Not deprecated | A_i |
|---|---|---|---|---|---|
| `moment()` / `moment(String,String)` / `moment.utc()` | yes | ✓ | ✓ | ✓ | 1 |
| `.format([String])` | yes | ✓ | ✓ | ✓ | 1 |
| `moment(String)` (ISO 8601 / RFC 2822) | yes | ✓ | ✓ | ✓ | 1 |
| `moment(String, String[, Boolean])` (strict) | yes | ✓ | ✓ | ✓ | 1 |
| `.add(Number, String)` / `.subtract(Number, String)` | yes | ✓ | ✓ | ✓ | 1 |
| `.isValid()` | yes | ✓ | ✓ | ✓ | 1 |
| `.isBefore(...)` / `.isAfter(...)` | yes | ✓ | ✓ | ✓ | 1 |
| `.fromNow(Boolean)` / `.toNow(Boolean)` / `.from(...)` | yes | ✓ | ✓ | ✓ | 1 |
| `moment.duration(...)` / `.asMinutes()/.asHours()/.asSeconds()` | yes | ✓ | ✓ | ✓ | 1 |
| `.utc()` / `.local()` | yes | ✓ | ✓ | ✓ | 1 |

**A = 10/10 = 100%**

### License (L) — MIT matches repo, valid, no conflict → **L = 100%**

**C_R(data3) = 100%**

---

## Summary

| README | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| data1.md | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| data2.md | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| data3.md | 100 | 100 | 100 | 100 | 100 | 100 | 100 |
| **average** | 100 | 100 | 100 | 100 | 100 | 100 | **100** |
