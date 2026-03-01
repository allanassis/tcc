# Axios

## Overview

Axios is a promise-based HTTP client for the browser and Node.js. It provides a simple and elegant API to perform asynchronous HTTP requests using familiar JavaScript syntax with support for the Promise API, making it easier to interact with RESTful APIs and handle HTTP communications.

### Domain Concepts

- **HTTP Requests & Responses:** Axios models HTTP request methods (GET, POST, PUT, DELETE, PATCH, etc.) and responses as JavaScript Promise objects.
- **Requests Configuration:** Axios uses configuration objects to specify request details such as URL, headers, method, data, and timeout.
- **Interceptors:** Allows adding custom logic to requests or responses before they are handled, useful for logging, injecting authentication tokens, or globally handling errors.
- **Cancellation:** Supports canceling requests using cancellation tokens.
- **Error Handling:** Provides a structured way to handle network errors, timeouts, or response status errors.
- **Request and Response Transformation:** Configuration allows intercepting and transforming data before sending the request or after receiving the response.

Axios abstracts the complexity of XMLHttpRequest (XHR) in browsers and the http module in Node.js, presenting a unified and consistent API for HTTP interactions.

---

## Installation

You can install Axios via npm or yarn.

### Using npm

```bash
npm install axios
```

### Using yarn

```bash
yarn add axios
```

Axios supports modern browsers and Node.js environments.

---

## Usage and Examples

### Basic GET Request

```js
const axios = require("axios");

axios
  .get("https://jsonplaceholder.typicode.com/posts/1")
  .then((response) => {
    console.log(response.data);
  })
  .catch((error) => {
    console.error(error);
  });
```

### POST Request with Data

```js
axios
  .post("https://jsonplaceholder.typicode.com/posts", {
    title: "foo",
    body: "bar",
    userId: 1,
  })
  .then((response) => {
    console.log(response.data);
  })
  .catch((error) => {
    console.error(error);
  });
```

### Using Async/Await

```js
async function fetchData() {
  try {
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/posts/1",
    );
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}
fetchData();
```

### Setting Default Configuration

```js
const instance = axios.create({
  baseURL: "https://api.example.com",
  timeout: 1000,
  headers: { Authorization: "Bearer token123" },
});

instance
  .get("/user")
  .then((response) => console.log(response.data))
  .catch((error) => console.error(error));
```

### Request Interceptors

```js
axios.interceptors.request.use(
  (config) => {
    // Modify config before request is sent
    config.headers["X-Custom-Header"] = "foobar";
    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);
```

### Response Interceptors

```js
axios.interceptors.response.use(
  (response) => {
    // Any status code within 2xx range triggers this
    // You can modify response here
    return response;
  },
  (error) => {
    // Handle response errors globally
    return Promise.reject(error);
  },
);
```

### Cancel Request Example

```js
const CancelToken = axios.CancelToken;
const source = CancelToken.source();

axios
  .get("/user/12345", {
    cancelToken: source.token,
  })
  .catch(function (thrown) {
    if (axios.isCancel(thrown)) {
      console.log("Request canceled", thrown.message);
    } else {
      // handle error
    }
  });

// Cancel the request
source.cancel("Operation canceled by the user.");
```

---

## API Reference

### `axios(config)`

Makes an HTTP request based on the specified config object.

- `config` (object) parameters include:
  - `url` (string): The server URL.
  - `method` (string): HTTP method ('get', 'post', 'put', etc.).
  - `baseURL` (string): Base URL prepended to `url`.
  - `headers` (object): Custom headers to send.
  - `params` (object): URL parameters to send with the request.
  - `data` (object|string|FormData): The request body data.
  - `timeout` (number): Timeout in milliseconds.
  - `responseType` (string): Expected response type ('json', 'blob', 'text', 'stream', etc.).
  - `cancelToken` (CancelToken): Token to cancel request.
  - Other advanced options (auth, maxContentLength, onUploadProgress, etc.).

Returns a Promise resolving to a response object.

---

### Shorthand Methods

- `axios.get(url[, config])`
- `axios.post(url[, data[, config]])`
- `axios.put(url[, data[, config]])`
- `axios.delete(url[, config])`
- `axios.patch(url[, data[, config]])`
- `axios.head(url[, config])`
- `axios.options(url[, config])`

These methods accept parameters for URL, optional data (for POST, PUT, PATCH), and optional config, and return a Promise.

---

### `axios.create([config])`

Creates a new Axios instance with a custom config.

- Useful to create separate clients with different base URLs or headers.

---

### `axios.CancelToken`

Factory to create cancel tokens to cancel requests.

---

### `axios.isCancel(value)`

Returns `true` if the value is a cancellation error, otherwise `false`.

---

### Response Object

Returned from successful requests:

- `data`: The response body (transformed to JSON if responseType is 'json').
- `status`: HTTP status code.
- `statusText`: HTTP status message.
- `headers`: Response headers.
- `config`: The request config used.
- `request`: The raw request object.

---

### Error Object

Thrown on request failure or bad HTTP status (if `validateStatus` is configured):

- `message`: Error message.
- `response`: The response object (if available).
- `request`: The request object.
- `config`: The request config.
- `code`: Error code (e.g., 'ECONNABORTED' for timeout).
- `isAxiosError`: Boolean flag.

---

## Contributing

Axios welcomes contributions! To contribute:

1. Fork the GitHub repository.
2. Create a topic branch for your feature or bugfix.
3. Write tests for new features or bugs.
4. Follow the project's coding style.
5. Run existing tests to ensure nothing breaks.
6. Submit a pull request with a clear description.

Be sure to review Axios's contribution guidelines for detailed instructions.

---

## License

Axios is licensed under the [MIT License](https://github.com/axios/axios/blob/master/LICENSE).

---

## Contact

- GitHub Repository: [https://github.com/axios/axios](https://github.com/axios/axios)
- Issues: Use GitHub Issues for bug reports and feature requests.
- Maintainers can be reached via GitHub or discussed in issues and pull requests.
