# Mocha Documentation

Mocha is a feature-rich JavaScript test framework running on Node.js and in the browser, making asynchronous testing simple and fun. Mocha tests run serially, allowing for flexible and accurate reporting, while mapping uncaught exceptions to the correct test cases.

---

## Conceptual Introduction

### Domain Concepts

- **Test Framework:** Mocha is a tool that facilitates writing, organizing, and running automated tests on JavaScript code.
- **Test Suites and Test Cases:** Tests are organized into suites (`describe` blocks) and individual test cases (`it`, `test`).
- **Hooks:** Setup and teardown functions such as `before`, `after`, `beforeEach`, and `afterEach` for lifecycle events around tests.
- **Asynchronous Testing:** Mocha supports async testing via callbacks, promises, async/await, allowing tests that perform asynchronous operations.
- **Reporters:** Different ways to display test results (progress reporters, spec reporters, JSON reporters, etc.).
- **Runners and Interfaces:** Mocha provides interfaces (`bdd`, `tdd`, `qunit`, etc.) to structure tests using various styles.
- **Retries and Timeouts:** Controls for retrying failed tests and specifying how long tests can run before timing out.
- **Globals and Test Context:** The test context (`this`) gives access to Mocha-specific features in tests and hooks.

### Mapping to API Terms

- `describe(title, fn)`: Defines a test suite, grouping tests logically.
- `it(title, fn)`: Defines an individual test case.
- Hooks functions such as `before(fn)`, `after(fn)`, `beforeEach(fn)`, `afterEach(fn)`.
- Asynchronous completion may be handled via `done` callback parameter or returning a promise.
- Mocha instance provides CLI commands for test execution, configuration options, and programmatic API.
- Various reporters for output through command-line or programmatic interfaces.

---

## Execution Facts

### Core API Elements

| API Element                       | Inputs                                          | Outputs                          | Errors / Side Effects                                       | Defaults / Constraints                                |
| --------------------------------- | ----------------------------------------------- | -------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------- |
| `describe(title, fn)`             | `title: string`, `fn: function`                 | None                             | Groups tests under a suite; throws if nested wrongly        | Can be nested; `title` required                       |
| `it(title, fn)` or `test()`       | `title: string`, `fn: function` (sync or async) | None                             | Defines a test; async tests supported; errors fail test     | Timeout default 2000ms; override per test             |
| `before(fn)`, `after(fn)`         | `fn: function`                                  | None                             | Hooks running before or after suites                        | Runs once per suite                                   |
| `beforeEach(fn)`, `afterEach(fn)` | `fn: function`                                  | None                             | Hooks running before or after each test                     | Runs around each test                                 |
| Test Function `fn(done)`          | `done` callback for async completion            | None                             | Must call `done()` or return a Promise; else test times out | Custom timeout possible                               |
| `this.timeout(ms)`                | `ms: number`                                    | None                             | Modifies timeout for test or hook                           | Default 2000ms                                        |
| `this.retries(n)`                 | `n: number`                                     | None                             | Retries failed tests up to `n` times                        | Default 0 retries                                     |
| Mocha CLI                         | CLI flags, options                              | Outputs test results and summary | Validates file globs, handles uncaught exceptions           | Supports config files, watch mode, and reporter flags |

### CLI Commands and Options

- `mocha [options] [files]`: Runs tests located in files or folders.
- Common options:
  - `--reporter <name>`: Specify reporter (e.g., `spec`, `dot`, `nyan`, `json`).
  - `--timeout <ms>`: Set test timeout in milliseconds.
  - `--grep <pattern>`: Only run tests matching pattern.
  - `--bail`: Exit after first test failure.
  - `--watch`: Rerun tests on file changes.
  - `--require <module>`: Require module before running tests.
- Runs tests serially, reporting results according to specified reporter.

### Configuration

