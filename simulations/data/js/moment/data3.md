# Moment.js

## Overview

Moment.js is a popular JavaScript library for parsing, validating, manipulating, and formatting dates and times in a simple and consistent way. It abstracts complex date operations and offers an easy-to-use API for working with dates across different locales, time zones, and formats, making date and time handling more reliable and less error-prone in JavaScript applications.

### Domain Concepts

- **Date and Time Representation:** Moment.js models points in time as Moment objects, encapsulating year, month, day, hour, minute, second, and millisecond components.
- **Parsing and Formatting:** Supports converting strings in various formats into Moment objects and formatting Moment objects back to strings.
- **Manipulation:** Allows adding or subtracting time units or setting date parts.
- **Validation:** Detects invalid dates or parsing errors.
- **Localization:** Handles date and time display according to locale-specific norms.
- **Timezone Support:** Converts and displays moments in different time zones.
- **Duration and Relative Time:** Supports representing time durations and human-friendly relative time strings.

---

## Installation

### Using npm

```bash
npm install moment
```

### Using yarn

```bash
yarn add moment
```

### Using CDN (for browser)

Include via script tag:

```html
<script src="https://cdn.jsdelivr.net/npm/moment@2.29.4/moment.min.js"></script>
```

### Importing in Code

```js
// ES6 import
import moment from "moment";

// CommonJS require
const moment = require("moment");
```

---

## Usage and Examples

### Creating Moment Objects

```js
// Current date and time
const now = moment();

// From a date string (ISO 8601, RFC 2822, or custom formats)
const birthday = moment("1990-05-15");
const fromFormat = moment("12-25-1995", "MM-DD-YYYY");

// From JavaScript Date
const dateObj = moment(new Date(2020, 11, 25));
```

### Formatting Dates

```js
console.log(now.format("YYYY-MM-DD")); // e.g., "2024-06-15"
console.log(now.format("dddd, MMMM Do")); // e.g., "Saturday, June 15th"
console.log(now.toISOString()); // ISO 8601 string
```

### Manipulating Dates

```js
const nextWeek = moment().add(7, "days");
const lastMonth = moment().subtract(1, "months");

// Set specific components
const birthday2024 = moment().year(2024).month(4).date(15);
```

### Comparison and Querying

```js
const date1 = moment("2024-06-01");
const date2 = moment("2024-06-15");

console.log(date1.isBefore(date2)); // true
console.log(date1.isSame(date2)); // false
console.log(date1.isAfter(date2)); // false
```

### Durations and Differences

```js
const start = moment("2024-01-01");
const end = moment("2024-06-15");
const duration = moment.duration(end.diff(start));

console.log(duration.asDays()); // Total days between start and end
console.log(duration.months()); // Months component
console.log(duration.days()); // Days component
```

### Relative Time (Humanized)

```js
console.log(moment().startOf("day").fromNow()); // "18 hours ago"
console.log(moment().add(3, "days").fromNow()); // "in 3 days"
```

### Localization

```js
moment.locale("fr");
console.log(moment().format("LLLL")); // French localized full date and time

moment.locale("en"); // Reset to English
```

---

## API Reference

### `moment(input, format, strict, locale)`

Creates a Moment instance.

- `input` (optional): Date or string to parse.
- `format` (optional): Format string to parse input.
- `strict` (optional): Boolean for strict parsing.
- `locale` (optional): Locale to use.

Returns a Moment object.

---

### Moment Instance Methods

- `.format(string)`: Formats moment into string using tokens.
- `.add(number, string)`: Adds time units, e.g. 'days', 'months'.
- `.subtract(number, string)`: Subtracts time units.
- `.diff(moment, string, Boolean)`: Difference between moments, optionally as float.
- `.startOf(string)`: Sets moment to start of unit (e.g., 'day', 'month').
- `.endOf(string)`: Sets moment to end of unit.
- `.isValid()`: Checks if the moment is valid.
- `.clone()`: Clones the moment instance.
- `.locale(string)`: Sets the locale.
- `.fromNow(Boolean)`: Returns humanized relative time.
- `.toISOString()`: Returns ISO 8601 string representation.
- `.toDate()`: Returns native JavaScript Date object.

---

### Static Methods

- `moment.utc()`: Creates a UTC moment.
- `moment.duration()`: Creates a duration object representing time span.
- `moment.locale()`: Gets or sets global locale.
- `moment.invalid()`: Returns an invalid moment.

---

## Contributing

Moment.js is open source and welcomes contributions. To contribute:

1. Fork the repo [https://github.com/moment/moment](https://github.com/moment/moment).
2. Create a feature branch.
3. Follow the [Coding Style Guide](https://momentjs.com/docs/#/functions/).
4. Write tests for new features or bug fixes.
5. Submit a pull request with clear description.

Refer to the project's CONTRIBUTING.md for detailed guidelines.

---

## License

Moment.js is licensed under the [MIT License](https://github.com/moment/moment/blob/develop/LICENSE).

---

## Contact

- Official repository: [https://github.com/moment/moment](https://github.com/moment/moment)
- Website: [https://momentjs.com](https://momentjs.com)
- Issue tracker: [GitHub Issues](https://github.com/moment/moment/issues)
