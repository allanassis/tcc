# Axios

## Overview

Axios is a promise-based HTTP client for browsers and Node.js. It provides a simple and rich API for making HTTP requests and handling responses, supporting the full range of HTTP methods and features typically required when communicating with RESTful APIs or other web services.

The main domain concepts Axios models include:

- **HTTP Requests and Responses:** Standard mechanisms of sending requests to and receiving responses from servers.
- **Interceptors:** Middleware-like hooks to transform requests or responses before they are handled by then or catch.
- **Cancellation:** Ability to cancel requests using Cancel Tokens.
- **Request Configuration:** Defining headers, parameters, timeouts, and other request-specific settings.
- **Promise API:** Enabling asynchronous request handling with modern JavaScript Promises.
- **Adapters:** Abstraction to support HTTP calls in different environments (e.g., XHR in browsers, http module in Node.js).

Axios is widely used for its ease of use, robust feature set, and ability to work seamlessly both in client-side and server-side JavaScript environments.

---

## Installation

Axios can be installed via npm or yarn. It supports all modern browsers and Node.js environments.

### Using npm

```bash
npm install axios
```

### Using yarn

```bash
yarn add axios
```

---

## Usage and Examples

### Basic GET Request

```js
const axios = require('axios');

axios.get('https://api.example.com/data')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

### POST Request with Data

```js
axios.post('https://api.example.com/user', {
  firstName: 'John',
  lastName: 'Doe'
})
.then(response => {
  console.log(response.data);
})
.catch(error => {
  console.error(error);
});
```

### Setting Request Headers and Configurations

```js
axios({
  method: 'get',
  url: 'https://api.example.com/data',
  headers: {
    'Authorization': 'Bearer TOKEN_VALUE'
  },
  timeout: 5000,
  params: {
    id: 12345
  }
})
.then(response => {
  console.log(response.data);
})
.catch(error => {
  console.error(error);
});
```

### Using Async/Await Pattern

```js
async function fetchData() {
  try {
    const response = await axios.get('https://api.example.com/data');
    console.log(response.data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}
fetchData();
```

### Request Cancellation

```js
const CancelToken = axios.CancelToken;
const source = CancelToken.source();

axios.get('/user/12345', {
  cancelToken: source.token
})
.then(response => {
  console.log(response.data);
})
.catch(thrown => {
  if (axios.isCancel(thrown)) {
    console.log('Request canceled', thrown.message);
  } else {
    console.error(thrown);
  }
});

// Cancel the request
source.cancel('Operation canceled by the user.');
```

### Using Interceptors

```js
// Add a request interceptor
axios.interceptors.request.use(config => {
  // Do something before request is sent
  console.log('Starting Request', config);
  return config;
}, error => {
  // Do something with request error
  return Promise.reject(error);
});

// Add a response interceptor
axios.interceptors.response.use(response => {
  // Any status code that lie within the range of 2xx cause this function to trigger
  console.log('Response:', response);
  return response;
}, error => {
  // Any status codes that falls outside the range of 2xx cause this function to trigger
  return Promise.reject(error);
});
```

---

## API Reference

### Axios Instance Methods

- `axios(config)`

  Sends an HTTP request based on the provided configuration object.

  - `config` (object): Request configuration, including:
    - `url` (string): Request URL.
    - `method` (string): HTTP method (get, post, put, delete, etc.).
    - `baseURL` (string): A base URL that will be prepended to `url`.
    - `headers` (object): Custom headers.
    - `params` (object): URL parameters.
    - `data` (object|string): Request body data.
    - `timeout` (number): Request timeout in milliseconds.
    - `responseType` (string): Expected response format (json, blob, text, etc.).
    - `cancelToken` (CancelToken): Token to cancel the request.

  - **Returns:** A Promise that resolves with the response or rejects with an error.

- `axios.get(url[, config])`

  Shortcut for sending a GET request.

- `axios.post(url[, data[, config]])`

  Shortcut for sending a POST request.

- `axios.put(url[, data[, config]])`

  Shortcut for sending a PUT request.

- `axios.delete(url[, config])`

  Shortcut for sending a DELETE request.

- `axios.create([config])`

  Creates a new Axios instance with custom configuration.

- `axios.CancelToken`

  Constructor for creating cancellation tokens.

- `axios.isCancel(value)`

  Returns `true` if the provided value is a cancellation error.

### Response Object

- `data` — The response body provided by the server.
- `status` — HTTP status code of the response.
- `statusText` — HTTP status message.
- `headers` — Headers from the response.
- `config` — The original request configuration.
- `request` — The request object.

### Interceptors

- `axios.interceptors.request.use(onFulfilled[, onRejected])`

  Adds a request interceptor.

- `axios.interceptors.response.use(onFulfilled[, onRejected])`

  Adds a response interceptor.

---

## License

Axios is open-source software licensed under the [MIT License](https://github.com/axios/axios/blob/master/LICENSE).