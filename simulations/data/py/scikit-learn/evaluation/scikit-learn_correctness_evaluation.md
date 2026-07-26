# Correctness Evaluation — scikit-learn (README-Gen)

Tool: README-Gen (structured ATRAK-grounded prompting, `gpt-4.1-mini-2025-04-14`)
READMEs evaluated (in order): `data1.md`, `data2.md`, `data3.md`
Project column value: `scikit-learn`

## Environment & Cross-Checked Sources

- **Isolated venv (pip path):** `python3 -m venv /tmp/eval-sklearn-venv` — Python 3.14.6.
  `pip install scikit-learn` → installed **scikit-learn 1.9.0** (deps: joblib 1.5.3,
  narwhals 2.24.0, numpy 2.5.1, scipy 1.18.0, threadpoolctl 3.6.0).
- **Isolated venv (source build):** `python3 -m venv /tmp/eval-sklearn-src-venv`;
  `git clone --depth 1 https://github.com/scikit-learn/scikit-learn.git` then
  `pip install .` → built and installed **scikit-learn 1.10.dev0** in 73 s
  (well under the 20-min cap), exit 0.
- **Authoritative metadata (installed artifact):**
  `pip show scikit-learn` / dist-info METADATA → `Requires-Python: >=3.11`.
- **Repository ground truth:** `pyproject.toml` → `requires-python = ">=3.11"`;
  `COPYING` → `BSD 3-Clause License`.
- **Installed-artifact introspection:** `inspect.signature` on every documented API
  element (see API tables); `hasattr` checks on `BaseEstimator`.
- **Official docs:** https://scikit-learn.org/stable/ — in particular
  `modules/generated/sklearn.base.BaseEstimator.html` (methods listed:
  `get_metadata_routing`, `get_params`, `set_params` only — no `fit`/`predict`/
  `transform`/`score`), plus the API index confirming the existence of every other
  documented element.
- conda was **not available** in the sandbox; `conda install scikit-learn` is a valid,
  standard conda-forge command and is treated as correct (documentation defect not
  found), with the sandbox limitation recorded.

Snippet execution note (applies to all three files): the rubric requires each snippet
to run **independently in a clean environment**, with *adding missing imports the only
permitted intervention*. Snippets that reference variables defined in a **previous**
snippet (e.g. `X_train`, `X`, `y`) or a class imported in a previous snippet (e.g.
`SVC` in `data3.md` S3) cannot be made to run by adding imports alone; supplying those
variables is a disallowed manual modification. Such snippets fail U1/U4. For
transparency, all three sections **do** run end-to-end when concatenated in order
(verified), but that is not the scored condition.

---

## README 1 — `data1.md`

### Project Title (T)
| Rule | Verdict | Evidence |
|---|---|---|
| T1 title matches repo/official name | 1 | Title `scikit-learn` == repo name. |
| T2 not a different project | 1 | Describes scikit-learn. |
| T3 no hallucinated terminology | 1 | No invented terms. |

**T = 3/3 = 100.00**

### Overview (O)
| Rule | Verdict | Evidence |
|---|---|---|
| O1 primary functionality correct | 1 | "open-source Python library for machine learning … tools for data mining and data analysis". |
| O2 supported by artifacts | 1 | sklearn ships supervised/unsupervised estimators, model selection, preprocessing, pipelines. |
| O3 no unsupported features | 1 | No fabricated features. |
| O4 correct domain | 1 | Machine learning / data analysis. |
| O5 terminology matches repo | 1 | supervised/unsupervised learning, model selection, preprocessing, pipelines, ensemble, metrics. |

**O = 5/5 = 100.00**

### Installation (I) — executed
Documented paths: `pip install scikit-learn`; `conda install scikit-learn`.
Prerequisites: Python (>=3.7), NumPy, SciPy (pandas/matplotlib mentioned as optional).

