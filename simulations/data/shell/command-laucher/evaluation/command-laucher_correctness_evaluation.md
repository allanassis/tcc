# Correctness Evaluation — CommandLauncher (README-Gen)

Project: **CommandLauncher** (`command-laucher`)
Repository (ground truth): https://github.com/criteo/command-launcher
Tool under evaluation: **README-Gen** (`gpt-4.1-mini-2025-04-14`, ATRAK-grounded)
READMEs (input order): `data1.md`, `data2.md`, `data3.md`

## Ground Truth Reference

Established by cloning the real repository (shallow) and building it locally.

- **Language / kind:** Go CLI application (`go.mod`, `main.go`, Cobra-based command tree).
- **Binary name:** default `cdt` (Criteo Dev Toolkit); the binary name is configurable at build time (docs also use `cola` as an example). Built locally via `go build -o cdt -ldflags='-X main.appName=cdt ...' main.go`.
- **What it is:** a small binary that CLI providers use to package and distribute command-line tools; developers download the launcher, which keeps commands up to date. Features: auto-completion, credential management (`login`), progressive rollout, monitoring, and "dropin" packages.
- **Real CLI surface** (`./cdt --help`): `completion`, `config`, `login`, `package` (subcommands `delete`, `inspect`, `install`, `list`, `pause`, `setup`), `remote`, `rename`, `update`, `version`.
- **Core functionality "Install packages":** real feature `cdt package install <dropin package>`.
- **License:** MIT — `LICENSE` reads `MIT License / Copyright (c) 2022 Criteo`.
- **Install method:** download a pre-built binary from the release page and copy to `PATH`, **or** build from source with `go build`. There is **no** PyPI package, **no** npm package, and **no** Homebrew formula.

### Cross-checked sources

1. Cloned repo `README.md`, `LICENSE`, `go.mod`, `main.go`, `cmd/*.go` (local, `/tmp/cl-groundtruth`).
2. Built binary `./cdt --help`, `./cdt package --help`, `./cdt version` (local execution).
3. Official docs site: https://criteo.github.io/command-launcher/
4. PyPI JSON API: `https://pypi.org/pypi/command-launcher/json` → **HTTP 404** (no such package).
5. GitHub API: `https://api.github.com/repos/xZepyx/command-launcher` → **HTTP 404**; `https://api.github.com/repos/criteo/command-launcher` → **HTTP 200**.
6. npm registry: `npm install command-launcher` resolves to `command-launcher@0.0.1-security`, a **security-holding placeholder** ("This package contained malicious code and was removed…"), no code entry point.

### Global observation

All three README-Gen files document **fundamentally different, hallucinated projects** that do not correspond to the real Go CLI:

- `data1.md`: a Python "Command Launcher" library (pip package + `CommandLauncher`/`argument` decorators), repo `github.com/xZepyx/command-launcher`.
- `data2.md`: a Python subprocess wrapper library (`CommandLauncher.run` → `CommandResult`).
- `data3.md`: a Node.js child-process wrapper (`require("command-launcher")`).

None matches criteo/command-launcher. Correctness of factual claims is therefore uniformly low; the title and (coincidentally) the MIT license happen to be correct.

---

## README 1 — `data1.md`

### Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 title matches repo/official name | 1 | Title "Command Launcher" matches project name (repo `command-launcher`, README title "Command Launcher"). |
| 2 does not describe a different project | 1 | The title string names this project, not another. |
| 3 no hallucinated terminology in title | 1 | "Command Launcher" contains no invented terms. |

**T = 3/3 × 100 = 100.00**

### Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 primary functionality correct | 0 | Describes a "lightweight **Python** tool / command dispatcher" with decorator-based command registration. Real project is a Go binary launcher that distributes/updates CLI apps. |
| 2 functionality supported by artifacts | 0 | No Python dispatcher, no `@launcher.command` API exists in the repo. |
| 3 no unsupported features | 0 | Structured argument schemas, decorator registration, env management — none exist. |
| 4 correct software domain | 0 | Frames it as a Python CLI-automation library; real domain is command distribution/launching (dropins, remote command repositories). |
| 5 terminology matches repo | 0 | "Command Registration / Argument Parsing / Execution Environment" absent from repo vocabulary (`dropin`, `package`, `remote`, `cola/cdt`). |

