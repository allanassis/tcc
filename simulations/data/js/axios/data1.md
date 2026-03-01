# Axios

## Overview

Axios is a popular JavaScript library used to make HTTP requests from both the browser and Node.js environments. It provides an easy-to-use, promise-based API for sending asynchronous HTTP requests to REST endpoints, handling responses, and managing errors. Axios supports features like interceptors, request cancellation, automatic JSON transformation, and timeout handling. It abstracts the complexities of XMLHttpRequest and the Fetch API to provide a consistent and intuitive interface for client-server communication.

### Domain Concepts

- **HTTP Requests**: Axios models the various HTTP methods (GET, POST, PUT, DELETE, etc.) enabling interaction with remote servers.
- **Promises**: Axios uses JavaScript promises to handle asynchronous operations, providing `.then()` and `.catch()` for response and error handling.
- **Interceptors**: Mechanisms to intercept and modify requests or responses globally before they are handled by `then` or `catch`.
- **Request Cancellation**: Using cancel tokens to abort in-progress requests.
- **Response Transformation**: Automatic transformation of request data before sending and response data before passing back to application logic.
- **Timeouts**: Support to set timeout limits for requests.
- **Cross-Site Requests**: Supports CORS and handling of cookies and credentials.

---

## Installation

### Using npm

```bash
npm install axios
```

### Using Yarn

```bash
yarn add axios
```

### CDN (Browser)

Include Axios via CDN for browser usage:

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

---

## Usage and Examples

### Basic GET Request

```js
const axios = require("axios");

axios
  .get("https://api.example.com/data")
  .then((response) => {
    console.log(response.data);
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
  });
```

### POST Request with JSON Payload

```js
axios
  .post("https://api.example.com/users", {
    firstName: "John",
    lastName: "Doe",
  })
  .then((response) => console.log(response.data))
  .catch((error) => console.error(error));
```

### Setting Custom Headers

```js
axios
  .get("https://api.example.com/private", {
    headers: { Authorization: "Bearer token123" },
  })
  .then((response) => console.log(response.data));
```

### Using Async/Await Syntax

```js
async function fetchData() {
  try {
    const response = await axios.get("https://api.example.com/data");
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}
fetchData();
```

### Request Cancellation

```js
const CancelToken = axios.CancelToken;
const source = CancelToken.source();

axios
  .get("/long-running-request", {
    cancelToken: source.token,
  })
  .catch((thrown) => {
    if (axios.isCancel(thrown)) {
      console.log("Request canceled", thrown.message);
    } else {
      // handle error
    }
  });

// Cancel the request
source.cancel("Operation canceled by the user.");
```

### Using Interceptors

```js
// Add a request interceptor
axios.interceptors.request.use(
  (config) => {
    // Modify config before request is sent
    config.headers["X-Custom-Header"] = "value";
    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);

// Add a response interceptor
axios.interceptors.response.use(
  (response) => {
    // Process response data
    return response;
  },
  (error) => {
    // Handle response errors globally
    return Promise.reject(error);
  },
);
```

---

## API Reference

### axios(config)

Main function to send HTTP requests. Can be called with a config object:

- `url` (string): Request URL.
- `method` (string): HTTP method (`get`, `post`, `put`, etc.), defaults to `get`.
- `baseURL` (string): Base URL prepended to `url` unless `url` is absolute.
- `headers` (object): HTTP headers.
- `params` (object): URL parameters for GET requests.
- `data` (object/string): Request body for POST, PUT, PATCH requests.
- `timeout` (number): Request timeout in milliseconds.
- `withCredentials` (boolean): Indicates whether cross-site Access-Control requests should be made using credentials.
- `responseType` (string): Indicates the type of data that the server will respond with (`json`, `blob`, `text`, etc.).
- `cancelToken` (CancelToken): Token to cancel the request.

Returns a `Promise` resolving to a `response` object with:

- `data`: The response body.
- `status`: HTTP status code.
- `statusText`: HTTP status message.
- `headers`: HTTP response headers.
- `config`: The request config.
- `request`: The underlying request object.

---

### axios.get(url[, config])

Shortcut for sending GET requests.

- `url` (string): The endpoint URL.
- `config` (object, optional): Additional config options.

Returns a `Promise`.

---

### axios.post(url[, data[, config]])

Shortcut for sending POST requests.

- `url` (string): The endpoint URL.
- `data` (any, optional): Data to send in the body.
- `config` (object, optional): Additional config options.

Returns a `Promise`.

---

### axios.create([config])

Creates a new Axios instance with a custom configuration.

- `config` (object, optional): Default config for the instance.

Example:

```js
const instance = axios.create({
  baseURL: "https://api.example.com",
  timeout: 1000,
  headers: { "X-Custom-Header": "foobar" },
});
```

---

### axios.CancelToken

Class to create tokens that can cancel requests.

```js
const source = axios.CancelToken.source();

axios.get("/user/12345", { cancelToken: source.token });

source.cancel("Operation canceled by the user.");
```

### axios.isCancel(value)

Function to determine whether a given error is due to a cancelled request.

---

## Contributing

Axios is an open-source project and welcomes contributions:

- Fork the repository on GitHub.
- Create a feature branch (`git checkout -b feature-name`).
- Commit your changes (`git commit -am 'Add new feature'`).
- Push to the branch (`git push origin feature-name`).
- Open a pull request describing your modifications.

Please adhere to the coding style, include tests for new features, and write clear commit messages.

---

## License

Axios is distributed under the [MIT License](https://github.com/axios/axios/blob/main/LICENSE).

---

## Contact

- Repository: [https://github.com/axios/axios](https://github.com/axios/axios)
- Issues: [https://github.com/axios/axios/issues](https://github.com/axios/axios/issues)
- Maintainers can be contacted via GitHub.