| Rule | Verdict | Evidence |
|---|---|---|
| I1 all required deps declared | 0 | Declares only NumPy, SciPy. Hard runtime deps **joblib** and **threadpoolctl** are not declared (installed-artifact `Requires: joblib, narwhals, numpy, scipy, threadpoolctl`). |
| I2 commands execute w/o modification | 1 | `pip install scikit-learn` → exit 0 (1.9.0). `conda install scikit-learn` is a valid standard command (conda unavailable in sandbox; no documentation defect). |
| I3 no unresolved dependency errors | 1 | pip resolved all deps cleanly. |
| I4 documented env requirements correct | 0 | Claims Python **>=3.7**; authoritative `Requires-Python` = **>=3.11** (METADATA + repo pyproject.toml). Version claim is incorrect. |
| I5 produces expected artifact | 1 | `import sklearn` works post-install; library artifact produced. |

**I = 3/5 = 60.00**

### Usage and Examples (U) — executed (k = 3)
| # | Snippet | Executes (only imports added) | Output match | Runtime exc. | Matches text | E_i |
|---|---|---|---|---|---|---|
| S1 | Basic Classification (iris + StandardScaler + SVC linear) | Yes (self-contained) | No specific output documented; prints classification_report (acc ≈ 0.98) | None | Yes | **1** |
| S2 | Pipeline (StandardScaler+PCA+LogisticRegression) | No — `NameError: name 'X_train' is not defined` | n/a | Yes | n/a | **0** |
| S3 | GridSearchCV over SVC | No — `NameError: name 'X_train' is not defined` | n/a | Yes | n/a | **0** |

**U = 1/3 = 33.33**

### API Reference (A) — 11 elements, validated by `inspect.signature` + official docs
| # | Element | A1 exists | A2 names | A3 types | A4 returns | A5 behavior | A6 not deprecated | A_i |
|---|---|---|---|---|---|---|---|---|
| 1 | `sklearn.svm.SVC(kernel, C, …)` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | `sklearn.ensemble.RandomForestClassifier(n_estimators, …)` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | `sklearn.linear_model.LogisticRegression(solver, …)` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 4 | `sklearn.cluster.KMeans(n_clusters=8, …)` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 5 | `sklearn.decomposition.PCA(n_components, …)` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 6 | `sklearn.model_selection.train_test_split(*arrays, test_size, …)` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 7 | `sklearn.model_selection.GridSearchCV(estimator, param_grid, …)` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 8 | `sklearn.metrics.classification_report(y_true, y_pred, …)` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 9 | `sklearn.preprocessing.StandardScaler()` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 10 | `sklearn.preprocessing.OneHotEncoder()` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 11 | `sklearn.pipeline.Pipeline(steps, …)` | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

Verified signatures (installed 1.9.0), e.g. `SVC(*, C=1.0, kernel='rbf', …)`,
`RandomForestClassifier(n_estimators=100, *, …)`, `KMeans(n_clusters=8, *, …)`,
`PCA(n_components=None, *, …)`, `train_test_split(*arrays, test_size=None, …)`,
`GridSearchCV(estimator, param_grid, *, …)`. All names/types/behaviors match; none deprecated.

**A = 11/11 = 100.00**

### License (L)
| Rule | Verdict | Evidence |
|---|---|---|
| L1 matches repo LICENSE | 1 | README: "BSD 3-Clause"; repo `COPYING` = "BSD 3-Clause License". |
| L2 valid identifier | 1 | BSD-3-Clause is a valid SPDX id. |
| L3 no conflicting info | 1 | Single consistent statement. |

**L = 3/3 = 100.00**

### C_R (data1) = (100 + 100 + 60 + 33.33 + 100 + 100) / 6 = **82.22**

---

## README 2 — `data2.md`

### Project Title (T)
Matches repo name; not a different project; no hallucinated terms. **T = 100.00**

### Overview (O)
Accurately describes scikit-learn as an open-source Python ML library built on
NumPy/SciPy/matplotlib, covering supervised/unsupervised learning and model evaluation;
domain and terminology correct. **O = 5/5 = 100.00**

