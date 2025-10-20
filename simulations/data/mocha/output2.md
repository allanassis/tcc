```md
# Mocha Documentation

Mocha is a feature-rich JavaScript test framework running on Node.js and in the browser, making asynchronous testing simple and fun. Mocha tests run serially, allowing for flexible and accurate reporting, while mapping uncaught exceptions to the correct test cases.

---

## Conceptual Introduction

### Domain Concepts

- **Test Framework:** Mocha provides an environment to write, organize, and run tests for JavaScript code.
- **Test Suites and Test Cases:** Tests are organized into suites (`describe()` blocks) and individual tests (`it()` blocks).
- **Hooks:** Lifecycle methods run before or after tests to set up preconditions or clean up.
- **Asynchronous Testing:** Supports asynchronous tests via callbacks, promises, async/await.
- **Reporters:** Output formats for test results, such as spec, dot, tap, json, etc.
- **Runners:** Responsible for executing tests and invoking reporters.
- **Interfaces:** Different syntaxes to write tests (BDD, TDD, QUnit style).
- **Timeouts:** Limit test execution time to catch hanging tests.
- **Pending Tests:** Tests defined but skipped or incomplete.

### Mapping to API Terms

- `describe(title, fn)`: Defines a test suite grouping.
- `it(title, fn)`: Defines an individual test case.
- Hooks: `before()`, `after()`, `beforeEach()`, `afterEach()` control lifecycle events.
- `this.timeout(ms)`: Sets timeout for tests or hooks.
- Mocha CLI runs tests and allows configuration via files or arguments.
- Mocha reporters display test results in user-friendly formats.

---

## Execution Facts

### Core API

| Function / Method          | Inputs                                    | Outputs                  | Errors / Side Effects                                    | Defaults / Constraints              |
|---------------------------|-------------------------------------------|--------------------------|----------------------------------------------------------|-----------------------------------|
| `describe(title, fn)`      | `title: string`, `fn: function`            | None                     | Groups tests; errors in `fn` propagate to tests          | Can be nested; title required      |
| `it(title, fn)`            | `title: string`, `fn: function`            | None                     | Runs a test; supports synchronous and async via `fn`     | Default timeout 2000ms; can override|
| `before(fn)`, `after(fn)`  | Lifecycle hook functions                    | None                     | Runs once before/after suite                              | Hook failures fail tests           |
| `beforeEach(fn)`, `afterEach(fn)` | Lifecycle hooks before/after each test | None                   | Run before/after every test                               | Hook can be async                  |
| `this.timeout(ms)`         | Timeout duration in milliseconds            | None                     | Sets per-test or hook timeout                             | Overrides default 2000ms           |
| `run()`                   | No inputs (programmatic runner start)       | Returns a `Runner` object | Starts test execution programmatically                   | Used in custom Mocha setups        |

### CLI Execution Facts

| CLI Command / Option         | Description                                 | Inputs                  | Outputs                        | Constraints / Notes                      |
|-----------------------------|---------------------------------------------|-------------------------|--------------------------------|----------------------------------------|
| `mocha [options] [files]`    | Run tests specified or default files        | Files/globs, cli flags  | Test results summary            | Default directory is `test`             |
| `--reporter <name>`          | Specifies reporter to format output          | Reporter name string    | Formatted test results          | Built-in reporters or custom possible   |
| `--timeout <ms>`             | Sets global test timeout                      | Integer milliseconds    | Enforces test/hook time limits  | Overrides default timeout                |
| `--require <module>`         | Loads modules before test execution           | Module path(s)          | Allows test setup               | Useful for transpilers or globals       |
| `--recursive`                | Includes subdirectories recursively           | Flag                    | Discovers all tests recursively | Common for large projects                |

### Configuration

- Mocha can be configured via `.mocharc.*` files (JSON, YAML, JS) or `package.json` under `mocha` key.
- Configuration controls interface, reporter, timeouts, file patterns, retries, etc.

---

## API Usage Patterns

### Pattern 1: Writing Synchronous and Asynchronous Tests

#### What the code does

Defines test suites and tests which may execute synchronous or asynchronous logic to verify functionality.

#### How it does it

- Uses `describe()` to group tests.
- Uses `it()` for individual tests.
- Async tests handled by returning promises, callbacks with `done`, or async functions.

#### Why it’s structured that way

- Separates tests logically for clarity and organization.
- Allows flexibility in writing async behavior without blocking the runner.
- Makes failures easily traceable to individual test cases.

#### Variation Points

- Provide test-specific timeouts to override default global timeout.
- Skip or mark tests as pending using `it.skip()`, `describe.skip()`, or `this.skip()`.

---

### Pattern 2: Using Hooks for Setup and Teardown

#### What the code does

Setup preconditions before suite or each test and cleanup afterward.

#### How it does it

- `before()` and `after()` run once per suite.
- `beforeEach()` and `afterEach()` run before and after every test in a suite.

#### Why it’s structured that way

- Reduces code duplication.
- Ensures consistent test environment preparation and cleanup.
- Helps avoid flaky tests by resetting state.

#### Variation Points

- Hooks can be async via returning promise or calling `done`.
- Nest hooks inside nested `describe()` calls for scoped setup.

---

### Pattern 3: Custom Reporters and Programmatic Test Running

#### What the code does

Customize how results are displayed or integrate Mocha into other tools.

#### How it does it

- Create or use built-in reporters.
- Use Mocha programmatically by creating a Mocha instance, adding test files, and calling `run()`.

#### Why it’s structured that way

- Supports integration with IDEs, CI tools, or custom workflows.
- Enhances reporting beyond CLI default.

#### Variation Points

- Swap reporters with `--reporter` option or programmatically.
- Control test execution lifecycle directly in scripts.

---

## Example Pattern: Basic Test Suite with Async Test and Hooks

```js
const assert = require('assert');

describe('Array', function () {
  before(function () {
    // Runs once before all tests
  });

  beforeEach(function () {
    // Runs before each test
  });

  it('should return -1 when the value is not present', function () {
    assert.strictEqual([1, 2, 3].indexOf(4), -1);
  });

  it('should support async test with done callback', function (done) {
    setTimeout(function () {
      assert.strictEqual(true, true);
      done();
    }, 100);
  });

  afterEach(function () {
    // Runs after each test
  });

  after(function () {
    // Runs once after all tests
  });
});
```

- **What:** Defines a synchronous and an asynchronous test within a suite, uses hooks for setup and teardown.
- **How:** Uses Mocha's BDD interface functions to organize tests and lifecycle.
- **Why:** Demonstrates basic, idiomatic Mocha usage covering common cases.
- **Variation:** Tests can return promises or use async/await instead of done; hooks can be async.

---

## Additional Developer Notes

- Mocha supports multiple interfaces: BDD (default), TDD, QUnit, exports.
- To test ES modules or TypeScript, transpilation is required or use `--require` with appropriate compilers.
- Mocha allows retries for flaky tests with `this.retries(n)` or CLI option `--retries n`.
- Use `--inspect` and `--inspect-brk` flags for debugging tests.
- Custom reporters can be found or written to tailor output formats to team or tool needs.

---

This documentation integrates Mocha's domain concepts, core API execution facts, and common usage patterns to provide a comprehensive and robust understanding suited for developers writing and running JavaScript tests with Mocha.
```

