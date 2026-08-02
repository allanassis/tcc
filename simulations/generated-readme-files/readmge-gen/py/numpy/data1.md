# NumPy

## Overview

NumPy (Numerical Python) is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays efficiently. NumPy is the foundational high-performance numerical computing library powering many other scientific computing and data analysis libraries in Python, such as SciPy, Pandas, and scikit-learn.

### Domain Concepts

- **ndarray:** NumPy's primary data structure, an N-dimensional array providing fast, vectorized operations.
- **Broadcasting:** A set of rules for applying arithmetic operations on arrays of different shapes.
- **Universal Functions (ufuncs):** Vectorized functions that operate element-wise on arrays.
- **Linear Algebra:** Support for matrix operations, decompositions, and solving linear systems.
- **Random Sampling:** Tools for pseudorandom number generation and statistical distributions.
- **Fourier Transforms:** Efficient computation of Fourier transforms and related algorithms.
- **Masked Arrays:** Arrays that may have missing or invalid entries filled with masks.

NumPy's main goal is to provide efficient storage and operations on dense multi-dimensional arrays and matrices, replacing traditional Python lists for numerical tasks with a more optimized approach leveraging compiled C code.

---

## Installation

### Requirements

- Python 3.8 or higher recommended.

### Using pip

```bash
pip install numpy
```

### Using conda

```bash
conda install numpy
```

NumPy is cross-platform and available on Linux, macOS, and Windows.

---

## Usage and Examples

### Importing NumPy

```python
import numpy as np
```

### Creating Arrays

```python
a = np.array([1, 2, 3, 4])
print(a)
# Output: [1 2 3 4]

b = np.zeros((2, 3))
print(b)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]

c = np.eye(3)
print(c)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

### Array Operations and Broadcasting

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Element-wise addition
print(x + y)
# Output: [5 7 9]

# Broadcasting: add scalar to array
print(x + 10)
# Output: [11 12 13]

# Multiplying matrix and vector
A = np.array([[1, 2], [3, 4]])
v = np.array([5, 6])
print(A @ v)
# Output: [17 39]
```

### Universal Functions (ufuncs)

```python
arr = np.array([0, np.pi/2, np.pi])
sin_vals = np.sin(arr)
print(sin_vals)
# Output: [0. 1. 0.]
```

### Linear Algebra Example

```python
from numpy.linalg import inv, eig

M = np.array([[1, 2], [3, 4]])
M_inv = inv(M)
eigenvalues, eigenvectors = eig(M)

print("Inverse:\n", M_inv)
print("Eigenvalues:", eigenvalues)
```

### Random Sampling

```python
rand_nums = np.random.rand(5)
print(rand_nums)

normal_samples = np.random.normal(loc=0, scale=1, size=10)
print(normal_samples)
```

---

## API Reference

Below are some of the core modules, functions, and classes available in NumPy:

### `numpy.ndarray`

The main array class. Supports multi-dimensional, homogeneous data, and vectorized operations.

- Creation via `np.array(data, dtype=...)`
- Attributes: `.shape`, `.dtype`, `.size`, `.ndim`
- Methods: `.reshape()`, `.astype()`, `.sum()`, `.mean()`, `.dot()`, `.T` (transpose)

### Array Creation Functions

- `np.array(object, dtype=None, ...)` - Create an array.
- `np.zeros(shape, dtype=float, ...)` - Array of zeros.
- `np.ones(shape, dtype=float, ...)` - Array of ones.
- `np.empty(shape, dtype=float, ...)` - Uninitialized array.
- `np.arange([start,] stop[, step])` - Create array with arithmetic progression.
- `np.linspace(start, stop, num=50)` - Create linearly spaced points.

### Mathematical Functions (ufuncs)

Element-wise functions optimized for arrays:

- `np.sin(x)`, `np.cos(x)`, `np.exp(x)`, `np.log(x)`, `np.sqrt(x)`
- Reduction: `np.sum(arr)`, `np.prod(arr)`, `np.min(arr)`, `np.max(arr)`

### Linear Algebra (`numpy.linalg`)

- `numpy.linalg.inv(a)` - Compute the (multiplicative) inverse of a matrix.
- `numpy.linalg.det(a)` - Compute determinant.
- `numpy.linalg.eig(a)` - Compute eigenvalues and eigenvectors.
- `numpy.linalg.solve(a, b)` - Solve linear system `ax = b`.
- `numpy.dot(a, b)` - Dot product of two arrays.

### Random (`numpy.random`)

- `numpy.random.rand(d0, d1, ..., dn)` - Uniform [0,1) samples.
- `numpy.random.randn(d0, d1, ..., dn)` - Samples from standard normal distribution.
- `numpy.random.randint(low, high, size)` - Random integers.
- `numpy.random.normal(loc=0.0, scale=1.0, size=None)` - Samples from normal distribution.

### Fourier Transform (`numpy.fft`)

- `numpy.fft.fft(a)` - Compute the one-dimensional discrete Fourier Transform.
- `numpy.fft.ifft(a)` - Inverse FFT.

### Masked Arrays (`numpy.ma`)

- `numpy.ma.masked_array(data, mask=...)` - Create arrays with masked values.

---

## License

NumPy is licensed under the BSD 3-Clause License. See the [LICENSE.txt](https://github.com/numpy/numpy/blob/main/LICENSE.txt) file for details.
