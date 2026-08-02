# lil-uri

## Overview

`lil-uri` is a minimalistic JavaScript library designed to provide a simple and efficient API for parsing, constructing, and manipulating URI (Uniform Resource Identifier) components. The library models core domain concepts surrounding URIs, including schemes, hosts, ports, paths, query parameters, fragments, and authentication. It offers utilities to decompose URIs into meaningful parts and reassemble them, facilitating easy handling of URIs in web development and networking tasks.

### Domain Concepts

- **URI Components:** The standardized parts of a URI according to RFC 3986, such as scheme, authority, path, query, and fragment.
- **Parsing:** Extracting individual components from URI strings.
- **Formatting:** Reconstructing URI strings from component parts.
- **Relative URI Resolution:** Combining base URIs with relative references.
- **Query Handling:** Parsing and serializing query parameters as key-value pairs.
- **Encoding & Decoding:** Properly encoding reserved characters to maintain URI validity.

`lil-uri` helps users by abstracting the complexity of URI syntax and provides a lightweight API to interact with the components programmatically.

---

## Installation

You can install `lil-uri` via npm:

```bash
npm install @lil-js/uri
```

The package supports modern JavaScript environments including Node.js and web browsers via bundlers.

---

## Usage and Examples

### Parsing a URI

```js
import { parse } from "@lil-js/uri";

const url = "https://user:pass@example.com:8080/path?query=123#hash";

const parsed = parse(url);

console.log(parsed);
/* Output:
{
  scheme: 'https',
  userinfo: 'user:pass',
  host: 'example.com',
  port: '8080',
  path: '/path',
  query: 'query=123',
  fragment: 'hash'
}
*/
```

### Formatting a URI

```js
import { format } from "@lil-js/uri";

const components = {
  scheme: "https",
  userinfo: "user:pass",
  host: "example.com",
  port: "8080",
  path: "/path",
  query: "query=123",
  fragment: "hash",
};

const uriString = format(components);
console.log(uriString);
// Output: "https://user:pass@example.com:8080/path?query=123#hash"
```

### Resolving a Relative URI

```js
import { resolve } from "@lil-js/uri";

const base = "https://example.com/dir/page.html";
const relative = "../image.png";

const resolved = resolve(base, relative);
console.log(resolved);
// Output: "https://example.com/image.png"
```

### Working with Query Parameters

```js
import { parseQuery, formatQuery } from "@lil-js/uri";

const queryString = "name=alice&age=30";

const queryObj = parseQuery(queryString);
console.log(queryObj);
// Output: { name: 'alice', age: '30' }

const newQuery = formatQuery({ search: "js", page: 1 });
console.log(newQuery);
// Output: "search=js&page=1"
```

---

## API Reference

### `parse(uri: string): UriComponents`

Parses a URI string into its component parts.

- **Parameters:**
  - `uri` (string): The URI string to parse.

- **Returns:** An object with the following properties (strings or undefined if not present):
  - `scheme` — The URI scheme, e.g., `"http"`.
  - `userinfo` — User information like username and password.
  - `host` — Domain or IP address.
  - `port` — Port number as a string.
  - `path` — The path component.
  - `query` — Raw query string after `?`.
  - `fragment` — The fragment identifier after `#`.

### `format(components: UriComponents): string`

Constructs a URI string from the given components.

- **Parameters:**
  - `components` (object): URI components, matching those from the `parse` output.

- **Returns:** URI string assembled from parts.

### `resolve(base: string, relative: string): string`

Resolves a relative URI against a base URI according to the standard URI resolution algorithm.

- **Parameters:**
  - `base` (string): The base URI.
  - `relative` (string): The relative URI to resolve against the base.

- **Returns:** An absolute URI string.

### `parseQuery(query: string): Record<string, string>`

Parses a query string into an object of key-value pairs.

- **Parameters:**
  - `query` (string): The raw query string (without leading `?`).

- **Returns:** An object mapping query parameter names to values.

### `formatQuery(params: Record<string, string>): string`

Serializes an object into a URL-encoded query string.

- **Parameters:**
  - `params` (object): Key-value pairs representing query parameters.

- **Returns:** URL-encoded query string.

---

## License

`lil-uri` is licensed under the MIT License. See the [LICENSE](https://github.com/lil-js/uri/blob/main/LICENSE) file for details.
