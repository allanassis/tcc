local_example = """
## 5.3 Example

### Input
```
"Generate API documentation for the package located in the following directory ./src/interfaces/cli/cli.py. Try to identify the public APIs of the package and the most important parts of these API to use in the documentation."
You MUST output ONLY the documentation in Markdown format, no more data.
```

### Output
```.md
# CLI Module Documentation for Package Documentation Generator

The CLI module provides a command-line interface to generate API documentation for software packages using the principles of ATORAK (A Theory of Robust API Knowledge). It leverages an LLM (Large Language Model) manager to process the input package path and generate comprehensive documentation output.

---

## Conceptual Introduction

### Domain Concepts

- **API Documentation Generation:** The process of automatically creating descriptive and structured documentation for software APIs to enhance developer understanding.
- **Command-Line Interface (CLI):** A text-based interface allowing users to interact with programs through commands.
- **Package Path:** The location of the software package to be documented. This can be a local folder, a GitHub repo, or other repository types.
- **LLM Model:** A large language model used to analyze and generate text. Supported models include 'gpt', 'gemini', and 'bedrock'.

### Mapping to API Terms

- The main CLI entry point is the `main()` function, invoked when running the CLI script.
- CLI arguments (`--path`, `--local`, `--model`) correspond to inputs for the documentation generation process.
- The CLI internally uses the `LLMManager` class's `generate_doc` method to create the documentation output.
- Errors in processing or invalid input result in program termination with an error message.

---

## Execution Facts

### Public API

#### `main()`

- **Description:** Entry function to parse command-line arguments and trigger the documentation generation.
- **Inputs:**
  - `--path` (string, required): Path to the target package (GitHub repo URL or local directory).
  - `--local` (boolean-like flag, optional, default: False): Indicates if the path is local.
  - `--model` (string, optional, default: 'gpt'): LLM model selection from ['gpt', 'gemini', 'bedrock'].
- **Outputs:**
  - Prints generated API documentation text to standard output.
- **Errors:**
  - Prints error message to standard error and exits with status code 1 on failure.

### Constraints and Behavior

- Must be run in an environment with `dotenv` configured for environment variables.
- Relies on `LLMManager` implementation and its connectivity or setup to operate correctly.
- The script expects the package path to be a valid location accessible with proper permissions.
- Defaults to GPT model if no model specified.
- Provides CLI feedback synchronously on console.

---

## API Usage Patterns

### Typical Use Case: Generating API Documentation via CLI

#### What the code does

- Receives user CLI input parameters for package location and model choice.
- Uses an LLM-driven backend (`LLMManager`) to generate robust API documentation text.
- Outputs the generated documentation to the console.

#### How it does it

- Uses `argparse` to parse and validate CLI arguments.
- Instantiates the `LLMManager`.
- Calls `generate_doc` with parsed inputs.
- Catches and displays exceptions gracefully.

#### Why it's structured that way

- Simplifies the usage of the documentation generator to a single CLI command.
- Allows flexible input for package location and model selection.
- Uses environment configuration for settings (`dotenv`).
- Provides user-friendly error handling for robustness.

#### Variation Points

- Change the `--path` argument to different repositories or local directories to document different packages.
- Switch the `--model` argument between supported LLMs according to need or availability.
- Extend CLI with additional options for future configuration (e.g., output format, verbosity).

---

## Example CLI Usage

```bash
python3 cli.py --path=https://github.com/example/repo --model=gpt
```

- **What:** Runs the CLI tool to generate API documentation for a GitHub repository using the GPT model.
- **How:** Parses the path and model from CLI, calls `LLMManager.generate_doc()`, and outputs results.
- **Why:** Enables quick, repeatable documentation generation from various package sources.
- **Variation:** Use `--local=true` to specify the path is a local folder. Swap model to 'gemini' or 'bedrock'.

---

## Additional Developer Notes

- Ensure `python-dotenv` is installed and `.env` is configured for environment variables if required.
- The CLI depends on `src.llm_manager.LLMManager` for the core logic — consulting its documentation is recommended.
- Catching broad exceptions ensures unexpected errors do not crash silently.

---

This documentation integrates the domain concept of CLI-driven package documentation, execution facts about input parameters and behavior, and usage patterns describing how to invoke and adapt the CLI for different tasks.
```


"""