**O = 0/5 × 100 = 0.00**

### Installation (I) — executed
Documented paths: (a) `pip install command-launcher`; (b) source: `git clone https://github.com/xZepyx/command-launcher.git && cd command-launcher && pip install .`

| Rule | Verdict | Evidence |
|---|---|---|
| 1 dependencies declared | 1 | Declares "Python 3.7 or higher". |
| 2 commands execute unmodified | 0 | `pip install command-launcher` → `ERROR: No matching distribution found` (PyPI 404). `git clone …xZepyx…` → `fatal: could not read Username` (repo 404). |
| 3 no unresolved dependency errors | 0 | pip reports "Could not find a version that satisfies the requirement command-launcher". |
| 4 environment requirements correct | 0 | Requires Python; real build requires Go ≥ 1.17. Python runtime claim is incorrect for this repo. |
| 5 expected executable artifact produced | 0 | No `command-launcher` CLI produced; every install path fails. |

**I = 1/5 × 100 = 20.00**

### Usage and Examples (U) — executed
| # | Snippet | Executes | Output matches | E_i |
|---|---|---|---|---|
| 1 | `command-launcher <command> [options] [arguments]` | No — binary not installed; also a template with placeholders | n/a | 0 |
| 2 | `command-launcher --help` | No — `command not found` (never installed) | n/a | 0 |
| 3 | Python `@launcher.command('greet')` script | No — `from command_launcher import …` → **ModuleNotFoundError** | n/a | 0 |
| 4 | `python myscript.py greet --name John` | No — depends on (3); module missing | Documented "Hello, John!" not produced | 0 |

**U = 0/4 × 100 = 0.00**

### API Reference (A)
| # | Element | Exists | A_i | Evidence |
|---|---|---|---|---|
| 1 | `CommandLauncher` class | No | 0 | No Python class in a Go repo. |
| 2 | `command(name)` decorator | No | 0 | Not present. |
| 3 | `run(args)` method | No | 0 | Not present. |
| 4 | `argument` decorator | No | 0 | Not present. |
| 5 | "Command Functions" | No | 0 | Not a real API surface. |

**A = 0/5 × 100 = 0.00**

### License (L)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 matches repo LICENSE | 1 | States "MIT License"; repo `LICENSE` is MIT (Copyright 2022 Criteo). Identifier matches. |
| 2 valid identifier | 1 | "MIT" is a valid SPDX identifier. |
| 3 no conflicting license info | 1 | Only MIT referenced (link points to wrong repo, but no conflicting license named). |

**L = 3/3 × 100 = 100.00**

**C_R(data1) = (100 + 0 + 20 + 0 + 0 + 100) / 6 = 36.67**

---

## README 2 — `data2.md`

### Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 | 1 | Title `command-launcher` matches repo name exactly. |
| 2 | 1 | Names this project. |
| 3 | 1 | No hallucinated terms in title. |

**T = 100.00**

### Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 | 0 | Describes a "Python library to run shell commands … capture stdout/stderr/exit status" — a subprocess wrapper, not the Go launcher. |
| 2 | 0 | No such Python library in repo. |
| 3 | 0 | Timeouts / process management / `CommandResult` — unsupported. |
| 4 | 0 | Domain (Python subprocess helper) differs from command distribution/launching. |
| 5 | 0 | Terminology (Process Management, Result Handling, Timeouts) absent from repo. |

**O = 0.00**

### Installation (I) — executed
Documented path: `pip install command-launcher` (Python 3.6+).

| Rule | Verdict | Evidence |
|---|---|---|
| 1 | 1 | Declares "Python 3.6 or later". |
| 2 | 0 | `pip install command-launcher` → No matching distribution (PyPI 404). |
| 3 | 0 | pip dependency-resolution error. |
| 4 | 0 | Python runtime incorrect for a Go project. |
| 5 | 0 | No artifact produced. |

**I = 1/5 × 100 = 20.00**

### Usage and Examples (U) — executed
| # | Snippet | Executes | E_i |
|---|---|---|---|
| 1 | `launcher.run("echo Hello, World!")` (with `from command_launcher import CommandLauncher`) | No — ModuleNotFoundError | 0 |
| 2 | `launcher.run("sleep 5", timeout=2)` | No — import fails | 0 |
| 3 | `launcher.run("cat", input_data="…")` | No — import fails | 0 |

