# Rich — README-Gen Correctness Evaluation

Tool under evaluation: **README-Gen** (structured ATRAK-grounded prompting,
`gpt-4.1-mini-2025-04-14`). READMEs evaluated in order: `data1.md`, `data2.md`,
`data3.md`.

## Environment & Ground-Truth Setup

- Clean venv: `python3 -m venv /tmp/eval-rich-venv` (Python **3.14.6**).
- `pip install rich` → **rich 15.0.0**, deps `markdown-it-py`, `pygments`.
- Authoritative package metadata (`importlib.metadata`): `Requires-Python:
  >=3.9.0`; `License: MIT`.
- Authoritative source metadata (cloned `Textualize/rich@main`,
  `pyproject.toml`): `python = ">=3.9.0"`; classifiers enumerate **Python 3.9,
  3.10, 3.11, 3.12, 3.13, 3.14** (no 3.6/3.7/3.8); `license = "MIT"`; `LICENSE`
  file = MIT (Copyright (c) 2020 Will McGugan).
- API signatures obtained via `inspect.signature` on rich 15.0.0.

### Cross-checked sources

1. Repository: https://github.com/Textualize/rich (cloned `main`, `pyproject.toml`, `LICENSE`).
2. Official docs: https://rich.readthedocs.io (Console, Table, Syntax, Progress, Panel, Live, Traceback, Prompt, logging.RichHandler reference pages).
3. Installed artifact introspection (`inspect.signature`, rich 15.0.0) in `/tmp/eval-rich-venv`.
4. PyPI package metadata (`Requires-Python`) via `importlib.metadata`.

### Key ground-truth signatures (rich 15.0.0)

```
Console.print(self, *objects, sep=' ', end='\n', style=None, justify=None, overflow=None,
              no_wrap=None, emoji=None, markup=None, highlight=None, width=None, height=None,
              crop=True, soft_wrap=None, new_line_start=False) -> None      # markup default None (=> console default True)
Console.status(self, status, *, spinner='dots', ...)                        # first param name is 'status', not 'text'
Console.input(self, prompt='', *, markup=True, emoji=True, password=False, stream=None) -> str
Console.rule(self, title='', *, characters='─', style='rule.line', align='center') -> None
Console.clear(self, home=True) -> None
Text(self, text='', style='', *, justify=None, overflow=None, no_wrap=None, end='\n', ...)
Text.append(self, text, style=None) -> Text
Text.stylize(self, style, start=0, end=None) -> None                        # start default 0, not None
Table(self, *headers, title=None, caption=None, ..., show_header=True, show_footer=False,
      show_lines=False, ..., row_styles=None, header_style='table.header', footer_style='table.footer', ...)
Table.add_column(self, header='', footer='', *, header_style=None, ..., style=None, justify='left',
                 ..., width=None, min_width=None, max_width=None, ratio=None, no_wrap=False) -> None
Table.add_row(self, *renderables, style=None, end_section=False) -> None
# Table.show_header is a bool constructor argument / instance attribute — THERE IS NO show_header() METHOD
Progress.add_task(self, description, start=True, total=100.0, completed=0, visible=True, **fields) -> TaskID
Progress.update(self, task_id, *, total=None, completed=None, advance=None, description=None, ...) -> None
Progress.start(self) / stop(self) / start_task(self, task_id) / stop_task(self, task_id) -> None
Syntax(self, code, lexer, *, theme='monokai', dedent=False, line_numbers=False, ...)   # 2nd param name is 'lexer'
Traceback.from_exception(exc_type, exc_value, traceback, *, ...) -> Traceback           # THREE required positionals
Prompt.ask(prompt='', *, console=None, password=False, choices=None, ..., default=...) -> Any  # first param 'prompt'
Panel(self, renderable, box=..., *, title=None, subtitle=None, style='none', ...)
Live(self, renderable=None, *, console=None, ..., refresh_per_second=4, ...); Live.update(self, renderable, *, refresh=False)
RichHandler(self, level=0, console=None, *, show_time=True, ..., markup=False, ...)
```

---

# README 1 — `data1.md`

## Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 exact match repo/official name | 1 | Title "Rich" == repo `Textualize/rich` / official name "Rich". |
| 2 not a different project | 1 | Describes the Rich terminal library. |
| 3 no hallucinated terminology | 1 | No invented product names. |

**T = (1+1+1)/3 × 100 = 100.00**

## Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality correct | 1 | "Python library for rich text and beautiful formatting in the terminal" — matches repo tagline. |
| 2 supported by artifacts | 1 | Console, tables, progress, syntax, markdown, tracebacks all exist in package. |
| 3 no unsupported features | 1 | Layout, live updates, panels, trees, tracebacks are all real modules. |
| 4 correct domain | 1 | Terminal / CLI text rendering. |
| 5 terminology matches repo | 1 | "Console", "markup", "syntax highlighting", "tracebacks" match repo vocabulary. |

**O = 5/5 × 100 = 100.00**

## Installation (I) — executed
Documented paths: (a) `pip install rich`; (b) `pip install --upgrade rich`. Claim: "compatible with Python 3.6 and above".

| Rule | Verdict | Evidence |
|---|---|---|
| 1 dependencies declared | 1 | `pip install rich` resolves declared deps (markdown-it-py, pygments) automatically; no missing deps. |
| 2 commands execute unmodified | 1 | `pip install rich` → exit 0 (rich 15.0.0). `--upgrade` is the same command with a valid flag. |
| 3 no unresolved dependency errors | 1 | Install completed cleanly; `import rich` succeeds. |
| 4 environment requirements correct | **0** | README says **Python 3.6+**. Authoritative `Requires-Python` = **>=3.9.0**; pyproject classifiers list only 3.9–3.14. 3.6/3.7/3.8 are NOT supported → claim incorrect. |
| 5 expected artifact produced | 1 | Importable `rich` package produced (library artifact); verified `import rich`. |

**I = 4/5 × 100 = 80.00**

## Usage and Examples (U) — executed
Executed with `/tmp/eval-rich-venv/bin/python`. ANSI-styled output accepted as matching a documented plain-text rendering when text content matches (recorded).

| # | Snippet | Executes (imports-only fix) | Output matches | E_i | Notes |
|---|---|---|---|---|---|
| S1 | Printing Rich Text | Yes (exit 0) | Yes — centered "Hello World!" styled | **1** | Self-contained (imports Console, builds console). |
| S2 | Markup styling | **No** | (n/a) | **0** | `NameError: console not defined`. Requires instantiating `console = Console()` — an object build, beyond the permitted *imports-only* intervention; the `console` dependency is not documented within the snippet (U1 & U2 fail). With console added it renders "This is red and this is underlined." (recorded). |
| S3 | Table example | **No** | (n/a) | **0** | Imports only `Table`; `console.print(table)` → `NameError: console not defined`. Same reason as S2. With console added, table renders correctly (recorded). |
| S4 | Progress `track` | Yes (exit 0) | Yes — "Processing..." bar to 100% | **1** | Self-contained. |
| S5 | Syntax highlighting | **No** | (n/a) | **0** | Imports only `Syntax`; `console.print(syntax)` → `NameError: console not defined`. With console added, highlighted code renders (recorded). |
| S6 | Live updating table | Yes (exit 0) | Yes — live-updating rows 0–9 | **1** | Self-contained. |

k = 6 executable snippets; passes = S1, S4, S6 = 3.

**U = 3/6 × 100 = 50.00**

## API Reference (A)
n = 7 documented elements. Each passes only if all six rules hold.

| Element | Exists | Names correct | Types | Returns | Behavior consistent | Not deprecated | A_i | Evidence |
|---|---|---|---|---|---|---|---|---|
| `Console` | 1 | **0** | 1 | 1 | **0** | 1 | **0** | `status(text, spinner='dots')` — real first param is `status`, not `text` (name wrong). `print(..., markup=False)` claims default markup **False**, but real default is None→True and S1 rendered markup without `markup=True` → documented default contradicts execution. |
| `Text` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | `Text(text, style, justify, overflow, no_wrap)`, `append(text, style)`, `stylize(style, start, end)` — all names real. Only `stylize` default `start` shown as None vs real 0 (minor default note; name/type/behavior fine). |
| `Table` | **0** | **0** | — | — | — | 1 | **0** | Documents method `show_header(show=True)`. No such method: `Table.show_header` is a bool constructor arg / instance attribute (introspection: `type object 'Table' has no attribute 'show_header'`). Hallucinated method. |
| `Progress` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | `add_task`, `update(task_id, advance=1)`, `start()`, `stop()` all exist with correct names (defaults total=None vs 100.0, advance=1 vs None are minor default notes). |
| `Syntax` | 1 | **0** | 1 | 1 | 1 | 1 | **0** | `Syntax(code, lexer_name, ...)` — real 2nd param is **`lexer`**, not `lexer_name`. `Syntax(code, lexer_name=...)` would raise TypeError. |
| `Traceback` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | `Traceback.from_exception(exc_type, exc_value, traceback)` matches the three required positionals exactly. |
| `Prompt` | 1 | **0** | 1 | 1 | 1 | 1 | **0** | `Prompt.ask(question, ...)` — real first param is **`prompt`**. `choices/default/password` kwargs are real, but the documented first param name is wrong. |