- Configuration via `.mocharc.*` files (`.mocharc.json`, `.mocharc.js`, `.mocharc.yaml`).
- Can specify options such as timeout, require, recursive test loading, reporter, UI.
- Supports programmatic usage through `Mocha` class.

---

## API Usage Patterns

### Pattern 1: Basic Test Suite

#### What the code does

Defines a test suite grouping related test cases and executes assertions within individual test cases.

#### How it does it

- Use `describe` to group tests.
- Use `it` to define test cases with assertions.
- Synchronous or asynchronous tests supported via callbacks or async functions.

#### Why it’s structured that way

- Provides intuitive nesting to organize tests hierarchically.
- Supports granular testing with clear descriptive titles.
- Allows async operations typical in JavaScript environments.

#### Variation Points

- Replace callbacks with returning promises or async functions.
- Use hooks `before`, `after` etc. to setup test state.
- Customize timeout per test using `this.timeout`.

---

### Pattern 2: Using Hooks for Setup/Teardown

#### What the code does

Runs code before or after all tests or each test to setup and cleanup environment.

#### How it does it

- `before` and `after` run once per suite.
- `beforeEach` and `afterEach` run around every test.
- Hooks support asynchronous code.

#### Why it’s structured that way

- Reduces duplication by sharing common preparation and teardown logic.
- Enables deterministic test execution environments.

#### Variation Points

- Mix synchronous and asynchronous hooks.
- Nest hooks within nested suites for scoped setup.

---

### Pattern 3: Programmatic Mocha Usage

#### What the code does

Run tests programmatically, enabling dynamic control over test loading and execution.

#### How it does it

- Instantiate `Mocha` class.
- Use `.addFile()` or `.files` to specify test files.
- Call `.run()` to execute tests and obtain results.
- Allows integration with custom tooling or CI pipelines.

#### Why it’s structured that way

- Provides API for advanced scenarios such as embedding test runs inside applications or CI jobs.

#### Variation Points

- Configure `Mocha` constructor options (e.g., timeout, reporter).
- Listen for events for custom reporting or logging.
- Use different interfaces (`bdd`, `tdd`).

---

## Example Pattern: Basic Asynchronous Test Suite

```javascript
const assert = require("assert");

describe("Array", function () {
  before(function () {
    // runs once before all tests in this block
  });

  beforeEach(function () {
    // runs before each test in this block
  });

  afterEach(function () {
    // runs after each test in this block
  });

  after(function () {
    // runs once after all tests in this block
  });

  it("should start empty", function () {
    const arr = [];
    assert.strictEqual(arr.length, 0);
  });

  it("should allow pushing asynchronously", function (done) {
    const arr = [];
    setTimeout(() => {
      arr.push(1);
      assert.strictEqual(arr.length, 1);
      done();
    }, 100);
  });

  it("should support promises", function () {
    return Promise.resolve(42).then((result) => {
      assert.strictEqual(result, 42);
    });
  });
});
```

- **What:** Defines a suite testing Array behavior with sync, async, and promises.
- **How:** Uses Mocha’s `describe`, `it`, hooks, assertions, and asynchronous signaling.
- **Why:** Demonstrates Mocha’s flexibility with different asynchronous patterns.
- **Variation:** Add custom timeouts, retries, or different assertion libraries.

---

## Additional Developer Notes

- Mocha does not include assertions; use with assertion libraries like Node’s built-in `assert`, Chai, Should.js, etc.
- Supports hundreds of reporters for output customization.
- Supports ES modules, TypeScript (via transpilation), and browser usage.
- Can be extended via custom interfaces or reporters.
- Community provides many plugins for enhanced features (coverage, mocks, coverage, etc.).
- Setup with `.mocharc` config file for customizing default behaviors.
- When running in watch mode, use utilities like `nodemon` or integrated watch.

---

This documentation integrates domain concepts, execution facts, and usage patterns to provide a robust foundation for developers leveraging Mocha to structure, run, and report JavaScript tests with flexibility and clarity.
