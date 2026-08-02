# NumPy — README-AI Correctness Evaluation

**Tool:** README-AI · **Project:** NumPy · **Repository:** https://github.com/numpy/numpy
**Core functionality (from manifest):** Create and manipulate arrays
**README evaluated:** `compare-readme-ai/numpy_readme_readmeai.md` (single file)

## Verification Environment

- Same clean venv as README-Gen: `/tmp/eval-numpy-venv`, **numpy 2.5.1**, Python 3.14, macOS arm64.
- README-AI file is ~1.25 MB; the bulk is an auto-generated "Project Structure / Project Index" file tree. Rubric-relevant sections: Title, Overview (empty), Features table, Getting Started (Prerequisites, Installation, Usage, Testing), Roadmap, Contributing, License.

## Cross-checked Sources

1. Installed artifact `numpy==2.5.1` (introspection).
2. Repository `https://github.com/numpy/numpy` (repo name `numpy`; `environment.yml`, `requirements/*.txt`, `pyproject.toml`/`meson.build` confirmed to exist as referenced).
3. `https://raw.githubusercontent.com/numpy/numpy/main/LICENSE.txt` → **BSD 3-Clause**.
4. Executed the README-AI pip install command to record real failure output (below).

---

## Section-by-section

### Project Title (T)
Header: `# NUMPY`.
- V1 matches repo name `numpy` (case-only difference) — **1**
- V2 not a different project — **1**
- V3 no hallucinated terminology — **1**
- **T = 100.00**

### Overview (O)
The `## Overview` section is **empty**. Per ground rule 7, the **Features** table is the only carrier of purpose/functionality information, so O is evaluated on it.
The Features table states, factually correctly: Primary Language = Python (with C/Cython/Fortran); Core Functionality = "Multi-dimensional array objects, numerical operations, linear algebra, Fourier transforms, random sampling"; BLAS/LAPACK & SIMD optimizations; `.pyi` stubs; meson/pyproject build; multiple RNGs (`_mt19937`, `_philox`, `_pcg64`); cross-platform. All claims verified against the repository.
- V1 primary functionality correctly described (arrays + numerical ops) — **1**
- V2 supported by artifacts — **1**
- V3 no unsupported features (all listed capabilities are real) — **1**
- V4 domain identifiable (numerical/scientific computing) — **1**
- V5 terminology matches repo — **1**
- **O = 100.00** *(scored on the Features table as the overview carrier; the dedicated Overview heading itself is blank)*

### Installation (I) — executed
Documented steps: `git clone https://github.com/numpy/numpy` → `cd numpy` → then one of:
- conda: `conda env create -f environment.yml`
- pip: `pip install -r requirements/test_requirements.txt, requirements/typing_requirements.txt, requirements/build_requirements.txt, ...` (comma-separated list of 12 requirements files)
- cmake: `echo 'INSERT-INSTALL-COMMAND-HERE'`

**Executed evidence** (`/tmp/eval-numpy-venv/bin/pip`):
```
$ pip install -r "requirements/test_requirements.txt, requirements/typing_requirements.txt, requirements/build_requirements.txt"
ERROR: Could not open requirements file: [Errno 2] No such file or directory:
'requirements/test_requirements.txt, requirements/typing_requirements.txt, requirements/build_requirements.txt'
[exit=1]
```
pip treats the comma-joined string as a single filename → the command cannot execute.

Rule-by-rule:
- V1 required dependencies explicitly & correctly declared: the pip step points only at *requirements files* (test/build/typing/etc.), never installs NumPy itself, and lists no way to build the package → **0**
- V2 commands execute without modification: the comma-separated `pip install -r` fails (evidence above); the cmake step is the placeholder `INSERT-INSTALL-COMMAND-HERE` (auto-fail) → **0**
- V3 no unresolved dependency errors → **0**
- V4 documented environment requirements correct: Prerequisites list "Package Manager: Conda, Pip, **Cmake**" — CMake is not NumPy's build tool (it uses Meson) and is misclassified as a package manager; no version constraints → **0**
- V5 installation produces the expected executable artifact: following the steps yields **no importable numpy** (no `pip install .`/build invocation) → **0**
- **I = 0.00**

### Usage and Examples (U) — executed; k = 3 code blocks
The `### Usage` section contains only placeholder commands:
1. `conda activate {venv}` / `python {entrypoint}` — unresolved placeholders `{venv}`, `{entrypoint}` → auto-fail (E=0)
2. `python {entrypoint}` — unresolved placeholder → auto-fail (E=0)
3. `echo 'INSERT-RUN-COMMAND-HERE'` — placeholder → auto-fail (E=0)

| Snippet | Executes | Placeholder? | Score |
|---|---|---|---|
| conda activate {venv}; python {entrypoint} | no | yes ({venv},{entrypoint}) | 0 |
| python {entrypoint} | no | yes ({entrypoint}) | 0 |
| echo 'INSERT-RUN-COMMAND-HERE' | prints literal placeholder | yes | 0 |

No real NumPy API usage appears anywhere in the file. ΣE = 0, k = 3 → **U = 0.00**

### API Reference (A)
The README-AI file has **no API Reference section** (no functions/classes/parameters documented). Per ground rule 8, a section absent entirely scores 0 → **A = 0.00**

### License (L)
Text: "Numpy is protected under the [LICENSE](https://choosealicense.com/licenses) License."
- V1 documented license matches repo LICENSE.txt (BSD 3-Clause): the README never states BSD-3-Clause; it links to a generic choosealicense.com index → **0**
- V2 license identifier valid: "LICENSE" is not a valid SPDX identifier → **0**
- V3 no conflicting licensing information: no second, contradictory textual license claim is made → **1**
- **L = (0 + 0 + 1)/3 × 100 = 33.33**

---

## Score

**C_R = (T + O + I + U + A + L) / 6 = (100 + 100 + 0 + 0 + 0 + 33.33) / 6 = 233.33 / 6 = 38.89**

| Column | value |
|---|---|
| title | 100.00 |
| overview | 100.00 |
| installation | 0.00 |
| usage | 0.00 |
| api | 0.00 |
| license | 33.33 |
| **correctness** | **38.89** |

Single README → the `average` row equals this row. Consistency check: 233.33/6 = 38.89 ✓.
