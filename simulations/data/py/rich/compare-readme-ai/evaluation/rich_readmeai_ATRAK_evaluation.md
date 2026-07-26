# Rich — README-AI ATRAK Evaluation

Dimension 3 assesses **presence, not correctness**. An element is **absent (0)**
only when the carrying section is empty/missing, is a bare name-only list, or
consists solely of unresolved template placeholders. Otherwise it is present,
even if incorrect.

File: `compare-readme-ai/rich_readme_readmeai.md`.

## Ground Truth Reference
- **Project:** Rich
- **Repository:** https://github.com/Textualize/rich
- **Domain:** Terminal / CLI rich-text rendering and formatting for Python.
- **Core domain entities:** Console, Style/markup, Text, renderables,
  Table/Column, Panel, Progress/Task, Live, Syntax, Traceback, Tree, Layout,
  Markdown, Prompt, RichHandler.
- **Core execution facts:** `pip install rich` (`Requires-Python >=3.9.0`; deps
  `markdown-it-py`, `pygments`); renders to a Console; MIT licensed.
- **Core usage patterns:** create Console + print markup; Table/Panel; Syntax;
  Progress/track; Live; RichHandler logging.

---

## Per-Element Evidence & Verdict

### K_D — Domain Concepts → **1 (present)**
The Features table provides evaluable conceptual content beyond bare names:
a Purpose statement ("Rich is a Python library for rich text and beautiful
formatting in the terminal"), Core Capabilities described with explanatory
phrases ("Rich text rendering with colors, styles, and emojis"; "Advanced
terminal formatting (tables, progress bars, markdown, syntax highlighting)";
"Tracebacks with syntax highlighting"), and Key Modules each with a short
gloss ("rich.console (console output management)", "rich.progress (progress
bars)"). This is names **with** explanation, so it is not a bare name-only
list → present.

### K_E — Execution Facts → **1 (present)**
Multiple runtime/installation facts are present (even where inaccurate):
Prerequisites (Python; Tox, Poetry), Installation steps (`git clone`,
`poetry install`), Supported Python Versions ("Python 3.6+"), Dependencies
("Minimal dependencies… uses `colorama` on Windows"), Testing (`poetry run
pytest`), License (MIT). Presence of execution facts is satisfied.

### K_U — Usage Patterns → **0 (absent)**
The only "Usage" content consists of unresolved template placeholders:
`echo 'INSERT-RUN-COMMAND-HERE'` (tox) and `poetry run python {entrypoint}`
(poetry, with `{entrypoint}` placeholder). There is **no** code example or
tutorial demonstrating how Rich itself is applied. The Contributing/Installation
shell commands are generic git/dev-workflow steps, not demonstrations of using
the Rich library. Per the explicit absent-rule ("the only candidate content
consists of unresolved template placeholders"), K_U is absent.

---

## Summary (README-AI ATRAK)

| README | K_D | K_E | K_U | ATRAK % |
|---|---|---|---|---|
| rich_readme_readmeai.md | 1 | 1 | 0 | 66.67 |
| **average** | 1.00 | 1.00 | 0.00 | **66.67** |

K = (1 + 1 + 0) / 3 × 100 = 66.67. Single-README: average equals the README row. ✓
