# NumPy

## Overview

NumPy (Numerical Python) is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a vast collection of high-level mathematical functions to operate on these arrays efficiently. NumPy serves as the foundation for most numerical and scientific computing libraries in Python including SciPy, Pandas, and scikit-learn, making it essential for data analysis, machine learning, and scientific research.

### Domain Concepts

- **ndarray:** The core data structure of NumPy, representing a multidimensional, homogeneous array of fixed-size items.
- **Broadcasting:** A powerful mechanism that allows NumPy to perform arithmetic operations on arrays of different shapes efficiently.
- **Vectorization:** The process of performing operations on entire arrays rather than their individual elements, enabling high-performance computing.
- **Universal Functions (ufunc):** Functions that operate element-wise on arrays, providing fast vectorized operations.
- **Linear Algebra:** NumPy includes a set of routines to perform matrix operations like dot products, inverses, eigenvalue computations, and more.
- **Random Sampling:** Facilities for generating random numbers and performing random sampling.

---

## Installation

NumPy can be installed on Windows, macOS, and Linux using various package managers.

### Using pip (Recommended)

```bash
pip install numpy
```

### Using conda (Anaconda/Miniconda)

```bash
conda install numpy
```

### Building from source

Clone the GitHub repository and build manually (advanced users):

```bash
git clone https://github.com/numpy/numpy.git
cd numpy
pip install cython  # prerequisite
pip install .
```

Verify installation:

```python
import numpy as np
print(np.__version__)
```

---

## Usage and Examples

### Creating Arrays

```python
import numpy as np

# Create a 1D array
a = np.array([1, 2, 3, 4])
print(a)
# Output: [1 2 3 4]

# Create a 2D array
b = np.array([[1, 2], [3, 4]])
print(b)
# Output:
# [[1 2]
#  [3 4]]
```

### Array Operations and Broadcasting

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Element-wise addition
z = x + y
print(z)  # [5 7 9]

# Broadcasting example
m = np.array([[1], [2], [3]])
n = np.array([4, 5, 6])
result = m + n
print(result)
# Output:
# [[5 6 7]
#  [6 7 8]
#  [7 8 9]]
```

### Universal Functions (ufunc)

```python
angles = np.array([0, np.pi/2, np.pi])
sines = np.sin(angles)
print(sines)
# Output: [0. 1. 0.]
```

### Linear Algebra Example

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)
print(C)
# Output:
# [[19 22]
#  [43 50]]

# Compute determinant
det = np.linalg.det(A)
print(det)  # -2.0000000000000004
```

### Random Sampling

```python
# Generate 5 random numbers from a standard normal distribution
random_samples = np.random.randn(5)
print(random_samples)
```

---

## API Reference

### Core Functions and Classes

#### `numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0)`

Creates an ndarray from any object exposing the array interface.

- **Parameters:**
  - `object`: array_like input data.
  - `dtype` (optional): Desired data type.
  - `copy` (bool): If True, then the object is copied.
  - `order`: Memory layout order ('C', 'F', 'A', or 'K').
  - `subok`: If True, subclasses are preserved.
  - `ndmin`: Minimum number of dimensions.

- **Returns:** ndarray

---

#### `numpy.ndarray`

The fundamental array class.

- Attributes:
  - `shape`: Tuple indicating array dimensions.
  - `dtype`: Data type of elements.
  - `size`: Total number of elements.
  - `ndim`: Number of array dimensions.

- Common Methods:
  - `reshape()`, `transpose()`, `astype()`, `sum()`, `mean()`, `max()`, and more.

---

#### Universal Functions (ufuncs)

Element-wise functions such as:

- `numpy.sin(x)`, `numpy.cos(x)`
- `numpy.exp(x)`, `numpy.log(x)`
- `numpy.add(x1, x2)`, `numpy.subtract(x1, x2)`

They support broadcasting and vectorized operations for performance.

---

#### `numpy.linalg` Module

Linear algebra routines:

- `numpy.linalg.inv(A)`: Matrix inverse.
- `numpy.linalg.det(A)`: Determinant.
- `numpy.linalg.eig(A)`: Eigenvalues and eigenvectors.
- `numpy.linalg.solve(A, b)`: Solve linear system.

---

#### `numpy.random` Module

Random number generation:

- `numpy.random.rand(d0, d1, ..., dn)`: Uniform distribution over [0, 1).
- `numpy.random.randn(d0, d1, ..., dn)`: Samples from standard normal distribution.
- `numpy.random.randint(low, high=None, size=None)`: Random integers.

---

## License

NumPy is licensed under the BSD 3-Clause License. See the [LICENSE.txt](https://github.com/numpy/numpy/blob/main/LICENSE.txt) file for details.
