# jq — README-Gen Correctness Evaluation

Deterministic, rule-based correctness assessment of the three README-Gen
generations (`data1.md`, `data2.md`, `data3.md`) for the project **jq**.

`C_R = (T + O + I + U + A + L) / 6`

## Cross-checked sources

- Repository (ground truth): https://github.com/jqlang/jq
- License file `COPYING`: https://raw.githubusercontent.com/jqlang/jq/master/COPYING → **MIT** (code), CC-BY-3.0 (docs)
- Official manual (jq 1.8): https://jqlang.org/manual/
- libjq C API header `src/jq.h`: https://raw.githubusercontent.com/jqlang/jq/master/src/jq.h
- `src/jv.h` (confirmed `jv_parse` present)
- Installed artifact used for execution: `jq-1.8.2` (`/opt/homebrew/bin/jq`, Homebrew)
- Source build executed locally in an isolated dir (`/tmp/jq_eval`)
- Package availability:
  - apt (Ubuntu/Debian): https://packages.ubuntu.com/search?keywords=jq — "lightweight and flexible command-line JSON processor" (jammy 1.6, noble 1.7.1, questing 1.8.1)
  - dnf (Fedora): https://packages.fedoraproject.org/pkgs/jq/jq/ — jq 1.8.x, License MIT AND ICU AND CC-BY-3.0
  - pacman (Arch): https://archlinux.org/packages/?name=jq — Extra, jq 1.8.2-1
  - Chocolatey: https://community.chocolatey.org/packages/jq — jq 1.8.1 (5M+ downloads)
  - Scoop main bucket: https://raw.githubusercontent.com/ScoopInstaller/Main/master/bucket/jq.json — jq 1.8.2, MIT

## Host-execution note (installation)

- `brew install jq` is directly runnable on this macOS host — verified (`jq-1.8.2`).
- apt-get / dnf / pacman / choco / scoop paths are OS-specific and not runnable
  on macOS; each documented package was verified to exist in the respective
  official repository (sources above). Per the run manifest these are not failed
  merely for OS mismatch.
- The **source build** IS runnable on macOS and was executed exactly as
  documented (see Installation evidence per README).

---

# README 1 — `data1.md`

### Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| T1 title matches repo/official name | 1 | Title `# jq` == repository name `jqlang/jq`. |
| T2 not a different project | 1 | Describes the jq JSON processor. |
| T3 no hallucinated terminology | 1 | No invented terms. |

**T = 3/3 × 100 = 100**

### Overview (O)
Overview describes jq as a "lightweight and flexible command-line JSON
processor" and lists domain concepts (JSON, Filters, Streams, Operators/
Functions, Modules, Pipelines).
| Rule | Verdict | Evidence |
|---|---|---|
| O1 primary functionality correct | 1 | "slice, filter, map, and transform structured JSON" matches jq (manual intro). |
| O2 supported by artifacts | 1 | Filters/pipelines/modules are core jq features (manual). |
| O3 no unsupported features | 1 | All listed concepts (streams, modules, pipelines) exist. |
| O4 correct domain | 1 | Command-line JSON processing. |
| O5 terminology matches repo | 1 | "filters", "pipelines", "modules" are jq's own terms. |

**O = 5/5 × 100 = 100**

### Installation (I) — executed
Documented paths: apt/dnf/pacman (Linux), `brew install jq` (macOS), Windows
binaries + `choco install jq`, and a **source build**:
```
git clone https://github.com/jqlang/jq.git
cd jq
autoreconf -i
./configure
make
sudo make install
```
Execution evidence:
- `brew install jq` → works (`jq-1.8.2`).
- apt/dnf/pacman/choco packages verified to exist (sources above).
- Source build run verbatim: `git clone` (no `--recursive`), `autoreconf -i`
  (ok), `./configure` (ok), **`make` FAILS**: `Making all in vendor/oniguruma`
  → `make[2]: *** No rule to make target 'all'. Stop.` The `vendor/oniguruma`
  submodule is empty because the documented steps omit
  `git submodule update --init`. A control build with `git clone --recursive`
  on the same host completed and produced a working `jq` binary (returns `5`
  for `{"x":5}|.x`), confirming the failure is caused by the omitted submodule
  step, not the host.

| Rule | Verdict | Evidence |
|---|---|---|
| I1 all dependencies explicitly declared | 0 | Source path omits the oniguruma submodule and the autotools/C toolchain prerequisites. |
| I2 commands execute without modification | 0 | `make` fails without the (undocumented) `git submodule update --init`. |
| I3 no unresolved dependency errors | 0 | Missing `vendor/oniguruma` dependency aborts the build. |
| I4 environment requirements correct | 1 | No incorrect version/env claim is made (no false `Requires-*`). |
| I5 produces expected executable artifact | 0 | Source path yields no `jq` binary as written (brew path does, but any failing path fails the rule). |

