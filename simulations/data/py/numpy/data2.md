# NumPy

## Overview

NumPy (Numerical Python) is an open-source library fundamental for scientific computing with Python. It provides support for large, multi-dimensional arrays and matrices, along with a rich collection of high-level mathematical functions to operate on these arrays efficiently. NumPy serves as the foundational package for numerical computations in Python and is widely used in data analysis, machine learning, artificial intelligence, physics, engineering, and many other fields.

### Domain Concepts

- **ndarray (N-dimensional array):** The core data structure in NumPy representing homogeneous multidimensional arrays.
- **Broadcasting:** Mechanism to perform arithmetic operations on arrays of different shapes.
- **Universal Functions (ufuncs):** Element-wise functions that operate on ndarrays.
- **Masked Arrays:** Arrays that may have missing or invalid entries.
- **Linear Algebra:** Includes matrix multiplication, decompositions, eigenvalues, etc.
- **Random Number Generation:** Tools for generating random numbers, sampling, and distributions.
- **Fourier Transforms:** Tools for signal processing and frequency analysis.

---

## Installation

NumPy requires Python 3.7 or newer and can be installed using pip, conda, or your system's package manager.

### Using pip (recommended)

```bash
pip install numpy
```

### Using conda

```bash
conda install numpy
```

### Verify installation

```python
import numpy as np
print(np.__version__)
```

NumPy supports multiple platforms including Linux, macOS, and Windows.

---

## Usage and Examples

### Creating ndarrays

```python
import numpy as np

# Create a 1D array
arr1d = np.array([1, 2, 3, 4])

# Create a 2D array
arr2d = np.array([[1, 2], [3, 4]])

print(arr1d)
print(arr2d)
```

### Array arithmetic and broadcasting

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
c = a + b

# Broadcasting example (adding scalar)
d = a + 10

print(c)  # [5 7 9]
print(d)  # [11 12 13]
```

### Universal functions (ufuncs)

```python
x = np.array([0, np.pi/2, np.pi])

# Calculate sine of each element
sin_x = np.sin(x)

print(sin_x)  # [0.0, 1.0, 0.0]
```

### Linear algebra operations

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
C = np.dot(A, B)

print(C)
```

### Random number generation

```python
# Create an array of 5 random floats between 0 and 1
rand_nums = np.random.rand(5)

print(rand_nums)
```

### Reshaping arrays

```python
arr = np.arange(6)
reshaped = arr.reshape((2, 3))

print(reshaped)
```

---

## API Reference

### Core Classes and Functions

#### `numpy.ndarray`

The main data structure representing an N-dimensional array.

- Attributes:
  - `shape`: Tuple of array dimensions.
  - `dtype`: Data-type of the array’s elements.
  - `size`: Number of elements in the array.
- Methods:
  - `reshape(newshape)`: Returns an array with a new shape.
  - `flatten()`: Returns a copy of the array collapsed into one dimension.
  - `transpose()`: Permute array dimensions.

#### Array Creation

- `numpy.array(object, dtype=None)`: Create an array from a Python list or tuple.
- `numpy.arange(start, stop, step)`: Create arrays with regularly spaced values.
- `numpy.zeros(shape)`: An array filled with zeros.
- `numpy.ones(shape)`: An array filled with ones.
- `numpy.empty(shape)`: Create uninitialized array.

#### Array Manipulation

- `numpy.reshape(a, newshape)`: Gives a new shape to an array without changing data.
- `numpy.concatenate((a1, a2, ...), axis=0)`: Join a sequence of arrays.
- `numpy.split(ary, indices_or_sections)`: Split an array into multiple sub-arrays.

#### Universal Functions

Functions applied element-wise to arrays; include `np.sin`, `np.cos`, `np.exp`, `np.log`, etc.

#### Linear Algebra (`numpy.linalg` module)

- `numpy.dot(a, b)`: Dot product of two arrays.
- `numpy.linalg.inv(a)`: Compute the inverse of a matrix.
- `numpy.linalg.eig(a)`: Eigenvalues and eigenvectors of a square array.

#### Random Number Generation (`numpy.random` module)

- `numpy.random.rand(d0, d1, ..., dn)`: Random values in a given shape.
- `numpy.random.randint(low, high, size)`: Random integers.

---

## Contributing

NumPy welcomes contributions from the community. You can contribute by:

- Reporting issues or bugs via the GitHub issue tracker.
- Submitting pull requests with bug fixes, improvements, or new features.
- Participating in discussions about design and future development.
- Updating documentation and examples for clarity.

### Contribution Guidelines

- Fork the repository and create a new branch for your feature or bug fix.
- Ensure your code passes existing tests and write new tests if applicable.
- Follow PEP 8 style guidelines and NumPy's code style.
- Submit pull requests with clear descriptions and references to related issues.

For detailed instructions, visit the [NumPy Contribution Guide](https://numpy.org/devdocs/dev/index.html).

---

## License

NumPy is licensed under the BSD 3-Clause License. See the [LICENSE.txt](https://github.com/numpy/numpy/blob/main/LICENSE.txt) file for details.

---

## Contact

- **Project repository:** [https://github.com/numpy/numpy](https://github.com/numpy/numpy)
- **Website and documentation:** [https://numpy.org](https://numpy.org)
- **Mailing list:** Subscribe via [https://mail.python.org/mailman/listinfo/numpy-discussion](https://mail.python.org/mailman/listinfo/numpy-discussion)
- **Issue Tracker:** [https://github.com/numpy/numpy/issues](https://github.com/numpy/numpy/issues)
