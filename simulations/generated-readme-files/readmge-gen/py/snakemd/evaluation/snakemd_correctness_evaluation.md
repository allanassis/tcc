# SnakeMD — README-Gen Correctness Evaluation

Tool: **README-Gen** · Project: **SnakeMD** · Repository:
<https://github.com/TheRenegadeCoder/SnakeMD> · Core functionality (per manifest):
**Generate README files**

## Ground-Truth Verification (sources cross-checked)

All claims below were verified against real artifacts, not memory:

1. **Installed artifact** — `pip install snakemd` into a clean venv
   (`/tmp/eval-snakemd-venv`, Python 3.14). `pip show snakemd` →
   `Name: SnakeMD, Version: 2.4.1, Summary: "A markdown generation library for
   Python.", License: MIT, Home-page: https://www.snakemd.io`.
   `Requires-Python: >=3.10,<4.0` (via `importlib.metadata`).
2. **Introspection** (`dir`, `inspect.signature`, `hasattr`): public API is
   `snakemd.new_doc() -> Document` plus element classes (`Document`, `Heading`,
   `Paragraph`, `Inline`, `MDList`, `Table`, `Code`, `Quote`, `Checklist`,
   `Alert`, `CSVTable`, `TableOfContents`, `Raw`, `HorizontalRule`, `Template`,
   `Block`, `Element`). `Document` exposes `add_heading`, `add_paragraph`,
   `add_ordered_list`, `add_unordered_list`, `add_table`, `add_code`,
   `add_quote`, `add_checklist`, `add_alert`, `add_horizontal_rule`,
   `add_table_of_contents`, `add_table_from_csv`, `add_raw`, `add_block`,
   `dump`, `get_elements`, `scramble`. Rendering is `str(doc)` / `doc.dump()`.
3. **Negative introspection**: `hasattr(snakemd, 'SnakeMD')` = **False**,
   `render` = **False**, `render_file` = **False**, `Game`/`NoteManager`/
   `Snake`/`Renderer` = **False**. `callable(snakemd)` = **False**.
4. **No CLI**: no `snakemd` entry-point/binary in `venv/bin`; `snakemd --help`
   → `No such file or directory` (exit 127). SnakeMD is a pure library.
