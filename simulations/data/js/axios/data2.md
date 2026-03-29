# Axios

## Overview

Axios is a popular promise-based HTTP client for JavaScript, designed to work both in the browser and in Node.js environments. It provides an easy and flexible way to send asynchronous HTTP requests to REST endpoints and handle responses. Axios abstracts the complexity of XMLHttpRequest or Node's HTTP module and offers a clean API that supports request and response interception, automatic JSON data transformation, cancellation, and timeout handling.

### Domain Concepts

- **HTTP Requests:** Axios models HTTP requests such as GET, POST, PUT, DELETE, PATCH, etc., to interact with web services.
- **Promises:** Axios uses JavaScript Promises for asynchronous control flow, returning a promise that resolves with the HTTP response or rejects with an error.
- **Interceptors:** Functions that allow transformation or logging of requests/responses before they are handled.
- **Request Configurations:** Structured options describing how HTTP requests should be made, including headers, query params, timeouts, and more.
- **Response Objects:** Structured data containing status, headers, and payload returned from an HTTP call.
- **Cancellation:** Ability to abort requests mid-flight using Cancel tokens.
- **Adapter:** Internal abstraction enabling Axios to work in different environments (browser or Node.js) with interchangeable HTTP implementations.

---

## Installation

Install Axios via npm or yarn:

```bash
npm install axios
```

or

```bash
yarn add axios
```

Axios is compatible with both browser and Node.js environments, with no additional setup required.

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
    console.error('Error fetching data:', error);
  });
```

### POST Request with JSON Payload

```js
axios.post('https://api.example.com/user', {
  firstName: 'John',
  lastName: 'Doe'
})
.then(response => {
  console.log('User created:', response.data);
})
.catch(error => {
  console.error('Error creating user:', error);
});
```

### Request with Custom Headers and Query Parameters

```js
axios.get('https://api.example.com/items', {
  params: { category: 'books', sort: 'asc' },
  headers: { 'Authorization': 'Bearer token' }
})
.then(response => {
  console.log(response.data);
});
```

### Using Async/Await

```js
async function fetchData() {
  try {
    const response = await axios.get('https://api.example.com/data');
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

fetchData();
```

### Using Interceptors

```js
// Request interceptor to add authentication token
axios.interceptors.request.use(config => {
  config.headers.Authorization = 'Bearer YOUR_TOKEN';
  return config;
}, error => {
  return Promise.reject(error);
});

// Response interceptor to log responses
axios.interceptors.response.use(response => {
  console.log('Response received:', response.status);
  return response;
}, error => {
  return Promise.reject(error);
});
```

### Cancelling Requests

```js
const CancelToken = axios.CancelToken;
const source = CancelToken.source();

axios.get('https://api.example.com/data', {
  cancelToken: source.token
}).catch(thrown => {
  if (axios.isCancel(thrown)) {
    console.log('Request canceled', thrown.message);
  } else {
    console.error('Error:', thrown);
  }
});

// Cancel the request
source.cancel('Operation canceled by the user.');
```

---

## API Reference

### axios(config)

Sends an HTTP request based on the provided configuration.

- **Parameters:**
  - `config` (object): Configuration object for the request.
    - `url` (string): The URL to send the request to.
    - `method` (string): HTTP method (GET, POST, PUT, DELETE, PATCH, etc.).
    - `baseURL` (string): Base URL prepended to `url`.
    - `headers` (object): Custom headers to send.
    - `params` (object): URL parameters to be appended.
    - `data` (any): Data to be sent as the request body.
    - `timeout` (number): Timeout in milliseconds.
    - `responseType` (string): Type of data expected back (e.g., 'json', 'blob').
    - `cancelToken` (CancelToken): Token to cancel request.
    - ...and others.

- **Returns:** A Promise that resolves to a response object or rejects with an error.

### axios.get(url[, config])

Shortcut for GET requests.

- **Parameters:**
  - `url` (string): URL for the HTTP request.
  - `config` (object, optional): Additional request configuration.

- **Returns:** Promise resolving to response object.

### axios.post(url[, data[, config]])

Shortcut for POST requests.

- **Parameters:**
  - `url` (string): URL for the HTTP request.
  - `data` (any, optional): Data to send as request body.
  - `config` (object, optional): Additional request configuration.

- **Returns:** Promise resolving to response object.

### axios.put(url[, data[, config]])

Shortcut for PUT requests.

### axios.delete(url[, config])

Shortcut for DELETE requests.

### axios.patch(url[, data[, config]])

Shortcut for PATCH requests.

### axios.create([config])

Creates a new Axios instance with a custom configuration.

- **Parameters:**
  - `config` (object, optional): Default configuration for the instance.

- **Returns:** New Axios instance with the custom config.

### axios.interceptors.request.use(onFulfilled, onRejected)

Adds a request interceptor.

- `onFulfilled` (function): Function to execute on intercepted request config.
- `onRejected` (function): Function to execute on request error.

Returns interceptor ID.

### axios.interceptors.response.use(onFulfilled, onRejected)

Adds a response interceptor.

### axios.CancelToken

Constructor for creating cancel tokens to abort requests.

### axios.isCancel(value)

Checks if an error was caused by cancellation.

---

## License

Axios is licensed under the MIT License. See the [LICENSE](https://github.com/axios/axios/blob/main/LICENSE) file for details.