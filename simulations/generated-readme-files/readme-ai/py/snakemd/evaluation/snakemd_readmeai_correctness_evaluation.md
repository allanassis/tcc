# SnakeMD — README-AI Correctness Evaluation

Tool: **README-AI** · Project: **SnakeMD** · Repository:
<https://github.com/TheRenegadeCoder/SnakeMD> · Core functionality (per
manifest): **Generate README files** · File evaluated:
`compare-readme-ai/snakemd_readme_readmeai.md`

## Ground-Truth Verification (sources cross-checked)

Same verified ground truth as the README-Gen evaluation:

- Installed `snakemd==2.4.1` in `/tmp/eval-snakemd-venv`; `Summary: "A markdown
  generation library for Python."`, `License: MIT`, `Requires-Python
  >=3.10,<4.0`. Public API = `snakemd.new_doc() -> Document` + `Document.add_*`
  methods; render via `str(doc)`/`doc.dump()`. **No CLI.**
- Repository (shallow clone + <https://github.com/TheRenegadeCoder/SnakeMD>,
  <https://www.snakemd.io>): branch `main`; uses **Poetry** (`pyproject.toml`,
  `poetry.lock`); `LICENSE` = MIT; test framework = **pytest** (202 tests).
- **Documented install flow executed**: `git clone` → `cd SnakeMD` →
  `poetry install` (Poetry 2.4.1 in `/tmp/poetry-venv`) → **exit 0**,
  `Installing the current project: SnakeMD (2.4.1)` plus dev deps (pytest,
  sphinx, pylint …). The library becomes importable.

The README describes SnakeMD as *"a Python library that streamlines the
programmatic creation of rich, structured Markdown documents"* using a
`Document` class — this **matches reality**. Two unresolved template
placeholders are present: `{entrypoint}` (Usage) and `{__test_framework__}`
(Testing); the License section body is a generic `choosealicense.com`
placeholder.

---

## Section-by-section

### Project Title (T)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Matches repo/official name | 1 | "SNAKEMD" = repo name (case-insensitive) |
| 2 | Not a different project | 1 | Names SnakeMD only |
| 3 | No hallucinated terms in title | 1 | Plain name |

**T = 100.00**

### Overview (O)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Primary functionality correct | 1 | "Python library … programmatic creation of … Markdown documents" — matches |
| 2 | Supported by artifacts | 1 | `Document` class + element/template modules exist (verified) |
| 3 | No unsupported features | 1 | Bullets (Document assembly; headings/lists/tables/alerts/checklists; CI/CD publishing; MIT) all map to real code (`add_table`, `add_alert`, `add_checklist`, `.github/workflows`) |
| 4 | Correct domain | 1 | Markdown generation domain correctly identified |
| 5 | Terminology matches repo | 1 | "Document", "elements", "templates", "Markdown" are repo terms |

**O = 100.00**

### Installation (I) — executed
Documented: clone → `cd SnakeMD` → `poetry install`; prereqs Python + Poetry.
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Dependencies declared | 1 | Poetry-managed (`pyproject.toml`/`poetry.lock`); prereqs list Python + Poetry |
| 2 | Commands execute unmodified | 1 | clone + `poetry install` ran verbatim → exit 0 |
| 3 | No unresolved dependency errors | 1 | All deps resolved/installed |
| 4 | Env requirements correct | 1 | Python + Poetry correct; consistent with `Requires-Python >=3.10` |
| 5 | Produces expected artifact | 1 | `Installing the current project: SnakeMD (2.4.1)` — library importable (README claims a library, not a CLI) |

**I = 5/5 × 100 = 100.00**

### Usage and Examples (U) — executed
| Snippet | Executed | E_i | Evidence |
|---|---|---|---|
| `poetry run python {entrypoint}` | fail | 0 | Unresolved placeholder `{entrypoint}` → auto-fail (prompt rule 6); no runnable entry given |

The only "how to use the tool" demonstration is the placeholder command; there
is no real library-usage code example (e.g. `new_doc()`/`add_*`). `poetry run
pytest` is a test-suite command (Testing section), not a usage demonstration,
and its description also contains the `{__test_framework__}` placeholder.
**k = 1, ΣE = 0 → U = 0.00**

### API Reference (A)
The README has **no API Reference section** documenting functions/classes with
parameters. The Features table and Project Index mention a "Document class" and
module summaries, but no method signatures, parameters, return types, or
endpoints are documented. Per the ground rule "if a README lacks a section
entirely, that section scores 0", there are no API elements to validate.

**n = 0 documented API elements → A = 0.00**

### License (L)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Matches repo LICENSE | 1 | README communicates MIT (license badge `github/license` + Overview "MIT licensed"); repo `LICENSE` = MIT. Correct license is documented (via the only non-placeholder carriers). |
| 2 | Valid identifier | 1 | "MIT" is a valid SPDX identifier |
| 3 | No conflicting license info | 1 | No second/different license stated; the License-section prose is a vague placeholder but not a *conflicting* license |

**L = 3/3 × 100 = 100.00**

Note: the dedicated License section body is a broken `choosealicense.com`
placeholder; credit for L comes from the accurate MIT signals elsewhere (badge
+ Overview) per ground rule 7 (evaluate the actual carrier of the information).
Correctness measures factual accuracy, and no incorrect license is asserted.

---

**C_R = (100 + 100 + 100 + 0 + 0 + 100) / 6 = 400/6 = 66.67**

## Summary

| readme | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| snakemd_readme_readmeai.md | 100 | 100 | 100 | 0 | 0 | 100 | 66.67 |
| **average** | 100 | 100 | 100 | 0 | 0 | 100 | **66.67** |

Single-README evaluation: the `average` row equals the sole data row. ✔

## Cross-checked sources
- Installed PyPI artifact `snakemd==2.4.1` (pip show / importlib.metadata / inspect).
- Repository: <https://github.com/TheRenegadeCoder/SnakeMD> (shallow clone + web).
- Official docs: <https://www.snakemd.io>.
- Executed documented install flow with Poetry 2.4.1 (`/tmp/poetry-venv`) →
  `poetry install` exit 0; `poetry run pytest --co` → 202 tests (framework =
  pytest).
