# Command Launcher README Correctness Evaluation

**Methodology:** Section 4.4.2 of *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis* (Andrade & Ribeiro, UERJ).

**Documentation Sources Cross-checked:**
- Official GitHub repository: https://github.com/criteo/command-launcher
- Real README: https://raw.githubusercontent.com/criteo/command-launcher/main/README.md
- LICENSE file: https://raw.githubusercontent.com/criteo/command-launcher/main/LICENSE (MIT, Copyright 2022 Criteo)
- `main.go`: https://raw.githubusercontent.com/criteo/command-launcher/main/main.go — confirms Go language, binary name `cdt`, app name `Criteo Dev Toolkit`
- `go.mod`: https://raw.githubusercontent.com/criteo/command-launcher/main/go.mod — confirms Go module `github.com/criteo/command-launcher`, Go >= 1.23
- `cmd/root.go`: https://raw.githubusercontent.com/criteo/command-launcher/main/cmd/root.go — confirms CLI commands: `version`, `config`, `completion`, `help`, `update`
- `cmd/config.go`: https://raw.githubusercontent.com/criteo/command-launcher/main/cmd/config.go — confirms `config [key]` / `config [key] [value]` subcommand
- `cmd/package-mgmt.go`: https://raw.githubusercontent.com/criteo/command-launcher/main/cmd/package-mgmt.go — confirms `package list`, `package install` subcommands
- `cmd/version.go`: confirms `version` subcommand
- `cmd/update.go`: confirms `update --package` / `update --self` subcommands
- `cmd/login.go`: confirms `login` subcommand with `--username`, `--password` flags
- GitHub Releases API: latest release `1.15.1`, binary assets named `cdt_*` and `cola_*` for Linux/macOS/Windows — **no `pip install`, no `npm install`**

**Key Ground Truth Facts:**
- Language: **Go** (not Python, not Node.js)
- Binary name: `cdt` (or `cola`) — a pre-built binary downloaded from releases
- Installation: download binary from release page, copy to PATH — **not pip, not npm**
- The tool is a **CLI command dispatcher** that syncs commands from a remote repository
- It is **not** a Python library, **not** a Node.js package
- License: **MIT** (Copyright 2022 Criteo)
- Repository: `criteo/command-launcher` (not `xZepyx/command-launcher`)

---

## Scoring Formula (from TCC §4.4.2)

Each section uses binary criteria Vᵢ ∈ {0,1}. Section scores are percentages. Final score:

```
CR = (T + O + I + U + A + L) / 6
```

---

## data1.md Evaluation

### Step-by-step Reasoning

**data1.md claims:** Command Launcher is a "lightweight Python tool" for automating CLI tasks, installed via `pip install command-launcher`, with a Python decorator-based API (`CommandLauncher`, `@launcher.command`, `@argument`).

---

**Project Title (T)**

Criteria:
1. Title exactly matches repository/official name → README says "Command Launcher". The official repo is `criteo/command-launcher`, official name is "Command Launcher" / "command-launcher". The title matches the name. ✅ V1=1
2. Title does not describe a different project → "Command Launcher" is the correct project name. ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucinated terms in the title itself. ✅ V3=1

**T = (1+1+1)/3 × 100 = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → README says "lightweight Python tool designed to simplify and automate the execution of command-line tasks." The real tool is a **Go binary** that acts as a command dispatcher syncing CLI tools from a remote repository. The description of "Python tool" is factually wrong — the project is written in Go. ❌ V1=0
2. Described functionality supported by repository artifacts → "Command Registration", "Argument Parsing", "Execution Environment" as Python concepts — none of these exist in the Go codebase as described. The real tool uses a manifest-based package system, not Python decorators. ❌ V2=0
3. Overview does not describe unsupported features → "Extensibility: new commands can be added as Python functions decorated or registered to the launcher" — this is hallucinated. The real extensibility is via dropin packages and manifest files, not Python decorators. ❌ V3=0
4. Correctly identifies software domain → The domain is partially correct (CLI command management/dispatcher), but the description frames it as a Python scripting tool rather than a Go-based CLI package manager. ❌ V4=0
5. Terminology matches repository terminology → "Command Registration", "Argument Parsing", "Execution Environment" do not match the repository's terminology ("dropin", "package", "remote repository", "sync", "cola/cdt"). ❌ V5=0

**O = (0+0+0+0+0)/5 × 100 = 0**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → README says "Python 3.7 or higher" and `pip install command-launcher`. The real tool requires Go >= 1.23 to build from source, or simply downloading a pre-built binary. Python is not required at all. ❌ V1=0
2. Installation commands execute without modification → `pip install command-launcher` — there is no `command-launcher` package on PyPI for this tool. The real installation is downloading a binary from GitHub releases. ❌ V2=0
3. No unresolved dependency errors → `pip install command-launcher` would either install a completely different package or fail. ❌ V3=0
4. Documented environment requirements correct → "Python 3.7 or higher" is wrong; the tool is a Go binary. ❌ V4=0
5. Installation produces expected executable artifact → `pip install` would not produce the `cdt`/`cola` binary. ❌ V5=0

