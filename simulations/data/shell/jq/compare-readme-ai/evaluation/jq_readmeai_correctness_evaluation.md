# jq — README-AI Correctness Evaluation

Deterministic correctness assessment of the README-AI generation
`jq_readme_readmeai.md` for the project **jq**.

`C_R = (T + O + I + U + A + L) / 6`

## Cross-checked sources
- Repository: https://github.com/jqlang/jq
- License `COPYING`: MIT (code), CC-BY-3.0 (docs)
- Manual: https://jqlang.org/manual/
- Installed artifact: `jq-1.8.2`; local source build in `/tmp/jq_eval`
- Package repos (apt/dnf/pacman/choco/scoop) — see README-Gen evaluation doc.

## Structure of the file
Title `JQ`, an **empty** `## Overview`, a `## Features` table, a
`## Project Structure` tree + file-index summaries, `## Getting Started`
(Prerequisites / Installation / Usage / Testing), Roadmap, Contributing,
`## License`, Acknowledgments. There is **no API Reference section**.

---

### Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| T1 matches repo/official name | 1 | `JQ` == `jq` (case only). |
| T2 not a different project | 1 | It is jq. |
| T3 no hallucinated terminology | 1 | Plain name. |

**T = 100**

### Overview (O)
The `## Overview` heading is empty. Per Ground Rule 7, the information the
Overview element expects (purpose/functionality) is carried elsewhere and is
evaluated under this section: the **Features** table ("Core written in C…",
"Uses parser.y (Bison) and lexer.l (Flex) for parsing JSON and jq
expressions", Autotools build, cross-compilation) and the Project-Index file
summaries (e.g. jq.1.prebuilt: "powerful and flexible transformation, querying,
and manipulation of JSON data directly from the command line").
| Rule | Verdict | Evidence |
|---|---|---|
| O1 primary functionality correct | 1 | Carrier states JSON transformation/querying — accurate. |
| O2 supported by artifacts | 1 | `parser.y`, `lexer.l`, `configure.ac` exist in the repo. |
| O3 no unsupported features | 1 | Bison/Flex/autotools/valgrind/scanbuild all real. |
| O4 correct domain | 1 | Command-line JSON processing. |
| O5 terminology matches repo | 1 | C, Bison, Flex, autotools are the repo's real terms. |

**O = 100** (carrier content is factually accurate; presence credited under Rule 7).

### Installation (I) — executed
Prerequisites: "Programming Language: **unknown**", "Package Manager:
Autotools", "Container Runtime: Docker". Installation steps: `git clone …`,
`cd jq`, then a Docker path `docker build -t jqlang/jq .` and an Autotools path
`echo 'INSERT-INSTALL-COMMAND-HERE'` (**unresolved placeholder**).
| Rule | Verdict | Evidence |
|---|---|---|
| I1 dependencies declared | 0 | "Programming Language: unknown"; oniguruma/toolchain not declared; autotools install is a placeholder. |
| I2 commands execute without modification | 0 | `echo 'INSERT-INSTALL-COMMAND-HERE'` is an unresolved placeholder (Ground Rule 6 auto-fail). |
| I3 no unresolved dependency errors | 0 | No real dependency resolution; the documented autotools install installs nothing. |
| I4 environment requirements correct | 0 | "Programming Language: unknown" is incorrect — jq's core is C (repo, Fedora metadata "written in portable C"). |
| I5 produces expected executable artifact | 0 | The placeholder install produces no `jq`. |

**I = 0/5 × 100 = 0**

### Usage and Examples (U) — executed
| # | Snippet | Result | E |
|---|---|---|---|
| 1 | `docker run -it {image_name}` | `{image_name}` unresolved placeholder (Rule 6) | 0 |
| 2 | `echo 'INSERT-RUN-COMMAND-HERE'` | placeholder; does not demonstrate jq usage; behaviour ≠ "Run the project" | 0 |
| 3 | `echo 'INSERT-TEST-COMMAND-HERE'` (Testing, `{__test_framework__}`) | placeholder | 0 |

No snippet demonstrates actual jq usage; all are unresolved placeholders.

**U = 0/3 × 100 = 0**

### API Reference (A)
There is **no API Reference section** and no documented jq function, filter,
flag, or endpoint anywhere in the file (only file-name summaries and a features
table). Per Ground Rule 8, a section that is entirely absent scores 0.

**A = 0**

### License (L)
"Jq is protected under the [LICENSE](https://choosealicense.com/licenses)
License. For more details, refer to the [LICENSE](…/licenses/) file."
| Rule | Verdict | Evidence |
|---|---|---|
| L1 matches repo LICENSE | 0 | Repo is MIT; the README never names MIT — the license is not identified. |
| L2 identifier valid | 0 | "LICENSE" is not a valid license identifier (unfilled template). |
| L3 no conflicting info | 1 | No second/contradictory license is stated. |

**L = 1/3 × 100 = 33.33**

### C_R = (100 + 100 + 0 + 0 + 0 + 33.33) / 6 = **38.89**

---

## Aggregate (single README → average = the row)

| Column | value |
|---|---|
| title | 100 |
| overview | 100 |
| installation | 0 |
| usage | 0 |
| api | 0 |
| license | 33.33 |
| **C_R** | **38.89** |
