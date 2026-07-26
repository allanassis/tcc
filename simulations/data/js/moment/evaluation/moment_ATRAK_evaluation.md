# Moment — README-Gen ATRAK Evaluation

ATRAK assesses **presence, not correctness** of three Knowledge Elements (K_D, K_E, K_U).
An element is absent (0) only when the carrying section is empty/missing, is a bare name-only list,
or contains only unresolved placeholders. Otherwise present (1).

## Ground Truth Reference

- **Project:** Moment (Moment.js)
- **Repository:** https://github.com/moment/moment
- **Domain:** JavaScript date & time library (parse, validate, manipulate, display dates/times)
- **Core domain entities:** Moment (point in time, mutable), Duration (contextless length of time),
  Locale (i18n), format tokens, UTC/offset mode, relative time.
- **Core execution facts:** installs via `npm install moment` (zero runtime deps, `engines=node:*`,
  MIT); `require('moment')` in Node loads all locales; mutable objects; `format()` default ISO 8601;
  `add/subtract/startOf` mutate & chain; `diff` returns number; `duration().humanize()/asX()`.
- **Core usage patterns:** create moment, parse with format string, format output, add/subtract time,
  compare (isBefore/isSame), relative time (fromNow), durations, localization, UTC/local.

## README 1 — `data1.md`

- **K_D — Domain Concepts: PRESENT (1).** Overview defines Date/Time Representations, Parsing,
  Formatting, Manipulation, Comparison, Durations & Intervals, Localization — each with an explanation
  (not a bare list).
- **K_E — Execution Facts: PRESENT (1).** Installation (npm/yarn/CDN), Node.js/browser support,
  API inputs/outputs, parameter types (`input`, `format`, `strict`), return types (Moment, boolean,
  Duration), duration conversions.
- **K_U — Usage Patterns: PRESENT (1).** Ten runnable code examples across create/parse/manipulate/
  compare/duration with what/why narration.
- **K(data1) = (1+1+1)/3 = 100%**

## README 2 — `data2.md`

- **K_D: PRESENT (1).** "Domain Concepts" list with definitions (Parsing, Manipulation, Formatting,
  Localization, Time Zones, Relative Time, Durations).
- **K_E: PRESENT (1).** Installation, API signatures with parameter/return descriptions, default ISO
  8601 behavior, chaining semantics.
- **K_U: PRESENT (1).** Six worked example blocks (create, manipulate, format, relative time,
  duration/diff, localization).
- **K(data2) = 100%**

## README 3 — `data3.md`

- **K_D: PRESENT (1).** "Main Domain Concepts" with definitions (Manipulation, Parsing/Formatting,
  Time Zones/UTC, Relative Time, Localization, Durations, Validation).
- **K_E: PRESENT (1).** Installation, parsing rules (ISO 8601/RFC 2822), strict parsing, UTC mode,
  duration conversions, return types.
- **K_U: PRESENT (1).** Seven example blocks including validation and UTC/local usage.
- **K(data3) = 100%**

## Summary

| README | K_D | K_E | K_U | ATRAK % |
|---|---|---|---|---|
| data1.md | 1 | 1 | 1 | 100 |
| data2.md | 1 | 1 | 1 | 100 |
| data3.md | 1 | 1 | 1 | 100 |
| **average** | 1 | 1 | 1 | **100** |

Cross-checked sources: installed `moment@2.30.1` (node introspection), https://github.com/moment/moment,
https://momentjs.com/docs/.
