# SnakeMD README Correctness Evaluation

**Methodology:** Section 4.4.2 of *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis*.

**Documentation Sources Cross-checked:**
- Official SnakeMD package installed: `pip install snakemd` → v2.4.0 (Python 3.13, macOS)
- `pip show snakemd` → `License: MIT`, `Requires-Python: >=3.10,<4.0`, `Summary: A markdown generation library for Python.`
- `importlib.metadata.metadata('snakemd')` → confirmed `Requires-Python: >=3.10,<4.0`
- SnakeMD GitHub repository: https://github.com/TheRenegadeCoder/SnakeMD
- SnakeMD LICENSE file (GitHub raw): `MIT License` — confirmed MIT
- SnakeMD official documentation: https://www.snakemd.io
- Live execution of all code snippets via `python3 -c "..."` in isolated shell
- `python3 -c "import snakemd; print(dir(snakemd))"` → public API confirmed: `Alert`, `Block`, `CSVTable`, `Checklist`, `Code`, `Document`, `Element`, `Heading`, `HorizontalRule`, `Inline`, `MDList`, `Paragraph`, `Quote`, `Raw`, `Table`, `TableOfContents`, `Template`, `new_doc`
- `shutil.which('snakemd')` → `None` (no CLI binary installed)
- `help(snakemd.Document)` → confirmed methods: `add_heading`, `add_paragraph`, `add_unordered_list`, `add_ordered_list`, `add_code`, `add_table`, `add_table_of_contents`, `add_block`, `add_checklist`, `add_alert`, `add_quote`, `add_raw`, `add_horizontal_rule`, `dump`, `get_elements`, `scramble`
- `help(snakemd.Inline)` → confirmed signature: `Inline(text, image=None, link=None, bold=False, italics=False, strikethrough=False, code=False, linebreak=False)`

---

## Scoring Formula (from TCC §4.4.2)

Each section uses binary criteria Vᵢ ∈ {0,1}. Section scores are percentages. Final score:

```
CR = (T + O + I + U + A + L) / 6
```

---

## data1.md Evaluation

### Step-by-step Reasoning

**Project Title (T)**

Criteria:
1. Title exactly matches repository/official name → README title is "SnakeMD". The official PyPI package name is `snakemd`, GitHub repo is `TheRenegadeCoder/SnakeMD`. The title matches. ✅ V1=1
2. Title does not describe a different project → Correct, title is "SnakeMD". ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucination in the title itself. ✅ V3=1

**T = (1+1+1)/3 × 100 = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → data1 describes SnakeMD as "a command-line tool and Python library designed to convert Markdown or a subset of Markdown with embedded Python code into styled, easy-to-read HTML resumes or CVs." This is **entirely wrong**. SnakeMD is a **Markdown generation library** — it generates Markdown documents programmatically in Python. It does not convert Markdown to HTML, does not produce resumes/CVs, and has no CLI. Confirmed via `pip show snakemd` ("A markdown generation library for Python.") and official docs at https://www.snakemd.io. ❌ V1=0
2. Described functionality supported by repository artifacts → "Markdown Parsing", "Python Code Execution", "Resume/CV Styling", "Templating and Export" — none of these are real SnakeMD features. `dir(snakemd)` shows `Document`, `Heading`, `Paragraph`, `MDList`, `Table`, `Code`, etc. — all for generating Markdown, not parsing or converting it. ❌ V2=0
3. Overview does not describe unsupported features → The overview describes a completely different product (a Markdown-to-HTML resume converter). All described features are unsupported. ❌ V3=0
4. Correctly identifies software domain → "resume writing and web publishing" is wrong. The actual domain is programmatic Markdown document generation. ❌ V4=0
5. Terminology matches repository terminology → "HTML resumes", "embedded Python code", `{{ ... }}` placeholders — none of this terminology appears in the actual SnakeMD codebase or documentation. ❌ V5=0