### Installation (I) — executed
Documented paths: `pip install scikit-learn`; `conda install scikit-learn`.
Prerequisites: Python (>=3.7), NumPy, SciPy, **Joblib, Threadpoolctl**.

| Rule | Verdict | Evidence |
|---|---|---|
| I1 all required deps declared | 1 | Declares NumPy, SciPy, Joblib, Threadpoolctl — all hard runtime deps (narwhals is a very recent 1.9.0 addition and not penalized). |
| I2 commands execute w/o modification | 1 | `pip install scikit-learn` → exit 0; conda command valid. |
| I3 no unresolved dependency errors | 1 | pip resolved cleanly. |
| I4 documented env requirements correct | 0 | Claims Python **>=3.7**; authoritative `Requires-Python` = **>=3.11**. Incorrect. |
| I5 produces expected artifact | 1 | `import sklearn` works. |

**I = 4/5 = 80.00**

### Usage and Examples (U) — executed (k = 3)
| # | Snippet | Executes (only imports added) | Output match | Runtime exc. | Matches text | E_i |
|---|---|---|---|---|---|---|
| S1 | Basic Classification (SVC linear, C=1.0) | Yes (self-contained) | No specific output documented; prints report (acc ≈ 0.98) | None | Yes | **1** |
| S2 | Pipeline (StandardScaler+PCA+SVC rbf) | No — `NameError: name 'X_train' is not defined` | n/a | Yes | n/a | **0** |
| S3 | `cross_val_score` (RandomForest) | No — `NameError: name 'X' is not defined` | n/a | Yes | n/a | **0** |

**U = 1/3 = 33.33**

### API Reference (A) — 7 elements
| # | Element | Verdict | Evidence |
|---|---|---|---|
| 1 | `sklearn.base.BaseEstimator` (docs `fit`, `predict`, `transform`, `fit_transform`, `score`) | **0** | `BaseEstimator` does NOT implement `fit`/`predict`/`transform`/`fit_transform`/`score` (verified `hasattr(...)==False`; official docs list only `get_metadata_routing`, `get_params`, `set_params`). A2/A5 fail. |
| 2 | `sklearn.preprocessing.StandardScaler` (copy, with_mean, with_std) | 1 | Signature `StandardScaler(*, copy=True, with_mean=True, with_std=True)` matches (bool params). |
| 3 | `sklearn.svm.SVC` (kernel, C, gamma) | 1 | Params exist with correct types. |
| 4 | `sklearn.pipeline.Pipeline` (named steps; fit/predict/transform) | 1 | Correct. |
| 5 | `sklearn.model_selection.train_test_split` (test_size, train_size, random_state) | 1 | Signature matches. |
| 6 | `sklearn.model_selection.cross_val_score` (estimator, X, y, cv) | 1 | Signature `cross_val_score(estimator, X, y=None, *, cv=None, …)` matches. |
| 7 | `sklearn.metrics.classification_report` (y_true, y_pred, target_names) | 1 | Signature matches; returns text report. |

**A = 6/7 = 85.71**

### License (L)
BSD 3-Clause; matches `COPYING`; valid id; no conflict. **L = 100.00**

### C_R (data2) = (100 + 100 + 80 + 33.33 + 85.71 + 100) / 6 = **83.17**

---

## README 3 — `data3.md`

### Project Title (T)
Matches repo name; not a different project; no hallucinated terms. **T = 100.00**

### Overview (O)
Accurately describes scikit-learn as an open-source Python ML library built on
NumPy/SciPy/matplotlib, covering classification, regression, clustering, dimensionality
reduction, model selection, preprocessing; domain and terminology correct.
**O = 5/5 = 100.00**

### Installation (I) — executed
Documented paths: `pip install scikit-learn`; **From Source** (`git clone …` + `cd` +
`pip install .`). Prerequisites: Python (>=3.7), NumPy, SciPy, **Joblib, Threadpoolctl**.

