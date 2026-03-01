# NumPy

## Overview

NumPy is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on these arrays efficiently. NumPy serves as the foundational building block for many scientific and data analysis libraries, enabling fast numerical computations and advanced data processing.

### Domain Concepts

- **N-dimensional arrays (ndarray):** Central data structure in NumPy representing multi-dimensional homogeneous data.
- **Broadcasting:** Rules that allow arithmetic operations between arrays of different shapes.
- **Universal Functions (ufuncs):** Functions that operate element-wise on ndarrays, offering vectorized performance.
- **Linear Algebra:** Matrix operations such as multiplication, eigenvalues, singular value decomposition, and more.
- **Random Sampling:** Generation of pseudorandom numbers for simulation and modeling.
- **FFT (Fast Fourier Transform):** Algorithms to compute discrete Fourier transforms efficiently.

---

## Installation

NumPy can be installed using popular Python package managers.

### Using pip

```bash
pip install numpy
```

### Using conda (Anaconda distribution)

```bash
conda install numpy
```

---

## Usage and Examples

### Creating Arrays

```python
import numpy as np

# Create a 1D array
a = np.array([1, 2, 3])
print(a)

# Create a 2D array
b = np.array([[1, 2], [3, 4]])
print(b)

# Create an array of zeros
z = np.zeros((2, 3))
print(z)

# Create an array of ones
o = np.ones((3, 2))
print(o)

# Create an array with a range of values
r = np.arange(0, 10, 2)
print(r)
```

### Array Operations and Broadcasting

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
c = a + b
print(c)  # Output: [5 7 9]

# Broadcasting example
d = a + 10
print(d)  # Output: [11 12 13]
```

### Universal Functions (ufuncs)

```python
a = np.array([0, np.pi/2, np.pi])

# Compute sine of each element
sin_a = np.sin(a)
print(sin_a)
```

### Linear Algebra Example

```python
from numpy.linalg import inv, eig

A = np.array([[1, 2], [3, 4]])
A_inv = inv(A)
print(A_inv)

eigenvalues, eigenvectors = eig(A)
print(eigenvalues)
print(eigenvectors)
```

### Random Sampling

```python
rand_arr = np.random.rand(3, 2)
print(rand_arr)

normal_samples = np.random.normal(loc=0.0, scale=1.0, size=5)
print(normal_samples)
```

---

## API Reference

### Core ndarray Object

- `numpy.array(object, dtype=None, ...)`  
  Creates an ndarray from any object exposing the array interface.

- `ndarray.shape`  
  Tuple of array dimensions.

- `ndarray.dtype`  
  Data type of elements in the array.

- `ndarray.reshape(shape)`  
  Returns an array with a new shape without changing data.

- `ndarray.T`  
  Transpose of the array.

### Array Creation Routines

- `numpy.zeros(shape, dtype=float, order='C')`  
  Create an array filled with zeros.

- `numpy.ones(shape, dtype=None, order='C')`  
  Create an array filled with ones.

- `numpy.arange([start,] stop[, step,], dtype=None)`  
  Return evenly spaced values within a given interval.

- `numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)`  
  Return evenly spaced numbers over a specified interval.

### Mathematical Functions

- `numpy.sin(x)`  
  Trigonometric sine, element-wise.

- `numpy.exp(x)`  
  Calculate the exponential of all elements in the input array.

- `numpy.sqrt(x)`  
  Return the non-negative square-root of an array, element-wise.

### Random Module

- `numpy.random.rand(d0, d1, ..., dn)`  
  Random values in a given shape from a uniform distribution over `[0, 1)`.

- `numpy.random.normal(loc=0.0, scale=1.0, size=None)`  
  Draw random samples from a normal (Gaussian) distribution.

### Linear Algebra Module (`numpy.linalg`)

- `inv(a)`  
  Compute the (multiplicative) inverse of a matrix.

- `eig(a)`  
  Compute the eigenvalues and right eigenvectors of a square array.

- `det(a)`  
  Compute the determinant of an array.

- `svd(a, full_matrices=True, compute_uv=True)`  
  Singular Value Decomposition.

---

## Contributing

NumPy is an open-source project that welcomes contributions from the community.

### How to contribute

1. Fork the repository on [GitHub](https://github.com/numpy/numpy).
2. Clone your fork locally.
3. Create a new branch for your work.
4. Follow style guidelines and write tests for new features or bug fixes.
5. Submit a pull request with clear descriptions of changes.
6. Engage with reviewers during the discussion phase.

For detailed instructions, see [NumPy's contribution guide](https://numpy.org/devdocs/dev/index.html).

---

## License

NumPy is licensed under the BSD 3-Clause License. See the [LICENSE.txt](https://github.com/numpy/numpy/blob/main/LICENSE.txt) file for details.

---

## Contact

- **Website:** [https://numpy.org/](https://numpy.org/)
- **GitHub Repository:** [https://github.com/numpy/numpy](https://github.com/numpy/numpy)
- **Community Support:**
  - Mailing lists: https://numpy.org/community/
  - Stack Overflow: https://stackoverflow.com/questions/tagged/numpy
  - Gitter chat: https://gitter.im/numpy/numpy
