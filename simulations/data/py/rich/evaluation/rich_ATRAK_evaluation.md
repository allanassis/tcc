# Rich — README-Gen ATRAK Evaluation

Dimension 3 assesses **presence, not correctness** of the three Knowledge
Elements [Thayer et al. 2021]. Hallucinated or factually wrong content still
counts as **present**; an element is **absent (0)** only when the carrying
section is empty/missing, is a bare name-only list, or consists solely of
unresolved template placeholders.

## Ground Truth Reference

- **Project:** Rich
- **Repository:** https://github.com/Textualize/rich
- **Domain:** Terminal / CLI rich-text rendering and formatting for Python.
- **Core domain entities:** Console, Style/markup, Text (styled spans),
  renderables, Table/Column, Panel, Progress/Task, Live, Syntax (highlighting),
  Traceback, Tree, Layout, Markdown, Prompt, RichHandler (logging).
- **Core execution facts:** installable via `pip install rich`
  (`Requires-Python >=3.9.0`; deps `markdown-it-py`, `pygments`); constructs
  render to a `Console`; classes accept styling/config parameters; supports
  live/animated output; MIT licensed.
- **Core usage patterns:** create a `Console` and `print` styled markup; build
  `Table`/`Panel`; render `Syntax`; drive `Progress`/`track`; `Live` updates;
  `RichHandler` for logging.

---

## README 1 — `data1.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1 (present)** | "### Domain Concepts" defines Console, Text Styling, Markup & ANSI codes, Syntax Highlighting, Tables & Layouts, Progress Bars, Live Updates, Tracebacks, Panels/Boxes/Trees — each with an explanatory sentence, not bare names. |
| **K_E Execution Facts** | **1 (present)** | Installation (`pip install rich`, Python version claim), dependency/runtime behavior, API constructor/method parameters and defaults, output descriptions. |
| **K_U Usage Patterns** | **1 (present)** | Six runnable code examples (printing, markup, tables, progress, syntax, live) with expected-output prose. |

**K = (1+1+1)/3 × 100 = 100.00**

## README 2 — `data2.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1 (present)** | Overview enumerates Styled Text, Console Rendering, Layouts, Components (Panels/Tables/Trees/Progress/Syntax), Live Updates, High-Level Abstractions — each defined. |
| **K_E Execution Facts** | **1 (present)** | Installation (pip + git source), platform/ANSI constraints, API constructor parameters (Console/Table/Syntax/Panel/Live), expected outputs. |
| **K_U Usage Patterns** | **1 (present)** | Five runnable examples (styled output, table, syntax, progress, live panel) with "Expected:" descriptions. |

**K = 100.00**

## README 3 — `data3.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1 (present)** | "### Key Domain Concepts" defines Styled Text & Markup, Renderable Objects, Layouts & Console, Syntax Highlighting, Progress/Live, Tables/Grids, Tracebacks/Logging. |
| **K_E Execution Facts** | **1 (present)** | Installation (pip + `rich[jupyter]` extra), cross-platform note, API parameters/defaults, logging configuration facts. |
| **K_U Usage Patterns** | **1 (present)** | Four runnable usage examples + a `RichHandler` logging usage example, each with output prose. |

**K = 100.00**

---

## Summary (README-Gen ATRAK)

| README | K_D | K_E | K_U | ATRAK % |
|---|---|---|---|---|
| data1.md | 1 | 1 | 1 | 100.00 |
| data2.md | 1 | 1 | 1 | 100.00 |
| data3.md | 1 | 1 | 1 | 100.00 |
| **average** | 1.00 | 1.00 | 1.00 | **100.00** |