passes = Text, Progress, Traceback = 3.

**A = 3/7 × 100 = 42.86**

## License (L)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo LICENSE | 1 | "MIT License" == repo LICENSE (MIT, Copyright 2020 Will McGugan). |
| 2 valid identifier | 1 | "MIT" is a valid SPDX identifier. |
| 3 no conflicting info | 1 | Only MIT stated. |

**L = 3/3 × 100 = 100.00**

### C_R (data1) = (100 + 100 + 80 + 50 + 42.86 + 100) / 6 = **78.81**

---

# README 2 — `data2.md`

## Project Title (T)
All three rules pass — title "Rich" matches repo. **T = 100.00**

## Overview (O)
Correctly describes Rich as a terminal rich-text/formatting library (colors, styles, layouts, panels, tables, progress, markdown, syntax highlighting, live updates, tracebacks, prompts). Domain and terminology match. Minor note: "gradients" is not a headline Rich feature, but colors/styles it references are supported; not a material unsupported-feature claim. **O = 5/5 × 100 = 100.00**

## Installation (I) — executed
Documented paths: (a) `pip install rich`; (b) `pip install git+https://github.com/Textualize/rich.git` (dev build from source). Claim: "Python 3.6 or above".

| Rule | Verdict | Evidence |
|---|---|---|
| 1 dependencies declared | 1 | pip resolves declared deps for both paths. |
| 2 commands execute unmodified | 1 | `pip install rich` → exit 0; `pip install git+https://…rich.git` in fresh venv `/tmp/eval-rich-v2` → **exit 0** (built from source, rich 15.0.0). |
| 3 no unresolved dependency errors | 1 | Both paths completed; `import rich` OK in both. |
| 4 environment requirements correct | **0** | "Python 3.6+" contradicts authoritative `Requires-Python >=3.9.0`. |
| 5 expected artifact produced | 1 | Importable `rich` produced from both PyPI and git-source installs. |

**I = 4/5 × 100 = 80.00**

## Usage and Examples (U) — executed
| # | Snippet | Executes | Output matches | E_i |
|---|---|---|---|---|
| S1 | Basic console output (`style="underline on yellow"`) | exit 0 | Yes — "Hello, Rich!" underlined on yellow, "Rich" bold magenta | **1** |
| S2 | Table (User Information) | exit 0 | Yes — titled table, cyan/magenta/green columns, 3 rows | **1** |
| S3 | Syntax highlighting | exit 0 | Yes — highlighted `greet` code with line numbers | **1** |
| S4 | Progress `track` | exit 0 | Yes — "Processing..." bar to 100% | **1** |
| S5 | Live updating Panel | exit 0 | Yes — panel updates with random values | **1** |

All snippets self-contained (each imports Console + builds `console`). k = 5, passes = 5.

**U = 5/5 × 100 = 100.00**

## API Reference (A)
n = 6 elements (the "Additional Noteworthy Modules" bullet list — rich.markdown/tree/traceback/theme/columns — are bare module names with one-line notes, not parameterized elements, so not counted as API elements; all named modules do exist).

| Element | Exists | Names | Types | Returns | Behavior | Not deprecated | A_i | Evidence |
|---|---|---|---|---|---|---|---|---|
| `Console` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | `.print(... markup=True ...)` matches effective default; `.input(prompt, password=False)`, `.clear()`, `.rule(title=None, style=None)` all real names. |
| `Table` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | Constructor `title, show_header, header_style, show_lines, row_styles` all real; `add_column(header, *, style, justify, ratio, no_wrap)`, `add_row(*cells, style)` real. |
| `Syntax` | 1 | **0** | 1 | 1 | 1 | 1 | **0** | Documents param **`language`**; real name is `lexer`. `Syntax(code, language=...)` → TypeError. |
| `Progress` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | Describes `track` helper and `Progress` instance; both exist and behave as described. |
| `Panel` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | `renderable, title, subtitle, style` all real Panel params. |
| `Live` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | `Live(renderable, refresh_per_second=4)` real; `.update(new_renderable)` — `new_renderable` is positional usage of real param `renderable`. |

passes = 5.

**A = 5/6 × 100 = 83.33**

## License (L)
MIT, matches repo, valid, no conflict. **L = 100.00**

### C_R (data2) = (100 + 100 + 80 + 100 + 83.33 + 100) / 6 = **93.89**

---

# README 3 — `data3.md`

## Project Title (T)
Title "Rich" matches repo. **T = 100.00**