**O = (0+0+0+0+0)/5 × 100 = 0**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → `pip install snakemd` is the correct install command. No additional dependencies required. ✅ V1=1
2. Installation commands execute without modification → `pip install snakemd` executes successfully (v2.4.0 installed, confirmed). ✅ V2=1
3. No unresolved dependency errors → Clean install confirmed. ✅ V3=1
4. Documented environment requirements correct → data1 states "Ensure Python 3.6+ is installed." However, `importlib.metadata` confirms `Requires-Python: >=3.10,<4.0`. Python 3.6 is factually incorrect for snakemd 2.4.0. ❌ V4=0
5. Installation produces expected executable artifact → `import snakemd` works post-install. However, data1 claims a CLI tool (`snakemd input_resume.md -o output_resume.html`) is produced. `shutil.which('snakemd')` returns `None` — no CLI binary is installed. The documented executable artifact (CLI) does not exist. ❌ V5=0

**I = (1+1+1+0+0)/5 × 100 = 60**

---

**Usage and Examples (U)**

Snippets evaluated (k=3 distinct executable blocks):

| # | Snippet | Execution Result | Output Match | Score |
|---|---------|-----------------|--------------|-------|
| E1 | CLI: `snakemd input_resume.md -o output_resume.html` | `shutil.which('snakemd')` → `None`. No CLI binary exists. Command fails with "command not found". ❌ | N/A — command does not exist | 0 |
| E2 | `from snakemd import SnakeMD; converter = SnakeMD(); html_output = converter.render(markdown_text)` | `from snakemd import SnakeMD` raises `ImportError: cannot import name 'SnakeMD' from 'snakemd'`. Class `SnakeMD` does not exist. ❌ | N/A — import fails | 0 |
| E3 | Markdown snippet with `{{ ... }}` Python code blocks | This is not a code snippet to execute — it is a Markdown example. However, it describes a feature (`{{ ... }}` Python evaluation) that does not exist in SnakeMD. Not executable as a standalone snippet. ❌ | Feature does not exist | 0 |

**U = 0/3 × 100 = 0**

---

**API Reference (A)**

Documented API elements (n=4):

| # | Element | Exists | Names Correct | Params Correct | Returns Correct | Behavior Correct | Not Deprecated | Score |
|---|---------|--------|--------------|----------------|-----------------|-----------------|----------------|-------|
| A1 | `SnakeMD` class | ❌ Does not exist. `hasattr(snakemd, 'SnakeMD')` → `False`. The actual main class is `Document`. | ❌ | ❌ | ❌ | ❌ | N/A | 0 |
| A2 | `SnakeMD.render(markdown_text: str) -> str` | ❌ Method does not exist. `Document` has no `render()` method. Confirmed via `help(snakemd.Document)`. | ❌ | ❌ | ❌ | ❌ | N/A | 0 |
| A3 | `SnakeMD.render_file(input_path: str) -> str` | ❌ Method does not exist. `Document` has no `render_file()` method. Confirmed via `help(snakemd.Document)`. | ❌ | ❌ | ❌ | ❌ | N/A | 0 |
| A4 | CLI options: `snakemd <input_file>`, `-o/--output`, `-h/--help` | ❌ No CLI binary exists. `shutil.which('snakemd')` → `None`. | ❌ | ❌ | ❌ | ❌ | N/A | 0 |

**A = 0/4 × 100 = 0**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → README states "MIT License". GitHub raw LICENSE confirms `MIT License`. ✅ V1=1
2. License identifier is valid → "MIT" is a valid SPDX identifier. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

**L = (1+1+1)/3 × 100 = 100**

---

### data1.md Final Score

```
CR = (100 + 0 + 60 + 0 + 0 + 100) / 6 = 43.33
```

**data1.md scores 43.33.** The README is a near-complete hallucination of a different product. The LLM invented a Markdown-to-HTML resume converter with a `SnakeMD` class, `render()` and `render_file()` methods, a CLI tool, and `{{ ... }}` Python embedding syntax — none of which exist in the actual SnakeMD package. The actual SnakeMD is a programmatic Markdown *generation* library. Only the title, the `pip install snakemd` command, and the MIT license are correct.

---

## data2.md Evaluation

### Step-by-step Reasoning

**Project Title (T)**

