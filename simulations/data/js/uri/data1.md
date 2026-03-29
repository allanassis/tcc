# lil-js/uri

## Overview

`lil-js/uri` is a minimalist JavaScript URI (Uniform Resource Identifier) library designed to parse, manipulate, and serialize URIs with a small, efficient footprint. This library provides essential domain concepts of the URI specification (RFC 3986) such as scheme, authority, path, query, and fragment, enabling developers to easily work with URIs by abstracting their complex components.

### Domain Concepts

- **URI Structure**: Components of a URI including scheme (protocol), authority (user info, host, port), path, query, and fragment.
- **Parsing**: Breaking down raw URI strings into structured, accessible components.
- **Serialization**: Composing URI components back into valid URI strings.
- **Query Parameter Manipulation**: Adding, updating, and removing query parameters in a URI.
- **Normalization**: Adjusting URI parts according to standard rules for consistency.

The library helps bridge the complexity of handling URIs in web and network applications, focusing on simplicity and correctness.

---

## Installation

You can install the `uri` package using npm or yarn:

```bash
npm install @lil-js/uri
```

or

```bash
yarn add @lil-js/uri
```

The package works in both Node.js and browser environments.

---

## Usage and Examples

### Basic Usage: Parsing a URI

```js
import URI from "@lil-js/uri";

const uri = new URI(
  "https://user:pass@example.com:8080/path/to/resource?foo=bar&baz=qux#section2",
);

console.log(uri.scheme); // 'https'
console.log(uri.userinfo); // 'user:pass'
console.log(uri.host); // 'example.com'
console.log(uri.port); // '8080'
console.log(uri.path); // '/path/to/resource'
console.log(uri.query); // 'foo=bar&baz=qux'
console.log(uri.fragment); // 'section2'
```

### Manipulating Query Parameters

```js
const uri = new URI("https://example.com/path?foo=bar");

uri.addQuery("baz", "qux");
console.log(uri.query); // 'foo=bar&baz=qux'

uri.setQuery("foo", "newvalue");
console.log(uri.query); // 'foo=newvalue&baz=qux'

uri.removeQuery("baz");
console.log(uri.query); // 'foo=newvalue'
```

### Serializing URI Back to String

```js
const uri = new URI("http://example.com");
uri.path = "/newpath";
uri.fragment = "top";

console.log(uri.toString()); // 'http://example.com/newpath#top'
```

### Normalizing a URI

```js
const uri = new URI("HTTP://Example.Com:80/%7Euser");
uri.normalize();

console.log(uri.toString()); // 'http://example.com/~user'
```

---

## API Reference

### `URI` class

The central class for parsing, manipulating, and serializing URIs.

#### Constructor

`new URI(uriString: string)`

- Parses the input URI string and initializes component properties.

#### Properties

- `scheme` (string): The protocol scheme (e.g., 'http', 'https').
- `userinfo` (string): User information (e.g., 'user:pass').
- `host` (string): Hostname or IP address.
- `port` (string): Port number as a string.
- `path` (string): Path component of the URI.
- `query` (string): Raw query string (key-value pairs as a string).
- `fragment` (string): Fragment identifier (after '#').

#### Methods

- `addQuery(key: string, value: string): void`

  Adds a new query parameter without affecting existing parameters with the same key.

- `setQuery(key: string, value: string): void`

  Sets or updates the value of the specified query parameter.

- `removeQuery(key: string): void`

  Removes all occurrences of the specified query parameter.

- `normalize(): void`

  Normalizes the URI components to conform with standard URI rules (e.g., lowercasing scheme and host, decoding percent-encoded unreserved characters).

- `toString(): string`

  Serializes the URI components back into a valid URI string.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/lil-js/uri/blob/main/LICENSE) file for details.
