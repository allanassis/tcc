# Moment.js

## Overview

Moment.js is a popular JavaScript library for parsing, validating, manipulating, and formatting dates and times in a simple and consistent way. It abstracts complex date-time operations into easy-to-use APIs, handling a wide variety of date formats, locales, time zones, and calendar arithmetic.

### Domain Concepts

- **Date and Time Parsing:** Converting strings or other representations into date objects.
- **Date and Time Manipulation:** Adding, subtracting, or adjusting units of time (years, months, days, hours, etc.).
- **Formatting:** Displaying dates and times in user-friendly or standardized string formats.
- **Localization:** Supporting multiple languages and locale-specific date/time formats.
- **Time Zones:** Handling timezone offsets and conversions.
- **Relative Time:** Expressing time differences in human-readable form (e.g., "2 days ago").
- **Durations:** Representing spans of time rather than specific dates.

Moment.js provides an intuitive and consistent API that enhances JavaScript’s native Date object capabilities and helps developers manage dates and times reliably.

---

## Installation

### Using npm

```bash
npm install moment
```

### Using Yarn

```bash
yarn add moment
```

### Using CDN

Include the following script tag in your HTML:

```html
<script src="https://cdn.jsdelivr.net/npm/moment@2.29.4/moment.min.js"></script>
```

---

## Usage and Examples

### Creating Moment Objects

```js
const moment = require('moment');

// Current date and time
const now = moment();
console.log(now.format()); // Outputs ISO 8601 string of current date/time

// Specific date
const birthday = moment('1990-12-25');
console.log(birthday.format('MMMM Do, YYYY')); // December 25th, 1990

// Parsing with custom format
const date = moment('12-25-1990', 'MM-DD-YYYY');
console.log(date.format('YYYY-MM-DD')); // 1990-12-25
```

### Manipulating Dates

```js
const m = moment();

// Add 7 days
const nextWeek = m.add(7, 'days');
console.log(nextWeek.format('YYYY-MM-DD'));

// Subtract 1 month
const lastMonth = m.subtract(1, 'month');
console.log(lastMonth.format('YYYY-MM-DD'));

// Start of day/month/year
console.log(m.startOf('day').format());
console.log(m.startOf('month').format());
console.log(m.startOf('year').format());
```

### Formatting Dates

```js
const now = moment();

console.log(now.format('MMMM Do YYYY, h:mm:ss a')); // April 27th 2024, 3:00:15 pm
console.log(now.format('ddd, hA'));                  // Sat, 3PM
console.log(now.toISOString());                       // ISO 8601 string
```

### Relative Time

```js
const past = moment().subtract(10, 'days');
console.log(past.fromNow()); // "10 days ago"

const future = moment().add(5, 'hours');
console.log(future.fromNow()); // "in 5 hours"
```

### Duration and Difference

```js
const start = moment('2024-01-01');
const end = moment('2024-04-01');

const duration = moment.duration(end.diff(start));
console.log(duration.asDays()); // Number of days between the two dates
console.log(duration.months());  // Months in duration

// Create a duration explicitly
const twoHours = moment.duration(2, 'hours');
console.log(twoHours.humanize()); // "2 hours"
```

### Localization

```js
moment.locale('fr');
console.log(moment().format('LL')); // Format date in French locale

moment.locale('en'); // Switch back to English
```

---

## API Reference

### `moment(input, format, strict)`

Creates a Moment object.

- `input` (string|Date|number|Moment|Array): The date/time input to parse.
- `format` (string|Array, optional): Specify the expected format(s) if parsing strings.
- `strict` (boolean, optional): Use strict parsing when `true`.

Returns: a Moment object representing the given date/time.

---

### Moment Object Methods

#### `.format(string)`

Format the moment to a string.

- `string` (string, optional): A formatting pattern (uses tokens like `YYYY`, `MM`, `DD`, `hh`, etc.). If omitted, defaults to ISO 8601.

Returns: formatted date string.

Example:

```js
moment().format('YYYY-MM-DD'); // "2024-04-27"
```

---

#### `.add(Number, String)`

Add time to the moment.

- Number (number): Quantity to add.
- String (string): Unit of time (`'years'`, `'months'`, `'days'`, `'hours'`, `'minutes'`, `'seconds'`, `'milliseconds'`, or their shorthand forms).

Returns: the same moment object for chaining.

---

#### `.subtract(Number, String)`

Subtract time similarly to `.add()`.

---

#### `.startOf(String)`

Set time to the start of a unit.

- String (string): Unit of time like `'year'`, `'month'`, `'day'`, `'hour'`, etc.

Returns: the same moment object.

---

#### `.diff(Moment, String, Boolean)`

Get the difference between two moments.

- Moment (Moment): The moment to subtract from this one.
- String (string, optional): Unit of time (`'years'`, `'months'`, `'days'`, etc.) to measure difference.
- Boolean (boolean, optional): If `true`, return a floating number instead of an integer.

Returns: difference as a number.

---

#### `.fromNow(Boolean)`

Relative time from now.

- Boolean (boolean, optional): If `true`, returns without suffix ("ago" or "in").

Returns: human-readable relative time string.

---

#### `.locale(String)`

Get or set the locale.

- String (string, optional): Locale code. If omitted, returns current locale.

Returns: the moment object if setting locale, or the current locale string if getting.

---

### Static Methods

#### `moment.locale([localeCode])`

Get or set the global locale.

#### `moment.duration(input, unit)`

Create a duration object representing a length of time.

- Input can be a number or an object specifying units.
- Unit is optional if input is object.

---

## License

Moment.js is released under the [MIT License](https://github.com/moment/moment/blob/develop/LICENSE).

---
