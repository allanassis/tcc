# Moment.js

## Overview

Moment.js is a popular JavaScript library for parsing, validating, manipulating, and formatting dates and times in JavaScript. It provides a simple and consistent API to handle date operations, overcoming many limitations of the native JavaScript Date object. Moment.js supports multiple formats, locales, and time zones, enabling developers to work effortlessly with dates and times across different requirements and regions.

### Domain Concepts

- **Date and Time Parsing:** Interpreting strings or timestamps into Date objects.
- **Date Manipulation:** Operations such as adding, subtracting, starting and ending units of time.
- **Date Formatting:** Converting Date objects to strings in various human-readable or standardized formats.
- **Locale Support:** Handling of different languages, calendars, and formatting conventions.
- **Relative Time:** Displaying time differences in natural language (e.g., "3 minutes ago").

Moment.js is widely used in web and server-side applications to handle complex date-time logic reliably.

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

### Browser Usage

Include Moment.js via CDN in your HTML:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.4/moment.min.js"></script>
```

---

## Usage and Examples

### Creating Moment Objects

```js
// Current date and time
const now = moment();

// Parsing from string
const birthday = moment("1990-12-25");

// Parsing with specific format
const custom = moment("12-25-1990", "MM-DD-YYYY");

// From Unix timestamp (seconds)
const timestamp = moment.unix(1609459200);
```

### Formatting Dates

```js
console.log(now.format("YYYY-MM-DD"));      // 2024-06-01
console.log(now.format("dddd, MMMM Do"));   // Saturday, June 1st
```

### Manipulating Dates

```js
const nextWeek = now.add(7, 'days');
const lastMonth = now.subtract(1, 'months');

// Start or end of time unit
const startOfYear = now.startOf('year');
const endOfDay = now.endOf('day');
```

### Calculating Differences and Durations

```js
const past = moment("2024-01-01");
const diffDays = now.diff(past, 'days');    // Number of days difference

const duration = moment.duration(2, 'hours');
console.log(duration.humanize());           // "2 hours"
```

### Relative Time

```js
console.log(moment().startOf('day').fromNow());   // e.g. "5 hours ago"
console.log(moment("2025-01-01").fromNow());      // e.g. "in 6 months"
```

### Locale and Timezone

```js
moment.locale('fr');
console.log(moment().format('LLLL'));  // French localized format

// Timezone support is available via moment-timezone add-on
```

---

## API Reference

### Main Functions and Methods

#### `moment([input], [format], [strict], [locale])`

Creates a Moment object representing a date/time.

- **Parameters:**
  - `input` (string | number | Date | Moment): Date/time value to parse. Optional, defaults to current time.
  - `format` (string | string[]): Parsing format(s) to interpret input string.
  - `strict` (boolean): Enable strict parsing (optional).
  - `locale` (string): Locale to use for this moment instance.

- **Returns:** Moment object.

---

#### Instance Methods

- `format(String) → String`  
Formats the moment to a string using tokens, e.g., `"YYYY-MM-DD"`, `"dddd, MMMM Do"`.

- `add(Number, String) → Moment`  
Adds time to the moment (e.g., `add(7, 'days')`).

- `subtract(Number, String) → Moment`  
Subtracts time from the moment.

- `startOf(String) → Moment`  
Sets to the start of a unit of time (e.g., `"year"`, `"month"`, `"day"`).

- `endOf(String) → Moment`  
Sets to the end of a unit of time.

- `diff(Moment | String | Number, String, Boolean) → Number`  
Calculates difference between moments in given units.

- `from(Moment | String | Number, Boolean) → String`  
Returns relative time from another moment or date.

- `fromNow(Boolean) → String`  
Returns relative time from now.

- `locale(String) → Moment`  
Sets or gets the locale.

---

#### Static Methods

- `moment.utc([input], [format], [strict])`  
Creates a moment in Coordinated Universal Time (UTC).

- `moment.unix(Number)`  
Create moment from Unix timestamp in seconds.

- `moment.duration(Number | Object, String)`  
Creates a duration object representing a length of time.

---

## Contributing

Moment.js is open-source and welcomes contributions to fix bugs, improve performance, or add features.

### How to contribute

1. Fork the repository on GitHub.
2. Create a new branch for your work.
3. Write clear, tested code.
4. Submit a pull request with detailed description.
5. Participate in code review and discussions.

Refer to the [CONTRIBUTING.md](https://github.com/moment/moment/blob/develop/CONTRIBUTING.md) in the repository for more details.

---

## License

Moment.js is licensed under the MIT License. See the [LICENSE](https://github.com/moment/moment/blob/develop/LICENSE) file for details.

---

## Contact

- Project repository: [https://github.com/moment/moment](https://github.com/moment/moment)
- Website: [https://momentjs.com/](https://momentjs.com/)
- Issue tracker: [https://github.com/moment/moment/issues](https://github.com/moment/moment/issues)

