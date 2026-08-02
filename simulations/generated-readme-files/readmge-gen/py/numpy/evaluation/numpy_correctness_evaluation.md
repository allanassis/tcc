# NumPy — README-Gen Correctness Evaluation

**Tool:** README-Gen · **Project:** NumPy · **Repository:** https://github.com/numpy/numpy
**Core functionality (from manifest):** Create and manipulate arrays
**READMEs evaluated (in order):** `data1.md`, `data2.md`, `data3.md`

## Verification Environment

- Clean venv: `python3 -m venv /tmp/eval-numpy-venv`
- Installed artifact: **numpy 2.5.1** (`pip install numpy`; wheel `numpy-2.5.1-cp314-cp314-macosx_14_0_arm64.whl`), Python 3.14, macOS arm64.
- All usage snippets executed independently with `/tmp/eval-numpy-venv/bin/python`.
- API elements verified by introspection (`hasattr`, `inspect.signature`) against the installed package.

## Cross-checked Sources

1. Installed artifact `numpy==2.5.1` — introspection of signatures and runtime behavior.
2. Repository `https://github.com/numpy/numpy` (repo name = `numpy`).
3. `https://raw.githubusercontent.com/numpy/numpy/main/LICENSE.txt` — confirmed **BSD 3-Clause** (3 redistribution conditions + no-endorsement clause; "Copyright (c) 2005-2025, NumPy Developers").
4. Official docs `https://numpy.org/doc/stable/` (API signatures: `numpy.array`, `numpy.linspace`, `numpy.linalg.*`, `numpy.random.*`, `numpy.fft.*`, `numpy.ma.masked_array`).

---

## Snippet execution log (shared across READMEs)

All snippets ran with exit code 0. The one recurring output mismatch is the sine example: every README documents `np.sin([0, pi/2, pi])` output as `[0. 1. 0.]`, but the real output is `[0.0000000e+00 1.0000000e+00 1.2246468e-16]` — the third element is `1.2246468e-16`, **not** `0`. This fails Usage rule 3 (documented output match) for that snippet in every README.

| Snippet file | Executes | Output documented? | Output matches? | Exception? |
|---|---|---|---|---|
| d1_s2_create | yes | yes | yes (`[1 2 3 4]`, zeros(2,3), eye(3)) | no |
| d1_s3_broadcast | yes | yes | yes (`[5 7 9]`,`[11 12 13]`,`[17 39]`) | no |
| d1_s4_ufunc (sin) | yes | yes (`[0. 1. 0.]`) | **no** (`...1.2246468e-16`) | no |
| d1_s5_linalg | yes | no explicit expected values | n/a | no |
| d1_s6_random | yes | no (random) | n/a | no |
| d2_s2_create | yes | yes | yes | no |
| d2_s3_broadcast | yes | yes | yes (`[[2 3 4][3 4 5][4 5 6]]`) | no |
| d2_s4_ufunc (sin) | yes | yes (`[0. 1. 0.]`) | **no** | no |
| d2_s5_linalg | yes | yes | yes (`[[19 22][43 50]]`, inv) | no |
| d2_s6_random (default_rng) | yes | no (random) | n/a | no |
| d3_s1_create | yes | yes | yes | no |
| d3_s2_broadcast | yes | yes | yes (`[[5 6 7][6 7 8][7 8 9]]`) | no |
| d3_s3_ufunc (sin) | yes | yes (`[0. 1. 0.]`) | **no** | no |
| d3_s4_linalg | yes | yes | yes (`[[19 22][43 50]]`, det `-2.0000000000000004`) | no |
| d3_s5_random (randn) | yes | no (random) | n/a | no |

No import interventions were needed beyond what each snippet already declared (`import numpy as np` present or added inside the block as documented).

---

## API introspection log (installed numpy 2.5.1)

All documented elements EXIST; signatures confirmed via `inspect.signature`:

