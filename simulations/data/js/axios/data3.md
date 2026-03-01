# Axios

## Overview

Axios is a popular, promise-based HTTP client for JavaScript that works in both the browser and Node.js environments. It provides an easy-to-use API to send asynchronous HTTP requests to REST endpoints, interact with external APIs, and handle responses with support for promises. Axios abstracts the complexity of XMLHttpRequests and Node.js HTTP modules, making HTTP communications straightforward and efficient.

### Domain Concepts

- **HTTP Requests and Responses:** Axios models the HTTP communication process, supporting methods like GET, POST, PUT, DELETE, and more.
- **Interceptors:** Functions to intercept and modify requests or responses before they are handled by then or catch.
- **Promises:** Axios relies on ES6 promises to facilitate asynchronous HTTP request processing.
- **Configuration:** Centralized options for requests such as headers, timeouts, query parameters, base URLs, and authentication.
- **Cancellation:** Supports cancelling requests using cancellation tokens.
- **Transformations:** Ability to modify request and response data before they are handled.
- **Adapters:** Different adapters for making requests in browsers or Node.js.
- **Error Handling:** Provides detailed error objects for HTTP, timeout, network errors, and cancellations.

---

## Installation

Install Axios via npm or Yarn:

```bash
npm install axios
```

or

```bash
yarn add axios
```

Axios supports all modern browsers and Node.js environments.

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

### POST Request with Data

```js
axios
  .post("https://api.example.com/user", {
    firstName: "John",
    lastName: "Doe",
  })
  .then((response) => {
    console.log("User created:", response.data);
  })
  .catch((error) => {
    console.error(error);
  });
```

### Creating an Axios Instance

Using an instance lets you set custom defaults:

```js
const api = axios.create({
  baseURL: "https://api.example.com",
  timeout: 1000,
  headers: { "X-Custom-Header": "foobar" },
});

api.get("/user").then((response) => console.log(response.data));
```

### Interceptors for Requests and Responses

```js
// Add a request interceptor
axios.interceptors.request.use(
  (config) => {
    // Modify config before sending request
    config.headers["Authorization"] = "Bearer token";
    return config;
  },
  (error) => Promise.reject(error),
);

// Add a response interceptor
axios.interceptors.response.use(
  (response) => {
    // Any status code within 2xx triggers this
    return response;
  },
  (error) => {
    // Handle errors or trigger refresh token workflows here
    return Promise.reject(error);
  },
);
```

### Canceling Requests

```js
const CancelToken = axios.CancelToken;
const source = CancelToken.source();

axios
  .get("/user/12345", {
    cancelToken: source.token,
  })
  .catch((thrown) => {
    if (axios.isCancel(thrown)) {
      console.log("Request canceled", thrown.message);
    }
  });

// Cancel the request
source.cancel("Operation canceled by the user.");
```

---

## API Reference

### axios(config)

Sends a HTTP request with the specified configuration.

- `config` (object): Configuration object including:
  - `url` (string): Request URL.
  - `method` (string): HTTP method (e.g., 'get', 'post', etc.).
  - `baseURL` (string): Base URL prepended to `url`.
  - `headers` (object): Custom HTTP headers.
  - `params` (object): URL parameters to be sent with the request.
  - `data` (object): Data to be sent as the request body.
  - `timeout` (number): Timeout in milliseconds.
  - `responseType` (string): The type of data that the server will respond with (e.g., 'json', 'blob').
  - `cancelToken`: Token for cancelling the request.
  - `onUploadProgress` (function): Called periodically with progress events during uploads.
  - `onDownloadProgress` (function): Called periodically with progress events during downloads.
- **Returns:** A Promise resolving to the response object.

### axios.request(config)

Alias for `axios(config)`.

### axios.get(url[, config])

Sends a GET request.

- `url` (string): The URL for the request.
- `config` (object, optional): Additional config options.

### axios.post(url, data[, config])

Sends a POST request with data.

- `url` (string): URL for the request.
- `data` (any): Data to be sent as the request body.
- `config` (object, optional): Additional config options.

### axios.put(url, data[, config])

Sends a PUT request.

### axios.delete(url[, config])

Sends a DELETE request.

### axios.create([config])

Creates a new Axios instance.

- `config` (object, optional): Default configuration for the instance.

### axios.interceptors

Allows registration of interceptors for requests and responses.

- `request.use(onFulfilled, onRejected)`: Registers a request interceptor.
- `response.use(onFulfilled, onRejected)`: Registers a response interceptor.

### axios.CancelToken

Allows creating tokens to cancel requests.

### axios.isCancel(value)

Determines if a value is a cancel error.

### Response Object

A fulfilled response has the following structure:

- `data`: The response payload.
- `status`: HTTP status code.
- `statusText`: HTTP status message.
- `headers`: Response headers.
- `config`: The request config.
- `request`: The request object.

---

## Contributing

Axios welcomes contributions from the community!

### How to contribute

- Fork the repo on GitHub.
- Create a branch with your feature or bug fix.
- Ensure tests pass and add new tests if applicable.
- Follow code style guidelines.
- Submit a pull request with a clear description of your changes.

Refer to the [contributing guide](https://github.com/axios/axios/blob/master/CONTRIBUTING.md) for more details.

---

## License

Axios is open source and distributed under the MIT License. See the [LICENSE](https://github.com/axios/axios/blob/master/LICENSE) file for details.

---

## Contact

- **Repository:** [https://github.com/axios/axios](https://github.com/axios/axios)
- **Issues:** Use GitHub Issues for bug reports and feature requests.
- **Twitter:** [@axios_http](https://twitter.com/axios_http)

For more information, visit the official documentation at [https://axios-http.com/](https://axios-http.com/).
