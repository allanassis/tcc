```md
# Mocha Documentation

Mocha is a feature-rich JavaScript test framework running on Node.js and in the browser, making asynchronous testing simple and fun. It provides developers with flexible and powerful tools for writing and running tests for JavaScript code. Mocha supports test organization, asynchronous testing, multiple reporters, and hooks to manage test lifecycles.

---

## Conceptual Introduction

### Domain Concepts

- **Testing Framework:** Mocha is designed to help developers write and structure tests for JavaScript codebases to ensure code correctness and functionality.
- **Test Suite:** A collection of related tests grouped together using `describe()` blocks.
- **Test Case:** An individual test defined with `it()` or `test()` functions.
- **Assertions:** Conditions or expressions that verify expected outcomes; Mocha does not provide assertions itself but is commonly paired with assertion libraries like Chai.
- **Hooks:** Special functions (`before`, `beforeEach`, `after`, `afterEach`) that run at specific points during test execution to set up or tear down testing environments.
- **Asynchronous Testing:** Mocha supports asynchronous tests via callbacks, Promises, async/await, or generators.
- **Reporters:** Mechanisms to format and display test results in different styles (e.g., spec, dot, JSON).
- **Interface Layers:** Different flavors of syntax provided by Mocha including BDD (Behavior Driven Development), TDD (Test Driven Development), and exports interface.
- **Timeouts:** Mocha lets you set test timeout duration to avoid hanging tests.

### Mapping to API Terms

- `describe(title, fn)` defines a test suite.
- `it(title, fn)` defines a test case.
- Hooks like `before(fn)`, `after(fn)`, `beforeEach(fn)`, and `afterEach(fn)` manage lifecycle phases.
- The CLI and programmatic APIs allow configuring reporter, timeout, files to test, and other options.
- Tests can be synchronous or asynchronous via multiple patterns supported.

---

## Execution Facts

### Core API Functions and Methods

| API Element             | Inputs                                       | Outputs                  | Errors / Side Effects                                       | Defaults / Constraints                        |
|------------------------|----------------------------------------------|--------------------------|-------------------------------------------------------------|-----------------------------------------------|
| `describe(title, fn)`   | `title: string`, `fn: function`               | None                     | Defines a test suite. Errors inside run as test failures.   | Nested suites allowed.                         |
| `it(title, fn)`         | `title: string`, `fn: function` or async function | None                  | Defines an individual test. Supports callback and Promises. | Timeout applies per test; default 2000ms.      |
| `before(fn)`, `after(fn)` | `fn: function`                              | None                     | Hooks run once before/after test suites.                     | Hook failures affect tests.                    |
| `beforeEach(fn)`, `afterEach(fn)` | `fn: function`                    | None                     | Hooks run before/after each test in suite.                   | Hook failures treated as test failures.       |
| `.timeout(ms)`          | `ms: number`                                 | Configures timeout        | Sets maximum allowed time for a test or hook.                | Default timeout 2000ms; 0 disables timeout.   |
| `.skip()`               | None                                         | Skips the test or suite   | Test or suite is skipped and marked as such.                 | Useful for temporarily disabling.              |
| `.only()`               | None                                         | Runs only this test or suite | Limits run scope to marked tests/suites.                    | Used for focused testing.                       |

### CLI Facts

| Command                   | Description                              | Inputs                      | Outputs                      | Constraints & Notes                      |
|---------------------------|------------------------------------------|-----------------------------|------------------------------|-------------------------------------------|
| `mocha [options] [files]` | Runs tests specified by file patterns   | Files to test, CLI options  | Test results reported on STDOUT | Supports recursive file search, timeout setting, reporter selection |
| `--timeout <ms>`           | Sets test timeout globally               | Time in milliseconds        | Applies to all tests          | Overrides default 2000ms timeout           |
| `--reporter <name>`        | Sets reporter format                     | Reporter name (e.g., spec)  | Formatted test results output | Multiple built-in and custom reporters available |
| `--require <module>`       | Preload modules before test execution   | Module names                | None                        | Useful for setup, transpilers, or globals  |
| `--watch`                  | Watches files and reruns tests on changes | None                       | Auto re-runs tests on file save | Requires supported environment             |

---

## API Usage Patterns

### Pattern 1: Writing Simple Synchronous Tests with BDD Interface

#### What the code does

Defines a test suite and basic test cases that run synchronously, verifying expected outcomes.

#### How it does it

- Use `describe` to group logically related tests.
- Use `it` functions to define individual tests.
- Use assertions from any assertion library (e.g., Chai) inside `it` callback.

#### Why it’s structured that way

- Simple, readable structure for organizing tests.
- Flexible to work with various assertion styles.
- BDD style encourages behavior-focused tests.

#### Variation Points

- Use `beforeEach` to set up shared test data.
- Mark tests `.skip()` to temporarily disable.
- Mark tests `.only()` to run focused tests.

---

### Pattern 2: Writing Asynchronous Tests with Promises or async/await

#### What the code does

Allows tests to return Promises or use async functions to handle asynchronous code testing.

#### How it does it

- `it` callback returns a Promise or declares async function.
- Mocha waits for Promise resolution or rejection before continuing.
- Supports error propagation through rejected Promises.

#### Why it’s structured that way

- Simplifies asynchronous test writing with modern JS syntax.
- Avoids callback hell and improves test maintainability.
- Ensures tests time out if Promise does not resolve.

#### Variation Points

- Use done callback style for legacy asynchronous code.
- Combine with hooks like `beforeEach` for async setup.
- Extend test timeout for longer async operations.

---

### Pattern 3: Customizing Test Runs via CLI Options and Reporters

#### What the code does

Configures test execution environment from command-line: selecting files, setting timeouts, choosing reporters.

#### How it does it

- Command-line flags modify runtime parameters.
- Reporters change format and detail level of test outputs.
- Require option preloads modules or setups.

#### Why it’s structured that way

- Separates test implementation from execution concerns.
- Provides flexibility for development, CI, or debugging needs.
- Allows integration with other tools and custom reporting.

#### Variation Points

- Use different built-in reporters like `dot`, `nyan`, `json`.
- Write custom reporters by extending Mocha reporter API.
- Enable watch mode to rerun tests on file changes during development.

---

## Example Pattern: Basic Mocha Test Suite with Async Test and Hooks

```javascript
const assert = require('assert');

