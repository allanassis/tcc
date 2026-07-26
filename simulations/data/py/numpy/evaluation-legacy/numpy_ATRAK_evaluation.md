# NumPy — ATORAK Adherence Evaluation

**Methodology:** Section 4.4.3 of *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis*.

**Theory of Robust API Knowledge (ATORAK)** [Thayer et al. 2021] defines three Knowledge Elements that a robust API document must communicate:

- **KD — Domain Concepts:** Fundamental entities and abstractions that define the problem domain — class names, data models, terminology that helps developers understand what the software represents and the conceptual space in which it operates.
- **KE — Execution Facts:** Concrete, verifiable facts about how the software behaves at runtime — function inputs/outputs, return types, dependencies, configuration requirements, installation steps, runtime constraints.
- **KU — Usage Patterns:** Recurring, purposeful combinations of API calls that solve real problems, expressed through code examples, tutorials, and demonstrations of *what*, *how*, and *why* the software is used.

Each element is binary: Ki ∈ {0, 1}. The adherence score per README is:

```
Kpercentage = (KD + KE + KU) / 3 × 100
```

The final score across the three generated READMEs is:

```
Kavg = (K1 + K2 + K3) / 3
```

> **Scope:** This evaluation assesses only **completeness** — whether each Knowledge Element is present in the README. Correctness of the content is not evaluated.

---

## Ground Truth Reference

- Tool: **numpy** — fundamental package for scientific computing in Python
- Repository: https://github.com/numpy/numpy
- Domain: Numerical computing, multi-dimensional arrays, linear algebra, random sampling, Fourier transforms
- Core domain entities: ndarray, Broadcasting, Vectorization, Universal Functions (ufuncs), Linear Algebra, Random Sampling, Fourier Transforms, Masked Arrays
- Core execution facts: `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`, `np.sin()`, `np.linalg.inv()`, `np.linalg.eig()`, `np.random.rand()`, `ndarray.shape`, `ndarray.dtype`, `ndarray.reshape()`
- Section mapping per TCC §3.2: Overview → KD, Usage and Examples → KU, API Reference → KE

---

## data1.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

The README must represent the conceptual vocabulary and entities of the NumPy domain — the fundamental abstractions that define what NumPy is and the problem space it operates in.

**Evidence in data1.md:**

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **ndarray** — "NumPy's primary data structure, an N-dimensional array providing fast, vectorized operations." ✅ Correctly identifies the central data structure.
- **Broadcasting** — "A set of rules for applying arithmetic operations on arrays of different shapes." ✅ Correct definition of the broadcasting mechanism.
- **Universal Functions (ufuncs)** — "Vectorized functions that operate element-wise on arrays." ✅ Correct; captures the element-wise, vectorized nature.
- **Linear Algebra** — "Support for matrix operations, decompositions, and solving linear systems." ✅ Correct; identifies the sub-domain.
- **Random Sampling** — "Tools for pseudorandom number generation and statistical distributions." ✅ Correct.
- **Fourier Transforms** — "Efficient computation of Fourier transforms and related algorithms." ✅ Correct.
- **Masked Arrays** — "Arrays that may have missing or invalid entries filled with masks." ✅ Correct; identifies the masked array concept.

The overview also correctly describes NumPy as "a fundamental package for scientific computing in Python" providing "support for large, multi-dimensional arrays and matrices" — accurate characterization of the domain.

**Assessment:** data1.md explicitly and completely represents the domain concepts of NumPy. Seven core entities are listed and defined in a dedicated subsection. The domain (numerical/scientific computing) is correctly identified. The conceptual vocabulary (ndarray, Broadcasting, ufuncs, linalg, random, fft, masked arrays) covers the full breadth of NumPy's problem space.

**KD = 1** ✅

---

#### KE — Execution Facts

The README must represent concrete, verifiable runtime facts: installation commands, function signatures, parameters, return types, and behavioral descriptions.

**Evidence in data1.md:**

*Installation facts:*
- `pip install numpy` — correct and executable. ✅
- `conda install numpy` — correct and executable. ✅
- "Python 3.8 or higher recommended" — correct environment requirement. ✅
- "cross-platform and available on Linux, macOS, and Windows" — accurate. ✅