5. **Repository** (shallow clone + <https://github.com/TheRenegadeCoder/SnakeMD>
   and <https://www.snakemd.io>): default branch **main**; root contains
   `LICENSE, README.md, docs, poetry.lock, pyproject.toml, readme.py, snakemd/,
   tests/`. **No `requirements.txt`, no root `snakemd.py`.** `LICENSE` line 1 =
   `MIT License`. The project's own README is generated *by* SnakeMD
   (`readme.py`) — confirming core functionality = programmatic Markdown/README
   generation. Test framework = **pytest** (`poetry run pytest --co` → 202
   tests).
6. **Correct-usage baseline executed**: `new_doc()` + `add_heading` +
   `add_paragraph` + `add_unordered_list` + `str(doc)` renders valid Markdown.
7. **npm cross-check**: `npm install snakemd` → **E404 Not Found** (no such npm
   package). SnakeMD is not a Node/npm package.

---

## README 1 — `data1.md`

Claim: SnakeMD is a CLI + library that converts Markdown-with-embedded-Python
into styled **HTML resumes/CVs**, via a `SnakeMD` class (`.render`,
`.render_file`) and a `snakemd input -o output` CLI.

### Project Title (T)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Matches repo/official name | 1 | Title is "SnakeMD" = repo name |
| 2 | Does not describe a different project | 1 | Title string names SnakeMD only |
| 3 | No hallucinated terminology in title | 1 | Plain name, no invented terms |

**T = 3/3 × 100 = 100.00**

### Overview (O)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Primary functionality correct | 0 | Real = Markdown generation; README says HTML resume/CV converter |
| 2 | Functionality supported by artifacts | 0 | No HTML/resume/rendering code exists |
| 3 | No unsupported features | 0 | "embedded Python execution in `{{ }}`", "styled HTML" unsupported |
| 4 | Correct software domain | 0 | Domain = MD generation, not resume/web publishing |
| 5 | Terminology matches repo | 0 | "resume", "CV", "HTML" absent from repo |

**O = 0/5 × 100 = 0.00**

### Installation (I) — executed
Commands: `pip install snakemd` (env: "Python 3.6+").
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Dependencies declared | 1 | pip + Python stated; real pkg has no runtime deps |
| 2 | Commands execute unmodified | 1 | `pip install snakemd` succeeded (SnakeMD 2.4.1) |
| 3 | No unresolved dependency errors | 1 | Clean install, no dep errors |
| 4 | Environment requirements correct | 0 | Claims "Python 3.6+"; real `Requires-Python >=3.10,<4.0` |
| 5 | Produces expected executable artifact | 0 | Expected `snakemd` CLI + `SnakeMD` class; neither exists |

**I = 3/5 × 100 = 60.00**

### Usage and Examples (U) — executed
| Snippet | Executed | Output match | E_i | Evidence |
|---|---|---|---|---|
| CLI `snakemd input_resume.md -o output_resume.html` | fail | n/a | 0 | `No such file or directory`, exit 127 (no CLI) |
| Python `from snakemd import SnakeMD; SnakeMD().render(...)` | fail | n/a | 0 | `ImportError: cannot import name 'SnakeMD'` |

(The `{{ }}` "markdown snippet" is illustrative input, not an executable program;
excluded from k. Its described behavior — Python executed inside `{{ }}` — is a
non-existent feature.) **k = 2, ΣE = 0 → U = 0.00**

### API Reference (A)
| Element | A_i | Evidence |
|---|---|---|
| `SnakeMD` class | 0 | `hasattr(snakemd,'SnakeMD')` = False |
| `SnakeMD.render(markdown_text)->str` | 0 | No such attribute/method |
| `SnakeMD.render_file(input_path)->str` | 0 | No such attribute/method |
| CLI options (`snakemd <file>`, `-o/--output`, `-h`) | 0 | No CLI exists |

**n = 4, ΣA = 0 → A = 0.00**

### License (L)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Matches repo LICENSE | 1 | States MIT; `LICENSE` = MIT License |
| 2 | Valid identifier | 1 | "MIT" is a valid SPDX id |
| 3 | No conflicting license info | 1 | Only MIT mentioned |

**L = 3/3 × 100 = 100.00**

**C_R(data1) = (100 + 0 + 60 + 0 + 0 + 100) / 6 = 43.33**

---

## README 2 — `data2.md`

Claim: SnakeMD is a **Snake-game-style Markdown note-taking terminal app**
(classes `Game`, `NoteManager`, `Snake`, `Renderer`), installed by cloning +
`pip install -r requirements.txt` and run via `python snakemd.py`.

### Project Title (T)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Matches repo/official name | 1 | "SnakeMD" |
| 2 | Not a different project | 1 | Title string names SnakeMD |
| 3 | No hallucinated terms in title | 1 | Plain name |

**T = 100.00**

### Overview (O)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Primary functionality correct | 0 | Real = MD generation; README says note-taking game |
| 2 | Supported by artifacts | 0 | No game/notes/curses code exists |
| 3 | No unsupported features | 0 | "snake navigation", "curses UI", "note storage" unsupported |
| 4 | Correct domain | 0 | Domain is MD generation, not games/notes |
| 5 | Terminology matches repo | 0 | "Snake", "NoteManager", "curses" absent from repo |

**O = 0.00**

### Installation (I) — executed
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Dependencies declared | 0 | Points to `requirements.txt`/std-lib; repo uses Poetry, no requirements.txt |
| 2 | Commands execute unmodified | 0 | `pip install -r requirements.txt` → file does not exist in repo |
| 3 | No unresolved dependency errors | 0 | Missing requirements.txt breaks the documented step |
| 4 | Env requirements correct | 0 | "Python 3.6+" + "curses"; real needs >=3.10, no curses dep |
| 5 | Produces expected artifact | 0 | `python snakemd.py` — no root `snakemd.py` exists |

**I = 0/5 × 100 = 0.00**

### Usage and Examples (U) — executed
| Snippet | Executed | E_i | Evidence |
|---|---|---|---|
| `python snakemd.py` (launch app) | fail | 0 | No root `snakemd.py`; nothing to run |

**k = 1, ΣE = 0 → U = 0.00**

### API Reference (A)
| Element | A_i | Evidence |
|---|---|---|
| `Game` class | 0 | Not in package |
| `NoteManager` class | 0 | Not in package |
| `Snake` class | 0 | Not in package |
| `Renderer` class | 0 | Not in package |
| `Game.run()` | 0 | Nonexistent |
| `NoteManager.load_notes(directory)` | 0 | Nonexistent |
| `NoteManager.save_note(note)` | 0 | Nonexistent |
| `Snake.move(direction)` | 0 | Nonexistent |
| `Renderer.draw()` | 0 | Nonexistent |

**n = 9, ΣA = 0 → A = 0.00**

### License (L)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Matches repo LICENSE | 1 | States MIT; repo LICENSE = MIT |
| 2 | Valid identifier | 1 | "MIT" valid |
| 3 | No conflicting info | 1 | Only MIT (link uses /master/ but license id is correct) |

**L = 100.00**

**C_R(data2) = (100 + 0 + 0 + 0 + 0 + 100) / 6 = 33.33**

---

## README 3 — `data3.md`

Claim: SnakeMD is a **Node.js/npm** Markdown-to-**terminal-ANSI** renderer; a
callable `snakemd(markdown: string): string`; installed via
`npm install -g snakemd`.

### Project Title (T)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Matches repo/official name | 1 | "SnakeMD" |
| 2 | Not a different project | 1 | Title names SnakeMD |
| 3 | No hallucinated terms in title | 1 | Plain name |

**T = 100.00**

### Overview (O)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Primary functionality correct | 0 | Real = MD generation (Python); README says terminal MD renderer (Node) |
| 2 | Supported by artifacts | 0 | No terminal-render/ANSI code; not a Node package |
| 3 | No unsupported features | 0 | "ANSI output", "syntax highlighting", "themes" unsupported |
| 4 | Correct domain | 0 | Wrong domain and wrong language (Node vs Python) |
| 5 | Terminology matches repo | 0 | "npm", "terminal", "ANSI" absent from repo |

**O = 0.00**

### Installation (I) — executed
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Dependencies declared | 0 | Declares Node 12+/npm; real is Python/pip |
| 2 | Commands execute unmodified | 0 | `npm install snakemd` → **E404 Not Found** |
| 3 | No unresolved dependency errors | 0 | Package does not exist on npm |
| 4 | Env requirements correct | 0 | "Node.js 12+"; real is Python >=3.10 |
| 5 | Produces expected artifact | 0 | No `snakemd` CLI / node module produced |

**I = 0.00**

### Usage and Examples (U) — executed
| Snippet | Executed | E_i | Evidence |
|---|---|---|---|
| CLI `snakemd README.md` | fail | 0 | No such CLI (Python pkg, no binary) |
| `cat README.md \| snakemd` | fail | 0 | No such CLI |
| JS `require("snakemd")` | fail | 0 | npm pkg 404; module not installable; `snakemd` (Python) not callable |

**k = 3, ΣE = 0 → U = 0.00**

### API Reference (A)
| Element | A_i | Evidence |
|---|---|---|
| `snakemd(markdown: string): string` | 0 | `callable(snakemd)` = False; documented JS function does not exist |

**n = 1, ΣA = 0 → A = 0.00**

### License (L)
| # | Rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Matches repo LICENSE | 1 | States MIT; repo = MIT |
| 2 | Valid identifier | 1 | "MIT" valid |
| 3 | No conflicting info | 1 | Only MIT |

**L = 100.00**

**C_R(data3) = (100 + 0 + 0 + 0 + 0 + 100) / 6 = 33.33**

---

## Section-score summary (README-Gen)

| readme | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| data1.md | 100 | 0 | 60 | 0 | 0 | 100 | 43.33 |
| data2.md | 100 | 0 | 0 | 0 | 0 | 100 | 33.33 |
| data3.md | 100 | 0 | 0 | 0 | 0 | 100 | 33.33 |
| **average** | 100 | 0 | 20 | 0 | 0 | 100 | **36.67** |

Average consistency check: mean of section means =
(100 + 0 + 20 + 0 + 0 + 100)/6 = 36.67 = mean of the three C_R rows. ✔

## Cross-checked sources
- Installed PyPI artifact `snakemd==2.4.1` (pip show / importlib.metadata / inspect).
- Repository: <https://github.com/TheRenegadeCoder/SnakeMD> (shallow clone + web).
- Official docs: <https://www.snakemd.io>.
- npm registry probe for `snakemd` (E404).
- Executed snippets & baselines under `/tmp` with the venv interpreter.
