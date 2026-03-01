# scikit-learn

## Overview

scikit-learn is a powerful and widely used open-source machine learning library for Python. It provides simple and efficient tools for data mining and data analysis built on top of NumPy, SciPy, and matplotlib. The library is designed to be accessible to both beginners and experts by offering a consistent API, comprehensive documentation, and a wide range of algorithms and utilities.

### Domain Concepts

- **Estimators:** Objects implementing a `fit` method to learn from data.
- **Transformers:** Estimators that manipulate or extract features via a `transform` method.
- **Predictors:** Estimators that can make predictions via a `predict` method.
- **Pipelines:** Mechanisms to chain multiple estimators for streamlined workflows.
- **Cross-Validation:** Techniques to assess model generalization on unseen data.
- **Model Selection:** Tools for hyperparameter tuning and model evaluation.
- **Supervised Learning:** Algorithms trained with labeled data (classification, regression).
- **Unsupervised Learning:** Algorithms trained with unlabeled data (clustering, dimensionality reduction).
- **Metrics:** Functions to evaluate prediction accuracy and other performance measures.

scikit-learn provides implementations of many machine learning algorithms and utilities, such as linear models, support vector machines, decision trees, ensemble methods, clustering, and preprocessing.

---

## Installation

### Prerequisites

- Python (>=3.7)
- NumPy (>=1.17.3)
- SciPy (>=1.3.2)

### Install via pip

```bash
pip install scikit-learn
```

### Install via conda (recommended for most users)

```bash
conda install scikit-learn
```

### Optional dependencies for enhanced performance and extended functionality

- `joblib` for parallel computing
- `threadpoolctl` for threadpool management

---

## Usage and Examples

### Basic Estimator Usage

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize model
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train model
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
```

### Pipeline Usage Example

Combine preprocessing and modeling steps in a pipeline:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(kernel='linear'))
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

### Cross-Validation Example

Perform K-fold cross-validation:

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(max_iter=200)
scores = cross_val_score(clf, X, y, cv=5)

print("Cross-validation scores:", scores)
print("Mean accuracy:", scores.mean())
```

### Hyperparameter Tuning with Grid Search

```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
grid = GridSearchCV(SVC(), param_grid, cv=5)
grid.fit(X_train, y_train)

print("Best parameters:", grid.best_params_)
print("Best cross-validation score:", grid.best_score_)
```

---

## API Reference

### Main Classes and Functions

#### Data Sets

- `sklearn.datasets.load_iris()`: Load Iris dataset.
- `sklearn.datasets.load_digits()`: Load Digits dataset.
- `sklearn.datasets.make_classification()`: Generate a random classification problem.

#### Model Selection

- `train_test_split(*arrays, test_size, train_size, random_state, shuffle)`: Split arrays or matrices into random train and test subsets.
- `cross_val_score(estimator, X, y, cv)`: Evaluate a score by cross-validation.
- `GridSearchCV(estimator, param_grid, cv)`: Exhaustive search over specified parameter values for an estimator.

#### Preprocessing

- `StandardScaler()`: Standardize features by removing the mean and scaling to unit variance.
- `MinMaxScaler()`: Transform features by scaling each feature to a given range.

#### Feature Extraction & Dimensionality Reduction

- `PCA()`: Principal component analysis.
- `SelectKBest()`: Select features according to the k highest scores.

#### Supervised Learning Algorithms

- `LinearRegression()`: Ordinary least squares Linear Regression.
- `LogisticRegression()`: Logistic Regression classifier.
- `SVC()`: C-Support Vector Classification.
- `RandomForestClassifier()`: Random Forest classifier.
- `GradientBoostingClassifier()`: Gradient Boosting for classification.
- `KNeighborsClassifier()`: k-Nearest Neighbors classifier.

#### Unsupervised Learning Algorithms

- `KMeans()`: K-Means clustering.
- `DBSCAN()`: Density-Based Spatial Clustering.
- `AgglomerativeClustering()`: Hierarchical clustering.

#### Metrics

- `accuracy_score(y_true, y_pred)`: Classification accuracy.
- `mean_squared_error(y_true, y_pred)`: Mean squared error regression loss.
- `confusion_matrix(y_true, y_pred)`: Compute confusion matrix.

#### Utility Functions

- `sklearn.pipeline.Pipeline(steps)`: Sequentially apply a list of transforms and a final estimator.
- `sklearn.externals.joblib`: Tools for lightweight pipelining and caching.

---

## Contributing

scikit-learn is an open-source project and welcomes contributions.

### How to contribute

1. Fork the repository: https://github.com/scikit-learn/scikit-learn
2. Clone your fork and create a feature branch.
3. Follow the coding style and write tests for your code.
4. Run existing tests and test your changes thoroughly.
5. Submit a pull request with a clear description of your changes.

Refer to the [Contributing Guide](https://scikit-learn.org/stable/developers/contributing.html) in the official documentation for detailed instructions.

---

## License

scikit-learn is licensed under the BSD 3-Clause "New" or "Revised" License. See the [LICENSE](https://github.com/scikit-learn/scikit-learn/blob/main/LICENSE) file for details.

---

## Contact

- **Project Repository:** https://github.com/scikit-learn/scikit-learn
- **Official Website:** https://scikit-learn.org
- **Issue Tracker:** https://github.com/scikit-learn/scikit-learn/issues
- **Mailing List:** https://mail.python.org/mailman/listinfo/scikit-learn
- **Twitter:** [@scikit_learn](https://twitter.com/scikit_learn)

For questions, support, or to discuss contributions, please use the GitHub issues or the mailing list.
