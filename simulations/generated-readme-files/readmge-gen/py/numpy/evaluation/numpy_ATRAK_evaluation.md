# NumPy — README-Gen ATRAK Evaluation

**Tool:** README-Gen · **Project:** NumPy · **Repository:** https://github.com/numpy/numpy
Binary presence of the three Knowledge Elements (Thayer et al. 2021). This dimension assesses **presence, not correctness**. Standard applied: *"listed is not communicated"* — a table/bullet list that only names concepts does not satisfy K_D; broken/placeholder commands do not satisfy K_E; examples without real API usage do not satisfy K_U.

## Ground Truth Reference

- **Project:** NumPy (Numerical Python)
- **Repository:** https://github.com/numpy/numpy
- **Domain:** Scientific / numerical computing in Python
- **Core domain entities:** `ndarray` (N-dimensional array), broadcasting, universal functions (ufuncs), vectorization, linear algebra, random sampling, Fourier transforms, masked arrays, dtypes
- **Core execution facts:** installs via `pip install numpy` / `conda install numpy` (verified artifact numpy 2.5.1); imported as `import numpy as np`; array creation/ops return `ndarray`; deterministic outputs for arithmetic/broadcasting; `numpy.linalg`, `numpy.random`, `numpy.fft`, `numpy.ma` submodules
- **Core usage:** create arrays (`np.array`, `np.zeros`, `np.eye`), element-wise & broadcast arithmetic, ufuncs, matrix ops, RNG sampling

---

## README 1 — `data1.md`

**K_D — Domain Concepts: 1.** Provides a "Domain Concepts" subsection that *defines* ndarray, broadcasting, ufuncs, linear algebra, random sampling, Fourier transforms, and masked arrays (each has an explanatory sentence, not just a name), and explains NumPy's goal of dense-array storage over Python lists. Conceptual vocabulary is taught → satisfies K_D.

**K_E — Execution Facts: 1.** States Python version requirement, install commands (`pip install numpy`, `conda install numpy` — verified working), import convention, and concrete inputs→outputs for arrays (e.g., `x + y → [5 7 9]`, `A @ v → [17 39]`). Real, verifiable execution facts → satisfies K_E.

**K_U — Usage Patterns: 1.** Multiple runnable, real-API examples (create/broadcast/ufunc/linalg/random) demonstrating what/how of use, executed successfully → satisfies K_U.

**K(data1) = (1+1+1)/3 × 100 = 100.00**

---

## README 2 — `data2.md`

**K_D: 1.** Domain Concepts subsection defines ndarray, vectorized operations, broadcasting, ufuncs, linear algebra, random sampling, Fourier transforms, and C/C++/Fortran integration with explanatory text.

**K_E: 1.** Prerequisites (Python 3.7+), install commands, and a verification step (`print(np.__version__)` → executed, `2.5.1`); documented deterministic outputs (dot `[[19 22][43 50]]`). Verifiable execution facts present.

**K_U: 1.** Real runnable API examples incl. modern `np.random.default_rng()` usage; executed successfully.

**K(data2) = 100.00**

---

## README 3 — `data3.md`

**K_D: 1.** Domain Concepts subsection defines ndarray, broadcasting, vectorization, ufunc, linear algebra, random sampling with explanatory text (conceptual vocabulary communicated).

**K_E: 1.** Install commands incl. build-from-source workflow, verification step, and documented deterministic outputs (det `-2.0000000000000004`, verified exact). Verifiable execution facts present.

**K_U: 1.** Real runnable API examples across creation/broadcast/ufunc/linalg/random; executed successfully.

**K(data3) = 100.00**

---

## Summary

| README | K_D | K_E | K_U | ATRAK |
|---|---|---|---|---|
| data1.md | 1 | 1 | 1 | 100.00 |
| data2.md | 1 | 1 | 1 | 100.00 |
| data3.md | 1 | 1 | 1 | 100.00 |
| **average** | 1.00 | 1.00 | 1.00 | **100.00** |

Consistency check: all three READMEs score 1/1/1 → average 100.00 ✓.