Criteria:
1. Title exactly matches repository/official name → "SnakeMD" matches official name. ✅ V1=1
2. Title does not describe a different project → Correct. ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucination. ✅ V3=1

**T = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → data2 describes SnakeMD as "a lightweight, markdown-based note-taking application inspired by the classic Snake game." This is **entirely wrong**. SnakeMD is a Markdown generation library. It has no game mechanics, no note-taking features, and no terminal UI. Confirmed via `pip show snakemd` ("A markdown generation library for Python."). ❌ V1=0
2. Described functionality supported by repository artifacts → "Interactive Note Navigation", "File-based Note Storage", "Real-time Editing", "Cross-platform terminal behavior" — none of these features exist in SnakeMD. `dir(snakemd)` shows only Markdown generation classes. ❌ V2=0
3. Overview does not describe unsupported features → The entire overview describes a completely different product (a Snake-game-inspired note-taking app). All features are unsupported. ❌ V3=0
4. Correctly identifies software domain → "note-taking application" and "game mechanic" are wrong. The actual domain is programmatic Markdown document generation. ❌ V4=0
5. Terminology matches repository terminology → "snake", "arrow keys", "WASD", "curses", "note blocks" — none of this terminology appears in the actual SnakeMD codebase. ❌ V5=0

**O = (0+0+0+0+0)/5 × 100 = 0**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → `pip install -r requirements.txt` is listed, but SnakeMD has no `requirements.txt` for end users — it is installed via `pip install snakemd`. The `git clone` approach is valid for source install. ✅ V1=1
2. Installation commands execute without modification → `git clone https://github.com/TheRenegadeCoder/SnakeMD.git` and `pip install -r requirements.txt` — the clone URL is correct. However, `pip install -r requirements.txt` would fail if no `requirements.txt` exists in the repo (SnakeMD uses `pyproject.toml`). The final step `python snakemd.py` fails because there is no `snakemd.py` script — SnakeMD is a library. ❌ V2=0
3. No unresolved dependency errors → `pip install -r requirements.txt` would fail (no such file). ❌ V3=0
4. Documented environment requirements correct → data2 states "Python 3.6 or higher". `Requires-Python: >=3.10,<4.0` confirmed. Python 3.6 is factually incorrect. ❌ V4=0
5. Installation produces expected executable artifact → data2 claims `python snakemd.py` runs the application. No such script exists — SnakeMD is a library, not a runnable script. ❌ V5=0

**I = (1+0+0+0+0)/5 × 100 = 20**

---

**Usage and Examples (U)**

Snippets evaluated (k=1 distinct executable block):

| # | Snippet | Execution Result | Output Match | Score |
|---|---------|-----------------|--------------|-------|
| E1 | `python snakemd.py` | No `snakemd.py` script exists. SnakeMD is a library. Command fails. ❌ | N/A | 0 |

No Python code snippets are provided in data2 — only terminal commands describing a game-like UI that does not exist.

**U = 0/1 × 100 = 0**

---

**API Reference (A)**

Documented API elements (n=8):

| # | Element | Exists | Score |
|---|---------|--------|-------|
| A1 | `Game` class | ❌ `hasattr(snakemd, 'Game')` → `False` | 0 |
| A2 | `NoteManager` class | ❌ `hasattr(snakemd, 'NoteManager')` → `False` | 0 |
| A3 | `Snake` class | ❌ `hasattr(snakemd, 'Snake')` → `False` | 0 |
| A4 | `Renderer` class | ❌ `hasattr(snakemd, 'Renderer')` → `False` | 0 |
| A5 | `Game.run()` | ❌ Class does not exist | 0 |
| A6 | `NoteManager.load_notes(directory)` | ❌ Class does not exist | 0 |
| A7 | `NoteManager.save_note(note)` | ❌ Class does not exist | 0 |
| A8 | `Snake.move(direction)` | ❌ Class does not exist | 0 |
| A9 | `Renderer.draw()` | ❌ Class does not exist | 0 |

All 9 documented API elements are hallucinated and do not exist in the snakemd package.

