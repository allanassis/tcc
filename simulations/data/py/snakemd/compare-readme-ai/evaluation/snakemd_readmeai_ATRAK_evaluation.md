# SnakeMD — README-AI ATRAK Evaluation

Dimension 3: Adherence to the Theory of Robust API Knowledge
[Thayer et al. 2021]. Binary presence of K_D / K_E / K_U. **Presence, not
correctness**, with the strict qualifiers: *"listed" is not "communicated"*;
**broken/placeholder commands do not satisfy K_E**; examples that do not show
real API usage do not satisfy K_U. File:
`compare-readme-ai/snakemd_readme_readmeai.md`.

## Ground Truth Reference

- **Project:** SnakeMD
- **Repository:** <https://github.com/TheRenegadeCoder/SnakeMD> (Python, branch `main`)
- **Domain:** programmatic generation of Markdown documents (incl. READMEs) in Python
- **Core domain entities:** `Document` (a Markdown file) composed of `Element`/
  `Block`/`Inline` pieces (`Heading`, `Paragraph`, `MDList`, `Table`, `Code`,
  `Quote`, `Checklist`, `Alert`, `CSVTable`, `TableOfContents`, `Raw`,
  `HorizontalRule`) and `Template`s.
- **Core execution facts:** installable from source with **Poetry**
  (`poetry install`, verified exit 0) or `pip install snakemd`
  (Requires-Python `>=3.10`, MIT); build with `snakemd.new_doc()` + `add_*`;
  render `str(doc)`/`dump()`; **no CLI**; tests via **pytest** (202 tests).
- **Verification:** installed `snakemd==2.4.1`; introspection; shallow clone;
  docs at <https://www.snakemd.io>; documented Poetry install executed.

---

## README — `snakemd_readme_readmeai.md`

| KE | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1** | The Overview and Project Index communicate the core abstraction, not just a list: elements are described as *"foundational building blocks … that can be incorporated into a document"* and `Document` as *"a collection of markdown elements … to assemble these elements into a coherent markdown document,"* with templates as reusable higher-level constructs. This teaches the conceptual vocabulary (Document / element / block / template) needed to understand what SnakeMD represents → K_D satisfied. |
| **K_E Execution Facts** | **1** | Contains real, **verified** execution facts: the documented `git clone` + `poetry install` flow runs to completion (exit 0, installs SnakeMD 2.4.1), and dependency management (Poetry, `pyproject.toml`/`poetry.lock`) and testing (pytest) are correctly stated. At least one genuine, non-broken command present → K_E satisfied. (The `{entrypoint}` placeholder affects only the Usage snippet, not the install facts.) |
| **K_U Usage Patterns** | **0** | There is **no example of real API usage**. The sole usage command is `poetry run python {entrypoint}` — an unresolved placeholder — and there is no code showing `new_doc()`/`add_*`/`str(doc)`. Per *"examples that do not show real API usage do not satisfy K_U"* and *"placeholder commands do not satisfy K_E/K_U"* → K_U not satisfied. |

**K = (1 + 1 + 0)/3 × 100 = 66.67**

---

## ATRAK summary (README-AI)

| readme | K_D | K_E | K_U | K |
|---|---|---|---|---|
| snakemd_readme_readmeai.md | 1 | 1 | 0 | 66.67 |
| **average** | 1.00 | 1.00 | 0.00 | **66.67** |

Single-README evaluation: the `average` row equals the sole data row;
(1 + 1 + 0)/3 × 100 = 66.67. ✔

## Cross-checked sources
- Installed PyPI artifact `snakemd==2.4.1` (introspection).
- Repository: <https://github.com/TheRenegadeCoder/SnakeMD>.
- Official docs: <https://www.snakemd.io>.
- Executed documented Poetry install (exit 0) + pytest collection (202 tests).