| Rule | Verdict | Evidence |
|---|---|---|
| I1 all required deps declared | 1 | Declares NumPy, SciPy, Joblib, Threadpoolctl. |
| I2 commands execute w/o modification | 1 | `pip install scikit-learn` → exit 0; source build `git clone --depth 1 …` + `pip install .` → exit 0 (built 1.10.dev0 in 73 s). |
| I3 no unresolved dependency errors | 1 | Both paths resolved cleanly. |
| I4 documented env requirements correct | 0 | Claims Python **>=3.7**; authoritative `Requires-Python` = **>=3.11**. Incorrect. |
| I5 produces expected artifact | 1 | `import sklearn` works from both pip and source-built artifact. |

**I = 4/5 = 80.00**

### Usage and Examples (U) — executed (k = 3)
| # | Snippet | Executes (only imports added) | Output match | Runtime exc. | Matches text | E_i |
|---|---|---|---|---|---|---|
| S1 | RandomForest on iris + accuracy_score | Yes (self-contained) | Prints `Accuracy: 1.00` (seeded, random_state=42; deterministic) | None | Yes | **1** |
| S2 | Pipeline (StandardScaler+SVC linear) | No — `NameError: name 'X_train' is not defined` | n/a | Yes | n/a | **0** |
| S3 | GridSearchCV over SVC | No — `NameError: name 'SVC' is not defined` (and `X_train` undefined) | n/a | Yes | n/a | **0** |

S1 note: `random_state=42` on both the split and the classifier makes the run
deterministic; observed `Accuracy: 1.00` matches the documented "Accuracy: {…}" format.

**U = 1/3 = 33.33**

### API Reference (A) — 7 elements
| # | Element | Verdict | Evidence |
|---|---|---|---|
| 1 | `sklearn.base.BaseEstimator` (docs `fit`, `predict`, `transform`, `fit_transform`) | **0** | Same as data2: `BaseEstimator` does not implement these methods (verified). A2/A5 fail. |
| 2 | `sklearn.ensemble.RandomForestClassifier` (n_estimators int, random_state int; fit/predict/predict_proba) | 1 | Signature matches; `predict_proba` exists (`hasattr==True`). |
| 3 | `sklearn.svm.SVC` (C float, kernel str; fit/predict/decision_function) | 1 | Matches; `decision_function` exists. |
| 4 | `sklearn.pipeline.Pipeline` (steps list; fit/predict/transform/fit_transform) | 1 | Matches. |
| 5 | `sklearn.model_selection.GridSearchCV` (estimator, param_grid, cv; best_params_/best_score_) | 1 | Matches. |
| 6 | `sklearn.datasets.load_iris()` | 1 | Exists (`load_iris(*, return_X_y=False, as_frame=False)`). |
| 7 | `sklearn.metrics.accuracy_score(y_true, y_pred)` | 1 | Matches. |

**A = 6/7 = 85.71**

### License (L)
BSD 3-Clause; matches `COPYING`; valid id; no conflict. **L = 100.00**

### C_R (data3) = (100 + 100 + 80 + 33.33 + 85.71 + 100) / 6 = **83.17**

---

## Section-score summary

| README | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| data1.md | 100.00 | 100.00 | 60.00 | 33.33 | 100.00 | 100.00 | 82.22 |
| data2.md | 100.00 | 100.00 | 80.00 | 33.33 | 85.71 | 100.00 | 83.17 |
| data3.md | 100.00 | 100.00 | 80.00 | 33.33 | 85.71 | 100.00 | 83.17 |
| **average** | 100.00 | 100.00 | 73.33 | 33.33 | 90.48 | 100.00 | **82.86** |

Consistency check: mean of the three C_R (82.22, 83.17, 83.17) = 82.86, and
(100+100+73.33+33.33+90.48+100)/6 = 82.86. ✓
