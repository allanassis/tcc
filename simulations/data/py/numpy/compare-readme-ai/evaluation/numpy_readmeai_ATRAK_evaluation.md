# NumPy — README-AI ATRAK Evaluation

**Tool:** README-AI · **Project:** NumPy · **Repository:** https://github.com/numpy/numpy
**README evaluated:** `compare-readme-ai/numpy_readme_readmeai.md`
Binary presence of the three Knowledge Elements (Thayer et al. 2021). Assesses **presence, not correctness**. Standard: *"listed is not communicated"* — a table/list that only names concepts does not satisfy K_D; broken/placeholder commands do not satisfy K_E; examples without real API usage do not satisfy K_U.

## Ground Truth Reference

- **Project:** NumPy (Numerical Python)
- **Repository:** https://github.com/numpy/numpy
- **Domain:** Scientific / numerical computing in Python
- **Core domain entities:** `ndarray`, broadcasting, ufuncs, vectorization, linear algebra, random sampling, Fourier transforms, masked arrays, dtypes
- **Core execution facts:** `pip install numpy` / `conda install numpy` (verified artifact 2.5.1); Python dependency; `import numpy as np`; submodules `linalg`/`random`/`fft`/`ma`; deterministic array outputs
- **Core usage:** array creation, broadcast/element-wise arithmetic, ufuncs, matrix ops, RNG sampling

---

## Per-element verdict

### K_D — Domain Concepts: **0**
The Overview section is empty. The **Features** table and Project Structure only *name* attributes ("Multi-dimensional array objects", "Random Number Generators", "Numerical Algorithms", "SIMD and Parallelism"). No domain concept is *defined* — there is no explanation of what an `ndarray` is, what broadcasting or a ufunc means, or the conceptual vocabulary a reader needs. This is exactly the "listed, not communicated" case the standard excludes → **K_D = 0**.

### K_E — Execution Facts: **1**
Independent of the broken/placeholder commands (which by the standard cannot count), the README still presents genuinely verifiable execution facts:
- **Dependencies declared:** Prerequisites list Python as the language and the package managers; the pip step enumerates the real `requirements/*.txt` files that exist in the repo.
- **Installation workflow facts:** `git clone https://github.com/numpy/numpy` and `cd numpy` are valid, executable steps (verified they are well-formed), and `conda env create -f environment.yml` references a real repo file.
- **Runtime/build facts (Features table):** cross-platform support (Linux/Windows/macOS), BLAS/LAPACK integration, meson/pyproject build system, `.pyi` typing stubs, minimal external dependencies — all accurate, verifiable facts about how the software is built and run.
Because verifiable execution facts (dependencies, install workflow, platform/build constraints) are present beyond the disqualified placeholder commands, presence is satisfied → **K_E = 1**.
*(Borderline note: the actionable install/usage/test commands are themselves broken or placeholders; the verdict rests on the non-command dependency/platform facts, per the presence-not-correctness rule.)*

### K_U — Usage Patterns: **0**
The Usage and Testing sections contain only placeholders: `python {entrypoint}`, `conda activate {venv}`, `echo 'INSERT-RUN-COMMAND-HERE'`, `{__test_framework__}`. There is no real NumPy API usage anywhere in the document — no array creation, no operations, no demonstrable what/how/why of use. Examples that do not show real API usage do not satisfy K_U → **K_U = 0**.

---

## Score

**K = (K_D + K_E + K_U)/3 × 100 = (0 + 1 + 0)/3 × 100 = 33.33**

| README | K_D | K_E | K_U | ATRAK |
|---|---|---|---|---|
| numpy_readme_readmeai.md | 0 | 1 | 0 | 33.33 |
| **average** | 0.00 | 1.00 | 0.00 | **33.33** |

Single README → average equals the row. Consistency check: (0+1+0)/3 = 33.33 ✓.
