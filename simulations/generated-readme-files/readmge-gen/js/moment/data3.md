# Moment.js

## Overview

Moment.js is a popular JavaScript library designed to parse, validate, manipulate, and display dates and times in JavaScript in a simple and consistent way. It abstracts the complex handling of date/time, providing an easy-to-use API that works across different browsers and environments.

### Main Domain Concepts

- **Date and Time Manipulation:** Work with JavaScript dates easily including addition, subtraction, and comparison.
- **Parsing and Formatting:** Parse dates from strings and format dates to readable strings in many locales.
- **Time Zones and UTC:** Support for UTC mode and localized time zones.
- **Relative Time:** Express time differences like "3 hours ago" or "in 2 days."
- **Localization (i18n):** Moment.js supports multiple languages and regional settings.
- **Durations:** Represent time spans independent of date/time.
- **Validation:** Check if dates are valid or invalid.

Moment.js helps developers accurately and consistently handle any date/time related operations, greatly easing cross-browser inconsistencies and complexity of native Date API.

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

### Using CDN

Include via CDN for browser usage:

```html
<script src="https://cdn.jsdelivr.net/npm/moment@2.29.4/min/moment.min.js"></script>
```

---

## Usage and Examples

### Creating a Moment Object

```js
const moment = require("moment");

// Create moment with current date/time
const now = moment();
console.log(now.format()); // Outputs current date/time in ISO 8601 format

// Create from a date string
const birthday = moment("1990-12-25");
console.log(birthday.format("MMMM Do, YYYY")); // December 25th, 1990
```

### Parsing Different Formats

```js
// Parsing custom formatted strings
const date = moment("12-25-1990", "MM-DD-YYYY");
console.log(date.format("YYYY-MM-DD")); // 1990-12-25
```

### Manipulating Dates

```js
const tomorrow = moment().add(1, "days");
console.log(tomorrow.format("YYYY-MM-DD")); // Tomorrow's date

const nextMonth = moment().add(1, "months");
console.log(nextMonth.format("YYYY-MM-DD"));

const twoHoursAgo = moment().subtract(2, "hours");
console.log(twoHoursAgo.format("HH:mm"));
```

### Displaying Relative Time

```js
const event = moment().add(3, "days");
console.log(event.fromNow()); // in 3 days

const pastEvent = moment().subtract(5, "minutes");
console.log(pastEvent.fromNow()); // 5 minutes ago
```

### Working with UTC and Timezones

```js
const utcMoment = moment.utc();
console.log(utcMoment.format()); // UTC date/time in ISO format

const localMoment = utcMoment.local();
console.log(localMoment.format()); // Converts to local timezone
```

### Validating Dates

```js
const validDate = moment("2023-02-28", "YYYY-MM-DD", true);
console.log(validDate.isValid()); // true

const invalidDate = moment("2023-02-30", "YYYY-MM-DD", true);
console.log(invalidDate.isValid()); // false
```

### Durations and Time Spans

```js
const duration = moment.duration(2, "hours");
console.log(duration.asMinutes()); // 120

const diff = moment("2023-12-25").diff(moment("2023-12-24"), "hours");
console.log(diff); // 24
```

---

## API Reference

### Creating Moments

- `moment()`  
  Creates a moment object representing the current date and time.

- `moment(String, String)`  
  Parses a date string with a specified format.

- `moment.utc()`  
  Creates a moment object in UTC mode.

### Formatting

- `.format([String])`  
  Formats the moment object to a string. If no format is specified, ISO 8601 string is returned.

### Parsing

- `moment(String)`  
  Parses a date string in ISO8601 or recognized RFC2822 date formats.

- `moment(String, String[, Boolean])`  
  Parses a date string with a custom format string. Optional strict parsing with boolean.

### Manipulation

- `.add(Number, String)`  
  Adds time to the moment object. Units include `'years', 'months', 'weeks', 'days', 'hours', 'minutes', 'seconds', 'milliseconds'`.

- `.subtract(Number, String)`  
  Subtracts time from the moment object (same units as add).

### Query & Validation

- `.isValid()`  
  Returns boolean whether the moment is a valid date.

- `.isBefore(Moment|String[, String])`  
  Checks if moment is before another moment or date.

- `.isAfter(Moment|String[, String])`  
  Checks if moment is after another moment or date.

### Relative Time

- `.fromNow(Boolean)`  
  Returns string representing relative time from now. Passing `true` omits suffix.

- `.toNow(Boolean)`  
  Returns string representing time to now.

- `.from(Moment|String[, Boolean])`  
  Returns relative time from another moment.

### Duration

- `moment.duration(Number|String|Object, String)`  
  Creates duration object.

- `.asMinutes()`, `.asHours()`, `.asSeconds()`, etc.  
  Returns duration expressed in requested units.

### Timezone & UTC

- `.utc()`  
  Converts moment to UTC mode.

- `.local()`  
  Converts moment from UTC back to local time.

---

## License

Moment.js is released under the MIT License. See the [LICENSE](https://github.com/moment/moment/blob/develop/LICENSE) file for details.