**I = 1/5 × 100 = 20**

### Usage and Examples (U) — executed
| # | Snippet | Executed result | Output match | E |
|---|---|---|---|---|
| 1 | `cat data.json \| jq .` | pretty-printed JSON | matches "formatted, indented JSON" | 1 |
| 2 | `jq '.name' input.json` on `{"name":"Alice",…}` | `"Alice"` | matches documented `"Alice"` | 1 |
| 3 | `jq '.[] \| select(.age > 26) \| .name'` | `"Alice"` | matches documented `"Alice"` | 1 |
| 4 | `jq '. + { "country": "Wonderland" }'` | object with added `country` | matches "Add new field" | 1 |
| 5 | `value=$(jq -r '.name' input.json); echo "Name is $value"` | `Name is Alice` | matches described behavior | 1 |

**U = 5/5 × 100 = 100**

### API Reference (A) — executed / manual-verified
Flags: `-c/--compact-output`, `-r/--raw-output`, `-s/--slurp`,
`-f/--from-file`, `--arg`, `--argjson`, `-n/--null-input`,
`-e/--exit-status`, `--version` — all exist and behave as documented
(manual + execution). Filters/functions: `.`, `.foo`, `.[]`, `select`,
arithmetic `+ - * / %`, comparisons, logical `and/or/not`, `map`, `reduce`,
`length`, `startswith`, `endswith`, `contains`, `index`, `sort`, `unique`,
`input`, `inputs` — all present in the manual. Execution-Facts subsection
(streaming, `|` piping, `$name` variables, multi-output lines) is accurate.
No deprecated/removed API documented as current.

| Element class | Count | Pass | Note |
|---|---|---|---|
| CLI flags | 9 | 9 | all in manual "Invoking jq" |
| Filters/operators/functions | 18 | 18 | all in manual |

**A = 100** (every documented element exists with correct names/behavior)

### License (L)
"released under the MIT License".
| Rule | Verdict | Evidence |
|---|---|---|
| L1 matches repo LICENSE | 1 | `COPYING` = MIT for code (confirmed). |
| L2 identifier valid | 1 | MIT is a valid SPDX id. |
| L3 no conflicting info | 1 | Only MIT stated. |

**L = 3/3 × 100 = 100**

### C_R (data1.md) = (100 + 100 + 20 + 100 + 100 + 100) / 6 = **86.67**

---

# README 2 — `data2.md`

### Project Title (T)
Title `jq - Command-line JSON Processor` (the official tagline).
T1=1 (contains repo name `jq`), T2=1, T3=1. **T = 100**

### Overview (O)
Describes parse/filter/transform/output of JSON; concepts JSON Data, Filters,
Pipelines, Streams, Slice and Dice, Functions — all accurate.
O1..O5 = 1. **O = 100**

### Installation (I) — executed
Paths: `brew install jq` (macOS), `apt-get`, `dnf`, Windows binaries +
Chocolatey + Scoop. **No source build.**
- `brew install jq` runs cleanly → `jq-1.8.2`.
- apt/dnf packages verified (sources above); choco + scoop packages verified.

| Rule | Verdict | Evidence |
|---|---|---|
| I1 dependencies declared | 1 | Package-manager installs; deps resolved by the manager, none omitted. |
| I2 commands execute without modification | 1 | `brew install jq` works verbatim; other paths are valid package installs. |
| I3 no unresolved dependency errors | 1 | Clean brew install; packages exist. |
| I4 environment requirements correct | 1 | No incorrect version/env claim. |
| I5 produces expected artifact | 1 | brew yields the `jq` binary. |

**I = 5/5 × 100 = 100**

### Usage and Examples (U) — executed
| # | Snippet | Executed result | Output match | E |
|---|---|---|---|---|
| 1 | `jq '.name' data.json` on `{"name":"John","age":30}` | `"John"` | matches `"John"` | 1 |
| 2 | `jq '.[] \| select(.age > 30)' data.json` | Bob object | matches documented object | 1 |
| 3 | `jq 'map(.age = .age * 2)' data.json` | ages 50/70 | matches documented output | 1 |
| 4 | `echo '{"foo": 42}' \| jq '.foo'` | `42` | matches `42` | 1 |
| 5 | `jq -r '.users[] \| select(.active) \| .email' users.json` | raw active emails | matches "raw emails of active users" | 1 |

**U = 5/5 × 100 = 100**

### API Reference (A)
API Reference section flags: `-c/--compact-output`, `-M/--monochrome-output`,
`-r/--raw-output`, `-s/--slurp`, `-f/--from-file`, `-n/--null-input` — all
exist. Filters: `.foo`, `.[]`, `select`, `map`, `.`; functions `length`,
`keys`, `has`, `split`, `gsub` — all exist (manual). All names/behaviour
correct.