## Overview (O)
Correctly describes terminal styling, markup, renderables, layouts, syntax highlighting, progress/live, tables, tracebacks + logging integration. Domain and terminology match repo. **O = 5/5 × 100 = 100.00**

## Installation (I) — executed
Documented paths: (a) `pip install rich`; (b) `pip install rich[jupyter]` (extra). Claim: "Python 3.6 and above".

| Rule | Verdict | Evidence |
|---|---|---|
| 1 dependencies declared | 1 | pip resolves deps; `[jupyter]` extra is a real extra. |
| 2 commands execute unmodified | 1 | `pip install rich` → exit 0; `pip install rich[jupyter]` in fresh venv `/tmp/eval-rich-v3` → **exit 0** (extra resolved: `import ipywidgets` succeeds). |
| 3 no unresolved dependency errors | 1 | Both completed cleanly. |
| 4 environment requirements correct | **0** | "Python 3.6+" contradicts authoritative `Requires-Python >=3.9.0`. |
| 5 expected artifact produced | 1 | Importable `rich` (+ jupyter extra deps) produced. |

**I = 4/5 × 100 = 80.00**

## Usage and Examples (U) — executed
| # | Snippet | Executes | Output matches | E_i |
|---|---|---|---|---|
| S1 | Basic console output | exit 0 | Yes — "Hello, Rich!" ("Rich" bold magenta) | **1** |
| S2 | Table (Star Wars) | exit 0 | Yes — titled table, aligned/colored columns, 3 rows | **1** |
| S3 | Syntax highlighting | exit 0 | Yes — highlighted `greet` code with line numbers | **1** |
| S4 | Progress (`Progress()` + `add_task`/`update`) | exit 0 | Yes — "[red]Processing..." bar fills to 100% | **1** |

k = 4 (all self-contained). passes = 4. (The `RichHandler` logging snippet is inside the API Reference section and is validated under the API element `RichHandler`, not counted here; it was executed successfully — see below.)

**U = 4/4 × 100 = 100.00**

## API Reference (A)
n = 6 elements.

| Element | Exists | Names | Types | Returns | Behavior | Not deprecated | A_i | Evidence |
|---|---|---|---|---|---|---|---|---|
| `Console` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | `print(... markup=True ...)`, `input(prompt)`, `rule(title=None, characters=None, style=None)`, `clear()` — all real names. |
| `Table` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | Constructor `title, show_header, header_style, show_footer, footer_style, caption, caption_style, padding, expand` all real; `add_column(...ratio, min_width, max_width)`, `add_row(*cells, style, end_section)` real. |
| `Syntax` | 1 | **0** | 1 | 1 | 1 | 1 | **0** | Documents `Syntax(code, lexer_name, ...)`; real 2nd param is `lexer`. |
| `Progress` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | `add_task(description, total, completed, visible, start)`, `update(task_id, completed, advance, description)`, `start_task`, `stop_task` — all real names. |
| `Traceback` | 1 | **0** | **0** | 1 | **0** | 1 | **0** | Documents `Traceback.from_exception(exception)` — a single param. Real signature requires **three** positionals `(exc_type, exc_value, traceback)`; `from_exception(exception)` would raise TypeError. |
| `RichHandler` | 1 | 1 | 1 | 1 | 1 | 1 | **1** | `logging.basicConfig(..., handlers=[RichHandler()])` executed (exit 0) and produced a rich-formatted log line ("Hello, Rich logging!"); `RichHandler` exists and is instantiable with no args. |

passes = Console, Table, Progress, RichHandler = 4.

**A = 4/6 × 100 = 66.67**

## License (L)
MIT, matches repo, valid, no conflict. **L = 100.00**

### C_R (data3) = (100 + 100 + 80 + 100 + 66.67 + 100) / 6 = **91.11**

---

# Summary (README-Gen)

| README | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| data1.md | 100.00 | 100.00 | 80.00 | 50.00 | 42.86 | 100.00 | 78.81 |
| data2.md | 100.00 | 100.00 | 80.00 | 100.00 | 83.33 | 100.00 | 93.89 |
| data3.md | 100.00 | 100.00 | 80.00 | 100.00 | 66.67 | 100.00 | 91.11 |
| **average** | 100.00 | 100.00 | 80.00 | 83.33 | 64.29 | 100.00 | **87.94** |

Average-row consistency check: T,O,L = 100.00; I = (80+80+80)/3 = 80.00; U = (50+100+100)/3 = 83.33; A = (42.86+83.33+66.67)/3 = 64.29; C_R = (78.81+93.89+91.11)/3 = 87.94. ✓
