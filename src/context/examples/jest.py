jest_example = """
## 5.2 Example

### Input
```
Generate API documentation for the package in the following address https://github.com/jestjs/jest. You can search on the web to understand what are the most importants parts to be added in the documentation.
You MUST output ONLY the documentation in Markdown format, no more data.
```

### Output
```md
# Jest

## Overview

Jest is a delightful JavaScript Testing Framework with a focus on simplicity. It is designed to ensure correctness of any JavaScript codebase by running tests in a predictable, fast, and reliable manner. Originally developed at Facebook, Jest works out of the box for most JavaScript projects, especially those using React, Node.js, or Babel. Jest supports snapshot testing, mock functions, and parallel test execution to provide a full-featured testing experience.

### Purpose and Goals

- Provide an intuitive and zero-configuration testing experience.
- Support testing of frontend and backend JavaScript code.
- Enable fast and reliable test execution with parallelism and intelligent test selection.
- Offer rich mocking capabilities to isolate code and create robust tests.
- Facilitate snapshot testing to capture and validate UI and data output changes.

---

## Features and Capabilities

- **Zero configuration**: Automatic setup for most projects, minimal setup required.
- **Snapshots**: Easily create and verify UI or data snapshots.
- **Isolated tests**: Each test file is sandboxed to avoid side effects.
- **Fast and parallel**: Runs tests concurrently by leveraging worker threads.
- **Mocking**: Supports manual and automatic mocks for functions and modules.
- **Code coverage**: Built-in support for code coverage reports.
- **Watch mode**: Intelligent rerun of tests related to changed files.
- **Rich reporters**: Includes console and third-party reporters for test outcomes.
- **Integrations**: Support for Babel, TypeScript, React, Vue, Angular, Node.js, and many more.

---

## Installation

### Prerequisites

- Node.js (>=10)
- npm or Yarn package manager

### Using npm

```bash
npm install --save-dev jest
```

### Using Yarn

```bash
yarn add --dev jest
```

### Adding Jest to your project

- Use the provided CLI to initialize Jest config or create a `jest.config.js` file manually.
- Run jest tests with:

```bash
npx jest
```
or

```bash
yarn jest
```

### Global installation (optional)

```bash
npm install -g jest
```

---

## Usage and Examples

### Basic Test Example

Create a test file `sum.test.js`:

```js
const sum = (a, b) => a + b;

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

Run tests with:

```bash
npx jest
```

Expected output:

```
 PASS  ./sum.test.js
  ✓ adds 1 + 2 to equal 3 (5 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

---

### Snapshot Testing Example

Test file `link.test.js`:

```js
const Link = () => {
  return '<a href="https://jestjs.io">Jest</a>';
};

test('renders correctly', () => {
  expect(Link()).toMatchSnapshot();
});
```

Run the test to create a snapshot. On subsequent runs, Jest verifies the output against the stored snapshot.

---

### Mock Function Example

```js
test('mock function example', () => {
  const mockFn = jest.fn().mockReturnValue(42);

  expect(mockFn()).toBe(42);
  expect(mockFn).toHaveBeenCalledTimes(1);
});
```

---

## API Reference

### `jest([options])`

Runs Jest test runner with specified options.

- `options` (object): Configuration options for Jest CLI.

---

### `test(name, fn, timeout)`

Defines a test case.

- `name` (string): Descriptive name of the test.
- `fn` (function): Test implementation.
- `timeout` (number, optional): Timeout in milliseconds.

---

### `expect(value)`

Creates an assertion object.

- `.toBe(value)`: Asserts value equality.
- `.toHaveBeenCalledTimes(number)`: Asserts mock function call count.
- `.toMatchSnapshot()`: Asserts value matches stored snapshot.

---

### `jest.fn(implementation)`

Creates a new mock function.

- `implementation` (function, optional): Custom mock implementation.

---

### Configuration Options (`jest.config.js` structure)

- `testEnvironment`: Environment for tests (`node`, `jsdom`, etc.).
- `transform`: Maps file extensions to transformers (e.g., Babel).
- `moduleNameMapper`: Module path aliases and mocks.
- `setupFilesAfterEnv`: List of files to configure test framework before tests run.
- `collectCoverage`: Collect code coverage information.
- `coverageDirectory`: Output directory for coverage reports.

---

## Contributing

Jest is open source and welcomes contributions!

### How to contribute

1. Fork the repository on GitHub.
2. Create a feature branch or bugfix branch.
3. Write tests for your changes.
4. Follow coding style guidelines.
5. Submit a pull request with a clear description.

### Development setup

- Clone the repo
- Run `yarn install` to install dependencies.
- Use `yarn test` to run tests.
- Use `yarn build` to build the system.

Refer to the [CONTRIBUTING.md](https://github.com/facebook/jest/blob/main/CONTRIBUTING.md) file in the repo for detailed instructions.

---

## License

Jest is licensed under the [MIT License](https://github.com/facebook/jest/blob/main/LICENSE).

---

## Contact

- Official repo: [https://github.com/facebook/jest](https://github.com/facebook/jest)
- Twitter: [@jestjs](https://twitter.com/jestjs)
- Community: [https://jestjs.io/community](https://jestjs.io/community)

For questions or discussion, visit the Jest Discord or GitHub Issues.
```


"""