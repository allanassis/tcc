# Rich — README-AI Correctness Evaluation

Tool under evaluation: **README-AI** (v0.6.0rc1, `gpt-4.1-mini-2025-04-14`).
File: `compare-readme-ai/rich_readme_readmeai.md` (single README).

## Environment & Ground-Truth Setup

Same as the README-Gen evaluation: clean venv `/tmp/eval-rich-venv` (Python
3.14.6), `rich 15.0.0`, authoritative `Requires-Python >=3.9.0`, `License:
MIT`; source `pyproject.toml` `python = ">=3.9.0"` with classifiers 3.9–3.14;
`LICENSE` = MIT. `inspect.signature` used for API ground truth.

### Cross-checked sources
1. https://github.com/Textualize/rich (cloned `main`; `pyproject.toml`, `LICENSE`).
2. https://rich.readthedocs.io (official docs).
3. Installed artifact introspection (rich 15.0.0).
4. PyPI metadata `Requires-Python` via `importlib.metadata`.

## Document structure (evaluable content)
- Header/Badges → title "RICH".
- `## Overview` → **empty**.
- `## Features` table → carries Purpose ("Rich is a Python library for rich text and beautiful formatting in the terminal"), Core Capabilities, Supported Python Versions (3.6+), Dependencies, Key Modules, License (MIT).
- `## Project Structure` + Project Index → file tree (ignored per rubric; not an API reference).
- `## Getting Started` → Prerequisites (Python; Tox, Poetry), Installation, Usage, Testing.
- `## Roadmap`, `## Contributing`, `## License`, `## Acknowledgments`.

Per ground rule 7, the empty `## Overview` heading's expected content is carried by the **Features** table, so Overview is evaluated against that table.

---

## Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 exact match | 1 | "RICH" is the project name (uppercased header styling) == repo `rich`. |
| 2 not a different project | 1 | Badges/links all point to Textualize/rich. |
| 3 no hallucinated terminology | 1 | No invented names. |

**T = 100.00**

## Overview (O) — evaluated via Features table (carrier)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality correct | 1 | Features "Purpose": "Rich is a Python library for rich text and beautiful formatting in the terminal." |
| 2 supported by artifacts | 1 | Core Capabilities (rich text, tables, progress, markdown, syntax highlighting, live updating, tracebacks) all exist. |
| 3 no unsupported features | 1 | All listed capabilities are real. |
| 4 correct domain | 1 | Terminal/CLI formatting. |
| 5 terminology matches repo | 1 | Module names rich.console/text/table/progress/syntax/traceback match repo. |

**O = 5/5 × 100 = 100.00** (the `## Overview` heading itself is empty, but the required information is present in the Features table.)

## Installation (I) — executed
Documented paths under "### Installation": (1) `git clone …/rich`; (2) `cd rich`; (3a) **Using tox**: `echo 'INSERT-INSTALL-COMMAND-HERE'`; (3b) **Using poetry**: `poetry install`. Prerequisites list "Python" (no version) and package managers "Tox, Poetry". Features table separately claims "Python 3.6+".

| Rule | Verdict | Evidence |
|---|---|---|
| 1 dependencies declared | **0** | No explicit declaration of Rich's install dependencies; the tox path's install command is the unresolved placeholder `INSERT-INSTALL-COMMAND-HERE`. |
| 2 commands execute unmodified | **0** | Placeholder `echo 'INSERT-INSTALL-COMMAND-HERE'` installs nothing (auto-fail, ground rule 6). `poetry install` cannot run — `poetry` is **not installed** and the README never documents how to obtain it. (`git clone --depth 1` step verified exit 0.) |
| 3 no unresolved dependency errors | **0** | Neither documented install path yields a resolved dependency set (placeholder / missing `poetry`). |
| 4 environment requirements correct | **0** | Prerequisites give no Python version; Features table says "Python 3.6+", contradicting authoritative `Requires-Python >=3.9.0`. Documenting Tox/Poetry as the install mechanism is also inaccurate (Rich is pip-installable). |
| 5 expected artifact produced | **0** | No importable/executable artifact is produced by the documented commands (placeholder produces nothing; poetry path unrunnable). |

**I = 0/5 × 100 = 0.00**

## Usage and Examples (U) — executed
"### Usage" contains two snippets:

| # | Snippet | Executes | E_i | Evidence |
|---|---|---|---|---|
| S1 | **tox**: `echo 'INSERT-RUN-COMMAND-HERE'` | placeholder | **0** | Unresolved placeholder `INSERT-RUN-COMMAND-HERE` (auto-fail, ground rule 6); demonstrates no Rich usage. |
| S2 | **poetry**: `poetry run python {entrypoint}` | no | **0** | Unresolved placeholder `{entrypoint}`; also `poetry` not installed. |

k = 2 documented executable snippets; passes = 0. No real Rich-usage code example exists anywhere in the README.

**U = 0/2 × 100 = 0.00**

## API Reference (A)
The README contains **no API Reference** of functions/classes/methods with
parameters. The Features table "Key Modules" lists module names
(rich.console, rich.text, …) with 3-word descriptions — bare names, no
parameterized elements — and the Project Index lists files only. Section is
absent (ground rule 8).

**A = 0.00** (n = 0 documented API elements → section scores 0).

## License (L)
`## License` section: "Rich is protected under the [LICENSE](https://choosealicense.com/licenses) License." (generic). Features table: "License: MIT License."

| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo LICENSE | 1 | Features table states **MIT**, which matches repo LICENSE (MIT). |
| 2 valid identifier | 1 | "MIT" is a valid SPDX identifier. |
| 3 no conflicting info | 1 | No *different* license is named anywhere; the License section is a vague/generic placeholder ("LICENSE License") but does not assert a conflicting license (e.g., not GPL vs MIT). |

**L = 3/3 × 100 = 100.00** (Caveat: the License *section* text is a generic placeholder; the correct MIT identifier is carried by the Features table.)

---

## C_R (README-AI)
C_R = (T + O + I + U + A + L) / 6 = (100 + 100 + 0 + 0 + 0 + 100) / 6 = **50.00**

| README | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| rich_readme_readmeai.md | 100.00 | 100.00 | 0.00 | 0.00 | 0.00 | 100.00 | 50.00 |
| **average** | 100.00 | 100.00 | 0.00 | 0.00 | 0.00 | 100.00 | **50.00** |

Single-README: average row equals the README row. ✓