*API Reference facts:*
- `numpy.ndarray` — documents `.shape`, `.dtype`, `.size`, `.ndim` attributes; `.reshape()`, `.astype()`, `.sum()`, `.mean()`, `.dot()`, `.T` methods. ✅
- `np.array(object, dtype=...)` — correct signature. ✅
- `np.zeros(shape, dtype=float, ...)` — correct signature. ✅
- `np.ones(shape, dtype=float, ...)` — correct signature. ✅
- `np.empty(shape, dtype=float, ...)` — correct signature. ✅
- `np.arange([start,] stop[, step])` — correct signature. ✅
- `np.linspace(start, stop, num=50)` — correct signature. ✅
- `np.sin(x)`, `np.cos(x)`, `np.exp(x)`, `np.log(x)`, `np.sqrt(x)` — correct ufuncs. ✅
- `np.sum(arr)`, `np.prod(arr)`, `np.min(arr)`, `np.max(arr)` — correct reduction functions. ✅
- `numpy.linalg.inv(a)`, `numpy.linalg.det(a)`, `numpy.linalg.eig(a)`, `numpy.linalg.solve(a, b)`, `numpy.dot(a, b)` — correct linalg functions. ✅
- `numpy.random.rand(d0,...,dn)`, `numpy.random.randn(d0,...,dn)`, `numpy.random.randint(low, high, size)`, `numpy.random.normal(loc, scale, size)` — correct random functions. ✅
- `numpy.fft.fft(a)`, `numpy.fft.ifft(a)` — correct FFT functions. ✅
- `numpy.ma.masked_array(data, mask=...)` — correct masked array constructor. ✅

**Assessment:** data1.md provides a comprehensive API Reference section with correct function signatures, parameter names, and behavioral descriptions across all major NumPy sub-modules (core, linalg, random, fft, ma). Installation commands are executable. All documented execution facts are present and verifiable.

**KE = 1** ✅

---

#### KU — Usage Patterns

The README must present recurring, purposeful combinations of API calls that solve real problems, communicating *what* the pattern does, *how* to execute it, and *why* it is useful.

**Evidence in data1.md:**

The "Usage and Examples" section presents the following patterns:

1. **Importing NumPy** — `import numpy as np`: Establishes the standard import convention. *What*: set up NumPy. *How*: standard alias import. ✅
2. **Creating Arrays** — `np.array([1,2,3,4])`, `np.zeros((2,3))`, `np.eye(3)` with expected outputs: Shows the fundamental array creation patterns. *What*: create arrays of different types. *How*: use creation functions with expected outputs shown. ✅
3. **Array Operations and Broadcasting** — element-wise addition `x + y`, scalar broadcasting `x + 10`, matrix-vector product `A @ v` with outputs: Shows the core vectorized operation patterns. *What*: perform arithmetic on arrays. *How*: use operators directly; *Why*: avoids explicit loops. ✅
4. **Universal Functions (ufuncs)** — `np.sin(arr)` on an array of angles with output: Shows element-wise function application. *What*: apply math functions to arrays. *How*: call ufunc directly on ndarray. ✅
5. **Linear Algebra Example** — `inv(M)`, `eig(M)` with output: Shows matrix operations. *What*: compute inverse and eigenvalues. *How*: import from `numpy.linalg` and call functions. ✅
6. **Random Sampling** — `np.random.rand(5)`, `np.random.normal(loc=0, scale=1, size=10)`: Shows random number generation. *What*: generate random samples. *How*: use `numpy.random` functions with distribution parameters. ✅

**Assessment:** data1.md presents six distinct usage patterns covering the most important NumPy workflows. Each pattern includes runnable code with expected outputs, demonstrating the *what* and *how* clearly. The patterns progress from basic (import, array creation) to advanced (linear algebra, random sampling), covering the full spectrum of NumPy usage. The *why* is implied through the domain context and section headings.

**KU = 1** ✅

---

### data1.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data1.md ATORAK Score: 100**

---

## data2.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