**I = (0+0+0+0+0)/5 × 100 = 0**

---

**Usage and Examples (U)**

Snippets evaluated (k=3):

| # | Snippet | Execution Result | Score |
|---|---------|-----------------|-------|
| E1 | `command-launcher <command> [options]` / `command-launcher --help` | The binary is named `cdt` or `cola`, not `command-launcher`. This command would fail unless the user renamed the binary. The CLI interface pattern is partially correct conceptually but the binary name is wrong. ❌ | 0 |
| E2 | Python decorator pattern `from command_launcher import CommandLauncher, argument` | This Python module does not exist. The real tool is a Go binary with no Python API. This snippet cannot execute. ❌ | 0 |
| E3 | `python myscript.py greet --name John` | Depends on the non-existent Python module above. Cannot execute. ❌ | 0 |

**U = 0/3 × 100 = 0**

---

**API Reference (A)**

Documented API elements (n=4): `CommandLauncher` class, `command(name)` decorator, `run(args)` method, `argument` decorator.

| # | Element | Exists in repo | Names Correct | Params Correct | Returns Correct | Behavior Correct | Not Deprecated |
|---|---------|---------------|--------------|----------------|-----------------|-----------------|----------------|
| A1 | `CommandLauncher` Python class | ❌ Does not exist | ❌ | ❌ | ❌ | ❌ | N/A |
| A2 | `command(name)` decorator | ❌ Does not exist | ❌ | ❌ | ❌ | ❌ | N/A |
| A3 | `run(args)` method | ❌ Does not exist as Python method | ❌ | ❌ | ❌ | ❌ | N/A |
| A4 | `argument` decorator | ❌ Does not exist | ❌ | ❌ | ❌ | ❌ | N/A |

All 4 documented API elements are hallucinated — they do not exist in the repository.

**A = 0/4 × 100 = 0**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → README states "MIT License" — confirmed MIT via LICENSE file. ✅ V1=1
2. License identifier is valid → "MIT" is a valid SPDX identifier. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

However, the LICENSE link points to `https://github.com/xZepyx/command-launcher/blob/master/LICENSE` — this is a **wrong repository URL** (not `criteo/command-launcher`). The license type is correct but the source reference is wrong. Per the criteria, the license identifier and match are evaluated — the type matches. V1=1 (type matches), V2=1 (valid identifier), V3=1 (no conflict).

**L = (1+1+1)/3 × 100 = 100**

---

### data1.md Final Score

```
CR = (100 + 0 + 0 + 0 + 0 + 100) / 6 = 33.33
```

**data1.md is a severely incorrect README.** The LLM hallucinated the entire technology stack, describing a Python library with a decorator-based API when the real tool is a Go binary CLI package manager. Only the title and license type are correct. All installation commands, usage examples, and API elements are fabricated and non-executable.

---

## data2.md Evaluation

### Step-by-step Reasoning

**data2.md claims:** `command-launcher` is a "lightweight Python library" for running shell commands from Python scripts, installed via `pip install command-launcher`, with `CommandLauncher` and `CommandResult` Python classes.

---

**Project Title (T)**

Criteria:
1. Title exactly matches repository/official name → "command-launcher" matches the repo name `criteo/command-launcher`. ✅ V1=1
2. Title does not describe a different project → Correct name. ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucinated terms in the title. ✅ V3=1

**T = (1+1+1)/3 × 100 = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → "lightweight Python library designed to simplify running shell commands from within Python scripts." The real tool is a **Go binary** CLI package manager/dispatcher. This is factually wrong. ❌ V1=0
2. Described functionality supported by repository artifacts → "Process Management", "Result Handling", "Timeouts" as Python subprocess concepts — none of these exist in the Go codebase as described. ❌ V2=0
3. Overview does not describe unsupported features → "Timeouts: Ability to limit the execution time of the commands" — this is hallucinated as a Python feature. ❌ V3=0
4. Correctly identifies software domain → Partially correct (command execution), but wrong technology and wrong use case. ❌ V4=0
5. Terminology matches repository terminology → "stdout", "stderr", "exit status", "subprocess" do not match the repository's terminology ("dropin", "package", "remote repository", "sync", "cdt/cola"). ❌ V5=0

