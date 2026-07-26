# SnakeMD — ATORAK Adherence Evaluation (Completeness)

**Methodology:** Section 4.4.3 of *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis*.

**Scope:** Completeness-only evaluation — assesses whether each Knowledge Element defined by the Theory of Robust API Knowledge is *present* in the generated README, regardless of factual correctness.

**Theory of Robust API Knowledge (ATORAK)** [Thayer et al. 2021] defines three Knowledge Elements that a robust API document must communicate:

- **KD — Domain Concepts:** Conceptual vocabulary, entities, and relationships that define the problem domain the API operates in. Mapped to the **Overview** section.
- **KE — Execution Facts:** Concrete facts about how the API behaves — commands, parameters, return values, environment requirements, installation steps. Mapped to the **Installation** and **API Reference** sections.
- **KU — Usage Patterns:** Recurring, purposeful combinations of API calls that solve real problems. Mapped to the **Usage and Examples** section.

Each element is binary: Ki ∈ {0, 1}. Ki = 1 if the knowledge element is present (the README contains a section/content that attempts to cover it); Ki = 0 otherwise.

The adherence score per README is:

```
Kpercentage = (KD + KE + KU) / 3 × 100
```

The final score across the three generated READMEs is:

```
Kavg = (K1 + K2 + K3) / 3
```

---

## data1.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

**Criterion:** Does the README contain content that attempts to communicate the conceptual vocabulary and domain of the tool?

**Evidence in data1.md:**

The **Overview** section contains an explicit **"Domain Concepts"** subsection with four bullet points:
- **Markdown Parsing** — describes the concept of processing Markdown content.
- **Python Code Execution** — describes embedded Python code execution.
- **Resume/CV Styling** — describes the styling output domain.
- **Templating and Export** — describes conversion and export concepts.

The Overview also provides a narrative paragraph identifying the software domain ("resume writing and web publishing") and explaining the purpose of the tool.

**Assessment:** The README clearly contains a dedicated Domain Concepts subsection within the Overview. It attempts to communicate the conceptual vocabulary and domain of the tool. The presence criterion is satisfied regardless of whether the described domain is factually correct.

**KD = 1** ✅

---

#### KE — Execution Facts

**Criterion:** Does the README contain content that attempts to communicate execution facts — installation commands, API signatures, parameters, environment requirements?

**Evidence in data1.md:**

- **Installation section** is present with `pip install snakemd` command and a Python version requirement ("Python 3.6+").
- **API Reference section** is present, documenting:
  - `SnakeMD` class description.
  - `SnakeMD.render(markdown_text: str) -> str` — method with parameter type and return type.
  - `SnakeMD.render_file(input_path: str) -> str` — method with parameter type and return type.
  - CLI options: `snakemd <input_file>`, `-o/--output`, `-h/--help`.

**Assessment:** The README contains both an Installation section and an API Reference section, both of which attempt to communicate execution facts. The presence criterion is satisfied.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Criterion:** Does the README contain content that attempts to demonstrate usage patterns through examples?

**Evidence in data1.md:**

The **Usage and Examples** section is present with three subsections:
1. **Command Line Interface (CLI) Usage** — provides a CLI invocation example with explanation of arguments.
2. **Example Markdown snippet with embedded Python code** — shows a Markdown template example.
3. **Using SnakeMD as a Python Library** — provides a Python code snippet with `from snakemd import SnakeMD`, instantiation, and a `converter.render()` call.

Each pattern includes a code block and a prose explanation of what it does.

**Assessment:** The README contains a dedicated Usage and Examples section with multiple code-based usage patterns. The presence criterion is satisfied.

**KU = 1** ✅

---

### data1.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data1.md ATORAK Score: 100**

---

## data2.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

**Criterion:** Does the README contain content that attempts to communicate the conceptual vocabulary and domain of the tool?

**Evidence in data2.md:**

The **Overview** section contains an explicit **"Domain Concepts"** subsection with five bullet points:
- **Markdown Notes** — describes the core concept of managing Markdown-formatted notes.
- **Interactive Note Navigation** — describes the game-like navigation concept.
- **File-based Note Storage** — describes the storage model.
- **Real-time Editing** — describes the editing concept.
- **Cross-platform Behavior** — describes the runtime environment concept.

The Overview also provides a narrative paragraph identifying the software domain and purpose.

**Assessment:** The README contains a dedicated Domain Concepts subsection within the Overview. It attempts to communicate the conceptual vocabulary and domain of the tool. The presence criterion is satisfied.

**KD = 1** ✅

---

#### KE — Execution Facts

**Criterion:** Does the README contain content that attempts to communicate execution facts — installation commands, API signatures, parameters, environment requirements?

**Evidence in data2.md:**

- **Installation section** is present with:
  - Prerequisites listed (Python 3.6+, Git, terminal with curses support).
  - Step-by-step commands: `git clone`, `python3 -m venv`, `pip install -r requirements.txt`, `python snakemd.py`.
- **API Reference section** is present, documenting:
  - `Game` class with description.
  - `NoteManager` class with description.
  - `Snake` class with description.
  - `Renderer` class with description.
  - `Game.run()` — method with behavioral description.
  - `NoteManager.load_notes(directory)` — method with parameter.
  - `NoteManager.save_note(note)` — method with parameter.
  - `Snake.move(direction)` — method with parameter.
  - `Renderer.draw()` — method with description.

**Assessment:** The README contains both an Installation section and an API Reference section, both of which attempt to communicate execution facts. The presence criterion is satisfied.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Criterion:** Does the README contain content that attempts to demonstrate usage patterns through examples?

