local_example = """
## 5.3 Example

### Input
```
"Generate API documentation for the package located in the following directory ./src/interfaces/cli/cli.py. Try to identify the public APIs of the package and the most important parts of these API to use in the documentation."
You MUST output ONLY the documentation in Markdown format, no more data.
```

### Output
```.md
# CLI Documentation Generator

## Overview

This package provides a command-line interface (CLI) tool designed to generate API documentation for software packages following the ATORAK principles. It leverages Large Language Models (LLMs) such as GPT, Gemini, or Bedrock to assist in creating concise, structured, and pedagogically effective documentation. The tool supports documentation generation from both local directories and remote repositories.

### Features and Capabilities

- Command-line interface for easy integration and automation.
- Supports multiple LLM backends: GPT, Gemini, and Bedrock.
- Accepts package paths as local folders or remote repository URLs.
- Produces documentation emphasizing clarity, relevance, and knowledge transfer.
- Gracefully handles exceptions and provides informative error reporting.

## Installation

1. **Environment Setup**

   Ensure Python 3 is installed.

2. **Clone and Install Dependencies**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   pip install -r requirements.txt
   ```

3. **Environment Variables**

   The CLI uses `dotenv` to load environment variables. Create a `.env` file in the root directory as needed for LLM API keys and configurations.

## Usage and Examples

```bash
python src/interfaces/cli/cli.py --path <package_path> [--local] [--model <model_choice>]
```

### Example 1: Generate documentation for a local package using GPT

```bash
python src/interfaces/cli/cli.py --path ./my_local_package --local True --model gpt
```

### Example 2: Generate documentation for a remote GitHub repository using Bedrock

```bash
python src/interfaces/cli/cli.py --path https://github.com/user/repo --model bedrock
```

Expected output: The generated API documentation printed to standard output.

## API Reference

- `--path`: (Required) The path of the package to document. This can be a local directory or a remote repository URL.
- `--local`: (Optional) Indicates if the package path is local (`True` or `False`). Default is `False`.
- `--model`: (Optional) LLM model to use for documentation generation. Choices are `gpt` (default), `gemini`, `bedrock`.

## Contributing

Contributions are welcome to enhance functionality, add support for more LLM providers, improve error handling, or extend CLI options. Please follow the repository's contribution guidelines:

- Fork the repository.
- Create a dedicated feature branch.
- Submit pull requests with clear descriptions of your changes.
- Include tests where applicable.

## License

This project is licensed under the terms specified in the repository's LICENSE file.

## Contact

For questions, issues, or contributions, please contact the maintainers via the repository's issue tracker or email listed in the project metadata.
```


"""