**Evidence in data2.md:**

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **ndarray** — "The central data structure in NumPy representing an N-dimensional array." ✅ Correct.
- **Vectorized Operations** — "Efficient, element-wise operations over arrays without explicit loops." ✅ Correct; explicitly names the "without explicit loops" benefit, which is a key domain concept.
- **Broadcasting** — "A mechanism allowing arithmetic operations on arrays of different shapes by automatically expanding their shapes." ✅ Correct; adds "automatically expanding their shapes" which is more precise than data1.md.
- **Universal Functions (ufuncs)** — "Fast, element-wise functions that operate on ndarrays." ✅ Correct.
- **Linear Algebra** — "Functions to perform matrix multiplication, eigenvalue computations, decompositions, etc." ✅ Correct.
- **Random Sampling** — "Utilities to generate random numbers following various probability distributions." ✅ Correct.
- **Fourier Transforms** — "Tools for frequency domain analysis." ✅ Correct.
- **Integration with C/C++ and Fortran** — "Interfaces for extending and accelerating computations." ✅ Correct; unique to data2.md, identifies the interoperability concept.

The overview correctly describes NumPy as enabling "scalable and high-performance computing workflows in Python" — accurate characterization.

**Assessment:** data2.md provides the most comprehensive domain concept representation of the three READMEs, listing eight entities including the unique "Vectorized Operations" as an explicit concept (distinct from ufuncs) and "Integration with C/C++ and Fortran" — both real and important NumPy domain concepts. All entities are correctly defined.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data2.md:**

*Installation facts:*
- `pip install numpy` — correct. ✅
- `conda install numpy` — correct. ✅
- "Python 3.7 or newer" — correct environment requirement. ✅
- Verification step: `import numpy as np; print(np.__version__)` — correct and executable. ✅ Unique to data2.md among the three.

*API Reference facts:*
- `numpy.ndarray` — documents creation functions, `.shape`, `.dtype`, `.size`, `.ndim`, `.reshape()`, `.flatten()`, `.transpose()`. ✅
- `numpy.array(object, dtype=None, ...)` — correct signature with description. ✅
- `numpy.zeros(shape, dtype=float, ...)` — correct. ✅
- `numpy.ones(shape, dtype=float, ...)` — correct. ✅
- `numpy.arange(start, stop, step, ...)` — correct. ✅
- `numpy.linspace(start, stop, num, ...)` — correct. ✅
- `numpy.sin(x)`, `numpy.cos(x)`, `numpy.exp(x)`, `numpy.log(x)`, `numpy.sqrt(x)` — correct ufuncs. ✅
- `numpy.linalg.inv(a)`, `numpy.linalg.eig(a)`, `numpy.linalg.norm(x)`, `numpy.dot(a, b)`, `numpy.matmul(a, b)` — correct linalg functions; adds `norm` and `matmul` not in data1.md. ✅
- `numpy.random.default_rng()` — correct modern RNG API. ✅
- `Generator.normal(loc, scale, size)`, `Generator.integers(low, high, size)` — correct Generator API. ✅
- `numpy.fft.fft(a)`, `numpy.fft.ifft(a)` — correct. ✅

**Assessment:** data2.md provides a comprehensive and accurate API Reference. Notably, it documents the modern `numpy.random.default_rng()` Generator API (the recommended approach since NumPy 1.17), `numpy.linalg.norm`, and `numpy.matmul` — all real and verifiable. The installation section uniquely includes a verification step. All execution facts are present and correct.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data2.md:**

The "Usage and Examples" section presents the following patterns:

1. **Creating Arrays** — `np.array([1,2,3])`, `np.array([[1,2],[3,4]])`, `np.zeros((3,4))`, `np.ones((2,2))` with outputs: Shows 1D, 2D, and utility array creation. *What*: create arrays of different shapes. *How*: use creation functions. ✅
2. **Array Operations and Broadcasting** — element-wise addition `x + y`, 2D broadcasting `z + x` with output showing shape expansion: Shows the broadcasting mechanism in action. *What*: perform arithmetic with shape broadcasting. *How*: use operators; NumPy automatically expands shapes. ✅ The 2D broadcasting example is more illustrative than data1.md's scalar example.
3. **Universal Functions (ufuncs)** — `np.sin(arr)` with output: Shows element-wise function application. ✅
4. **Linear Algebra** — `np.dot(A, B)` matrix multiplication with output, `np.linalg.inv(A)`: Shows matrix operations. *What*: multiply matrices and compute inverse. *How*: use `np.dot` and `np.linalg.inv`. ✅
5. **Random Sampling** — `rng = np.random.default_rng()` then `rng.normal(loc=0, scale=1, size=5)`: Shows the modern Generator-based random API. *What*: generate random samples. *How*: create a Generator instance, call distribution methods. *Why*: the recommended modern approach for reproducible random number generation. ✅