Rule 7 note: the separate **"Feedback and Debugging"** section documents
`--debug-dump` and `--verbose`, which do NOT exist (`jq: Unknown option
--debug-dump` / `--verbose`, verified by execution). This section is outside
the six rubric correctness sections and is not the sole carrier of API
information (the API Reference section already carries it), so per Ground Rule
7 it is **ignored** for scoring. It is recorded here as an observed defect but
does not lower the API score.

**A = 100** (all elements in the actual API Reference section are valid)

### License (L)
"licensed under the MIT License". L1=1, L2=1, L3=1. **L = 100**

### C_R (data2.md) = (100 + 100 + 100 + 100 + 100 + 100) / 6 = **100**

---

# README 3 — `data3.md`

### Project Title (T)
Title `# jq`. T1=1, T2=1, T3=1. **T = 100**

### Overview (O)
Describes jq as a functional JSON processor "similar to how sed, awk, and grep
operate on text"; concepts JSON Data, Filters, Pipelines/Composition,
Streaming, Functions/Operators, Variables/Assignments, Modules — all accurate
(manual). O1..O5 = 1. **O = 100**

### Installation (I) — executed
Paths: apt/dnf/pacman, `brew install jq`, Windows (stedolan releases + choco),
and a **source build**:
```
git clone https://github.com/stedolan/jq.git
cd jq
autoreconf -i
./configure
make
sudo make install
```
- `brew install jq` → works. `stedolan/jq` redirects to `jqlang/jq` (valid).
  Package paths verified.
- Source build has the **same defect as data1**: omits
  `git submodule update --init`; `make` fails on `vendor/oniguruma`
  (`No rule to make target 'all'`). Verified locally; control `--recursive`
  build succeeds, isolating the omission as the cause.

| Rule | Verdict | Evidence |
|---|---|---|
| I1 dependencies declared | 0 | oniguruma submodule + toolchain not declared. |
| I2 commands execute without modification | 0 | `make` fails without submodule init. |
| I3 no unresolved dependency errors | 0 | Missing `vendor/oniguruma`. |
| I4 environment requirements correct | 1 | No incorrect version/env claim. |
| I5 produces expected artifact | 0 | Source path yields no binary as written. |

**I = 1/5 × 100 = 20**

### Usage and Examples (U) — executed
| # | Snippet | Executed result | Output match | E |
|---|---|---|---|---|
| 1 | `jq '.' data.json` | pretty-printed JSON | matches "formatted nicely indented" | 1 |
| 2 | `jq '.name' data.json` | field value | matches "extract value of name" | 1 |
| 3 | `jq '.[] \| select(.age > 30)' data.json` | filtered object | matches | 1 |
| 4 | `jq '.[] \| .isAdult = (.age >= 18)' data.json` | objects with `isAdult` | matches "add isAdult based on age" | 1 |
| 5 | `jq '.[] \| select(.age >= 18) \| .name' data.json` | adult names | matches | 1 |
| 6 | `jq --arg city "London" '.[] \| select(.city == $city)' data.json` | London record | matches "assign/reuse variables" | 1 |

**U = 6/6 × 100 = 100**

### API Reference (A) — executed / manual & source verified
Flags: `-c`, `-r`, `-s`, `-n`, `--stream`, `--arg`, `--argjson` — all exist.
Filters/functions: `.foo`, `.[]`, `select`, `map`, `length`, arithmetic,
comparison, logical, `startswith`, `endswith`, `contains`, `..`, `keys`,
`has`, `type`, `tonumber`, `tostring`, `explode`, `implode`, array/object
construction `[]`/`{}` — all present in the manual.
**C API** (libjq): `jq_init`, `jq_compile`, `jq_start`, `jq_next` — all
present in `src/jq.h`; `jv_parse` — present in `src/jv.h`. All correct and
current.

| Element class | Count | Pass |
|---|---|---|
| CLI flags | 7 | 7 |
| Filters/operators/functions | 19 | 19 |
| libjq C API symbols | 5 | 5 |

**A = 100**

### License (L)
"licensed under the MIT License". L1=1, L2=1, L3=1. **L = 100**

### C_R (data3.md) = (100 + 100 + 20 + 100 + 100 + 100) / 6 = **86.67**

---

## Aggregate (mean of the 3 READMEs)

| Column | data1 | data2 | data3 | average |
|---|---|---|---|---|
| title | 100 | 100 | 100 | 100 |
| overview | 100 | 100 | 100 | 100 |
| installation | 20 | 100 | 20 | 46.67 |
| usage | 100 | 100 | 100 | 100 |
| api | 100 | 100 | 100 | 100 |
| license | 100 | 100 | 100 | 100 |
| **C_R** | **86.67** | **100** | **86.67** | **91.11** |

Average C_R = (86.67 + 100 + 86.67) / 3 = **91.11** (consistent with the mean
of each column: (100+100+46.67+100+100+100)/6 = 91.11).
