# NumPy

## Overview

NumPy (Numerical Python) is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays efficiently. NumPy is a core component in the Python scientific stack, widely used for numerical computations, data analysis, machine learning, and engineering tasks.

### Domain Concepts

- **ndarray:** The central data structure in NumPy representing an N-dimensional array.
- **Vectorized Operations:** Efficient, element-wise operations over arrays without explicit loops.
- **Broadcasting:** A mechanism allowing arithmetic operations on arrays of different shapes by automatically expanding their shapes.
- **Universal Functions (ufuncs):** Fast, element-wise functions that operate on ndarrays.
- **Linear Algebra:** Functions to perform matrix multiplication, eigenvalue computations, decompositions, etc.
- **Random Sampling:** Utilities to generate random numbers following various probability distributions.
- **Fourier Transforms:** Tools for frequency domain analysis.
- **Integration with C/C++ and Fortran:** Interfaces for extending and accelerating computations.

NumPy abstracts numerical and scientific computation concepts into efficient implementations that enable scalable and high-performance computing workflows in Python.

---

## Installation

NumPy supports multiple platforms and Python versions. It can be installed easily using package managers.

### Prerequisites

- Python 3.7 or newer
- pip or conda package manager

### Using pip

```bash
pip install numpy
```

### Using conda

```bash
conda install numpy
```

### Verifying the installation

```python
import numpy as np
print(np.__version__)
```

NumPy is cross-platform and works on Windows, macOS, and Linux.

---

## Usage and Examples

This section illustrates common usage patterns demonstrating how to create and manipulate arrays, perform computations, and utilize prominent features of NumPy.

### Creating Arrays

```python
import numpy as np

# From Python lists:
a = np.array([1, 2, 3])
print(a)  # Output: [1 2 3]

# Multi-dimensional array:
b = np.array([[1, 2], [3, 4]])
print(b)
# Output:
# [[1 2]
#  [3 4]]

# Creating arrays of zeros or ones:
zeros = np.zeros((3, 4))
ones = np.ones((2, 2))
```

### Array Operations and Broadcasting

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Element-wise addition:
print(x + y)  # Output: [5 7 9]

# Broadcasting example:
z = np.array([[1], [2], [3]])
print(z + x)
# Output:
# [[2 3 4]
#  [3 4 5]
#  [4 5 6]]
```

### Universal Functions (ufuncs)

```python
arr = np.array([0, np.pi/2, np.pi])

# Element-wise sine:
sin_arr = np.sin(arr)
print(sin_arr)
# Output: [0. 1. 0.]
```

### Linear Algebra

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication:
C = np.dot(A, B)
print(C)
# Output:
# [[19 22]
#  [43 50]]

# Inverse of a matrix:
inv_A = np.linalg.inv(A)
print(inv_A)
```

### Random Sampling

```python
rng = np.random.default_rng()

# Draw 5 samples from a normal distribution:
samples = rng.normal(loc=0, scale=1, size=5)
print(samples)
```

---

## API Reference

### Core Classes and Functions

#### `numpy.ndarray`

The primary array class representing fixed-size, multidimensional arrays. Arrays support various operations:

- Creation: `array()`, `zeros()`, `ones()`, `empty()`, `arange()`, `linspace()`
- Attributes: `.shape`, `.dtype`, `.size`, `.ndim`
- Methods: `.reshape()`, `.flatten()`, `.transpose()`, etc.

#### Array Creation Functions

- `numpy.array(object, dtype=None, ...)`: Creates an ndarray from any object exposing the array interface.
- `numpy.zeros(shape, dtype=float, ...)`: Creates an array filled with zeros.
- `numpy.ones(shape, dtype=float, ...)`: Creates an array filled with ones.
- `numpy.arange(start, stop, step, ...)`: Returns evenly spaced values within an interval.
- `numpy.linspace(start, stop, num, ...)`: Returns evenly spaced numbers over a specified interval.

#### Universal Functions (ufuncs)

Functions that operate element-wise on ndarrays:

- `numpy.sin(x)`, `numpy.cos(x)`, `numpy.exp(x)`, `numpy.log(x)`, `numpy.sqrt(x)`, etc.

#### Linear Algebra (`numpy.linalg`)

- `numpy.linalg.inv(a)`: Compute the (multiplicative) inverse of a matrix.
- `numpy.linalg.eig(a)`: Compute eigenvalues and eigenvectors.
- `numpy.linalg.norm(x)`: Compute vector or matrix norm.
- `numpy.dot(a, b)`: Dot product of two arrays.
- `numpy.matmul(a, b)`: Matrix product of two arrays.

#### Random Sampling (`numpy.random`)

- `numpy.random.default_rng()`: Create a new random number generator instance.
- `Generator.normal(loc=0.0, scale=1.0, size=None)`: Draw samples from a normal distribution.
- `Generator.integers(low, high=None, size=None)`: Draw random integers.

#### Fourier Transform (`numpy.fft`)

- `numpy.fft.fft(a)`: Compute the one-dimensional discrete Fourier Transform.
- `numpy.fft.ifft(a)`: Compute the one-dimensional inverse discrete Fourier Transform.

---

## License

NumPy is licensed under the BSD 3-Clause License.  
For full license details, see the [LICENSE.txt](https://github.com/numpy/numpy/blob/main/LICENSE.txt) file in the NumPy repository.
