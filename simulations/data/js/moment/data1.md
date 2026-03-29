# Moment.js

## Overview

Moment.js is a widely-used JavaScript library designed for parsing, validating, manipulating, and displaying dates and times in JavaScript. It simplifies working with dates by providing an intuitive and rich API for handling date-time operations, formatting, and internationalization. Moment.js models several key domain concepts related to time and calendars:

- **Date and Time Representations:** Moments encapsulate a point in time with support for time zones and locales.
- **Parsing:** Convert date/time strings into Moment objects using flexible formats or heuristics.
- **Formatting:** Convert Moment objects to strings with specified formats or localized outputs.
- **Manipulation:** Add, subtract, set, or query parts of a date/time (e.g., day, month, year, hour).
- **Comparison:** Compare moments for equality, order, or duration differences.
- **Durations and Intervals:** Represent spans of time, perform arithmetic, and format them.
- **Localization:** Support for various locales and languages for formatting and parsing.

Moment.js serves as a foundational tool in many JavaScript projects requiring robust date and time handling, abstracting away many of JavaScript's native Date pitfalls.

---

## Installation

Moment.js can be installed in various environments.

### Using npm

```bash
npm install moment
```

### Using Yarn

```bash
yarn add moment
```

### Using CDN

Include directly in HTML via:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.4/moment.min.js"></script>
```

Moment.js works in Node.js and all modern browsers.

---

## Usage and Examples

### Creating Moments

Create a moment representing the current date and time:

```js
const moment = require("moment");
const now = moment();
console.log(now.format());
// Outputs ISO 8601 format, e.g. 2024-06-01T14:05:32+00:00
```

Create a moment from a specific date string:

```js
const birthday = moment("1990-12-25", "YYYY-MM-DD");
console.log(birthday.format("MMMM Do, YYYY"));
// Outputs "December 25th, 1990"
```

### Parsing Dates with Custom Formats

```js
const dateStr = "31/01/2024 15:30";
const date = moment(dateStr, "DD/MM/YYYY HH:mm");
console.log(date.format());
// Outputs parsed ISO string
```

### Manipulating Dates

Add 7 days:

```js
const nextWeek = moment().add(7, "days");
console.log(nextWeek.format("YYYY-MM-DD"));
```

Subtract 3 months:

```js
const threeMonthsAgo = moment().subtract(3, "months");
console.log(threeMonthsAgo.format("YYYY-MM-DD"));
```

Set specific units:

```js
const newYear = moment().month(0).date(1);
console.log(newYear.format("YYYY-MM-DD")); // Jan 1 of current year
```

### Comparing Moments

Check if one date is before another:

```js
const date1 = moment("2023-01-01");
const date2 = moment("2024-01-01");
console.log(date1.isBefore(date2)); // true
```

Check if two moments are the same day:

```js
const date1 = moment("2024-06-01");
const date2 = moment("2024-06-01T10:00");
console.log(date1.isSame(date2, "day")); // true
```

### Duration and Humanize

Create a duration of 2 hours and 15 minutes:

```js
const duration = moment.duration({ hours: 2, minutes: 15 });
console.log(duration.humanize()); // "2 hours"
```

Get difference between two moments:

```js
const start = moment("2024-06-01 08:00");
const end = moment("2024-06-01 10:30");
const diff = moment.duration(end.diff(start));
console.log(diff.asMinutes()); // 150
```

---

## API Reference

### `moment(input, format, strict)`

Creates a Moment object.

- `input` (string|Date|Moment|number|array): The date/time input.
- `format` (string|string[], optional): Format(s) to parse the input.
- `strict` (boolean, optional): Whether to use strict parsing.

Returns a Moment instance representing the parsed date/time.

---

### `moment().format(formatString)`

Formats the Moment to a string.

- `formatString` (string, optional): Formatting tokens (e.g., `"YYYY-MM-DD"`, `"MMMM Do, YYYY"`).

Returns a formatted string representing the date/time.

---

### `moment().add(amount, unit)`

Adds time to the moment.

- `amount` (number): Amount of time units to add.
- `unit` (string): Unit of time (`'days'`, `'months'`, `'years'`, `'hours'`, `'minutes'`, `'seconds'`, etc).

Returns the modified Moment.

---

### `moment().subtract(amount, unit)`

Subtracts time from the moment.

- Parameters identical to `.add()`.

Returns the modified Moment.

---

### `moment().isBefore(momentInput, unit)`

Checks if the current moment is before another.

- `momentInput` (Moment|Date|string): The moment to compare with.
- `unit` (string, optional): Granularity (e.g., `'day'`, `'month'`).

Returns boolean.

---

### `moment().isSame(momentInput, unit)`

Checks if the current moment is same as another.

- Parameters identical to `.isBefore()`.

Returns boolean.

---

### `moment.duration(input, unit)`

Creates a Duration object representing a span of time.

- `input` (number|object|string): Number with unit or object with time properties.
- `unit` (string, optional): Unit for number input.

Returns a Duration instance.

---

### Common Duration Methods

- `.humanize()`: Converts duration to human-readable string.
- `.asMilliseconds()`, `.asSeconds()`, `.asMinutes()`, `.asHours()`, `.asDays()`: Converts duration into specified units.

---

### Localization

- `moment.locale(localeName)`: Sets the locale globally.
- `moment().locale(localeName)`: Sets the locale for a single Moment.

---

## License

Moment.js is licensed under the MIT License. For full details, see the [LICENSE](https://github.com/moment/moment/blob/develop/LICENSE) file.
