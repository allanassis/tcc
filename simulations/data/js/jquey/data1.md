# jQuery

## Overview

jQuery is a fast, small, and feature-rich JavaScript library designed to simplify HTML DOM tree traversal and manipulation, event handling, animation, and Ajax interactions for rapid web development. It abstracts many of the complexities of working directly with DOM and cross-browser inconsistencies, providing a clean and easy-to-use API that works across a multitude of browsers.

### Key Domain Concepts

- **DOM Manipulation:** Select, traverse, and modify elements within the HTML document.
- **Event Handling:** Simplify attaching event handlers, event delegation, and custom events.
- **Ajax:** Simplify asynchronous HTTP requests and response handling.
- **Effects and Animation:** Built-in methods for creating UI animations and effects.
- **Utilities:** Helper functions for tasks like iteration, type checking, and data manipulation.
- **Deferreds and Promises:** Manage asynchronous operations with clean callback management.

---

## Installation

You can include jQuery in your project using one of the methods below:

### Via CDN (recommended for quick use)

Add this line in your HTML's `<head>` or just before the closing `</body>` tag:

```html
<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
```

### Via npm

```bash
npm install jquery
```

Then in your JavaScript code:

```js
import $ from "jquery";
```

### Download and host locally

Download from the official website: [https://jquery.com/download/](https://jquery.com/download/)

---

## Usage and Examples

### Selecting Elements

```js
// Select all paragraphs
$("p").css("color", "blue"); // Changes text color to blue
```

### Event Handling

```js
// Attach click event to buttons
$("button").on("click", function () {
  alert("Button clicked!");
});
```

### DOM Manipulation

```js
// Add a class to selected divs
$("div.container").addClass("active");

// Append new content
$("ul#menu").append("<li>New Item</li>");
```

### Ajax Request

```js
$.ajax({
  url: "/api/data",
  method: "GET",
  dataType: "json",
})
  .done(function (data) {
    console.log("Data retrieved:", data);
  })
  .fail(function (jqXHR, textStatus) {
    console.error("Request failed:", textStatus);
  });
```

### Animations

```js
// Fade out an element over 500ms
$("#box").fadeOut(500);
```

---

## API Reference

### Core Selector Function: `$(selector, [context])`

- **Purpose:** Selects DOM elements matching the CSS selector.
- **Parameters:**
  - `selector` (string | HTMLElement | function): A CSS selector, DOM element, or function executed on document ready.
  - `context` (optional, Element | Document): Context within which to search for the selector.
- **Returns:** jQuery object wrapping the matching elements.

### Commonly Used Methods on jQuery Objects

- `.addClass(className)`: Adds one or more classes to each element.
- `.removeClass(className)`: Removes one or more classes from each element.
- `.css(propertyName, value)`: Gets or sets CSS properties.
- `.on(eventType, handler)`: Attaches event handlers.
- `.off(eventType, handler)`: Removes event handlers.
- `.html([htmlString])`: Gets or sets inner HTML.
- `.text([textString])`: Gets or sets text content.
- `.append(content)`: Inserts content at the end of each selected element.
- `.prepend(content)`: Inserts content at the beginning.
- `.attr(attributeName, value)`: Gets or sets attributes.
- `.remove()`: Removes elements from the DOM.
- `.fadeIn(duration, callback)`: Displays element with fade-in effect.
- `.fadeOut(duration, callback)`: Hides element with fade-out effect.

### Ajax Methods and Utilities

- `$.ajax(settings)`: Perform an asynchronous HTTP request.
- `$.get(url, data, success, dataType)`: Shortcut for GET requests.
- `$.post(url, data, success, dataType)`: Shortcut for POST requests.
- `$.getJSON(url, data, success)`: GET request that expects JSON.

### Utility Functions

- `$.each(collection, callback)`: Iterate over arrays or objects.
- `$.extend(target, object1, [objectN])`: Merge contents of objects into first object.
- `$.isFunction(obj)`: Check if object is a function.
- `$.Deferred()`: Creates a deferred object for managing asynchronous callbacks.
- `$.data(element, key, value)`: Store arbitrary data associated with an element.

### Document Ready

```js
$(function () {
  // code here is executed when the DOM is fully loaded
});
```

---

## Contributing

jQuery is open source and welcomes contributions from the community.

### How to contribute

1. Fork the repository on GitHub: [https://github.com/jquery/jquery](https://github.com/jquery/jquery)
2. Clone your fork and create a feature branch.
3. Make your changes and ensure all tests pass.
4. Write clear, descriptive commit messages.
5. Submit a pull request with detailed description of your changes.

### Development Setup

- Clone repository locally.
- Run `npm install` to install dependencies.
- Use `npm test` to run the test suite.
- Follow the [coding guidelines](https://contribute.jquery.org/code-reviews/) for consistent style.

---

## License

jQuery is released under the MIT License. See the [LICENSE.txt](https://github.com/jquery/jquery/blob/main/LICENSE.txt) file for details.

---

## Contact

- Official Website: [https://jquery.com](https://jquery.com)
- GitHub Repository: [https://github.com/jquery/jquery](https://github.com/jquery/jquery)
- Mailing List and Community: [https://jquery.com/community/](https://jquery.com/community/)
