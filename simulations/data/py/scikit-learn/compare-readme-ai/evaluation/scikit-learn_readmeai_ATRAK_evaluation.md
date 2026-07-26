# ATRAK Evaluation — scikit-learn (README-AI)

Dimension 3 — Adherence to the Theory of Robust API Knowledge (Thayer et al. 2021).
**Presence, not correctness.** Absent (0) only when the carrying section is empty/missing,
a bare name-only list, or solely unresolved template placeholders.

README: `compare-readme-ai/scikit_readme_readmeai.md`. Project column: `scikit-learn`.

## Ground Truth Reference

- **Project:** scikit-learn
- **Repository:** https://github.com/scikit-learn/scikit-learn
- **Domain:** Machine learning library for Python.
- **Core domain entities:** estimators, transformers, classifiers/regressors, clustering,
  dimensionality reduction, pipelines, model selection/cross-validation, preprocessing,
  metrics, datasets.
- **Core execution facts:** pip/conda install; runtime deps numpy, scipy, joblib,
  threadpoolctl (narwhals in 1.9.0+); `Requires-Python >=3.11`; estimators expose
  `fit`/`predict`/`transform`.
- **Core usage patterns:** load data → split → fit → predict → evaluate; pipelines; CV.

---

## Per-element verdicts

| Element | Verdict | Evidence |
|---|---|---|
| **K_D Domain Concepts** | **1 (present)** | The **Features** table describes domain/algorithm concepts with explanations, not bare names: "Core Algorithms — classification, regression, clustering … k-means, hierarchical clustering, decision trees, SVM", "Data Structures — nearest neighbor search, trees, graph algorithms", "OpenMP & Parallelism", "Performance Optimization via Cython". These are evaluable descriptions of what the software represents. |
| **K_E Execution Facts** | **1 (present)** | Getting Started provides execution/runtime facts: Prerequisites ("Python; Conda, Pip"), Installation commands (`git clone`, `cd`, `conda env create -f …`, `pip install -r …`), Testing (`pytest`), dependency-management and build-system rows in Features (`pyproject.toml`, environment lock files). (Correctness of these — e.g. malformed commands — is penalized only under the correctness dimension.) |
| **K_U Usage Patterns** | **0 (absent)** | The only candidate carrier is the `Usage` section, whose entire content is unresolved template placeholders (`conda activate {venv}`, `python {entrypoint}`); `Testing` likewise uses `{__test_framework__}`/`{venv}`. There are no scikit-learn usage examples/tutorials demonstrating how the library is applied. Per the ATRAK absent criterion (content consisting solely of unresolved template placeholders), K_U is absent. |

**K = (1 + 1 + 0)/3 × 100 = 66.67**

---

## Summary

| README | domain_concepts | execution_facts | usage_patterns | atrak_score |
|---|---|---|---|---|
| scikit_readme_readmeai.md | 1 | 1 | 0 | 66.67 |
| **average** | 1 | 1 | 0 | **66.67** |

Single README → average row equals the README row.
