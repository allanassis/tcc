# lil-uri

## Overview

`lil-uri` is a lightweight and efficient JavaScript library designed to parse, manipulate, and serialize URIs (Uniform Resource Identifiers). It provides an intuitive API to handle all components of a URI such as scheme, authority, path, query, and fragment while following the specifications outlined in RFC 3986. The library is minimalistic yet powerful, aiming to offer developers a fast and easy way to work with URIs in browser and Node.js environments.

### Domain Concepts

- **URI Components:** The distinct parts of a URI, including scheme, host, port, path, query parameters, and fragment.
- **Parsing and Serialization:** Transforming URI strings into accessible objects and converting those objects back into valid URI strings.
- **Query Parameters Handling:** Manipulating URI query parameters in a straightforward and flexible manner.
- **Immutability and Mutability:** Allowing creation of URI instances with chainable methods to modify parts without affecting the original.

---

## Installation

### Via npm

```bash
npm install lil-uri
```

This works for Node.js and frontend projects using bundlers like Webpack or Rollup.

### Via yarn

```bash
yarn add lil-uri
```

---

## Usage and Examples

### Basic URI Parsing

```js
import URI from "lil-uri";

const uri = new URI(
  "https://user:pass@example.com:8080/path/to/resource?foo=bar&baz=qux#fragment",
);

console.log(uri.scheme); // 'https'
console.log(uri.authority); // 'user:pass@example.com:8080'
console.log(uri.host); // 'example.com'
console.log(uri.port); // 8080
console.log(uri.path); // '/path/to/resource'
console.log(uri.query.toString()); // 'foo=bar&baz=qux'
console.log(uri.fragment); // 'fragment'
```

### Modifying URI Components

All setters return a new instance leaving the original URI unchanged.

```js
const uri = new URI("https://example.com");

const updatedUri = uri
  .withPath("/new/path")
  .withQuery({ foo: "bar" })
  .withFragment("section1");

console.log(updatedUri.toString());
// Output: 'https://example.com/new/path?foo=bar#section1'
```

### Working with Query Parameters

You can manipulate query parameters easily:

```js
let uri = new URI("https://example.com?foo=1&bar=2");

uri = uri.withQuery(uri.query.set("bar", "3").set("baz", "4"));

console.log(uri.toString());
// 'https://example.com?foo=1&bar=3&baz=4'
```

### Serialization

Convert the URI object back to a string:

```js
const uri = new URI("https://example.com/path?q=1#frag");
console.log(uri.toString()); // 'https://example.com/path?q=1#frag'
```

---

## API Reference

### `new URI(uriString)`

Creates a new URI instance by parsing the given URI string.

- **Parameters:**
  - `uriString` (string): The URI string to parse.
- **Returns:** A URI object representing the parsed URI.

---

### Properties of URI instance

- `scheme` (string): The URI scheme (e.g., `http`, `https`).
- `authority` (string): The authority component, including user info, host, and port.
- `userInfo` (string|null): User credentials (`user:pass`), if present.
- `host` (string): Hostname or IP address.
- `port` (number|null): The port number, if specified.
- `path` (string): The path component of the URI.
- `query` (QueryObject): An object to access and manipulate query parameters.
- `fragment` (string|null): The fragment identifier after the `#`.

---

### Methods of URI instance

- `toString()`: Returns the full URI string.
- `withScheme(scheme)`: Returns a new URI with the scheme replaced.
- `withAuthority(authority)`: Returns a new URI with the authority replaced.
- `withUserInfo(userInfo)`: Returns a new URI with the user info replaced.
- `withHost(host)`: Returns a new URI with the host replaced.
- `withPort(port)`: Returns a new URI with the port replaced.
- `withPath(path)`: Returns a new URI with the path replaced.
- `withQuery(query)`: Returns a new URI with the query replaced. `query` can be a string, an object, or a QueryObject.
- `withFragment(fragment)`: Returns a new URI with the fragment replaced.

---

### QueryObject API

The `query` property is an instance of a query parameters handler supporting:

- `get(param)`: Gets the value of a query parameter.
- `set(param, value)`: Sets a query parameter and returns a new QueryObject.
- `delete(param)`: Deletes a query parameter and returns a new QueryObject.
- `has(param)`: Returns `true` if the parameter exists.
- `toString()`: Serializes the query parameters to a URI encoded string.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Submit pull requests with clear descriptions.
4. Write tests for new features or bug fixes.
5. Follow the existing code style.

Please report issues and suggest features via the GitHub repository's Issues tab.

---

## License

`lil-uri` is licensed under the MIT License. See the LICENSE file in the repository for details.

---

## Contact

- GitHub: [https://github.com/lil-js/uri](https://github.com/lil-js/uri)
- Issues: Use the GitHub Issues page for bug reports and feature requests.
