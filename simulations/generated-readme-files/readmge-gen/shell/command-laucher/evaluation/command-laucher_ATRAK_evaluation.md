# ATRAK Evaluation — CommandLauncher (README-Gen)

Project: **CommandLauncher** (`command-laucher`)
Repository: https://github.com/criteo/command-launcher
Tool: **README-Gen**
READMEs (input order): `data1.md`, `data2.md`, `data3.md`

> ATRAK is a **presence-only** dimension. Content that is factually wrong or
> hallucinated still counts as **present** — factual accuracy is scored in the
> correctness dimension and must not be double-counted here. An element is
> **absent (0)** only when the carrying section is empty/missing, is a bare
> name-only list, or consists solely of unresolved placeholders.

## Ground Truth Reference

- **Project:** command-launcher (Criteo) — a Go CLI binary (default name `cdt`, e.g. `cola`).
- **Repository:** https://github.com/criteo/command-launcher
- **Domain:** distribution and launching of command-line tools. A small launcher binary synchronises with a remote command repository, keeps commands up to date, and lets developers add their own "dropin" packages.
- **Core domain entities:** command launcher binary, command, package, dropin, remote command repository, registry, credential/login, progressive rollout, auto-update, monitoring.
- **Core execution facts:** built with `go build` (Go ≥ 1.17); distributed as a pre-built binary copied onto `PATH`; CLI subcommands `package install/list/inspect/delete/setup/pause`, `remote`, `update`, `login`, `config`, `version`, `rename`, `completion`; MIT licensed.
- **Core usage:** `cola <command>` runs a launched command; `cdt package install <pkg>` installs a dropin package.

Note: All three README-Gen files describe hallucinated non-Go projects. Under ATRAK's presence-only rule, incorrect content still counts as present, so each Knowledge Element can still score 1 provided the README supplies evaluable (non-empty, non-placeholder, non-bare-name) content for it.

---

## README 1 — `data1.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D — Domain Concepts** | 1 | Dedicated "Domain Concepts" subsection defines Command Registration, Argument Parsing, Execution Environment, Command Execution, Extensibility — each with an explanatory sentence (not bare names). Evaluable content present (though describing a fictional Python tool). |
| **K_E — Execution Facts** | 1 | Provides installation commands (`pip install`, source build), Python ≥ 3.7 requirement, CLI invocation form, API parameters/types (`type`, `default`, `help`), and a documented expected output ("Hello, John!"). |
| **K_U — Usage Patterns** | 1 | Multiple worked examples: CLI invocation, a full `@launcher.command('greet')` script, and a run command with expected output — demonstrations of how/why to use it. |

**K(data1) = (1 + 1 + 1)/3 × 100 = 100.00**

## README 2 — `data2.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D** | 1 | "Domain Concepts" subsection defines Command Execution, Process Management, Result Handling, Timeouts with explanatory prose. |
| **K_E** | 1 | Install command + Python ≥ 3.6 requirement; method signature with parameter types (`timeout: Optional[int]`, `input_data: Optional[str]`), return type `CommandResult`, attribute types, and documented expected output. |
| **K_U** | 1 | Three usage examples (basic run, timeout handling, stdin input) with narrative what/how. |

**K(data2) = 100.00**

## README 3 — `data3.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D** | 1 | "Domain Concepts" subsection defines Command Execution, Process Management, Cross-Platform Compatibility, Callback and Promise APIs with explanations. |
| **K_E** | 1 | Install commands (`npm`, `yarn`), Node.js ≥ 10 requirement, function signatures with parameter/return types (callback `(error, stdout, stderr)`, `Promise<{stdout,stderr}>`, `Buffer`). |
| **K_U** | 1 | Three usage examples (callback, async/await Promise, synchronous) with surrounding explanation. |

**K(data3) = 100.00**

---

## ATRAK summary

| README | K_D | K_E | K_U | ATRAK |
|---|---|---|---|---|
| data1.md | 1 | 1 | 1 | 100.00 |
| data2.md | 1 | 1 | 1 | 100.00 |
| data3.md | 1 | 1 | 1 | 100.00 |
| **average** | 1.00 | 1.00 | 1.00 | **100.00** |

Consistency check: each column mean over the three READMEs = 1.00; ATRAK mean = 100.00. ✓

### Cross-checked sources
- Cloned repo `README.md`, `LICENSE`, `cmd/*.go`, built `./cdt --help` (local).
- https://criteo.github.io/command-launcher/
- PyPI 404, npm security-holder, GitHub repo existence checks (see correctness evaluation for details).
