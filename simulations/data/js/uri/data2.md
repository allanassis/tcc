# uri

## Overview

The `uri` package is a compact and efficient JavaScript library designed for parsing, manipulating, and formatting URIs (Uniform Resource Identifiers). It provides developers with tools to easily handle web addresses by breaking them down into their constituent parts such as scheme, host, path, query parameters, and fragment identifiers.

### Domain Concepts

- **URI (Uniform Resource Identifier):** A string of characters used to identify a resource on the internet, commonly known as URLs but more general.
- **Parsing:** Breaking down a URI string into meaningful components such as scheme, authority, path, query, and fragment.
- **Formatting:** Constructing a URI string back from its components.
- **Query Parameter Handling:** Reading and modifying key-value pairs passed as part of the URI after the `?`.

Understanding these domain concepts is essential to effectively manipulate URIs within web applications, API clients, or any context where resource addressing and navigation are involved.

---

## Installation

To include `uri` in your JavaScript or Node.js project, you can install it using npm:

```bash
npm install @lil-js/uri
```

or using yarn:

```bash
yarn add @lil-js/uri
```

This package is compatible with modern JavaScript environments including Node.js and frontend bundlers.

---

## Usage and Examples

Below are common usage patterns explaining how to parse, modify, and serialize URIs using the `uri` package.

### Parsing a URI

Parse a URI string into its components:

```js
import { Uri } from "@lil-js/uri";

const myUri = Uri.parse(
  "https://example.com:8080/path/to/resource?foo=bar&baz=qux#section",
);

console.log(myUri.scheme); // 'https'
console.log(myUri.host); // 'example.com'
console.log(myUri.port); // '8080'
console.log(myUri.path); // '/path/to/resource'
console.log(myUri.queryParams); // { foo: 'bar', baz: 'qux' }
console.log(myUri.fragment); // 'section'
```

### Modifying Query Parameters

You can manipulate query parameters via an object interface:

```js
const myUri = Uri.parse("https://example.com?foo=bar");

myUri.queryParams.baz = "qux";
myUri.queryParams.foo = "updated";

console.log(myUri.toString());
// Outputs: 'https://example.com?foo=updated&baz=qux'
```

### Constructing a New URI

Create a new URI from components:

```js
const newUri = new Uri({
  scheme: "https",
  host: "api.example.com",
  path: "/v1/users",
  queryParams: { page: "1", sort: "name" },
});

console.log(newUri.toString());
// Outputs: 'https://api.example.com/v1/users?page=1&sort=name'
```

---

## API Reference

### `Uri`

The main class representing a URI and its components.

#### Constructor

```ts
new Uri(options: {
  scheme?: string,
  host?: string,
  port?: string | number,
  path?: string,
  queryParams?: Record<string, string>,
  fragment?: string,
})
```

- **Parameters:**
  - `scheme` (string, optional): The scheme/protocol of the URI like `http`, `https`.
  - `host` (string, optional): The hostname or IP address.
  - `port` (string | number, optional): The port number.
  - `path` (string, optional): The path component of the URI.
  - `queryParams` (object, optional): Key-value pairs representing query parameters.
  - `fragment` (string, optional): The fragment identifier after `#`.

#### Properties

- `scheme: string | undefined` - URI scheme.
- `host: string | undefined` - URI host.
- `port: string | number | undefined` - Port number.
- `path: string | undefined` - Path after the host.
- `queryParams: Record<string, string>` - Query parameters as an object.
- `fragment: string | undefined` - Fragment identifier.

#### Methods

- `static parse(uriString: string): Uri`  
  Parses a URI string and returns a `Uri` instance with all parts extracted.

- `toString(): string`  
  Returns the full URI string constructed from the instance components.

---

## Contributing

Contributions are welcome to improve URI parsing accuracy, support additional URI components, or enhance API usability.

How to contribute:

1. Fork the repository on GitHub.
2. Create a new feature or bugfix branch.
3. Write clean, well-documented code.
4. Ensure tests cover your changes.
5. Submit a pull request with a clear description of your modifications.

Refer to the contributor guidelines in the repository for detailed instructions.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/lil-js/uri/blob/main/LICENSE) file for details.

---

## Contact

- **Repository:** [https://github.com/lil-js/uri](https://github.com/lil-js/uri)
- For issues and pull requests, please use the GitHub Issues page in the repository.
