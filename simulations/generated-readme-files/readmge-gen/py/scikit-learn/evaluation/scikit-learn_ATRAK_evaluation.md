# ATRAK Evaluation — scikit-learn (README-Gen)

Dimension 3 — Adherence to the Theory of Robust API Knowledge (Thayer et al. 2021).
**Presence, not correctness**: content that is factually wrong still counts as present.
An element is absent (0) only when the carrying section is empty/missing, is a bare
name-only list, or consists solely of unresolved template placeholders.

READMEs (in order): `data1.md`, `data2.md`, `data3.md`. Project column: `scikit-learn`.

## Ground Truth Reference

- **Project:** scikit-learn
- **Repository:** https://github.com/scikit-learn/scikit-learn
- **Domain:** Machine learning library for Python (data mining / data analysis).
- **Core domain entities:** estimators, transformers, predictors, classifiers/regressors,
  clustering, dimensionality reduction, pipelines, model selection / cross-validation,
  preprocessing, metrics, datasets.
- **Core execution facts:** Python library installed via pip/conda (`pip install
  scikit-learn`); runtime deps numpy, scipy, joblib, threadpoolctl (narwhals in 1.9.0+);
  `Requires-Python >=3.11`; estimators expose `fit`/`predict`/`transform`; returns arrays,
  scores, reports.
- **Core usage patterns:** load dataset → `train_test_split` → scale → fit an estimator →
  predict → evaluate; pipelines; grid search / cross-validation.

---

## README 1 — `data1.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1 (present)** | "Domain Concepts" section defines Supervised/Unsupervised Learning, Model Selection, Preprocessing, Pipelines & Feature Unions, Ensemble Methods, Metrics & Evaluation — each with an explanatory definition (not a bare name list). |
| **K_E Execution Facts** | **1 (present)** | Installation (pip/conda), prerequisites (Python version, NumPy, SciPy), platform support; API Reference lists parameters, types, and methods (`fit`, `predict`, `transform`) — runtime/dependency/config facts. |
| **K_U Usage Patterns** | **1 (present)** | Three runnable code examples (classification, pipeline, grid search) with what/how narrative. |

**K = (1+1+1)/3 × 100 = 100.00**

## README 2 — `data2.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1 (present)** | Defines Estimators, Transformers, Predictors, Pipelines, Cross-validation, Model Selection/Hyperparameter tuning, Metrics, Datasets — with descriptions. |
| **K_E Execution Facts** | **1 (present)** | Installation, prerequisites (incl. Joblib, Threadpoolctl), platform support; API Reference documents parameters, return values, methods. |
| **K_U Usage Patterns** | **1 (present)** | Classification, pipeline, and cross-validation code examples with narrative. |

**K = 100.00**

## README 3 — `data3.md`

| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1 (present)** | Defines Estimators, Transformers, Classifiers/Regressors, Pipelines, Model Evaluation & Selection, Datasets — with descriptions. |
| **K_E Execution Facts** | **1 (present)** | Installation (pip + from source), prerequisites, platform support; API Reference with parameters/types/methods. |
| **K_U Usage Patterns** | **1 (present)** | RandomForest training, preprocessing pipeline, and grid-search cross-validation examples with narrative. |

**K = 100.00**

---

## Summary

| README | domain_concepts | execution_facts | usage_patterns | atrak_score |
|---|---|---|---|---|
| data1.md | 1 | 1 | 1 | 100.00 |
| data2.md | 1 | 1 | 1 | 100.00 |
| data3.md | 1 | 1 | 1 | 100.00 |
| **average** | 1 | 1 | 1 | **100.00** |

All three READMEs carry substantive, defined content for every ATRAK element.
(Correctness issues such as the incorrect `BaseEstimator` methods and the wrong Python
version are penalized only under the correctness dimension, not here.)
