jest_example = """
## 5.2 Example

### Input
```

### Output
```md
# Jest Documentation

Jest is a delightful JavaScript Testing Framework with a focus on simplicity. It provides an integrated zero-configuration testing experience, supporting snapshot testing, mock functions, asynchronous testing, and code coverage analysis. Jest is widely used for testing React applications but supports any JavaScript codebase.

---

## Conceptual Introduction

### Domain Concepts

- **Testing Framework:** Jest is a tool that helps developers write and run tests to verify that their code works as expected.
- **Test Suites and Test Cases:** In Jest, tests are organized in suites (`describe` blocks) and cases (`test` or `it` blocks).
- **Assertions:** Statements that specify expected outcomes using Jest’s matcher functions like `expect(value).toBe(expected)`.
- **Mock Functions:** Functions that replace real implementations to isolate units under test and simulate behavior.
- **Snapshot Testing:** Captures the rendered output of components or functions and compares future runs to detect unexpected changes.
- **Code Coverage:** The measurement of how much of the codebase is exercised by tests, generating reports for analysis.
- **Watch Mode:** Runs tests automatically based on file changes to provide rapid feedback during development.

### Mapping to API Terms

- `describe()`: Defines a test suite grouping.
- `test()` / `it()`: Defines an individual test case.
- `expect()`: Creates an assertion object to test values.
- Mocking utilities such as `jest.fn()` and `jest.mock()` simulate dependencies.
- Snapshots are created and compared using `toMatchSnapshot()`.
- CLI commands and configuration control execution environment, watch mode, coverage, and reporters.

---

## Execution Facts

### Core API (Functions and Methods)

| API Element              | Inputs                                      | Outputs                  | Errors / Side Effects                                      | Defaults / Constraints                        |
|--------------------------|---------------------------------------------|-------------------------|------------------------------------------------------------|-----------------------------------------------|
| `describe(name, fn)`      | `name: string`, `fn: function`              | None                    | Runs contained tests in a suite; errors propagate as test failures | Nestable for organize tests; name required    |
| `test(name, fn, timeout?)`| `name: string`, `fn: function`, `timeout? number` | None                    | Runs a test case; async tests must return Promise or call done callback | Timeout defaults to 5s; override per test     |
| `expect(value)`           | `value: any`                                 | Expectation object       | Constructs matcher API for assertions                      | Matchers chained after call                    |
| `jest.fn(implementation?)`| Optional function to mock                   | Mock function            | Tracks calls, instances, and allow manual resolution      | Records calls for inspection                    |
| `jest.mock(moduleName, factory?, options?)` | Module specifier string or path, factory function for manual mock | Mocks imported module    | Replaces module calls with mocks during test runtime      | Hoisted to top of scope; can use automock      |

### CLI Execution Facts

| Command                   | Description                                   | Inputs              | Outputs                                        | Constraints & Notes                             |
|---------------------------|-----------------------------------------------|---------------------|------------------------------------------------|-------------------------------------------------|
| `jest`                    | Runs all tests                                | CLI options         | Test results printed, code coverage optional | Supports config via `jest.config.js` or package.json; supports parallel test running |
| `jest --watch`            | Watch mode to re-run tests on file changes    | CLI options         | Tests rerun on save; interactive test running | Monitors git changes or all files; interactive filters supported                        |
| `jest --coverage`         | Generates a coverage report for the test run  | CLI options         | Coverage reports in multiple formats          | Instrumentation needed; thresholds configurable |
| `jest --updateSnapshot`   | Update existing snapshot files                 | CLI options         | Overwrites snapshots detected as outdated     | Use carefully to avoid overwriting valid snapshots |

### Configuration

- Jest supports configuration via `jest.config.js`, JSON, or `package.json`.
- Configuration properties control test environment, coverage thresholds, module paths, and transform pipelines.
- Supports custom reporters, setup files, test environment selections (jsdom or node).

---

## API Usage Patterns

### Pattern 1: Writing and Organizing Tests

#### What the code does

Organizes tests in logical groups (`describe`), defines individual tests (`test` or `it`), and uses `expect` assertions to validate outcomes.

#### How it does it

- `describe` scopes tests for clarity and reuse.
- `test` runs a single assertion case, supporting synchronous and asynchronous code.
- `expect` provides flexible matchers like `.toBe()`, `.toEqual()`, `.toHaveBeenCalled()`, etc.

#### Why it’s structured that way

- Makes test suites readable and maintainable.
- Supports clear failure reports with descriptive naming.
- Allows modular testing of discrete units of behavior.

#### Variation Points

- Use `beforeEach` and `afterEach` hooks inside `describe` to setup/teardown shared state.
- Parameterized tests via `test.each` for data-driven scenarios.

---

### Pattern 2: Mocking Dependencies

#### What the code does

Replaces real module dependencies or functions with controllable mock implementations to isolate units and simulate different behaviors.

#### How it does it

- `jest.fn()` creates mock functions tracking calls and allowing return value manipulation.
- `jest.mock()` replaces entire modules with custom or auto-generated mocks at load time.
- Mock function methods (`mockReturnValue`, `mockImplementation`) define behaviors.

#### Why it’s structured that way

- Enables testing units independently from external dependencies.
- Empowers testing edge cases by simulating specific responses or errors.
- Helps verify interactions (e.g., "was this function called with these parameters?").

#### Variation Points

- Use manual mocks stored under `__mocks__` to customize module behavior.
- Reset mocks between tests with `jest.resetAllMocks()`.

---

### Pattern 3: Snapshot Testing

#### What the code does

Captures rendered output or data structures and compares them against stored "snapshots" to detect unintended changes.

#### How it does it

- Use `expect(value).toMatchSnapshot()` to automate snapshot creation and verification.
- Jest stores snapshots as text files alongside tests.
- Failing tests indicate snapshot divergence.

#### Why it’s structured that way

- Provides a fast, reliable way to verify UI or serialized output.
- Reduces manual assertion writing for complex outputs.
- Snapshots can be updated when intentional changes occur.

#### Variation Points

- Parametrize snapshots with `toMatchInlineSnapshot()` for compact tests.
- Combine with mock functions for isolated component renders.

---

## Example Pattern: Simple Test Suite with Mocks and Snapshot

```javascript
// math.js
function add(a, b) {
  return a + b;
}
module.exports = { add };

// math.test.js
const math = require('./math');

describe('Math utils', () => {
  test('adds two numbers correctly', () => {
    expect(math.add(1, 2)).toBe(3);
  });

  test('adds returns snapshot', () => {
    expect(math.add(5, 10)).toMatchSnapshot();
  });
});

// mocking example
jest.mock('./math', () => ({
  add: jest.fn((a, b) => 42),
}));

test('mocked add returns fixed value', () => {
  const math = require('./math');
  expect(math.add(1, 2)).toBe(42);
  expect(math.add).toHaveBeenCalledWith(1, 2);
});
```

- **What:** Defines test suite for math utils, asserts correctness, and creates a snapshot. Demonstrates mocking the `add` function.
- **How:** Uses `describe` and `test` for organization, `expect` for assertions, and `jest.mock` to replace the module during a test.
- **Why:** Shows core Jest mechanisms to ensure test reliability and isolation.
- **Variation:** Modify the mock implementation for different behaviors or add async tests.

---

## Additional Developer Notes

- Jest automatically finds tests in `__tests__` directories or files with `.test.js`/`.spec.js` suffixes.
- Supports Babel and TypeScript through transformations (`babel-jest`, `ts-jest`).
- Integrates easily with Continuous Integration (CI) servers and coverage tools.
- Offers advanced features like custom matchers and JSON reporters for extensibility.
- For performance, isolate slow tests or use selective running with `--testNamePattern`.

---

This documentation integrates Jest’s domain concepts, execution facts, and usage patterns to provide a robust foundation for developers aiming to write reliable, maintainable JavaScript tests with Jest.
```


"""