**U = 0/3 × 100 = 0.00**

### API Reference (A)
| # | Element | Exists | A_i |
|---|---|---|---|
| 1 | `CommandLauncher` class | No | 0 |
| 2 | `run(command, timeout, input_data) -> CommandResult` | No | 0 |
| 3 | `CommandResult` (stdout/stderr/exit_code/timed_out) | No | 0 |

**A = 0/3 × 100 = 0.00**

### License (L)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 | 1 | "MIT License" matches repo MIT. |
| 2 | 1 | Valid identifier. |
| 3 | 1 | No conflicting info. |

**L = 100.00**

**C_R(data2) = (100 + 0 + 20 + 0 + 0 + 100) / 6 = 36.67**

---

## README 3 — `data3.md`

### Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 | 1 | Title `command-launcher` matches repo name. |
| 2 | 1 | Names this project. |
| 3 | 1 | No hallucinated terms. |

**T = 100.00**

### Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 | 0 | Describes a "**Node.js** utility to launch external commands … callbacks/Promises". Real project is a Go binary. |
| 2 | 0 | No Node.js module in repo. |
| 3 | 0 | Callback/Promise/sync exec APIs unsupported. |
| 4 | 0 | Node child-process domain differs from launcher/distribution. |
| 5 | 0 | Terminology mismatch. |

**O = 0.00**

### Installation (I) — executed
Documented paths: `npm install command-launcher` / `yarn add command-launcher` (Node.js 10+).

| Rule | Verdict | Evidence |
|---|---|---|
| 1 dependencies declared | 1 | Declares "Node.js 10 or later". |
| 2 commands execute unmodified | 1 | `npm install command-launcher` → `added 1 package … found 0 vulnerabilities` (exit 0). yarn hits the same registry entry. |
| 3 no unresolved dependency errors | 1 | npm reported no dependency errors. |
| 4 environment requirements correct | 0 | Node.js runtime is wrong for a Go project. |
| 5 expected executable artifact produced | 0 | Installed package is `command-launcher@0.0.1-security`, a **security-holding placeholder** with no code; `require("command-launcher")` → "Cannot find module". The documented library is not produced. |

**I = 3/5 × 100 = 60.00**

### Usage and Examples (U) — executed
| # | Snippet | Executes | E_i |
|---|---|---|---|
| 1 | `commandLauncher("ls", ["-l","/usr"], cb)` | No — `require("command-launcher")` throws "Cannot find module" (security-holder has no entry point) | 0 |
| 2 | `commandLauncher.exec("node", ["--version"])` | No — same require failure | 0 |
| 3 | `commandLauncher.execSync("echo", ["Hello World"])` | No — same require failure | 0 |

**U = 0/3 × 100 = 0.00**

### API Reference (A)
| # | Element | Exists | A_i |
|---|---|---|---|
| 1 | `commandLauncher(command, args?, callback?)` | No | 0 |
| 2 | `commandLauncher.exec(command, args?) -> Promise` | No | 0 |
| 3 | `commandLauncher.execSync(command, args?) -> Buffer` | No | 0 |

**A = 0/3 × 100 = 0.00**

### License (L)
| Rule | Verdict | Evidence |
|---|---|---|
| 1 | 1 | "MIT License" matches repo MIT. |
| 2 | 1 | Valid identifier. |
| 3 | 1 | No conflicting info. |

**L = 100.00**

**C_R(data3) = (100 + 0 + 60 + 0 + 0 + 100) / 6 = 43.33**

---

## Section-score summary

| README | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| data1.md | 100.00 | 0.00 | 20.00 | 0.00 | 0.00 | 100.00 | 36.67 |
| data2.md | 100.00 | 0.00 | 20.00 | 0.00 | 0.00 | 100.00 | 36.67 |
| data3.md | 100.00 | 0.00 | 60.00 | 0.00 | 0.00 | 100.00 | 43.33 |
| **average** | 100.00 | 0.00 | 33.33 | 0.00 | 0.00 | 100.00 | **38.89** |

Average consistency check: installation = (20+20+60)/3 = 33.33; correctness = (36.67+36.67+43.33)/3 = 38.89. ✓
