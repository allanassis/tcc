# scikit-learn

## Overview

scikit-learn is a powerful, open-source Python library for machine learning. It provides simple and efficient tools for data mining, data analysis, and modeling, built on top of well-established scientific Python libraries such as NumPy, SciPy, and matplotlib. Its primary domain concepts include supervised and unsupervised learning algorithms, model selection and evaluation techniques, preprocessing, and pipeline building. scikit-learn abstracts complex machine learning concepts into accessible APIs to facilitate rapid development and experimentation.

### Domain Concepts

- **Estimators:** Objects implementing `fit` and sometimes `predict` or `transform` methods, representing machine learning models or data preprocessors.
- **Supervised Learning:** Algorithms that learn from labeled data, such as classification and regression.
- **Unsupervised Learning:** Techniques like clustering and dimensionality reduction working on unlabeled data.
- **Model Selection:** Techniques such as cross-validation, grid search, and hyperparameter tuning.
- **Preprocessing:** Data transformation tools including scaling, encoding, normalization, and feature extraction.
- **Pipelines:** Sequential chains of transforms and estimators facilitating reproducibility and workflow simplification.

---

## Installation

scikit-learn requires Python (>=3.7). It is compatible across major platforms (Linux, macOS, Windows).

### Using pip

```bash
pip install scikit-learn
```

### Using conda

```bash
conda install scikit-learn
```

### Optional dependencies for enhanced performance

- `numpy`, `scipy`: Required dependencies.
- `joblib`: Used for parallel computing.
- `threadpoolctl`: Controls thread pools for underlying libraries.

---

## Usage and Examples

### Example 1: Simple Classification with Logistic Regression

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Instantiate model
model = LogisticRegression(max_iter=200)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
```

### Example 2: Data Preprocessing with a Pipeline

```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
X, y = load_iris(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Build pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2)),
    ('clf', LogisticRegression())
])

# Train
pipe.fit(X_train, y_train)

# Predict and evaluate
print("Test score:", pipe.score(X_test, y_test))
```

### Example 3: Model Selection with Grid Search

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

scikit-learn’s API is centered around a consistent interface of classes and functions.

### Estimators

- `fit(X, y=None)`: Fit the model or transformer with training data X and target y.
- `predict(X)`: Predict target for samples in X (supervised learners).
- `transform(X)`: Transform samples X (transformers).
- `fit_transform(X, y=None)`: Fit to data and transform it in one step when applicable.

### Core Modules and Classes

#### Datasets

- `load_iris()`, `load_diabetes()`, `load_boston()`, etc.: Load example datasets.
- `fetch_20newsgroups()`, `fetch_openml()`: Download large datasets.

#### Supervised Learning Algorithms

- `linear_model.LogisticRegression`: Logistic regression classifier.
- `svm.SVC`: Support Vector Classification.
- `tree.DecisionTreeClassifier`: Decision tree classifier.
- `ensemble.RandomForestClassifier`: Ensemble of decision trees.

#### Unsupervised Learning Algorithms

- `cluster.KMeans`: K-means clustering.
- `decomposition.PCA`: Principal Component Analysis.

#### Model Selection and Evaluation

- `model_selection.train_test_split`: Split data into training and test sets.
- `model_selection.GridSearchCV`: Exhaustive search over specified parameter values.
- `metrics.accuracy_score`: Classification accuracy metric.
- `metrics.mean_squared_error`: Regression error metric.

#### Preprocessing

- `preprocessing.StandardScaler`: Standardize features.
- `preprocessing.OneHotEncoder`: Encode categorical features.
- `feature_extraction.text.TfidfVectorizer`: Convert a collection of raw documents to a matrix of TF-IDF features.

#### Pipelines and Utilities

- `pipeline.Pipeline`: To chain transformers and estimators.
- `joblib.Parallel`: Parallel computing support.
- `utils.validation.check_array`: Input validation helper.

---

## Contributing

scikit-learn is an open-source project that welcomes contributions:

- Fork the repository and clone it locally.
- Follow the contribution guidelines in CONTRIBUTING.md.
- Write clear, well-documented code with accompanying tests.
- Run the test suite using `pytest` before submitting PRs.
- Use the issue tracker to report bugs and request features.
- Join the community mailing list and developer meetings for discussion.

For more detailed guidelines, visit the [scikit-learn contributing page](https://scikit-learn.org/stable/developers/contributing.html).

---

## License

scikit-learn is distributed under the BSD 3-Clause License. See the [LICENSE](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING) file for details.

---

## Contact

- Official website: [https://scikit-learn.org](https://scikit-learn.org)
- Source code and issues: [https://github.com/scikit-learn/scikit-learn](https://github.com/scikit-learn/scikit-learn)
- Mailing list: user@scikit-learn.org
- Developer resources and community: [https://scikit-learn.org/stable/developers/index.html](https://scikit-learn.org/stable/developers/index.html)
