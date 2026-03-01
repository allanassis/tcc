# NumPy

## Overview

NumPy (Numerical Python) is an open-source Python library that provides support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays efficiently. It forms the foundational package for scientific computing with Python and serves as a basis for many other libraries in data science, machine learning, engineering, and numerical computations.

### Domain Concepts

- **ndarray**: A powerful n-dimensional array object, the core data structure in NumPy.
- **Vectorization**: Element-wise operations on arrays without explicit loops for efficiency.
- **Broadcasting**: Rules to apply arithmetic operations on arrays of different shapes.
- **Universal Functions (ufuncs)**: Fast element-wise functions written in C for performance.
- **Linear Algebra**: Matrix operations, decompositions, and eigenvalue computations.
- **Random Sampling**: Generating random numbers from various probability distributions.
- **Fourier Transforms**: Computing discrete Fourier transforms for signal processing.
- **Integration with C/C++/Fortran**: Interfacing with low-level languages for speed.

NumPy enables the creation, manipulation, and analysis of large datasets and numerical models with speed and ease, providing essential building blocks for scientific and engineering computations.

---

## Installation

NumPy supports multiple platforms including Windows, macOS, and Linux. It is compatible with Python versions 3.7 and above.

### Using pip (Recommended)

```bash
pip install numpy
```

### Using conda (Anaconda distribution)

```bash
conda install numpy
```

### Verifying Installation

Run the following Python code after installation:

```python
import numpy as np
print(np.__version__)
```

This should print the installed NumPy version.

---

## Usage and Examples

### Creating Arrays

```python
import numpy as np

# Create a 1-dimensional array
arr1 = np.array([1, 2, 3, 4])
print(arr1)

# Create a 2x3 array of zeros
arr2 = np.zeros((2, 3))
print(arr2)

# Create an array with evenly spaced values
arr3 = np.arange(0, 10, 2)
print(arr3)
```

### Basic Operations and Broadcasting

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
c = a + b
print(c)  # Output: [5 7 9]

# Broadcasting example
d = a + 5
print(d)  # Output: [6 7 8]
```

### Universal Functions (ufuncs)

```python
angles = np.array([0, np.pi/2, np.pi])
sin_values = np.sin(angles)
print(sin_values)
```

### Linear Algebra

```python
from numpy.linalg import inv, eig

A = np.array([[1, 2], [3, 4]])

# Matrix inversion
A_inv = inv(A)
print(A_inv)

# Eigenvalues and eigenvectors
values, vectors = eig(A)
print(values)
print(vectors)
```

### Random Sampling

```python
# Generate 5 random numbers from a standard normal distribution
rand_nums = np.random.randn(5)
print(rand_nums)
```

---

## API Reference

### Core Data Structures

- **`numpy.ndarray`**

  The primary array type. Supports multi-dimensional data with homogeneous types.

  Common attributes:
  - `.shape`: Tuple of array dimensions.
  - `.dtype`: Data type of elements.
  - `.size`: Total number of elements.
  - `.ndim`: Number of array dimensions.

### Array Creation Functions

- `numpy.array(object, dtype=None, ...)`

  Create an array from any object exposing the array interface.

- `numpy.zeros(shape, dtype=float, ...)`

  Create an array filled with zeros.

- `numpy.ones(shape, dtype=float, ...)`

  Create an array filled with ones.

- `numpy.arange([start,] stop, [step,])`

  Return evenly spaced values within a given interval.

- `numpy.linspace(start, stop, num=50)`

  Return evenly spaced numbers over a specified interval.

### Array Manipulation

- `numpy.reshape(a, newshape)`

  Gives a new shape to an array without changing its data.

- `numpy.concatenate((a1, a2, ...), axis=0)`

  Join a sequence of arrays along an existing axis.

- `numpy.transpose(a, axes=None)`

  Permute the dimensions of an array.

### Mathematical Functions

- `numpy.add(x1, x2)`

- `numpy.subtract(x1, x2)`

- `numpy.multiply(x1, x2)`

- `numpy.divide(x1, x2)`

- `numpy.sqrt(x)`

- `numpy.exp(x)`

- `numpy.log(x)`

(Ufuncs operate element-wise on arrays.)

### Linear Algebra (`numpy.linalg` module)

- `inv(a)`

  Compute the multiplicative inverse of a matrix.

- `det(a)`

  Compute the determinant of a matrix.

- `eig(a)`

  Compute the eigenvalues and right eigenvectors of a square array.

- `svd(a)`

  Singular value decomposition.

### Random Sampling (`numpy.random` module)

- `rand(d0, d1, ..., dn)`

  Random values in a given shape.

- `randn(d0, d1, ..., dn)`

  Samples from the “standard normal” distribution.

- `randint(low, high=None, size=None)`

  Random integers from low (inclusive) to high (exclusive).

### Fourier Transforms (`numpy.fft` module)

- `fft(a)`

  Compute the one-dimensional discrete Fourier Transform.

- `ifft(a)`

  Compute the one-dimensional inverse discrete Fourier Transform.

---

## Contributing

NumPy is an open source project, welcoming contributions from the community.

### How to contribute:

1. Fork the repository: https://github.com/numpy/numpy
2. Work on your feature or bug fix on a separate branch.
3. Write tests for your changes.
4. Follow the coding style and guidelines as described in the CONTRIBUTING.md.
5. Submit pull requests with a clear description of your modifications.

You can also contribute by reporting bugs, suggesting features, updating documentation, or helping with reviews.

---

## License

NumPy is licensed under the BSD 3-Clause License. See the [LICENSE.txt](https://github.com/numpy/numpy/blob/main/LICENSE.txt) file for details.

---

## Contact

- Official website: https://numpy.org/
- GitHub repository: https://github.com/numpy/numpy
- Mailing list and community forums are available on the official website.
- For issues and discussion: Use GitHub Issues or NumPy mailing lists.