| Documented element | Exists | Signature (installed) | Notes |
|---|---|---|---|
| `numpy.ndarray` | ✓ | `(shape, dtype=None, buffer=None, offset=0, strides=None, order=None)` | attrs shape/dtype/size/ndim ✓; methods reshape/astype/sum/mean/dot/T/flatten/transpose/max ✓ |
| `numpy.array` | ✓ | `(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, ndmax=0, like=None)` | data3's documented params are a correct subset |
| `numpy.zeros` | ✓ | `(shape, dtype=None, order='C', *, device, like)` | default resolves to float64 (`dtype=float` OK) |
| `numpy.ones` | ✓ | `(shape, dtype=None, order='C', ...)` | |
| `numpy.empty` | ✓ | `(shape, dtype=None, order='C', ...)` | |
| `numpy.arange` | ✓ | `(start_or_stop, /, stop=None, step=1, *, dtype, ...)` | matches classic `[start,]stop[,step]` doc form |
| `numpy.linspace` | ✓ | `(start, stop, num=50, endpoint=True, ...)` | `num=50` correct |
| `numpy.sin/cos/exp/log/sqrt/add/subtract` | ✓ | ufunc `(x, /, out=None, ...)` / `(x1,x2,/...)` | |
| `numpy.sum/prod/min/max` | ✓ | `(a, axis=None, ...)` | |
| `numpy.dot` | ✓ | `(a, b, out=None)` | data1 lists it under linalg heading but name `numpy.dot` is correct |
| `numpy.matmul` | ✓ | ufunc `(x1, x2, /, ...)` | |
| `numpy.linalg.inv/det/eig/solve/norm` | ✓ | `(a)`,`(a)`,`(a)`,`(a, b)`,`(x, ord=None, ...)` | |
| `numpy.random.rand/randn` | ✓ | `(*args)` | legacy but NOT deprecated → rule 6 pass |
| `numpy.random.randint` | ✓ | `(low, high=None, size=None, dtype=int)` | |
| `numpy.random.normal` | ✓ | `(loc=0.0, scale=1.0, size=None)` | |
| `numpy.random.default_rng` | ✓ | `(seed=None)` | |
| `Generator.normal` | ✓ | `(loc=0.0, scale=1.0, size=None)` | |
| `Generator.integers` | ✓ | `(low, high=None, size=None, dtype=int64, endpoint=False)` | |
| `numpy.fft.fft/ifft` | ✓ | `(a, n=None, axis=-1, norm=None, out=None)` | |
| `numpy.ma.masked_array` | ✓ | `(data=None, mask=False, dtype=None, ...)` | |

All documented elements pass all 6 API rules in every README (exist, correct names, correct/consistent parameter types, correct return behavior confirmed by execution, no deprecated-as-current elements).

---

## README 1 — `data1.md`

### Project Title (T)
- V1 title = "NumPy" matches repo name `numpy` — **1**
- V2 not a different project — **1**
- V3 no hallucinated terminology — **1**
- **T = 100.00**

### Overview (O)
- V1 primary functionality (N-dim arrays + math functions) correctly described — **1**
- V2 supported by artifacts (ndarray, ufuncs, linalg, random, fft, ma all exist) — **1**
- V3 no unsupported features (masked arrays, Fourier all real) — **1**
- V4 correct domain (scientific/numerical computing) — **1**
- V5 terminology matches repo (ndarray, broadcasting, ufuncs) — **1**
- **O = 100.00**

### Installation (I) — executed, re-scored under tightened rules

**Documented paths:** pip, conda. (No verification snippet; no source build.)

**Environment:** clean venv `python3 -m venv /tmp/numpy-install-recheck` (Python 3.14.6, macOS arm64). Installed artifact: **numpy 2.5.1** (`pip install numpy` → `Successfully installed numpy-2.5.1`, wheel `numpy-2.5.1-cp314-cp314-macosx_14_0_arm64.whl`).

**Authoritative metadata checked** (`pip show numpy` + `importlib.metadata` + PyPI JSON `https://pypi.org/pypi/numpy/json`): **`Requires-Python: >=3.12`**; `Requires-Dist: None` (no mandatory runtime dependencies).

**conda path validation:** conda is not installed locally, so `conda install numpy` was validated against `https://anaconda.org/anaconda/numpy` — package `numpy` **2.5.1** exists, macOS-arm64 supported ⇒ the command references a real, installable package.