**Assessment:** data2.md presents five distinct usage patterns. The broadcasting example is the most illustrative of the three READMEs, showing a 2D case that clearly demonstrates shape expansion. The random sampling pattern uses the modern `default_rng()` API, which is the currently recommended approach. All patterns include runnable code with expected outputs.

**KU = 1** ✅

---

### data2.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data2.md ATORAK Score: 100**

---

## data3.md Evaluation

### Step-by-step Reasoning

#### KD — Domain Concepts

**Evidence in data3.md:**

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **ndarray** — "The core data structure of NumPy, representing a multidimensional, homogeneous array of fixed-size items." ✅ Correct; adds "homogeneous" and "fixed-size items" — the most precise definition of the three READMEs.
- **Broadcasting** — "A powerful mechanism that allows NumPy to perform arithmetic operations on arrays of different shapes efficiently." ✅ Correct.
- **Vectorization** — "The process of performing operations on entire arrays rather than their individual elements, enabling high-performance computing." ✅ Correct; explicitly names the performance benefit.
- **Universal Functions (ufunc)** — "Functions that operate element-wise on arrays, providing fast vectorized operations." ✅ Correct.
- **Linear Algebra** — "NumPy includes a set of routines to perform matrix operations like dot products, inverses, eigenvalue computations, and more." ✅ Correct.
- **Random Sampling** — "Facilities for generating random numbers and performing random sampling." ✅ Correct.

The overview correctly describes NumPy as "the foundation for most numerical and scientific computing libraries in Python including SciPy, Pandas, and scikit-learn" — accurate and adds ecosystem context.

**Assessment:** data3.md correctly represents the domain concepts of NumPy. Six core entities are listed. The ndarray definition is the most precise of the three READMEs, explicitly noting "homogeneous" and "fixed-size items" — key properties of the ndarray type. The domain is correctly identified as numerical/scientific computing with ecosystem context (SciPy, Pandas, scikit-learn).

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data3.md:**

*Installation facts:*
- `pip install numpy` — correct. ✅
- `conda install numpy` — correct. ✅
- Building from source: `git clone`, `pip install cython`, `pip install .` — correct advanced installation path. ✅ Unique to data3.md.
- Verification: `import numpy as np; print(np.__version__)` — correct. ✅

*API Reference facts:*
- `numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0)` — the most complete signature of the three READMEs, documenting all parameters with types and defaults. ✅
- `numpy.ndarray` — documents `.shape`, `.dtype`, `.size`, `.ndim`, `.reshape()`, `.transpose()`, `.astype()`, `.sum()`, `.mean()`, `.max()`. ✅
- `numpy.sin(x)`, `numpy.cos(x)`, `numpy.exp(x)`, `numpy.log(x)`, `numpy.add(x1, x2)`, `numpy.subtract(x1, x2)` — correct ufuncs; adds binary ufuncs `add` and `subtract`. ✅
- `numpy.linalg.inv(A)`, `numpy.linalg.det(A)`, `numpy.linalg.eig(A)`, `numpy.linalg.solve(A, b)` — correct. ✅
- `numpy.random.rand(d0,...,dn)`, `numpy.random.randn(d0,...,dn)`, `numpy.random.randint(low, high, size)` — correct. ✅

**Assessment:** data3.md provides the most detailed function signature documentation of the three READMEs. The `numpy.array()` signature includes all parameters with types and defaults (`copy=True`, `order='K'`, `subok=False`, `ndmin=0`), which are all correct and verifiable. The source build instructions are a unique and accurate addition. All execution facts are present and correct.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data3.md:**

The "Usage and Examples" section presents the following patterns:

