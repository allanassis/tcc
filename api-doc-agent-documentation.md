# API Documentation Agent Package

This package provides an AI-powered agent for generating API documentation by leveraging state-of-the-art language models (LLMs) and following the principles from the paper "A Theory of Robust API Knowledge" (ATORAK).

---

## Conceptual Introduction

### Domain Concepts

- **API Documentation Agent:** A software agent that produces robust API documentation by combining domain concepts, execution facts, and usage patterns.
- **ATORAK Principles:** Completeness, consistency, clarity, correctness, context awareness, and comprehensive coverage to guide the documentation generation.
- **Language Model Providers:** Supports multiple LLM backends such as GPT (OpenAI), Gemini (Google), Bedrock (AWS), and DeepSeek.
- **Dual Chat Modes:** The agent offers two modes for documentation generation:
  - ATORAK-enhanced mode that integrates rich context and structured reasoning.
  - Raw LLM mode using basic prompt instructions without structured ATORAK knowledge.

### Mapping to API Terms

- API documentation generation is initiated by prompts describing the target package or repository.
- The `LLMManager` class manages model setup, prompt composition with ATORAK context, and invoking language models.
- The HTTP server exposes REST routes for interacting with the agent via JSON requests.
- The CLI allows direct command-line invocation with parameters specifying the target path and model.

---

## Execution Facts

### CLI Interface

#### Script: `cli.py`

- **Arguments:**
  - `--path`: Required. Path or URL of the package/repo to document.
  - `--local`: Optional boolean flag indicating if path is local directory.
  - `--model`: Optional choice of LLM model (`gpt`, `gemini`, `bedrock`). Default is `gpt`.

- **Behavior:** Constructs a prompt for generating documentation of the specified package.
- **Output:** Prints the generated API documentation text.
- **Errors:** Prints error message and exits with code 1 on failure.

### HTTP Server Interface

#### Server Routes

- `GET /` - Serves the main interface webpage.
- `POST /atorak/chat/<model>` - Accepts JSON payload with `prompt` key, replies with ATORAK-enhanced response.
- `POST /raw/chat/<model>` - Accepts JSON payload with `prompt` key, replies with raw LLM response.
- Models supported in routes: `gpt`, `gemini`, `bedrock`.

#### Behavior

- Routes use the `LLMManager` to obtain model provider and run the agent.
- ATORAK chat uses an agent initialized with ATORAK context instructions.
- Raw chat uses a general assistant agent with simple helpful instructions.

### LLMManager Class

- Manages multiple LLM backends.
- Providers dictionary maps model names to setup functions.
- Setup functions instantiate model clients with specific IDs.
- `generate_doc(path, model)` generates API docs given a path and model.
- `run_prompt(prompt, model)` runs arbitrary prompt with chosen model.

### Environment Variable Requirements

- `OPENAI_API_KEY` for OpenAI (GPT).
- `GOOGLE_API_KEY` for Google Gemini.
- AWS credentials for Bedrock.
- `DEEPSEEK_API_KEY` for DeepSeek.

---

## API Usage Patterns

### Pattern: Generating API Documentation from CLI

```bash
python cli.py --path "https://github.com/username/repository" --model gpt
```

- **What:** Generates API documentation for a remote GitHub repo using the GPT model.
- **How:** CLI parses args, constructs ATORAK prompt, calls `LLMManager.generate_doc`, prints output.
- **Why:** Simple user interface for on-demand documentation generation.
- **Variation:** Use `--local` for local directories; switch model to `gemini` or `bedrock`.

### Pattern: Using HTTP API Server

- Start server with `python server.py`
- Send POST request to `/atorak/chat/gpt` with JSON body: `{ "prompt": "Generate API doc for XYZ" }`
- Receive structured response JSON including generated docs.
- Switch endpoint to `/raw/chat/gpt` for non-ATORAK raw LLM responses.

### Pattern: Instantiating and Using LLMManager in Code

```python
from src.llm_manager import LLMManager

llm_mgr = LLMManager()

# Generate documentation for a project path
doc_text = llm_mgr.generate_doc('/path/to/project', 'gpt')

# Run a custom prompt
response = llm_mgr.run_prompt('Explain the usage of API XYZ', 'gemini')
```

- **What:** Programmatic access to documentation generation and prompt running.
- **How:** Calls appropriate provider and agent internally.
- **Why:** Enables integration into other Python tools or workflows.

---

## Additional Developer Notes

- Ensure `.env` file is properly configured with API keys before running.
- The documentation quality depends on input prompt clarity and model capabilities.
- ATORAK context improves the robustness and reasoning in generated docs versus raw prompts.
- Extending to new LLM models requires updating `LLMManager` providers.

---

This documentation integrates conceptual introductions, execution facts, and usage patterns according to the practice of creating robust API knowledge and documentation following ATORAK paper principles.