**O = (0+0+0+0+0)/5 × 100 = 0**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → "Python 3.6 or later" and `pip install command-launcher` — wrong language and wrong package manager. ❌ V1=0
2. Installation commands execute without modification → `pip install command-launcher` does not install the criteo tool. ❌ V2=0
3. No unresolved dependency errors → Would install wrong package or fail. ❌ V3=0
4. Documented environment requirements correct → "Python 3.6 or later" is wrong; tool is a Go binary. ❌ V4=0
5. Installation produces expected executable artifact → No `cdt`/`cola` binary produced. ❌ V5=0

**I = (0+0+0+0+0)/5 × 100 = 0**

---

**Usage and Examples (U)**

Snippets evaluated (k=3):

| # | Snippet | Execution Result | Score |
|---|---------|-----------------|-------|
| E1 | `from command_launcher import CommandLauncher` / `launcher.run("echo Hello, World!")` | Python module does not exist. Cannot execute. ❌ | 0 |
| E2 | `launcher.run("sleep 5", timeout=2)` / `result.timed_out` | Non-existent Python API. Cannot execute. ❌ | 0 |
| E3 | `launcher.run("cat", input_data="Hello from stdin\n")` | Non-existent Python API. Cannot execute. ❌ | 0 |

**U = 0/3 × 100 = 0**

---

**API Reference (A)**

Documented API elements (n=2 classes, ~5 attributes/methods): `CommandLauncher.run(command, timeout, input_data)`, `CommandResult` with `stdout`, `stderr`, `exit_code`, `timed_out`.

| # | Element | Exists in repo | Score |
|---|---------|---------------|-------|
| A1 | `CommandLauncher` Python class | ❌ Does not exist | 0 |
| A2 | `CommandLauncher.run(command, timeout, input_data)` | ❌ Does not exist | 0 |
| A3 | `CommandResult` class | ❌ Does not exist | 0 |
| A4 | `CommandResult.stdout` | ❌ Does not exist | 0 |
| A5 | `CommandResult.stderr` | ❌ Does not exist | 0 |
| A6 | `CommandResult.exit_code` | ❌ Does not exist | 0 |
| A7 | `CommandResult.timed_out` | ❌ Does not exist | 0 |

All 7 documented API elements are hallucinated.

**A = 0/7 × 100 = 0**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → "MIT License" — confirmed MIT. ✅ V1=1
2. License identifier is valid → "MIT" is valid. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

Note: LICENSE link again points to wrong repo `xZepyx/command-launcher`. License type is correct.

**L = (1+1+1)/3 × 100 = 100**

---

### data2.md Final Score

```
CR = (100 + 0 + 0 + 0 + 0 + 100) / 6 = 33.33
```

**data2.md is a severely incorrect README.** Same fundamental hallucination as data1.md — the LLM invented a Python subprocess wrapper library. The tool is a Go binary CLI package manager. Only title and license type are correct.

---

## data3.md Evaluation

### Step-by-step Reasoning

**data3.md claims:** `command-launcher` is a "simple Node.js utility" for launching external commands from JavaScript, installed via `npm install command-launcher`, with a callback/Promise/sync JavaScript API.

---

**Project Title (T)**

Criteria:
1. Title exactly matches repository/official name → "command-launcher" matches the repo name. ✅ V1=1
2. Title does not describe a different project → Correct name. ✅ V2=1
3. Title does not contain hallucinated terminology → No hallucinated terms in the title. ✅ V3=1

**T = (1+1+1)/3 × 100 = 100**

---

**Overview (O)**

Criteria:
1. Primary functionality correctly described → "simple Node.js utility designed to facilitate launching external commands or executable files from JavaScript code." The real tool is a **Go binary** CLI package manager. This is factually wrong. ❌ V1=0
2. Described functionality supported by repository artifacts → "Callback and Promise APIs", "Cross-Platform Compatibility" as Node.js concepts — none exist in the Go codebase. ❌ V2=0
3. Overview does not describe unsupported features → "Supporting both callback functions and Promises" — hallucinated Node.js API. ❌ V3=0
4. Correctly identifies software domain → Partially correct (command execution), but wrong technology and wrong use case. ❌ V4=0
5. Terminology matches repository terminology → "callback", "Promise", "child process", "async/await" do not match the repository's terminology ("dropin", "package", "remote repository", "sync", "cdt/cola"). ❌ V5=0

**O = (0+0+0+0+0)/5 × 100 = 0**

---

**Installation (I)**

Criteria:
1. All required dependencies explicitly declared → "Node.js 10 or later" and `npm install command-launcher` — wrong language and wrong package manager. ❌ V1=0
2. Installation commands execute without modification → `npm install command-launcher` would install a different npm package, not the criteo Go tool. ❌ V2=0
3. No unresolved dependency errors → Would install wrong package. ❌ V3=0
4. Documented environment requirements correct → "Node.js 10 or later" is wrong; tool is a Go binary. ❌ V4=0
5. Installation produces expected executable artifact → No `cdt`/`cola` binary produced. ❌ V5=0

