# ATRAK Evaluation — CommandLauncher (README-AI)

Project: **CommandLauncher** (`command-laucher`)
Repository: https://github.com/criteo/command-launcher
Tool: **README-AI** (v0.6.0rc1)
README: `compare-readme-ai/command-launcher.md`

> ATRAK is **presence-only**. Incorrect/hallucinated content still counts as
> present. An element is **absent (0)** only when the carrying section is
> empty/missing, is a bare name-only list, or consists solely of unresolved
> placeholders (e.g. `{entrypoint}`, `INSERT-RUN-COMMAND-HERE`).

## Ground Truth Reference

- **Project:** command-launcher (Criteo) — a Go CLI launcher binary (default `cdt`, e.g. `cola`).
- **Repository:** https://github.com/criteo/command-launcher
- **Domain:** distribution/launching of command-line tools; a launcher synchronises with a remote command repository, auto-updates commands, and supports developer "dropin" packages.
- **Core domain entities:** command launcher binary, command, package, dropin, remote command repository, registry, credential/login, progressive rollout, auto-update, monitoring.
- **Core execution facts:** `go build` (Go ≥ 1.17) or pre-built binary on `PATH`; CLI subcommands `package install/list/…`, `remote`, `update`, `login`, `config`, `version`; dependencies include cobra, viper, go-keyring, graphite-golang, afero, conc; MIT licensed.
- **Core usage:** `cola <command>`; `cdt package install <pkg>`.

---

## README — `command-launcher.md`

### K_D — Domain Concepts
**Verdict: 0 (absent).**

The natural carrier, `## Overview`, is **empty**. The remaining candidate content is the "Features" table, whose bullets describe implementation **architecture and tooling** (Go, Cobra, TOML config, Go modules, logrus, GitHub Actions, testify, afero, conc, graphite) rather than the problem-domain abstractions. There is no conceptual explanation of what a command launcher *is*, nor of dropins, packages, or remote command repositories as domain entities. With the Overview empty and only architecture/execution facts elsewhere, no evaluable domain-concept content is provided.

### K_E — Execution Facts
**Verdict: 1 (present).**

Abundant runtime/build/dependency facts are provided:
- Prerequisites: "Programming Language: Go", package managers.
- Installation: `git clone`, `cd`, `go build`.
- Testing: `go test ./...`.
- Features table lists concrete dependencies and integrations (go-keyring/wincred credential management, viper config, graphite-golang metrics, afero FS, conc concurrency, GitHub Actions CI, `.pkg` package files, TOML configuration).

These are evaluable execution facts (present regardless of any inaccuracies).

### K_U — Usage Patterns
**Verdict: 0 (absent).**

The dedicated "Usage" subsection consists solely of unresolved placeholders:
`go run {entrypoint}` and `echo 'INSERT-RUN-COMMAND-HERE'`. Per the ATRAK rule, placeholder-only content is absent. No demonstration of applying the tool (e.g. `cola <command>` / `cdt package install`) is provided. The `go build` and `go test ./...` commands are build/test execution facts (counted under K_E), not demonstrations of how the software is applied to its purpose.

### Verdict
| Element | Value |
|---|---|
| K_D | 0 |
| K_E | 1 |
| K_U | 0 |

**K = (0 + 1 + 0)/3 × 100 = 33.33**

---

## ATRAK summary

| README | K_D | K_E | K_U | ATRAK |
|---|---|---|---|---|
| command-launcher.md | 0 | 1 | 0 | 33.33 |
| **average** | 0.00 | 1.00 | 0.00 | **33.33** |

Single-README evaluation: the average row equals the README row. ✓

### Cross-checked sources
- Cloned repo `README.md`, `LICENSE`, `cmd/*.go`; built `./cdt --help` (local `/tmp/cl-groundtruth`).
- https://criteo.github.io/command-launcher/
- Local execution of the README-AI documented commands (`go build` OK; `go run {entrypoint}` malformed-path error).