**A = 0/9 × 100 = 0**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → README states "MIT License". GitHub raw LICENSE confirms `MIT License`. ✅ V1=1
2. License identifier is valid → "MIT" is a valid SPDX identifier. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

**L = (1+1+1)/3 × 100 = 100**

---

### data2.md Final Score

```
CR = (100 + 0 + 20 + 0 + 0 + 100) / 6 = 36.67
```

**data2.md scores 36.67.** The README is a complete hallucination of a Snake-game-inspired note-taking terminal application. The LLM invented `Game`, `NoteManager`, `Snake`, and `Renderer` classes, a `python snakemd.py` entry point, and curses-based terminal UI — none of which exist. The actual SnakeMD is a programmatic Markdown generation library. Only the title and MIT license are correct. The installation section is worse than data1 because it also fails on dependency resolution and the run command.

---

## data3.md Evaluation

### Step-by-step Reasoning

**Project Title (T)**

Criteria:
1. Title exactly matches repository/official name → "SnakeMD" matches official name. ✅ V1=1
2. Title does not describe a different project → Correct. ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucination. ✅ V3=1

**T = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → data3 describes SnakeMD as "a Markdown parser designed to transform Markdown content into stylized terminal output." This is **wrong**. SnakeMD is a Markdown *generation* library (it creates Markdown from Python objects), not a Markdown parser or terminal renderer. Confirmed via `pip show snakemd` ("A markdown generation library for Python."). ❌ V1=0
2. Described functionality supported by repository artifacts → "Terminal Rendering", "Text Parsing and Tokenization", "Themes and Styling", ANSI escape sequences — none of these features exist in SnakeMD. The library produces `.md` files, not terminal-styled output. ❌ V2=0
3. Overview does not describe unsupported features → The overview describes a completely different product (a terminal Markdown renderer). All described features are unsupported. ❌ V3=0
4. Correctly identifies software domain → "terminal rendering" and "CLI documentation display" are wrong. The actual domain is programmatic Markdown document generation. ❌ V4=0
5. Terminology matches repository terminology → "ANSI escape sequences", "syntax highlighting", "tokenization", "themes" — none of this terminology appears in the actual SnakeMD codebase. ❌ V5=0

**O = (0+0+0+0+0)/5 × 100 = 0**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → data3 lists `Node.js (version 12 or later)` and `npm` as prerequisites. SnakeMD is a **Python** package, not a Node.js package. `pip show snakemd` confirms it is a Python package. ❌ V1=0
2. Installation commands execute without modification → `npm install -g snakemd` — this is the wrong package manager. SnakeMD is installed via `pip install snakemd`, not npm. Running `npm install -g snakemd` would install a completely different (unrelated) npm package named snakemd if one exists, or fail. ❌ V2=0
3. No unresolved dependency errors → npm-based install would not produce the Python snakemd package. ❌ V3=0
4. Documented environment requirements correct → data3 states "Node.js (version 12 or later)" — entirely wrong. SnakeMD requires Python >=3.10,<4.0. ❌ V4=0
5. Installation produces expected executable artifact → `npm install -g snakemd` would not produce the Python snakemd library. ❌ V5=0

**I = (0+0+0+0+0)/5 × 100 = 0**

---

**Usage and Examples (U)**

Snippets evaluated (k=3 distinct executable blocks):

| # | Snippet | Execution Result | Output Match | Score |
|---|---------|-----------------|--------------|-------|
| E1 | CLI: `snakemd README.md` | `shutil.which('snakemd')` → `None`. No CLI binary exists. Command fails. ❌ | N/A | 0 |
| E2 | `cat README.md \| snakemd` | Same as above — no CLI binary. Fails. ❌ | N/A | 0 |
| E3 | `const snakemd = require("snakemd"); const styledText = snakemd(markdownText);` | This is JavaScript/Node.js code. SnakeMD is a Python library. `require("snakemd")` is not valid Python. Executing this as Python raises `SyntaxError`. ❌ | N/A — wrong language | 0 |

**U = 0/3 × 100 = 0**

---

**API Reference (A)**

Documented API elements (n=1):

