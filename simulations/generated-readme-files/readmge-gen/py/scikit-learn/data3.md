# scikit-learn

## Overview

scikit-learn is a widely-used open-source machine learning library for the Python programming language. It provides simple and efficient tools for data mining and data analysis, built on top of NumPy, SciPy, and matplotlib. The library covers many standard machine learning and statistical modeling tasks including classification, regression, clustering, dimensionality reduction, model selection, and preprocessing.

### Domain Concepts

- **Estimators**: Objects implementing machine learning algorithms. They follow a standard interface with `fit()`, `predict()`, and `transform()` methods.
- **Transformers**: Estimators that preprocess or transform data (e.g., scaling features) via `fit()` and `transform()`.
- **Classifiers and Regressors**: Algorithms that predict discrete labels or continuous outputs based on input data.
- **Pipelines**: Tools for chaining transformers and estimators sequentially to build complex workflows.
- **Model Evaluation & Selection**: Tools and metrics for assessing model performance and selecting model hyperparameters.
- **Datasets**: Utilities for loading and generating datasets for experimentation and benchmarking.

scikit-learn abstracts complex mathematical and statistical methods into easy-to-use interfaces, making it accessible to both beginners and experts.

---

## Installation

### Prerequisites

- Python (>=3.7)
- NumPy, SciPy
- Joblib
- Threadpoolctl

### Install via pip

```bash
pip install scikit-learn
```

### From Source

Clone the repository and install with:

```bash
git clone https://github.com/scikit-learn/scikit-learn.git
cd scikit-learn
pip install .
```

scikit-learn supports all major operating systems including Linux, macOS, and Windows.

---

## Usage and Examples

### Basic Example: Training a Classifier

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=42)

# Create RandomForest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train model
clf.fit(X_train, y_train)

# Predict on test set
y_pred = clf.predict(X_test)

# Evaluate accuracy
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
```

### Example: Data Preprocessing and Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(kernel='linear'))
])

pipeline.fit(X_train, y_train)
print(f"Test Accuracy: {pipeline.score(X_test, y_test):.2f}")
```

### Model Selection with Cross-Validation

```python
from sklearn.model_selection import GridSearchCV

param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
grid = GridSearchCV(SVC(), param_grid, cv=5)
grid.fit(X_train, y_train)

print("Best parameters:", grid.best_params_)
print("Best cross-validation accuracy:", grid.best_score_)
```

---

## API Reference

### Main Classes and Methods

#### `sklearn.base.BaseEstimator`

Base class for all estimators in scikit-learn.

- `fit(X, y)`: Fit model to data.
- `predict(X)`: Predict target values.
- `transform(X)`: Transform input data.
- `fit_transform(X, y)`: Fit and transform data.

#### `sklearn.ensemble.RandomForestClassifier`

Random forest classifier for classification tasks.

- `n_estimators` (int): Number of trees in the forest.
- `random_state` (int): Seed for reproducibility.
- Methods: `fit`, `predict`, `predict_proba`

#### `sklearn.svm.SVC`

Support Vector Classifier.

- `C` (float): Regularization parameter.
- `kernel` (str): Specifies the kernel type ('linear', 'rbf', etc.)
- Methods: `fit`, `predict`, `decision_function`

#### `sklearn.pipeline.Pipeline`

Sequentially apply a list of transforms and a final estimator.

- `steps` (list): List of (name, transform/estimator) tuples.
- Methods: `fit`, `predict`, `transform`, `fit_transform`

#### `sklearn.model_selection.GridSearchCV`

Exhaustive search over specified parameter values for an estimator.

- `estimator`: The model to optimize.
- `param_grid`: Dictionary with parameters names and lists of values.
- `cv` (int): Cross-validation splitting strategy.
- Methods: `fit`, `predict`, `score`, `best_params_`, `best_score_`

### Utility Functions

- `sklearn.datasets.load_iris()`: Load and return the iris dataset.
- `sklearn.metrics.accuracy_score(y_true, y_pred)`: Compute classification accuracy.

---

## License

scikit-learn is licensed under the BSD 3-Clause "New" or "Revised" License. See the [LICENSE](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING) file for details.