- V1 required dependencies declared — numpy wheel has no mandatory runtime deps; pip/conda paths require nothing beyond Python — **1**
- V2 commands execute without modification — `pip install numpy` succeeded (2.5.1); `conda install numpy` validated as a real package on anaconda.org — **1**
- V3 no unresolved dependency errors — clean pip install, zero declared/required deps — **1**
- V4 environment requirement correct — README states **"Python 3.8 or higher recommended"**, but authoritative `Requires-Python` is **`>=3.12`**. 3.8 is **below** the actual minimum (numpy 2.5.1 will not install on 3.8–3.11); the documented version claim is incorrect — **0**
- V5 expected artifact produced — `import numpy` works — **1**
- **I = (4/5)×100 = 80.00**

### Usage and Examples (U) — executed, k = 6 snippets
Snippets: (1) `import numpy as np`, (2) create, (3) broadcast, (4) sin ufunc, (5) linalg, (6) random.
- Snippet 4 (sin) fails rule 3 (documented `[0. 1. 0.]` ≠ actual `...1.2246468e-16`) → E4 = 0.
- All other 5 snippets pass all five rules → E = 1 each.
- ΣE = 5, k = 6 → **U = 83.33**

### API Reference (A) — n elements
All documented elements exist with correct names/types/behavior and none deprecated (see introspection log). Every A_i = 1 → **A = 100.00**

### License (L)
- V1 "BSD 3-Clause License" matches repo LICENSE.txt — **1**
- V2 identifier valid (SPDX `BSD-3-Clause`) — **1**
- V3 no conflicting license info — **1**
- **L = 100.00**

**C_R(data1) = (100 + 100 + 80.00 + 83.33 + 100 + 100) / 6 = 93.89**

---

## README 2 — `data2.md`

### Project Title (T) = 100.00
Same as data1: "NumPy" ✓, not different ✓, no hallucination ✓.

### Overview (O) = 100.00
Adds "vectorized operations" and "integration with C/C++/Fortran" — all supported by repo. All 5 rules pass.

### Installation (I) — executed, re-scored under tightened rules

**Documented paths:** pip, conda, verification snippet.
- pip: `pip install numpy` → `Successfully installed numpy-2.5.1` (venv `/tmp/numpy-install-recheck`).
- conda: `conda install numpy` validated via `https://anaconda.org/anaconda/numpy` (2.5.1, macOS-arm64) — conda not installed locally.
- verification snippet `import numpy as np; print(np.__version__)` → printed **`2.5.1`**.

**Authoritative metadata:** `Requires-Python: >=3.12` (`pip show numpy` + PyPI JSON); no runtime deps.

- V1 required dependencies declared — none required beyond Python — **1**
- V2 commands execute without modification — pip ✓, verify snippet ✓ (`2.5.1`), conda package exists — **1**
- V3 no unresolved dependency errors — **1**
- V4 environment requirement correct — README states **"Python 3.7 or newer"**, but authoritative `Requires-Python` is **`>=3.12`**. 3.7 is **below** the actual minimum ⇒ documented version claim is incorrect — **0**
- V5 expected artifact produced — import + version confirmed — **1**
- **I = (4/5)×100 = 80.00**

### Usage and Examples (U) — executed, k = 5 snippets
Snippets: (1) create, (2) broadcast, (3) sin ufunc, (4) linalg dot+inv, (5) random `default_rng().normal`.
- Snippet 3 (sin) fails rule 3 (same `[0. 1. 0.]` mismatch) → E3 = 0.
- Others pass all five rules (broadcast `[[2 3 4]...]` ✓; dot `[[19 22][43 50]]` ✓; default_rng runs, no documented output).
- ΣE = 4, k = 5 → **U = 80.00**

### API Reference (A) = 100.00
All elements exist incl. `default_rng`, `Generator.normal`, `Generator.integers`, `matmul`, `linalg.norm`. All A_i = 1.

### License (L) = 100.00
BSD 3-Clause, valid, no conflict.

**C_R(data2) = (100 + 100 + 80.00 + 80 + 100 + 100) / 6 = 93.33**

---

## README 3 — `data3.md`

### Project Title (T) = 100.00
"NumPy" ✓.

### Overview (O) = 100.00
Describes ndarray, broadcasting, vectorization, ufunc, linalg, random — all supported. 5/5.

### Installation (I) — executed, re-scored under tightened rules