| # | Element | Exists | Score |
|---|---------|--------|-------|
| A1 | `snakemd(markdown: string): string` — a callable function taking a markdown string and returning a terminal-formatted string | ❌ `snakemd` module is not callable. `python3 -c "import snakemd; snakemd('# Hello')"` raises `TypeError: 'module' object is not callable`. The function does not exist. | 0 |

**A = 0/1 × 100 = 0**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → README states "MIT License". GitHub raw LICENSE confirms `MIT License`. ✅ V1=1
2. License identifier is valid → "MIT" is a valid SPDX identifier. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

**L = (1+1+1)/3 × 100 = 100**

---

### data3.md Final Score

```
CR = (100 + 0 + 0 + 0 + 0 + 100) / 6 = 33.33
```

**data3.md scores 33.33.** This is the worst of the three READMEs. The LLM hallucinated a Node.js terminal Markdown renderer, providing npm installation instructions, JavaScript code snippets, and a `snakemd(markdown)` callable function — all of which are wrong. SnakeMD is a Python library for generating Markdown documents. The installation section scores 0 because it describes the entirely wrong ecosystem (Node.js/npm instead of Python/pip). Only the title and MIT license are correct.

---

## Summary: All Three SnakeMD READMEs

| README | T | O | I | U | A | L | CR |
|--------|---|---|---|---|---|---|-----|
| data1.md | 100 | 0 | 60 | 0 | 0 | 100 | **43.33** |
| data2.md | 100 | 0 | 20 | 0 | 0 | 100 | **36.67** |
| data3.md | 100 | 0 | 0 | 0 | 0 | 100 | **33.33** |
| **Average** | **100** | **0** | **26.67** | **0** | **0** | **100** | **37.78** |

### Final Average Score (Equation 2 from TCC)

```
Score_avg = (43.33 + 36.67 + 33.33) / 3 = 37.78
```

---

## Analysis and Observations

**Why all three score critically low:**

SnakeMD is a non-famous, niche Python library. The LLM had insufficient training data about it and hallucinated three entirely different products:

- **data1.md** — Invented a Markdown-to-HTML resume converter with a `SnakeMD` class, `render()` method, and CLI tool.
- **data2.md** — Invented a Snake-game-inspired terminal note-taking application with `Game`, `NoteManager`, `Snake`, and `Renderer` classes.
- **data3.md** — Invented a Node.js terminal Markdown renderer with npm installation and a JavaScript API.

All three READMEs share the same two correct elements: the project title ("SnakeMD") and the MIT license. These are the only facts the LLM got right consistently.

**Systematic failures:**

1. **Overview (O = 0 across all three):** Every README describes a completely different product. The actual SnakeMD is a programmatic Markdown *generation* library — it creates `.md` files from Python objects using classes like `Document`, `Heading`, `Paragraph`, `MDList`, `Table`, `Code`, `Inline`. None of the three READMEs mention any of these real classes.

2. **API Reference (A = 0 across all three):** All documented API elements are hallucinated. data1 invents `SnakeMD.render()` and `SnakeMD.render_file()`. data2 invents `Game`, `NoteManager`, `Snake`, `Renderer`. data3 invents a callable `snakemd(markdown)` function. None exist in the actual package.

3. **Usage and Examples (U = 0 across all three):** All code snippets fail to execute. data1's `from snakemd import SnakeMD` raises `ImportError`. data2's `python snakemd.py` fails (no such script). data3's `require("snakemd")` is JavaScript in a Python package.

4. **Installation degrades across READMEs:** data1 gets the `pip install snakemd` command right (60/100). data2 uses `git clone` + `pip install -r requirements.txt` + `python snakemd.py` — all wrong (20/100). data3 uses `npm install -g snakemd` — completely wrong ecosystem (0/100).

**Root cause:** SnakeMD is a low-visibility library. The LLM likely encountered the name "SnakeMD" with insufficient context and pattern-matched to superficially similar tools: a Markdown-to-HTML converter (data1), a terminal app with "snake" in the name (data2), and a Node.js Markdown renderer (data3). This is a textbook case of LLM hallucination on non-famous APIs, as studied in the TCC's evaluation framework.
