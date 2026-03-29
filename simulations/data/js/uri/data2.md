# lil-uri

## Overview

`lil-uri` is a minimalistic and efficient JavaScript library focused on parsing and manipulating URI (Uniform Resource Identifier) strings. It models the domain concepts of URIs as defined by RFC 3986, including components such as scheme, authority, path, query, and fragment. The library provides lightweight tools to decompose, modify, and recompose URIs, enabling developers to work with URLs and URIs conveniently in web or server-side JavaScript environments.

### Domain Concepts

- **URI Components:** The basic parts of a URI including scheme (protocol), host, port, path, query parameters, and fragment.
- **Parsing:** Transforming a URI string into an object representation for programmatic access.
- **Serialization:** Converting the URI object back into a valid URI string.
- **Manipulation:** Modifying individual parts of the URI such as changing the query parameters or path.
- **Normalization:** Handling encoding and decoding of URI components to ensure compliance and interoperability.

---

## Installation

You can install `lil-uri` via npm:

```bash
npm install lil-uri
```

Alternatively, use yarn:

```bash
yarn add lil-uri
```

The library is designed for usage in Node.js or browser environments supporting ES modules.

---

## Usage and Examples

### Basic Parsing and Serialization

```js
import uri from "lil-uri";

const url =
  "https://user:pass@example.com:8080/path/to/file?search=foo#section1";

// Parse the URI string into an object
const parsed = uri(url);

console.log(parsed);
// Output:
// {
//   scheme: 'https',
//   userinfo: 'user:pass',
//   host: 'example.com',
//   port: '8080',
//   path: '/path/to/file',
//   search: 'search=foo',
//   hash: 'section1'
// }

// Modify components
parsed.path = "/new/path";
parsed.search = "search=bar";

// Serialize back to string
const newUrl = parsed.toString();
console.log(newUrl);
// Output: https://user:pass@example.com:8080/new/path?search=bar#section1
```

### Accessing Query Parameters

```js
import uri from "lil-uri";

const url = "https://example.com/page?foo=1&bar=2";
const u = uri(url);

// Get the value of 'foo'
const fooValue = u.query.get("foo"); // '1'

// Set a new query parameter
u.query.set("baz", "3");

// Convert to string
console.log(u.toString());
// Output: https://example.com/page?foo=1&bar=2&baz=3
```

### Creating a URI from Components

```js
import uri from "lil-uri";

const u = uri();

u.scheme = "http";
u.host = "example.org";
u.path = "/index.html";
u.query.set("id", "123");

console.log(u.toString());
// Output: http://example.org/index.html?id=123
```

---

## API Reference

### `uri(input?: string | URI): URI`

- **Purpose:** Parses a URI string into a URI object or clones an existing URI object. If no argument is provided, returns an empty URI.
- **Parameters:**
  - `input` (optional): A URI string to parse or a URI object to clone.
- **Returns:** A `URI` object representing the parsed URI components.

---

### URI Object Properties

- `scheme` (string): The URI scheme or protocol (e.g., `'http'`, `'https'`).
- `userinfo` (string | undefined): User information (e.g., `'user:pass'`).
- `host` (string | undefined): The hostname or IP address.
- `port` (string | undefined): The network port as a string.
- `path` (string): The path component (e.g., `'/path/to/resource'`).
- `search` (string): The query string portion including key-value pairs.
- `hash` (string): The fragment identifier after `#`.

---

### URI Object Methods

- `toString(): string`

  Serializes the URI object back into a URI string that can be used in browsers or HTTP requests.

- `query` (Map-like interface)

  An object implementing Map-like methods to access and modify query parameters:
  - `get(key: string): string | undefined` — Retrieve the value of a query parameter.
  - `set(key: string, value: string): void` — Set the value for a query parameter.
  - `delete(key: string): void` — Remove a query parameter.
  - `has(key: string): boolean` — Check if a query parameter exists.
  - `keys(): IterableIterator<string>` — Iterate over query parameter keys.
  - `values(): IterableIterator<string>` — Iterate over query parameter values.
  - `entries(): IterableIterator<[string, string]>` — Iterate over key-value pairs.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/lil-js/uri/blob/main/LICENSE) file for details.