**Documented paths:** pip, conda, **build from source**, verification snippet.
- pip: `pip install numpy` → `numpy-2.5.1` ✓ (venv `/tmp/numpy-install-recheck`).
- conda: validated via `https://anaconda.org/anaconda/numpy` (2.5.1, macOS-arm64) ✓ — conda not installed locally.
- verify snippet `import numpy as np; print(np.__version__)` → `2.5.1` ✓.
- **source build executed exactly as documented** in a fresh venv `python3 -m venv /tmp/numpy-src-build`:
  - `git clone https://github.com/numpy/numpy.git` → cloned `main` @ `d94e42fd82` ✓
  - `pip install cython` → `cython-3.2.9` ✓
  - `pip install .` → **FAILED** at *Preparing metadata (pyproject.toml)* with:
    `meson-python: error: Could not find the specified meson: "vendored-meson/meson/meson.py"`
  - **Root cause:** numpy pins its build to the **vendored-meson git submodule**; the documented steps omit `git submodule update --init`, so the required submodules (vendored-meson, highway, pocketfft, svml, x86-simd-sort, pythoncapi-compat listed in `.gitmodules`) are never fetched. The documented `pip install cython` step is irrelevant to the failure (PEP 517 build isolation supplies build backends). The build aborted in <10 s, before any compilation — **no artifact produced**. (No 20-minute wait was needed; the failure is deterministic at metadata generation.)

**Authoritative metadata:** `Requires-Python: >=3.12` (`pip show numpy` + PyPI JSON); no runtime deps.

Per-rule (a rule fails if violated by **any** documented path):
- V1 required dependencies declared — the source path requires initialized git submodules (incl. vendored meson) and a build toolchain; README declares only `cython`. Required dependencies are **not** fully declared — **0**
- V2 commands execute without modification — source `pip install .` fails; it needs an undocumented `git submodule update --init` first — **0**
- V3 no unresolved dependency errors — build aborts on missing `vendored-meson/meson/meson.py`, an unresolved build dependency — **0**
- V4 environment requirement correct — data3 documents no Python version claim; platform claims (Windows/macOS/Linux) are correct and nothing contradicts authoritative `Requires-Python >=3.12` — **1**
- V5 expected artifact produced — the source path never yields an importable numpy (pip/conda would, but the source path fails) — **0**
- **I = (1/5)×100 = 20.00**

### Usage and Examples (U) — executed, k = 5 snippets
Snippets: (1) create, (2) broadcast, (3) sin ufunc, (4) linalg dot+det, (5) random `randn`.
- Snippet 3 (sin) fails rule 3 (same `[0. 1. 0.]` mismatch) → E3 = 0.
- Snippet 4 passes: `np.dot` → `[[19 22][43 50]]` ✓ and `np.linalg.det` → `-2.0000000000000004` **matches the documented value exactly**.
- Others pass all five rules.
- ΣE = 4, k = 5 → **U = 80.00**

### API Reference (A) = 100.00
`numpy.array` full signature documented and correct; ndarray, ufuncs, linalg (inv/det/eig/solve), random (rand/randn/randint) all exist. All A_i = 1.

### License (L) = 100.00
BSD 3-Clause, valid, no conflict.

**C_R(data3) = (100 + 100 + 20.00 + 80 + 100 + 100) / 6 = 83.33**

---

## Averages (arithmetic mean over data1, data2, data3)

| Column | data1 | data2 | data3 | average |
|---|---|---|---|---|
| title | 100.00 | 100.00 | 100.00 | 100.00 |
| overview | 100.00 | 100.00 | 100.00 | 100.00 |
| installation | 80.00 | 80.00 | 20.00 | 60.00 |
| usage | 83.33 | 80.00 | 80.00 | 81.11 |
| api | 100.00 | 100.00 | 100.00 | 100.00 |
| license | 100.00 | 100.00 | 100.00 | 100.00 |
| **correctness** | **93.89** | **93.33** | **83.33** | **90.18** |

Consistency check: mean(93.89, 93.33, 83.33) = 270.55/3 = 90.18 ✓; mean(80.00, 80.00, 20.00) = 180.00/3 = 60.00 ✓; mean(83.33, 80, 80) = 243.33/3 = 81.11 ✓.
