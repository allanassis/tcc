# scikit-learn

## Overview

scikit-learn is an open-source Python library that provides simple, efficient tools for data mining and data analysis. Built on top of NumPy, SciPy, and matplotlib, it is one of the most popular machine learning libraries, widely used for building predictive data models. The project emphasizes ease of use, performance, and well-documented APIs that cover a broad variety of supervised and unsupervised learning algorithms.

### Domain Concepts

- **Estimators**: Core abstractions that implement machine learning algorithms. Every model, transformer, or predictor inherits from the BaseEstimator class.
- **Transformers**: Objects that can transform data, typically used for preprocessing like scaling, normalization, or feature extraction.
- **Predictors**: Estimators capable of making predictions on new data.
- **Pipelines**: Chains of transformers and estimators to assemble workflows.
- **Cross-validation**: Techniques to assess model generalization performance.
- **Model Selection and Hyperparameter tuning**: Includes grid search and randomized search.
- **Metrics**: Functions to evaluate the performance of models.
- **Datasets**: Utilities to load and generate toy datasets for experimenting and benchmarking.

The tool models concepts in supervised learning (classification, regression), unsupervised learning (clustering, dimensionality reduction), and model evaluation.

---

## Installation

### Prerequisites

- Python (>=3.7)
- NumPy
- SciPy
- Joblib
- Threadpoolctl

### Install via pip

```bash
pip install scikit-learn
```

### Install via conda (recommended for scientific Python stack users)

```bash
conda install scikit-learn
```

scikit-learn supports major OS platforms including Linux, macOS, and Windows.

---

## Usage and Examples

### Basic Classification Example

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Load example dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Instantiate and train an SVM classifier
clf = SVC(kernel='linear', C=1.0)
clf.fit(X_train, y_train)

# Predict on test set
y_pred = clf.predict(X_test)

# Evaluate performance
print(classification_report(y_test, y_pred))
```

### Pipeline Usage Example

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC

# Create a pipeline combining preprocessing and a classifier
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2)),
    ('svc', SVC(kernel='rbf'))
])

pipe.fit(X_train, y_train)
print(pipe.score(X_test, y_test))
```

### Cross-validation Example

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=100)
scores = cross_val_score(clf, X, y, cv=5)
print("Cross-validation scores:", scores)
print("Mean score:", scores.mean())
```

---

## API Reference

### Core Classes and Functions

#### `sklearn.base.BaseEstimator`

The base class for all estimators in scikit-learn, implementing the basic interface.

- Methods:
  - `fit(X, y=None)`: Fit model to data.
  - `predict(X)`: Perform prediction.
  - `transform(X)`: Transform data.
  - `fit_transform(X, y=None)`: Fit and transform data.
  - `score(X, y)`: Return the mean accuracy on the given test data and labels.

#### `sklearn.preprocessing.StandardScaler`

Standardize features by removing the mean and scaling to unit variance.

- Parameters:
  - `copy` (bool): Whether to copy input data or overwrite.
  - `with_mean` (bool): Center data before scaling.
  - `with_std` (bool): Scale data to unit variance.

#### `sklearn.svm.SVC`

C-Support Vector Classification.

- Parameters include:
  - `kernel`: Specifies the kernel type (`linear`, `poly`, `rbf`, `sigmoid`).
  - `C`: Regularization parameter.
  - `gamma`: Kernel coefficient.

#### `sklearn.pipeline.Pipeline`

Chains multiple estimators into a single estimator.

- Parameters:
  - Sequential list of named steps `(name, estimator)`.

- Methods:
  - `fit(X, y)`: Fit all steps.
  - `predict(X)`: Call predict of final step.
  - `transform(X)`: Call transform of final step if available.

#### `sklearn.model_selection.train_test_split`

Split arrays or matrices into random train and test subsets.

- Parameters:
  - `test_size`: Proportion of dataset included in test split.
  - `train_size`: Proportion of dataset included in train split.
  - `random_state`: Seed for random number generator.

- Returns:
  - Splits of X and y into train and test datasets.

#### `sklearn.model_selection.cross_val_score`

Evaluate a score by cross-validation.

- Parameters:
  - `estimator`: The object to use to fit the data.
  - `X`: Array-like of features.
  - `y`: Array-like of target.
  - `cv`: Number of folds or cross-validation generator.

- Returns:
  - Array of scores of the estimator for each run of the cross-validation.

#### `sklearn.metrics.classification_report`

Build a text report showing the main classification metrics.

- Parameters:
  - `y_true`: True labels.
  - `y_pred`: Predicted labels.
  - `target_names`: Names of the classes.

- Returns:
  - A string summary of precision, recall, f1-score, and support.

---

## License

scikit-learn is distributed under the BSD 3-Clause License. See the [LICENSE](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING) file for details.
