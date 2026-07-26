# SnakeMD — README-Gen ATRAK Evaluation

Dimension 3: Adherence to the Theory of Robust API Knowledge
[Thayer et al. 2021]. Binary presence of K_D / K_E / K_U per README. This
dimension assesses **presence, not correctness**: content that is factually
wrong or hallucinated still counts as present — factual accuracy is already
penalized by the correctness dimension and is not double-counted here. An
element is absent only when the README provides no evaluable content for it
(empty/missing carrying section, bare name-only list, or unresolved template
placeholders).

## Ground Truth Reference

- **Project:** SnakeMD
- **Repository:** <https://github.com/TheRenegadeCoder/SnakeMD> (Python, branch `main`)
- **Domain:** programmatic generation of Markdown documents (incl. READMEs) in Python
- **Core domain entities:** `Document` (a Markdown file), composable `Element`/
  `Block`/`Inline` pieces (`Heading`, `Paragraph`, `MDList`, `Table`, `Code`,
  `Quote`, `Checklist`, `Alert`, `CSVTable`, `TableOfContents`, `Raw`,
  `HorizontalRule`), and `Template`s.
- **Core execution facts:** install `pip install snakemd` (Requires-Python
  `>=3.10,<4.0`, MIT, no runtime deps); build a doc with `snakemd.new_doc()`
  and `Document.add_*` methods; render with `str(doc)` / `doc.dump(name)`;
  **no CLI**; tests run under **pytest**.
- **Verification:** installed `snakemd==2.4.1` into `/tmp/eval-snakemd-venv`
  (introspection); shallow clone; docs at <https://www.snakemd.io>; npm probe
  (E404).

> Note: the factual findings below (broken commands, hallucinated APIs) are
> recorded for traceability but do **not** reduce ATRAK presence scores; they
> are penalized in the correctness evaluation
> (`snakemd_correctness_evaluation.md`).

---

## README 1 — `data1.md`

| KE | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1** | Dedicated "Domain Concepts" section that *defines* concepts with explanatory vocabulary (Markdown Parsing, Python Code Execution, Resume/CV Styling, Templating & Export) — evaluable conceptual content, not a name-only list. The described domain is hallucinated, but presence is satisfied. |
| **K_E Execution Facts** | **1** | Installation and configuration facts present: `pip install snakemd` (verified working, exit 0), stated inputs/outputs/return types, and environment requirements. Evaluable execution content present. |
| **K_U Usage Patterns** | **1** | Usage and Examples section contains concrete code examples (e.g., `SnakeMD().render(...)`) and CLI invocations with explanatory text. The demonstrated API is hallucinated (ImportError on execution — penalized under correctness), but the section carries real evaluable usage content, not placeholders. |

**K(data1) = (1 + 1 + 1)/3 × 100 = 100.00**

## README 2 — `data2.md`

| KE | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1** | "Domain Concepts" section defines Markdown Notes, Interactive Note Navigation, File-based Storage, Real-time Editing, Cross-platform behavior with explanatory vocabulary. Hallucinated domain, but evaluable conceptual content present. |
| **K_E Execution Facts** | **1** | Installation section documents concrete commands (`pip install -r requirements.txt`, `python snakemd.py`) and environment facts ("Python 3.6+", curses). The commands are broken against the real repository (penalized under correctness: I = 0), but they are actual documented execution content, not placeholders. |
| **K_U Usage Patterns** | **1** | Usage section demonstrates how to run and interact with the (hallucinated) application, including invocation commands and interaction walkthrough. Evaluable usage content present. |

**K(data2) = (1 + 1 + 1)/3 × 100 = 100.00**

## README 3 — `data3.md`

| KE | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1** | "Domain Concepts" section defines Markdown Syntax, Terminal Rendering, Text Parsing/Tokenization, Themes & Styling with explanatory vocabulary. Hallucinated Node/terminal domain, but evaluable conceptual content present. |
| **K_E Execution Facts** | **1** | Installation section documents `npm install snakemd` and environment requirements (Node.js 12+). Factually wrong for this Python project (npm E404 — penalized under correctness: I = 0), but concrete documented execution content, not placeholders. |
| **K_U Usage Patterns** | **1** | Usage and Examples section provides code snippets (`require("snakemd")`) and CLI examples (`snakemd README.md`) with expected outputs. Hallucinated tool, but evaluable usage content present. |

**K(data3) = (1 + 1 + 1)/3 × 100 = 100.00**

---

## ATRAK summary (README-Gen)

| readme | K_D | K_E | K_U | K |
|---|---|---|---|---|
| data1.md | 1 | 1 | 1 | 100.00 |
| data2.md | 1 | 1 | 1 | 100.00 |
| data3.md | 1 | 1 | 1 | 100.00 |
| **average** | 1.00 | 1.00 | 1.00 | **100.00** |

Average consistency check: mean K = (100 + 100 + 100)/3 = 100.00;
column means (1.00, 1.00, 1.00) → 100.00. ✔

## Note on presence vs correctness

All three READMEs carry substantive (though largely hallucinated) content in
the sections mapped to each Knowledge Element: Overview → K_D,
Installation/API facts → K_E, Usage and Examples → K_U. Under the
presence-only rule, hallucinated-but-evaluable content counts as present;
its inaccuracy is fully reflected in the correctness scores (C_R averages
36.67 for these files). None of the three failure modes for absence
(empty section, name-only list, unresolved placeholders) occurs in these
READMEs.
