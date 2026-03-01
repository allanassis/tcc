# Moment.js

## Overview

Moment.js is a popular JavaScript library designed to parse, validate, manipulate, and display dates and times in JavaScript in a straightforward and consistent way. It provides an elegant and comprehensive API to work with date and time values beyond the built-in capabilities of JavaScript, making date/time handling easier and more reliable across different browsers and time zones.

### Domain Concepts

- **Moment Object:** The core date/time object provided by Moment.js which represents a point in time.
- **Parsing:** Converting strings, arrays, or other date formats into moment objects.
- **Formatting:** Converting moment objects into customized string representations.
- **Manipulation:** Changing parts of a date/time such as adding or subtracting days, months, years, etc.
- **Time Zones and UTC:** Supporting UTC and local time manipulations and conversions.
- **Relative Time:** Displaying date/time differences in a human-readable relative format (e.g., "3 days ago").
- **Localization:** Support for many locales and languages with localized formatting and date/time terms.

---

## Installation

Moment.js can be installed via npm, yarn, or used directly in the browser.

### Using npm

```bash
npm install moment
```

### Using Yarn

```bash
yarn add moment
```

### Using a CDN (Browser)

Add this script tag to your HTML:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.4/moment.min.js"></script>
```

---

## Usage and Examples

### Creating Moment Objects

You can create a moment object representing the current date and time:

```js
const moment = require("moment");
const now = moment();
console.log(now.toString());
```

Or parse a specific date string:

```js
const date = moment("2024-06-13");
console.log(date.format("YYYY-MM-DD"));
```

### Formatting Dates

Format a moment object into a readable string:

```js
const now = moment();
console.log(now.format("MMMM Do YYYY, h:mm:ss a")); // e.g. June 13th 2024, 3:45:12 pm
```

Common format tokens:

- `YYYY` - 4 digit year
- `MM` - 2 digit month
- `DD` - 2 digit day of month
- `HH` - 2 digit hour (24h clock)
- `hh` - 2 digit hour (12h clock)
- `mm` - minutes
- `ss` - seconds
- `a` - am/pm

### Manipulating Dates

Add or subtract time units:

```js
const today = moment();
const nextWeek = today.add(7, "days");
console.log(nextWeek.format("YYYY-MM-DD"));
```

Subtract 3 months:

```js
const past = moment().subtract(3, "months");
console.log(past.format());
```

### Displaying Relative Time

Output relative time from now:

```js
console.log(moment("2023-06-01").fromNow()); // e.g. "a year ago"
```

### Working with UTC

Create and display UTC moment:

```js
const utcMoment = moment.utc();
console.log(utcMoment.format());
```

Convert local to UTC and vice versa:

```js
const local = moment();
const utc = local.utc();
console.log(utc.format());
```

---

## API Reference

### moment(input, format, strict)

Create a moment object.

- `input` (string|Date|Array|number): Input date/time to parse.
- `format` (string|array, optional): Format of the input string.
- `strict` (boolean, optional): Whether to use strict parsing.

Returns: Moment object.

### moment().format(formatString)

Formats the moment object into a string.

- `formatString` (string, optional): Defines output format.

Returns: Formatted string.

### moment().add(value, unit)

Adds time to the moment object.

- `value` (number): Quantity to add.
- `unit` (string): Time unit. Examples: `"days"`, `"months"`, `"years"`, `"hours"`.

Returns: Moment object (modified).

### moment().subtract(value, unit)

Subtracts time from the moment object.

- `value` (number): Quantity to subtract.
- `unit` (string): Time unit.

Returns: Moment object (modified).

### moment().diff(moment, unit, float)

Get difference between two moments.

- `moment` (Moment): Moment object to compare.
- `unit` (string, optional): Unit of measurement. Defaults to milliseconds.
- `float` (boolean, optional): Return float instead of integer.

Returns: Number representing the difference.

### moment().fromNow(withoutSuffix)

Relative time from now.

- `withoutSuffix` (boolean, optional): Omit suffix (e.g., "ago").

Returns: String representation.

### moment.utc(input)

Creates a moment in UTC mode.

- `input` (optional): Date/time input.

Returns: Moment object in UTC.

### moment.locale(localeName, [values])

Get or set the current locale.

- `localeName` (string): Locale identifier, e.g., `"en"`, `"fr"`.
- `values` (object, optional): Custom locale configuration.

Returns: Locale object or Moment.

---

## Contributing

Moment.js welcomes community contributions to improve the library, fix bugs, and extend functionality.

To contribute:

1. Fork the [Moment.js GitHub repository](https://github.com/moment/moment).
2. Create a branch for your feature or bugfix.
3. Write tests for any new functionality.
4. Submit a pull request with detailed description of changes.

Please follow the coding style and maintain compatibility with existing API.

---

## License

Moment.js is released under the MIT License. See the [LICENSE](https://github.com/moment/moment/blob/develop/LICENSE) file for details.

---

## Contact

- **GitHub Repository:** [https://github.com/moment/moment](https://github.com/moment/moment)
- **Website:** [https://momentjs.com/](https://momentjs.com/)
- **Issues & Support:** Use the GitHub Issues tab to report bugs or request features.