1. **Creating Arrays** — 1D `np.array([1,2,3,4])`, 2D `np.array([[1,2],[3,4]])` with outputs: Shows basic array creation. ✅
2. **Array Operations and Broadcasting** — element-wise addition `x + y`, 2D broadcasting `m + n` with output showing the full result matrix: Shows broadcasting with a clear 3×3 output. *What*: perform arithmetic with broadcasting. *How*: use operators; NumPy expands shapes automatically. ✅
3. **Universal Functions (ufunc)** — `np.sin(angles)` with output: Shows element-wise function application. ✅
4. **Linear Algebra Example** — `np.dot(A, B)` with output, `np.linalg.det(A)` with output: Shows matrix multiplication and determinant computation. *What*: perform matrix operations. *How*: use `np.dot` and `np.linalg.det`. ✅
5. **Random Sampling** — `np.random.randn(5)`: Shows random number generation. *What*: generate standard normal samples. *How*: call `np.random.randn`. ✅

**Assessment:** data3.md presents five distinct usage patterns. The broadcasting example shows a 3×3 output matrix, making the shape expansion mechanism visually clear. The linear algebra section uniquely includes `np.linalg.det` with its output (`-2.0000000000000004`), demonstrating floating-point precision behavior. All patterns include runnable code with expected outputs.

**KU = 1** ✅

---

### data3.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data3.md ATORAK Score: 100**

---

## Summary: All Three NumPy READMEs — ATORAK Adherence

| README | KD (Domain Concepts) | KE (Execution Facts) | KU (Usage Patterns) | Kpercentage |
|--------|---------------------|---------------------|---------------------|-------------|
| data1.md | 1 | 1 | 1 | **100** |
| data2.md | 1 | 1 | 1 | **100** |
| data3.md | 1 | 1 | 1 | **100** |

### Final Average Score (Equation 16 from TCC §4.4.3)

```
Kavg = (100 + 100 + 100) / 3 = 100
```

**NumPy ATORAK Average Score: 100**

---

## Analysis and Observations

**Why all three score 100 on ATORAK adherence:**

NumPy is one of the most widely used Python libraries, with extensive public documentation, tutorials, and academic references in LLM training data. The model correctly identified and represented all three knowledge elements in every generated README.

**KD (Domain Concepts) — all three score 1:**
All three READMEs include an explicit "Domain Concepts" subsection in the Overview, listing and correctly defining the core NumPy entities. data1.md defines 7 concepts (ndarray, Broadcasting, ufuncs, Linear Algebra, Random Sampling, Fourier Transforms, Masked Arrays). data2.md defines 8 concepts, adding "Vectorized Operations" as an explicit concept and "Integration with C/C++ and Fortran". data3.md defines 6 concepts with the most precise ndarray definition (explicitly noting "homogeneous" and "fixed-size items").

**KE (Execution Facts) — all three score 1:**
All three READMEs provide correct, executable installation commands, correct API Reference sections with accurate function signatures and parameter names, and correct environment requirements. data1.md is the most comprehensive in sub-module coverage (includes `numpy.ma`). data2.md uniquely documents the modern `numpy.random.default_rng()` Generator API and `numpy.matmul`. data3.md provides the most detailed `numpy.array()` signature with all parameters and defaults.

**KU (Usage Patterns) — all three score 1:**
All three READMEs present multiple named usage patterns covering the core NumPy workflows (array creation, broadcasting, ufuncs, linear algebra, random sampling). data1.md adds the `numpy.linalg.eig` eigenvalue pattern and masked arrays reference. data2.md uses the modern `default_rng()` random pattern. data3.md uniquely includes `np.linalg.det` with floating-point output and source build instructions.

**Qualitative differences (not affecting binary ATORAK score):**
- data1.md: Broadest sub-module coverage (7 domain concepts, includes fft and masked arrays in API Reference), 6 usage patterns.
- data2.md: Most comprehensive domain concept list (8 entities), documents modern Generator API, includes installation verification step.
- data3.md: Most precise function signatures (full `numpy.array()` parameter list), includes source build instructions, 5 usage patterns.

**This result is consistent with the TCC's hypothesis** that high-popularity libraries with extensive public documentation are the easiest case for LLM-based README generation. NumPy's ubiquity in LLM training data ensures that all three knowledge elements are naturally and correctly present in every generated README.
