# scikit-learn

## Overview

scikit-learn is a powerful and widely-used open-source Python library for machine learning. It provides simple and efficient tools for data mining and data analysis, built on top of NumPy, SciPy, and matplotlib. The library is designed to interoperate with the Python numerical and scientific libraries and champions a consistent, easy-to-use API.

### Domain Concepts

- **Supervised Learning:** Algorithms that learn a mapping from inputs to outputs based on example input-output pairs (e.g., classification, regression).
- **Unsupervised Learning:** Algorithms that detect patterns in data without labeled responses (e.g., clustering, dimensionality reduction).
- **Model Selection:** Tools and strategies to compare, validate, and tune models to ensure optimal performance.
- **Preprocessing:** Techniques to transform raw data into a suitable form for modeling, including normalization, encoding, and feature extraction.
- **Pipelines and Feature Unions:** Tools to assemble multiple processing steps into one coherent estimator or transformer.
- **Ensemble Methods:** Combining multiple models to improve robustness and accuracy.
- **Metrics and Evaluation:** Quantitative measures to evaluate the performance of models.

scikit-learn balances ease of use with flexibility, targeting a wide range of users from beginners to advanced practitioners in machine learning.

---

## Installation

### Prerequisites

- Python (>=3.7)
- NumPy
- SciPy

scikit-learn also works well with pandas and matplotlib for data handling and visualization.

### Install via pip

```bash
pip install scikit-learn
```

### Install via conda

```bash
conda install scikit-learn
```

scikit-learn supports Windows, macOS, and Linux platforms.

---

## Usage and Examples

### Basic Classification Example

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Load dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train classifier
clf = SVC(kernel='linear', random_state=42)
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

# Evaluate
print(classification_report(y_test, y_pred))
```

---

### Pipeline Usage Example

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2)),
    ('logreg', LogisticRegression(random_state=42))
])

pipeline.fit(X_train, y_train)
print(pipeline.score(X_test, y_test))
```

---

### Grid Search for Model Selection

```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svc = SVC()
clf = GridSearchCV(svc, parameters)
clf.fit(X_train, y_train)

print("Best parameters set:")
print(clf.best_params_)
```

---

## API Reference

### Supervised Learning Estimators

- `class sklearn.svm.SVC(kernel='rbf', C=1.0, ...)`

  Support Vector Classifier. Key parameters:
  - `kernel` (str): Specifies the kernel type to be used.
  - `C` (float): Regularization parameter.
  - `fit(X, y)`: Fit the model according to the given training data.
  - `predict(X)`: Perform classification on samples in X.

- `class sklearn.ensemble.RandomForestClassifier(n_estimators=100, ...)`

  Random Forest classifier using an ensemble of decision trees.
  - `n_estimators` (int): Number of trees in the forest.
  - `fit(X, y)`, `predict(X)`

- `class sklearn.linear_model.LogisticRegression(...)`

  Logistic Regression classifier.
  - `solver` (str): Algorithm to use in optimization.
  - `fit(X, y)`, `predict(X)`

---

### Unsupervised Learning Estimators

- `class sklearn.cluster.KMeans(n_clusters=8, ...)`

  K-means clustering.
  - `n_clusters` (int): The number of clusters to form.
  - `fit(X)`, `predict(X)`

- `class sklearn.decomposition.PCA(n_components=None, ...)`

  Principal Component Analysis for dimensionality reduction.
  - `n_components` (int or float): Number of components to keep.
  - `fit(X)`, `transform(X)`

---

### Model Selection and Evaluation

- `sklearn.model_selection.train_test_split(*arrays, test_size=None, ...)`

  Split arrays or matrices into random train and test subsets.

- `class sklearn.model_selection.GridSearchCV(estimator, param_grid, ...)`

  Exhaustive search over specified parameter values for an estimator.

- `sklearn.metrics.classification_report(y_true, y_pred, ...)`

  Build a text report showing the main classification metrics.

---

### Preprocessing

- `class sklearn.preprocessing.StandardScaler()`

  Standardize features by removing the mean and scaling to unit variance.

- `class sklearn.preprocessing.OneHotEncoder()`

  Encode categorical integer features as a one-hot numeric array.

---

### Pipelines

- `class sklearn.pipeline.Pipeline(steps, ...)`

  Chain multiple estimators into one. Includes transformers and final estimators.

---

## License

scikit-learn is released under the BSD 3-Clause "New" or "Revised" License.  
See the [LICENSE](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING) file for details.