describe('Array', function() {
  before(function() {
    // runs once before all tests in this block
    console.log('Setup before tests');
  });

  beforeEach(function() {
    // runs before each test in this block
  });

  afterEach(function() {
    // runs after each test in this block
  });

  after(function() {
    // runs once after all tests in this block
    console.log('Cleanup after all tests');
  });

  it('should return -1 when value not present', function() {
    assert.strictEqual([1, 2, 3].indexOf(4), -1);
  });

  it('should resolve asynchronously with async/await', async function() {
    const result = await Promise.resolve(42);
    assert.strictEqual(result, 42);
  });

  it.skip('this test is skipped', function() {
    // skipped test
  });

  it.only('this test runs exclusively', function() {
    assert.strictEqual(1 + 1, 2);
  });
});
```

- **What:** Defines a test suite for Array methods with synchronous and asynchronous tests.
- **How:** Uses hooks to prepare and cleanup, `it` for test cases, including async one returning Promise.
- **Why:** Demonstrates core Mocha features for test organization and lifecycle.
- **Variation:** Mark tests skipped or exclusive; extend hooks and assertions as needed.

---

## Additional Developer Notes

- Mocha does not include assertions; integrate with libraries like Chai, Should.js, or Node’s assert module.
- Supports running tests in Node.js and browsers.
- Supports ES6, TypeScript via transpilers and Babel integration.
- Provides programmatic APIs to run tests without CLI.
- Timeout can be globally or per-test configured.
- Reporters can be extended or custom-built for advanced reporting needs.
- Use `.only()` and `.skip()` sparingly and remove before committing code.

---

This documentation integrates Mocha's domain concepts, concrete execution details of API functions and CLI options, and example usage patterns to provide developers with a comprehensive, robust understanding to write and manage tests effectively using Mocha.
```
