# lil-uri

## Overview

`lil-uri` is a minimalist and fast JavaScript library for parsing, manipulating, and formatting URIs (Uniform Resource Identifiers) in compliance with the URL standard. It focuses on providing a lightweight implementation that easily integrates into projects requiring URI manipulation without the overhead of larger libraries.

### Domain Concepts

- **URI Components:** The tool models the fundamental parts of a URI including scheme, hostname, port, pathname, search parameters (query), and fragment.
- **URL Parsing:** The extraction and representation of these components from a URI string.
- **URI Manipulation:** The ability to modify these components individually and serialize them back into a complete URI string.
- **Standards Compliance:** Behavior aligned with the WHATWG URL Standard, making it suitable for web-related applications.

The library aims to help developers handle URIs reliably, ensuring consistent parsing and formatting suitable for browsers, Node.js, or other JavaScript environments.

---

## Installation

To install `lil-uri` using npm, run:

```bash
npm install lil-uri
```

Or if you use yarn:

```bash
yarn add lil-uri
```

This package works in Node.js and modern browsers supporting ES modules.

---

## Usage and Examples

### Basic Usage

Import the `URI` class and create an instance by passing a URI string:

```js
import { URI } from "lil-uri";

const url = new URI("https://example.com:8080/path/to/page?name=test#info");

console.log(url.scheme); // "https"
console.log(url.hostname); // "example.com"
console.log(url.port); // "8080"
console.log(url.pathname); // "/path/to/page"
console.log(url.search); // "?name=test"
console.log(url.hash); // "#info"
```

### Manipulate URI Components

You can modify parts of the URI and serialize the result:

```js
url.pathname = "/new/path";
url.search = "?name=updated";
url.hash = "#details";

console.log(url.toString());
// Output: "https://example.com:8080/new/path?name=updated#details"
```

### Create a URI from Components

You can instantiate and build a URI using individual pieces:

```js
const anotherUrl = new URI();
anotherUrl.scheme = "http";
anotherUrl.hostname = "mysite.com";
anotherUrl.pathname = "/home";

console.log(anotherUrl.toString());
// Output: "http://mysite.com/home"
```

---

## API Reference

### `class URI`

The core class representing a parsed URI, allowing access and modification of its components.

#### Constructor

- `new URI(uriString?: string)`

Constructs a new `URI` instance. If a URI string is provided, it parses and populates the components. If omitted, starts with an empty URI.

#### Properties

- `scheme: string`  
  The URI scheme/protocol (e.g., `http`, `https`, `ftp`).

- `username: string`  
  The username portion of the authority, if any.

- `password: string`  
  The password portion of the authority, if any.

- `hostname: string`  
  The domain or IP address.

- `port: string`  
  The port number as a string (empty string if not specified).

- `pathname: string`  
  The path component (starting with `/`).

- `search: string`  
  The query string including leading `?` (empty string if none).

- `hash: string`  
  The fragment identifier including `#` (empty string if none).

#### Methods

- `toString(): string`

Returns the full URI string serialized from the current components.

- `toJSON(): string`

Returns the URI string, similar to `toString()`, useful for JSON serialization.

#### Example

```js
const uri = new URI("https://user:pass@example.com:8080/path?query=1#frag");
uri.password = "newpass";
console.log(uri.toString());
// "https://user:newpass@example.com:8080/path?query=1#frag"
```

---

## Contributing

Contributions to `lil-uri` are welcome! To contribute:

1. Fork the repository on GitHub.
2. Create a topic branch (`git checkout -b feature/your-feature`).
3. Make your changes with clear, concise commit messages.
4. Test your changes to ensure robustness.
5. Open a pull request against the `main` branch describing your changes.

Please follow the existing code style and include tests for new features or bug fixes.

---

## License

`lil-uri` is distributed under the MIT License. See the LICENSE file in the repository for details.

---

## Contact

- **Repository:** [https://github.com/lil-js/uri](https://github.com/lil-js/uri)
- **Issues and feature requests:** Use GitHub issues in the repository.
- **Author:** Maintained by the lil-js team.

For inquiries, please open issues or pull requests on GitHub.