**Evidence in data2.md:**

The **Usage and Examples** section is present with:
- A numbered list of six interaction steps (Navigate notes, Select a note, Edit or create notes, Save notes, Create new notes, Delete notes) — each describing a usage pattern with a *what* and *how*.
- A **Running the Application** subsection with a code block (`python snakemd.py`) and a prose description of what happens after running it.

**Assessment:** The README contains a Usage and Examples section that attempts to demonstrate usage patterns. Although the patterns are described procedurally rather than through code snippets, the section is present and communicates how to use the tool. The presence criterion is satisfied.

**KU = 1** ✅

---

### data2.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data2.md ATORAK Score: 100**

---

## data3.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

**Criterion:** Does the README contain content that attempts to communicate the conceptual vocabulary and domain of the tool?

**Evidence in data3.md:**

The **Overview** section contains an explicit **"Domain Concepts"** subsection with four bullet points:
- **Markdown Syntax** — describes the markup language concept.
- **Terminal Rendering** — describes the output rendering concept.
- **Text Parsing and Tokenization** — describes the parsing process concept.
- **Themes and Styling** — describes the styling concept.

The Overview also provides a narrative paragraph identifying the software domain ("terminal rendering of Markdown") and explaining the purpose of the tool.

**Assessment:** The README contains a dedicated Domain Concepts subsection within the Overview. It attempts to communicate the conceptual vocabulary and domain of the tool. The presence criterion is satisfied.

**KD = 1** ✅

---

#### KE — Execution Facts

**Criterion:** Does the README contain content that attempts to communicate execution facts — installation commands, API signatures, parameters, environment requirements?

**Evidence in data3.md:**

- **Installation section** is present with:
  - Prerequisites listed (Node.js version 12+, npm).
  - `npm install -g snakemd` (global install command).
  - `npm install snakemd` (local install command).
- **API Reference section** is present, documenting:
  - `snakemd(markdown: string): string` — function signature with parameter type, return type, and behavioral description.
  - A **Key Execution Facts** subsection listing supported Markdown elements (headers, bold/italic, code blocks, lists, blockquotes, links) and behavioral notes (ANSI escape sequences, syntax highlighting, graceful fallback).

**Assessment:** The README contains both an Installation section and an API Reference section, both of which attempt to communicate execution facts. The presence criterion is satisfied.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Criterion:** Does the README contain content that attempts to demonstrate usage patterns through examples?

**Evidence in data3.md:**

The **Usage and Examples** section is present with three subsections:
1. **Using SnakeMD as a CLI Tool** — provides `snakemd README.md` command with explanation.
2. **Rendering from Standard Input** — provides `cat README.md | snakemd` pipe pattern with explanation of when to use it.
3. **Using SnakeMD Programmatically** — provides a JavaScript code snippet with `require("snakemd")`, file reading, and `snakemd(markdownText)` call.

Each pattern includes a code block and a prose explanation of what it does and why it is useful.

**Assessment:** The README contains a dedicated Usage and Examples section with three distinct usage patterns, each with code and explanation. The presence criterion is satisfied.

**KU = 1** ✅

---

### data3.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data3.md ATORAK Score: 100**

---

## Summary: All Three SnakeMD READMEs — ATORAK Adherence

| README | KD (Domain Concepts) | KE (Execution Facts) | KU (Usage Patterns) | Kpercentage |
|--------|---------------------|---------------------|---------------------|-------------|
| data1.md | 1 | 1 | 1 | **100** |
| data2.md | 1 | 1 | 1 | **100** |
| data3.md | 1 | 1 | 1 | **100** |

### Final Average Score (Equation 16 from TCC §4.4.3)

```
Kavg = (100 + 100 + 100) / 3 = 100
```

**snakemd ATORAK Average Score: 100**

---

## Analysis and Observations

**Why all three score 100 on ATORAK completeness adherence:**

All three generated READMEs follow the same structural template defined in the prompting strategy (§3.4 of the TCC). The prompt explicitly instructs the LLM to include:
- An **Overview** section with a **Domain Concepts** subsection → satisfies KD.
- An **Installation** section and an **API Reference** section → satisfies KE.
- A **Usage and Examples** section with code snippets → satisfies KU.

Because the LLM consistently follows the structural prompt, all three knowledge elements are present in every generated README, regardless of whether the content is factually correct.

**Key insight — completeness vs. correctness divergence:**

The ATORAK completeness score (100/100 for all three) stands in sharp contrast to the correctness scores from §4.4.2 (43.33, 36.67, 33.33). This reveals a critical finding: the LLM reliably produces structurally complete READMEs that satisfy the ATORAK knowledge element presence requirement, but the content of those elements is entirely hallucinated for a non-famous library like snakemd.

- **data1.md** — Invents a Markdown-to-HTML resume converter. All three knowledge elements are structurally present but describe a different product.
- **data2.md** — Invents a Snake-game-inspired note-taking terminal app. All three knowledge elements are structurally present but describe a different product.
- **data3.md** — Invents a Node.js terminal Markdown renderer. All three knowledge elements are structurally present but describe a different product (and wrong ecosystem).

**Conclusion:** For snakemd, the ATORAK completeness evaluation confirms that the prompting strategy successfully enforces structural adherence to the Theory of Robust API Knowledge. The failure mode is not structural incompleteness but semantic hallucination — the LLM fills the correct structural slots with incorrect content. This distinction is important for interpreting the evaluation results: a README can score 100 on ATORAK completeness while scoring near 0 on correctness.