**I = (0+0+0+0+0)/5 × 100 = 0**

---

**Usage and Examples (U)**

Snippets evaluated (k=3):

| # | Snippet | Execution Result | Score |
|---|---------|-----------------|-------|
| E1 | `const commandLauncher = require("command-launcher")` / callback API | npm package `command-launcher` is not the criteo tool. The API described does not match any real package. Cannot execute correctly. ❌ | 0 |
| E2 | `commandLauncher.exec("node", ["--version"])` Promise API | Non-existent API for this tool. Cannot execute. ❌ | 0 |
| E3 | `commandLauncher.execSync("echo", ["Hello World"])` | Non-existent API for this tool. Cannot execute. ❌ | 0 |

**U = 0/3 × 100 = 0**

---

**API Reference (A)**

Documented API elements (n=3): `commandLauncher(command, args, callback)`, `commandLauncher.exec(command, args)`, `commandLauncher.execSync(command, args)`.

| # | Element | Exists in repo | Score |
|---|---------|---------------|-------|
| A1 | `commandLauncher(command, args, callback)` | ❌ Does not exist | 0 |
| A2 | `commandLauncher.exec(command, args): Promise` | ❌ Does not exist | 0 |
| A3 | `commandLauncher.execSync(command, args): Buffer` | ❌ Does not exist | 0 |

All 3 documented API elements are hallucinated.

**A = 0/3 × 100 = 0**

---

**License (L)**

Criteria:
1. Documented license matches repository LICENSE file → "MIT License" — confirmed MIT. ✅ V1=1
2. License identifier is valid → "MIT" is valid. ✅ V2=1
3. No conflicting licensing information → Only MIT mentioned. ✅ V3=1

Note: LICENSE link again points to wrong repo `xZepyx/command-launcher`. License type is correct.

**L = (1+1+1)/3 × 100 = 100**

---

### data3.md Final Score

```
CR = (100 + 0 + 0 + 0 + 0 + 100) / 6 = 33.33
```

**data3.md is a severely incorrect README.** The LLM hallucinated a Node.js child process wrapper library. The tool is a Go binary CLI package manager. Only title and license type are correct.

---

## Summary: All Three command-launcher READMEs

| README | T | O | I | U | A | L | CR |
|--------|---|---|---|---|---|---|-----|
| data1.md | 100 | 0 | 0 | 0 | 0 | 100 | **33.33** |
| data2.md | 100 | 0 | 0 | 0 | 0 | 100 | **33.33** |
| data3.md | 100 | 0 | 0 | 0 | 0 | 100 | **33.33** |
| **Average** | **100** | **0** | **0** | **0** | **0** | **100** | **33.33** |

### Final Average Score (Equation 2 from TCC)

```
Score_avg = (33.33 + 33.33 + 33.33) / 3 = 33.33
```

---

## Analysis and Observations

**Why all three score 33.33:**

Command Launcher (`criteo/command-launcher`) is a low-popularity repository (44 stars) with no usage instructions in its README. The real README is developer/contributor-focused (build instructions, test instructions, release process) and does not contain end-user usage examples. This matches the TCC's classification: low-popularity + no usage instructions.

The LLM failed catastrophically on this repository because:

1. **Wrong language identification:** Each of the three READMEs identified a different language — data1.md said Python, data2.md said Python (subprocess), data3.md said Node.js. The real language is **Go**.

2. **Hallucinated package managers:** `pip install command-launcher` (data1, data2) and `npm install command-launcher` (data3) are both wrong. The real installation is downloading a pre-built binary (`cdt` or `cola`) from GitHub releases.

3. **Hallucinated APIs:** All three READMEs invented entirely fictional APIs (Python decorator pattern, Python subprocess wrapper, Node.js child process wrapper) that have no correspondence to the actual Go codebase.

4. **Wrong repository reference:** All three link to `xZepyx/command-launcher` in the LICENSE URL, which is a different repository entirely.

5. **Only correct elements:** The project name ("command-launcher") and the license type (MIT) were correctly identified across all three READMEs. The MIT license is a common default that the LLM likely guessed correctly.

**Root cause:** The `criteo/command-launcher` repository is a low-popularity Go project with minimal end-user documentation. The LLM had insufficient training data about this specific tool and defaulted to generating plausible-sounding but entirely fabricated documentation based on the name "command-launcher" alone, associating it with common patterns from more popular tools in other languages.

**This result validates the TCC's hypothesis** that low-popularity repositories without usage instructions are the hardest case for LLM-based README generation, as the model cannot rely on prior knowledge and must extract information purely from repository artifacts.
