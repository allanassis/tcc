<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# SCIKIT-LEARN

<em></em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/scikit-learn/scikit-learn?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/scikit-learn/scikit-learn?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/scikit-learn/scikit-learn?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/scikit-learn/scikit-learn?style=default&color=0080ff" alt="repo-language-count">

<!-- default option, no dependency badges. -->


<!-- default option, no dependency badges. -->

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview



---

## Features

<code>❯ REPLACE-ME</code>

---

## Project Structure

```sh
└── scikit-learn/
    ├── .github
    │   ├── FUNDING.yml
    │   ├── ISSUE_TEMPLATE
    │   ├── PULL_REQUEST_TEMPLATE.md
    │   ├── dependabot.yml
    │   ├── labeler-file-extensions.yml
    │   ├── labeler-module.yml
    │   ├── scripts
    │   └── workflows
    ├── AGENTS.md
    ├── CITATION.cff
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── COPYING
    ├── Makefile
    ├── README.rst
    ├── SECURITY.md
    ├── asv_benchmarks
    │   ├── .gitignore
    │   ├── asv.conf.json
    │   └── benchmarks
    ├── benchmarks
    │   ├── .gitignore
    │   ├── bench_20newsgroups.py
    │   ├── bench_covertype.py
    │   ├── bench_feature_expansions.py
    │   ├── bench_glm.py
    │   ├── bench_glmnet.py
    │   ├── bench_hist_gradient_boosting.py
    │   ├── bench_hist_gradient_boosting_adult.py
    │   ├── bench_hist_gradient_boosting_categorical_only.py
    │   ├── bench_hist_gradient_boosting_higgsboson.py
    │   ├── bench_hist_gradient_boosting_threading.py
    │   ├── bench_isolation_forest.py
    │   ├── bench_isolation_forest_predict.py
    │   ├── bench_isotonic.py
    │   ├── bench_kernel_pca_solvers_time_vs_n_components.py
    │   ├── bench_kernel_pca_solvers_time_vs_n_samples.py
    │   ├── bench_lasso.py
    │   ├── bench_lof.py
    │   ├── bench_mnist.py
    │   ├── bench_online_ocsvm.py
    │   ├── bench_pca_solvers.py
    │   ├── bench_plot_fastkmeans.py
    │   ├── bench_plot_hierarchical.py
    │   ├── bench_plot_incremental_pca.py
    │   ├── bench_plot_lasso_path.py
    │   ├── bench_plot_neighbors.py
    │   ├── bench_plot_nmf.py
    │   ├── bench_plot_omp_lars.py
    │   ├── bench_plot_parallel_pairwise.py
    │   ├── bench_plot_polynomial_kernel_approximation.py
    │   ├── bench_plot_randomized_svd.py
    │   ├── bench_plot_svd.py
    │   ├── bench_plot_ward.py
    │   ├── bench_random_projections.py
    │   ├── bench_rcv1_logreg_convergence.py
    │   ├── bench_saga.py
    │   ├── bench_sample_without_replacement.py
    │   ├── bench_sgd_regression.py
    │   ├── bench_sparsify.py
    │   ├── bench_text_vectorizers.py
    │   ├── bench_tree.py
    │   ├── bench_tsne_mnist.py
    │   └── plot_tsne_mnist.py
    ├── build_tools
    │   ├── Makefile
    │   ├── check-meson-openmp-dependencies.py
    │   ├── circle
    │   ├── codespell_ignore_words.txt
    │   ├── generate_authors_table.py
    │   ├── get_comment.py
    │   ├── github
    │   ├── linting.sh
    │   ├── shared.sh
    │   ├── update_environments_and_lock_files.py
    │   └── wheels
    ├── doc
    │   ├── Makefile
    │   ├── README.md
    │   ├── about.rst
    │   ├── api
    │   ├── api_reference.py
    │   ├── binder
    │   ├── callbacks.rst
    │   ├── common_pitfalls.rst
    │   ├── communication_team.rst
    │   ├── communication_team_emeritus.rst
    │   ├── computing
    │   ├── computing.rst
    │   ├── conf.py
    │   ├── conftest.py
    │   ├── contributor_experience_team.rst
    │   ├── contributor_experience_team_emeritus.rst
    │   ├── css
    │   ├── data_interoperability.rst
    │   ├── data_transforms.rst
    │   ├── datasets
    │   ├── datasets.rst
    │   ├── developers
    │   ├── documentation_team.rst
    │   ├── faq.rst
    │   ├── getting_started.rst
    │   ├── glossary.rst
    │   ├── governance.rst
    │   ├── images
    │   ├── index.rst.template
    │   ├── inspection.rst
    │   ├── install.rst
    │   ├── install_instructions_conda.rst
    │   ├── institutional_support.rst
    │   ├── js
    │   ├── jupyter-lite.json
    │   ├── jupyter_lite_config.json
    │   ├── logos
    │   ├── machine_learning_map.rst
    │   ├── maintainers.rst
    │   ├── maintainers_emeritus.rst
    │   ├── make.bat
    │   ├── metadata_routing.rst
    │   ├── min_dependency_substitutions.rst.template
    │   ├── min_dependency_table.rst.template
    │   ├── model_persistence.rst
    │   ├── model_selection.rst
    │   ├── modules
    │   ├── presentations.rst
    │   ├── related_projects.rst
    │   ├── roadmap.rst
    │   ├── scss
    │   ├── sphinxext
    │   ├── supervised_learning.rst
    │   ├── support.rst
    │   ├── templates
    │   ├── testimonials
    │   ├── unsupervised_learning.rst
    │   ├── user_guide.rst
    │   ├── visualizations.rst
    │   ├── whats_new
    │   └── whats_new.rst
    ├── examples
    │   ├── README.txt
    │   ├── applications
    │   ├── bicluster
    │   ├── calibration
    │   ├── callbacks
    │   ├── classification
    │   ├── cluster
    │   ├── compose
    │   ├── covariance
    │   ├── cross_decomposition
    │   ├── datasets
    │   ├── decomposition
    │   ├── developing_estimators
    │   ├── ensemble
    │   ├── feature_selection
    │   ├── frozen
    │   ├── gaussian_process
    │   ├── impute
    │   ├── inspection
    │   ├── kernel_approximation
    │   ├── linear_model
    │   ├── manifold
    │   ├── miscellaneous
    │   ├── mixture
    │   ├── model_selection
    │   ├── multiclass
    │   ├── multioutput
    │   ├── neighbors
    │   ├── neural_networks
    │   ├── preprocessing
    │   ├── release_highlights
    │   ├── semi_supervised
    │   ├── svm
    │   ├── text
    │   └── tree
    ├── maint_tools
    │   ├── bump-dependencies-versions.py
    │   ├── check_xfailed_checks.py
    │   ├── sort_whats_new.py
    │   ├── update_tracking_issue.py
    │   ├── vendor_array_api_compat.sh
    │   ├── vendor_array_api_extra.sh
    │   └── whats_missing.sh
    ├── meson.build
    ├── pyproject.toml
    └── sklearn
        ├── __check_build
        ├── __init__.py
        ├── _build_utils
        ├── _config.py
        ├── _distributor_init.py
        ├── _isotonic.pyx
        ├── _loss
        ├── _min_dependencies.py
        ├── base.py
        ├── calibration.py
        ├── callback
        ├── cluster
        ├── compose
        ├── conftest.py
        ├── covariance
        ├── cross_decomposition
        ├── datasets
        ├── decomposition
        ├── discriminant_analysis.py
        ├── dummy.py
        ├── ensemble
        ├── exceptions.py
        ├── experimental
        ├── externals
        ├── feature_extraction
        ├── feature_selection
        ├── frozen
        ├── gaussian_process
        ├── impute
        ├── inspection
        ├── isotonic.py
        ├── kernel_approximation.py
        ├── kernel_ridge.py
        ├── linear_model
        ├── manifold
        ├── meson.build
        ├── metrics
        ├── mixture
        ├── model_selection
        ├── multiclass.py
        ├── multioutput.py
        ├── naive_bayes.py
        ├── neighbors
        ├── neural_network
        ├── pipeline.py
        ├── preprocessing
        ├── random_projection.py
        ├── semi_supervised
        ├── svm
        ├── tests
        ├── tree
        └── utils
```

### Project Index

<details open>
	<summary><b><code>SCIKIT-LEARN/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/CITATION.cff'>CITATION.cff</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/meson.build'>meson.build</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/COPYING'>COPYING</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/README.rst'>README.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- asv_benchmarks Submodule -->
	<details>
		<summary><b>asv_benchmarks</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ asv_benchmarks</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/asv.conf.json'>asv.conf.json</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- benchmarks Submodule -->
			<details>
				<summary><b>benchmarks</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ asv_benchmarks.benchmarks</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/metrics.py'>metrics.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/manifold.py'>manifold.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/config.json'>config.json</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/neighbors.py'>neighbors.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/model_selection.py'>model_selection.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/datasets.py'>datasets.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/linear_model.py'>linear_model.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/common.py'>common.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/utils.py'>utils.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/cluster.py'>cluster.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/ensemble.py'>ensemble.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/decomposition.py'>decomposition.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/asv_benchmarks/benchmarks/svm.py'>svm.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- sklearn Submodule -->
	<details>
		<summary><b>sklearn</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ sklearn</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/conftest.py'>conftest.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/multiclass.py'>multiclass.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/_isotonic.pyx'>_isotonic.pyx</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/kernel_approximation.py'>kernel_approximation.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/random_projection.py'>random_projection.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/isotonic.py'>isotonic.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/multioutput.py'>multioutput.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/kernel_ridge.py'>kernel_ridge.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/_distributor_init.py'>_distributor_init.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/_min_dependencies.py'>_min_dependencies.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/meson.build'>meson.build</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/naive_bayes.py'>naive_bayes.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/pipeline.py'>pipeline.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/discriminant_analysis.py'>discriminant_analysis.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/exceptions.py'>exceptions.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/_config.py'>_config.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/dummy.py'>dummy.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/base.py'>base.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/calibration.py'>calibration.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- tree Submodule -->
			<details>
				<summary><b>tree</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.tree</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_utils.pyx'>_utils.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_tree.pxd'>_tree.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_partitioner.pxd'>_partitioner.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_criterion.pyx'>_criterion.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_splitter.pyx'>_splitter.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_export.py'>_export.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_splitter.pxd'>_splitter.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_criterion.pxd'>_criterion.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_reingold_tilford.py'>_reingold_tilford.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_partitioner.pyx'>_partitioner.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_classes.py'>_classes.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_utils.pxd'>_utils.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_tree.pyx'>_tree.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- metrics Submodule -->
			<details>
				<summary><b>metrics</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.metrics</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_scorer.py'>_scorer.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_classification.py'>_classification.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_regression.py'>_regression.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_dist_metrics.pyx.tp'>_dist_metrics.pyx.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_dist_metrics.pxd.tp'>_dist_metrics.pxd.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/pairwise.py'>pairwise.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_ranking.py'>_ranking.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_fast.pyx'>_pairwise_fast.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- cluster Submodule -->
					<details>
						<summary><b>cluster</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.metrics.cluster</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/cluster/_expected_mutual_info_fast.pyx'>_expected_mutual_info_fast.pyx</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/cluster/_bicluster.py'>_bicluster.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/cluster/meson.build'>meson.build</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/cluster/_unsupervised.py'>_unsupervised.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/cluster/_supervised.py'>_supervised.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- _plot Submodule -->
					<details>
						<summary><b>_plot</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.metrics._plot</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_plot/regression.py'>regression.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_plot/det_curve.py'>det_curve.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_plot/precision_recall_curve.py'>precision_recall_curve.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_plot/roc_curve.py'>roc_curve.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_plot/confusion_matrix.py'>confusion_matrix.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- _pairwise_distances_reduction Submodule -->
					<details>
						<summary><b>_pairwise_distances_reduction</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.metrics._pairwise_distances_reduction</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_middle_term_computer.pyx.tp'>_middle_term_computer.pyx.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_middle_term_computer.pxd.tp'>_middle_term_computer.pxd.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_classmode.pxd'>_classmode.pxd</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_dispatcher.py'>_dispatcher.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_base.pyx.tp'>_base.pyx.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_base.pxd.tp'>_base.pxd.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/meson.build'>meson.build</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_datasets_pair.pyx.tp'>_datasets_pair.pyx.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_datasets_pair.pxd.tp'>_datasets_pair.pxd.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_argkmin_classmode.pyx.tp'>_argkmin_classmode.pyx.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_radius_neighbors_classmode.pyx.tp'>_radius_neighbors_classmode.pyx.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_argkmin.pxd.tp'>_argkmin.pxd.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_argkmin.pyx.tp'>_argkmin.pyx.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_radius_neighbors.pxd.tp'>_radius_neighbors.pxd.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/metrics/_pairwise_distances_reduction/_radius_neighbors.pyx.tp'>_radius_neighbors.pyx.tp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- ensemble Submodule -->
			<details>
				<summary><b>ensemble</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.ensemble</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_forest.py'>_forest.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_voting.py'>_voting.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_bootstrap.py'>_bootstrap.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_bagging.py'>_bagging.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_gb.py'>_gb.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_weight_boosting.py'>_weight_boosting.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_gradient_boosting.pyx'>_gradient_boosting.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_iforest.py'>_iforest.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_stacking.py'>_stacking.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- _hist_gradient_boosting Submodule -->
					<details>
						<summary><b>_hist_gradient_boosting</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.ensemble._hist_gradient_boosting</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/predictor.py'>predictor.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/binning.py'>binning.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/common.pxd'>common.pxd</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/_predictor.pyx'>_predictor.pyx</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/splitting.pyx'>splitting.pyx</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/histogram.pyx'>histogram.pyx</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/gradient_boosting.py'>gradient_boosting.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/meson.build'>meson.build</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/_gradient_boosting.pyx'>_gradient_boosting.pyx</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/grower.py'>grower.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/utils.py'>utils.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/_binning.pyx'>_binning.pyx</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/ensemble/_hist_gradient_boosting/common.pyx'>common.pyx</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- experimental Submodule -->
			<details>
				<summary><b>experimental</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.experimental</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/experimental/enable_hist_gradient_boosting.py'>enable_hist_gradient_boosting.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/experimental/enable_halving_search_cv.py'>enable_halving_search_cv.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/experimental/enable_iterative_imputer.py'>enable_iterative_imputer.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- cluster Submodule -->
			<details>
				<summary><b>cluster</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.cluster</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_agglomerative.py'>_agglomerative.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_hierarchical_fast.pxd'>_hierarchical_fast.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_optics.py'>_optics.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_dbscan.py'>_dbscan.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_bicluster.py'>_bicluster.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_k_means_common.pxd'>_k_means_common.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_feature_agglomeration.py'>_feature_agglomeration.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_dbscan_inner.pyx'>_dbscan_inner.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_k_means_elkan.pyx'>_k_means_elkan.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_kmeans.py'>_kmeans.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_spectral.py'>_spectral.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_k_means_minibatch.pyx'>_k_means_minibatch.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_bisect_k_means.py'>_bisect_k_means.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_affinity_propagation.py'>_affinity_propagation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_birch.py'>_birch.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_k_means_common.pyx'>_k_means_common.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_mean_shift.py'>_mean_shift.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_k_means_lloyd.pyx'>_k_means_lloyd.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_hierarchical_fast.pyx'>_hierarchical_fast.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- _hdbscan Submodule -->
					<details>
						<summary><b>_hdbscan</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.cluster._hdbscan</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_hdbscan/_tree.pxd'>_tree.pxd</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_hdbscan/_reachability.pyx'>_reachability.pyx</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_hdbscan/meson.build'>meson.build</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_hdbscan/hdbscan.py'>hdbscan.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_hdbscan/_linkage.pyx'>_linkage.pyx</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cluster/_hdbscan/_tree.pyx'>_tree.pyx</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- feature_extraction Submodule -->
			<details>
				<summary><b>feature_extraction</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.feature_extraction</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_extraction/_hashing_fast.pyx'>_hashing_fast.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_extraction/_hash.py'>_hash.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_extraction/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_extraction/_dict_vectorizer.py'>_dict_vectorizer.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_extraction/_stop_words.py'>_stop_words.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_extraction/text.py'>text.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_extraction/image.py'>image.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- __check_build Submodule -->
			<details>
				<summary><b>__check_build</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.__check_build</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/__check_build/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/__check_build/_check_build.pyx'>_check_build.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- _loss Submodule -->
			<details>
				<summary><b>_loss</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn._loss</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/_loss/link.py'>link.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/_loss/_loss.pyx.tp'>_loss.pyx.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/_loss/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/_loss/loss.py'>loss.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/_loss/_loss.pxd'>_loss.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- semi_supervised Submodule -->
			<details>
				<summary><b>semi_supervised</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.semi_supervised</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/semi_supervised/_label_propagation.py'>_label_propagation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/semi_supervised/_self_training.py'>_self_training.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- gaussian_process Submodule -->
			<details>
				<summary><b>gaussian_process</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.gaussian_process</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/gaussian_process/_gpc.py'>_gpc.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/gaussian_process/kernels.py'>kernels.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/gaussian_process/_gpr.py'>_gpr.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- compose Submodule -->
			<details>
				<summary><b>compose</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.compose</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/compose/_target.py'>_target.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/compose/_column_transformer.py'>_column_transformer.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- datasets Submodule -->
			<details>
				<summary><b>datasets</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.datasets</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_samples_generator.py'>_samples_generator.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_olivetti_faces.py'>_olivetti_faces.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_kddcup99.py'>_kddcup99.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_svmlight_format_fast.pyx'>_svmlight_format_fast.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_california_housing.py'>_california_housing.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_species_distributions.py'>_species_distributions.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_covtype.py'>_covtype.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_arff_parser.py'>_arff_parser.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_rcv1.py'>_rcv1.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_lfw.py'>_lfw.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_svmlight_format_io.py'>_svmlight_format_io.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_twenty_newsgroups.py'>_twenty_newsgroups.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/_openml.py'>_openml.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- images Submodule -->
					<details>
						<summary><b>images</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.datasets.images</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/images/README.txt'>README.txt</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- descr Submodule -->
					<details>
						<summary><b>descr</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.datasets.descr</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/olivetti_faces.rst'>olivetti_faces.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/diabetes.rst'>diabetes.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/digits.rst'>digits.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/rcv1.rst'>rcv1.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/twenty_newsgroups.rst'>twenty_newsgroups.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/breast_cancer.rst'>breast_cancer.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/species_distributions.rst'>species_distributions.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/iris.rst'>iris.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/kddcup99.rst'>kddcup99.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/lfw.rst'>lfw.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/california_housing.rst'>california_housing.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/linnerud.rst'>linnerud.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/covtype.rst'>covtype.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/descr/wine_data.rst'>wine_data.rst</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- externals Submodule -->
			<details>
				<summary><b>externals</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.externals</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/conftest.py'>conftest.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/_array_api_compat_vendor.py'>_array_api_compat_vendor.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/_arff.py'>_arff.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- array_api_compat Submodule -->
					<details>
						<summary><b>array_api_compat</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.externals.array_api_compat</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/_internal.py'>_internal.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/LICENSE'>LICENSE</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/py.typed'>py.typed</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
							<!-- dask Submodule -->
							<details>
								<summary><b>dask</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ sklearn.externals.array_api_compat.dask</b></code>
									<!-- array Submodule -->
									<details>
										<summary><b>array</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ sklearn.externals.array_api_compat.dask.array</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/dask/array/_info.py'>_info.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/dask/array/_aliases.py'>_aliases.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/dask/array/linalg.py'>linalg.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/dask/array/fft.py'>fft.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- cupy Submodule -->
							<details>
								<summary><b>cupy</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ sklearn.externals.array_api_compat.cupy</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/cupy/_typing.py'>_typing.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/cupy/_info.py'>_info.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/cupy/_aliases.py'>_aliases.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/cupy/linalg.py'>linalg.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/cupy/fft.py'>fft.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- torch Submodule -->
							<details>
								<summary><b>torch</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ sklearn.externals.array_api_compat.torch</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/torch/_typing.py'>_typing.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/torch/_info.py'>_info.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/torch/_aliases.py'>_aliases.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/torch/linalg.py'>linalg.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/torch/fft.py'>fft.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- numpy Submodule -->
							<details>
								<summary><b>numpy</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ sklearn.externals.array_api_compat.numpy</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/numpy/_typing.py'>_typing.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/numpy/_info.py'>_info.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/numpy/_aliases.py'>_aliases.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/numpy/linalg.py'>linalg.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/numpy/fft.py'>fft.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- common Submodule -->
							<details>
								<summary><b>common</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ sklearn.externals.array_api_compat.common</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/common/_fft.py'>_fft.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/common/_typing.py'>_typing.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/common/_linalg.py'>_linalg.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/common/_aliases.py'>_aliases.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_compat/common/_helpers.py'>_helpers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<!-- _scipy Submodule -->
					<details>
						<summary><b>_scipy</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.externals._scipy</b></code>
							<!-- sparse Submodule -->
							<details>
								<summary><b>sparse</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ sklearn.externals._scipy.sparse</b></code>
									<!-- csgraph Submodule -->
									<details>
										<summary><b>csgraph</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ sklearn.externals._scipy.sparse.csgraph</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/_scipy/sparse/csgraph/_laplacian.py'>_laplacian.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<!-- array_api_extra Submodule -->
					<details>
						<summary><b>array_api_extra</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.externals.array_api_extra</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/LICENSE'>LICENSE</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/py.typed'>py.typed</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/_delegation.py'>_delegation.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/testing.py'>testing.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
							<!-- _lib Submodule -->
							<details>
								<summary><b>_lib</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ sklearn.externals.array_api_extra._lib</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/_lib/_at.py'>_at.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/_lib/_lazy.py'>_lazy.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/_lib/_backends.py'>_backends.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/_lib/_testing.py'>_testing.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/_lib/_funcs.py'>_funcs.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- _utils Submodule -->
									<details>
										<summary><b>_utils</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ sklearn.externals.array_api_extra._lib._utils</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/_lib/_utils/_typing.py'>_typing.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/_lib/_utils/_compat.pyi'>_compat.pyi</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/_lib/_utils/_typing.pyi'>_typing.pyi</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/_lib/_utils/_compat.py'>_compat.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/array_api_extra/_lib/_utils/_helpers.py'>_helpers.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
						</blockquote>
					</details>
					<!-- _numpydoc Submodule -->
					<details>
						<summary><b>_numpydoc</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.externals._numpydoc</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/_numpydoc/docscrape.py'>docscrape.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- _packaging Submodule -->
					<details>
						<summary><b>_packaging</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.externals._packaging</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/_packaging/version.py'>version.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/externals/_packaging/_structures.py'>_structures.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- linear_model Submodule -->
			<details>
				<summary><b>linear_model</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.linear_model</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_quantile.py'>_quantile.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_least_angle.py'>_least_angle.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_sag_fast.pyx.tp'>_sag_fast.pyx.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_sag.py'>_sag.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_passive_aggressive.py'>_passive_aggressive.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_sgd_fast.pyx.tp'>_sgd_fast.pyx.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_logistic.py'>_logistic.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_omp.py'>_omp.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_perceptron.py'>_perceptron.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_cd_fast.pyx'>_cd_fast.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_theil_sen.py'>_theil_sen.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_linear_loss.py'>_linear_loss.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_coordinate_descent.py'>_coordinate_descent.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_ridge.py'>_ridge.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_stochastic_gradient.py'>_stochastic_gradient.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_huber.py'>_huber.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_bayes.py'>_bayes.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_ransac.py'>_ransac.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- _glm Submodule -->
					<details>
						<summary><b>_glm</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.linear_model._glm</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_glm/glm.py'>glm.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/linear_model/_glm/_newton_solver.py'>_newton_solver.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- impute Submodule -->
			<details>
				<summary><b>impute</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.impute</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/impute/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/impute/_knn.py'>_knn.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/impute/_iterative.py'>_iterative.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- utils Submodule -->
			<details>
				<summary><b>utils</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.utils</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/optimize.py'>optimize.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_bitset.pyx'>_bitset.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_missing.py'>_missing.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_arpack.py'>_arpack.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_heap.pxd'>_heap.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_dataframe.py'>_dataframe.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_chunking.py'>_chunking.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/fixes.py'>fixes.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/murmurhash.pyx'>murmurhash.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/sparsefuncs_fast.pyx'>sparsefuncs_fast.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_available_if.py'>_available_if.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/discovery.py'>discovery.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_user_interface.py'>_user_interface.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/deprecation.py'>deprecation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_random.pxd'>_random.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_array_api.py'>_array_api.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_openmp_helpers.pyx'>_openmp_helpers.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_sparse.py'>_sparse.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/estimator_checks.py'>estimator_checks.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/multiclass.py'>multiclass.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_typedefs.pxd'>_typedefs.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_response.py'>_response.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_sorting.pyx'>_sorting.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/graph.py'>graph.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_vector_sentinel.pxd'>_vector_sentinel.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_bunch.py'>_bunch.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_fast_dict.pyx'>_fast_dict.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_plotting.py'>_plotting.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_pprint.py'>_pprint.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_optional_dependencies.py'>_optional_dependencies.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/metadata_routing.py'>metadata_routing.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/random.py'>random.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_blas_int.pxi.in'>_blas_int.pxi.in</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_cython_blas.pyx'>_cython_blas.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_weight_vector.pxd.tp'>_weight_vector.pxd.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_cython_blas.pxd'>_cython_blas.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_mocking.py'>_mocking.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_fast_dict.pxd'>_fast_dict.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/arrayfuncs.pyx'>arrayfuncs.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_isfinite.pyx'>_isfinite.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_weight_vector.pyx.tp'>_weight_vector.pyx.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_vector_sentinel.pyx'>_vector_sentinel.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_unique.py'>_unique.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/stats.py'>stats.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_sorting.pxd'>_sorting.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_set_output.py'>_set_output.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/class_weight.py'>class_weight.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_typedefs.pyx'>_typedefs.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_random.pyx'>_random.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_openmp_helpers.pxd'>_openmp_helpers.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_show_versions.py'>_show_versions.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_metadata_requests.py'>_metadata_requests.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/metaestimators.py'>metaestimators.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_seq_dataset.pyx.tp'>_seq_dataset.pyx.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/murmurhash.pxd'>murmurhash.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_testing.py'>_testing.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/extmath.py'>extmath.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_encode.py'>_encode.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_seq_dataset.pxd.tp'>_seq_dataset.pxd.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/parallel.py'>parallel.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_heap.pyx'>_heap.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/sparsefuncs.py'>sparsefuncs.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_tags.py'>_tags.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_param_validation.py'>_param_validation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_mask.py'>_mask.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_indexing.py'>_indexing.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_bitset.pxd'>_bitset.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/validation.py'>validation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- _repr_html Submodule -->
					<details>
						<summary><b>_repr_html</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.utils._repr_html</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_repr_html/params.py'>params.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_repr_html/features.css'>features.css</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_repr_html/params.css'>params.css</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_repr_html/features.py'>features.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_repr_html/estimator.js'>estimator.js</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_repr_html/common.py'>common.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_repr_html/fitted_attributes.py'>fitted_attributes.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_repr_html/estimator.css'>estimator.css</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_repr_html/estimator.py'>estimator.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_repr_html/base.py'>base.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- _test_common Submodule -->
					<details>
						<summary><b>_test_common</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.utils._test_common</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/_test_common/instance_generator.py'>instance_generator.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
					<!-- src Submodule -->
					<details>
						<summary><b>src</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.utils.src</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/src/MurmurHash3.h'>MurmurHash3.h</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/utils/src/MurmurHash3.cpp'>MurmurHash3.cpp</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- covariance Submodule -->
			<details>
				<summary><b>covariance</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.covariance</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/covariance/_graph_lasso.py'>_graph_lasso.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/covariance/_empirical_covariance.py'>_empirical_covariance.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/covariance/_shrunk_covariance.py'>_shrunk_covariance.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/covariance/_elliptic_envelope.py'>_elliptic_envelope.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/covariance/_robust_covariance.py'>_robust_covariance.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- neural_network Submodule -->
			<details>
				<summary><b>neural_network</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.neural_network</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neural_network/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neural_network/_rbm.py'>_rbm.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neural_network/_stochastic_optimizers.py'>_stochastic_optimizers.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neural_network/_multilayer_perceptron.py'>_multilayer_perceptron.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- feature_selection Submodule -->
			<details>
				<summary><b>feature_selection</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.feature_selection</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_selection/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_selection/_variance_threshold.py'>_variance_threshold.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_selection/_rfe.py'>_rfe.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_selection/_from_model.py'>_from_model.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_selection/_mutual_info.py'>_mutual_info.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_selection/_univariate_selection.py'>_univariate_selection.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_selection/_sequential.py'>_sequential.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- inspection Submodule -->
			<details>
				<summary><b>inspection</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.inspection</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/inspection/_partial_dependence.py'>_partial_dependence.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/inspection/_permutation_importance.py'>_permutation_importance.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/inspection/_pd_utils.py'>_pd_utils.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- _plot Submodule -->
					<details>
						<summary><b>_plot</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.inspection._plot</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/inspection/_plot/decision_boundary.py'>decision_boundary.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/inspection/_plot/partial_dependence.py'>partial_dependence.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- svm Submodule -->
			<details>
				<summary><b>svm</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.svm</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/_bounds.py'>_bounds.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/_liblinear.pyx'>_liblinear.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/_libsvm.pxi'>_libsvm.pxi</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/_liblinear.pxi'>_liblinear.pxi</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/_libsvm.pyx'>_libsvm.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/_libsvm_sparse.pyx'>_libsvm_sparse.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/_newrand.pyx'>_newrand.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/_classes.py'>_classes.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- src Submodule -->
					<details>
						<summary><b>src</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ sklearn.svm.src</b></code>
							<!-- newrand Submodule -->
							<details>
								<summary><b>newrand</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ sklearn.svm.src.newrand</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/newrand/newrand.h'>newrand.h</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- liblinear Submodule -->
							<details>
								<summary><b>liblinear</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ sklearn.svm.src.liblinear</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/liblinear/linear.cpp'>linear.cpp</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/liblinear/linear.h'>linear.h</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/liblinear/liblinear_helper.c'>liblinear_helper.c</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/liblinear/COPYRIGHT'>COPYRIGHT</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/liblinear/_cython_blas_helpers.h'>_cython_blas_helpers.h</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/liblinear/tron.h'>tron.h</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/liblinear/tron.cpp'>tron.cpp</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- libsvm Submodule -->
							<details>
								<summary><b>libsvm</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ sklearn.svm.src.libsvm</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/libsvm/libsvm_sparse_helper.c'>libsvm_sparse_helper.c</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/libsvm/libsvm_template.cpp'>libsvm_template.cpp</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/libsvm/_svm_cython_blas_helpers.h'>_svm_cython_blas_helpers.h</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/libsvm/svm.h'>svm.h</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/libsvm/LIBSVM_CHANGES'>LIBSVM_CHANGES</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/libsvm/libsvm_helper.c'>libsvm_helper.c</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/svm/src/libsvm/svm.cpp'>svm.cpp</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- manifold Submodule -->
			<details>
				<summary><b>manifold</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.manifold</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/manifold/_utils.pyx'>_utils.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/manifold/_classical_mds.py'>_classical_mds.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/manifold/_locally_linear.py'>_locally_linear.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/manifold/_t_sne.py'>_t_sne.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/manifold/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/manifold/_isomap.py'>_isomap.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/manifold/_mds.py'>_mds.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/manifold/_barnes_hut_tsne.pyx'>_barnes_hut_tsne.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/manifold/_spectral_embedding.py'>_spectral_embedding.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- mixture Submodule -->
			<details>
				<summary><b>mixture</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.mixture</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/mixture/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/mixture/_bayesian_mixture.py'>_bayesian_mixture.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/mixture/_gaussian_mixture.py'>_gaussian_mixture.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- preprocessing Submodule -->
			<details>
				<summary><b>preprocessing</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.preprocessing</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/_data.py'>_data.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/_target_encoder.py'>_target_encoder.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/_encoders.py'>_encoders.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/_discretization.py'>_discretization.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/_polynomial.py'>_polynomial.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/_label.py'>_label.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/_target_encoder_fast.pyx'>_target_encoder_fast.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/_csr_polynomial_expansion.pyx'>_csr_polynomial_expansion.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/preprocessing/_function_transformer.py'>_function_transformer.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- callback Submodule -->
			<details>
				<summary><b>callback</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.callback</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/callback/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/callback/_callback_context.py'>_callback_context.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/callback/_transport.py'>_transport.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/callback/_callback_support.py'>_callback_support.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/callback/_progressbar.py'>_progressbar.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/callback/_scoring_monitor.py'>_scoring_monitor.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- frozen Submodule -->
			<details>
				<summary><b>frozen</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.frozen</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/frozen/_frozen.py'>_frozen.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- model_selection Submodule -->
			<details>
				<summary><b>model_selection</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.model_selection</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/model_selection/_search.py'>_search.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/model_selection/_classification_threshold.py'>_classification_threshold.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/model_selection/_validation.py'>_validation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/model_selection/_plot.py'>_plot.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/model_selection/_search_successive_halving.py'>_search_successive_halving.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/model_selection/_split.py'>_split.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- _build_utils Submodule -->
			<details>
				<summary><b>_build_utils</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn._build_utils</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/_build_utils/version.py'>version.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/_build_utils/tempita.py'>tempita.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- decomposition Submodule -->
			<details>
				<summary><b>decomposition</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.decomposition</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_factor_analysis.py'>_factor_analysis.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_nmf.py'>_nmf.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_sparse_pca.py'>_sparse_pca.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_kernel_pca.py'>_kernel_pca.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_incremental_pca.py'>_incremental_pca.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_fastica.py'>_fastica.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_pca.py'>_pca.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_truncated_svd.py'>_truncated_svd.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_cdnmf_fast.pyx'>_cdnmf_fast.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_dict_learning.py'>_dict_learning.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_lda.py'>_lda.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/_online_lda_fast.pyx'>_online_lda_fast.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- cross_decomposition Submodule -->
			<details>
				<summary><b>cross_decomposition</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.cross_decomposition</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/cross_decomposition/_pls.py'>_pls.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- neighbors Submodule -->
			<details>
				<summary><b>neighbors</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sklearn.neighbors</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_classification.py'>_classification.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_partition_nodes.pyx'>_partition_nodes.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_nca.py'>_nca.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_base.py'>_base.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_quad_tree.pyx'>_quad_tree.pyx</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_graph.py'>_graph.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_regression.py'>_regression.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_kd_tree.pyx.tp'>_kd_tree.pyx.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_binary_tree.pxi.tp'>_binary_tree.pxi.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_ball_tree.pyx.tp'>_ball_tree.pyx.tp</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/meson.build'>meson.build</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_nearest_centroid.py'>_nearest_centroid.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_unsupervised.py'>_unsupervised.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_kde.py'>_kde.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_lof.py'>_lof.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_quad_tree.pxd'>_quad_tree.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/neighbors/_partition_nodes.pxd'>_partition_nodes.pxd</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- maint_tools Submodule -->
	<details>
		<summary><b>maint_tools</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ maint_tools</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/maint_tools/vendor_array_api_extra.sh'>vendor_array_api_extra.sh</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/maint_tools/check_xfailed_checks.py'>check_xfailed_checks.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/maint_tools/whats_missing.sh'>whats_missing.sh</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/maint_tools/bump-dependencies-versions.py'>bump-dependencies-versions.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/maint_tools/sort_whats_new.py'>sort_whats_new.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/maint_tools/update_tracking_issue.py'>update_tracking_issue.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/maint_tools/vendor_array_api_compat.sh'>vendor_array_api_compat.sh</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- examples Submodule -->
	<details>
		<summary><b>examples</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ examples</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/README.txt'>README.txt</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- bicluster Submodule -->
			<details>
				<summary><b>bicluster</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.bicluster</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/bicluster/plot_bicluster_newsgroups.py'>plot_bicluster_newsgroups.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/bicluster/plot_spectral_biclustering.py'>plot_spectral_biclustering.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/bicluster/plot_spectral_coclustering.py'>plot_spectral_coclustering.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/bicluster/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- classification Submodule -->
			<details>
				<summary><b>classification</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.classification</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/classification/plot_classifier_comparison.py'>plot_classifier_comparison.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/classification/plot_lda.py'>plot_lda.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/classification/plot_lda_qda.py'>plot_lda_qda.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/classification/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/classification/plot_classification_probability.py'>plot_classification_probability.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/classification/plot_digits_classification.py'>plot_digits_classification.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- tree Submodule -->
			<details>
				<summary><b>tree</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.tree</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/tree/plot_unveil_tree_structure.py'>plot_unveil_tree_structure.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/tree/plot_cost_complexity_pruning.py'>plot_cost_complexity_pruning.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/tree/plot_iris_dtc.py'>plot_iris_dtc.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/tree/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/tree/plot_tree_regression.py'>plot_tree_regression.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- developing_estimators Submodule -->
			<details>
				<summary><b>developing_estimators</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.developing_estimators</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/developing_estimators/sklearn_is_fitted.py'>sklearn_is_fitted.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/developing_estimators/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- ensemble Submodule -->
			<details>
				<summary><b>ensemble</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.ensemble</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_hgbt_regression.py'>plot_hgbt_regression.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_forest_importances.py'>plot_forest_importances.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_gradient_boosting_categorical.py'>plot_gradient_boosting_categorical.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_adaboost_multiclass.py'>plot_adaboost_multiclass.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_adaboost_twoclass.py'>plot_adaboost_twoclass.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_ensemble_oob.py'>plot_ensemble_oob.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_adaboost_regression.py'>plot_adaboost_regression.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_monotonic_constraints.py'>plot_monotonic_constraints.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_stack_predictors.py'>plot_stack_predictors.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_gradient_boosting_oob.py'>plot_gradient_boosting_oob.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_gradient_boosting_regression.py'>plot_gradient_boosting_regression.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_isolation_forest.py'>plot_isolation_forest.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_bias_variance.py'>plot_bias_variance.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_forest_hist_grad_boosting_comparison.py'>plot_forest_hist_grad_boosting_comparison.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_feature_transformation.py'>plot_feature_transformation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_random_forest_embedding.py'>plot_random_forest_embedding.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_random_forest_regression_multioutput.py'>plot_random_forest_regression_multioutput.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_gradient_boosting_quantile.py'>plot_gradient_boosting_quantile.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_gradient_boosting_early_stopping.py'>plot_gradient_boosting_early_stopping.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_forest_iris.py'>plot_forest_iris.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_gradient_boosting_regularization.py'>plot_gradient_boosting_regularization.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_voting_decision_regions.py'>plot_voting_decision_regions.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/ensemble/plot_voting_regressor.py'>plot_voting_regressor.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- cluster Submodule -->
			<details>
				<summary><b>cluster</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.cluster</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_hdbscan.py'>plot_hdbscan.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_affinity_propagation.py'>plot_affinity_propagation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_bisect_kmeans.py'>plot_bisect_kmeans.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_inductive_clustering.py'>plot_inductive_clustering.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_feature_agglomeration_vs_univariate_selection.py'>plot_feature_agglomeration_vs_univariate_selection.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_digits_linkage.py'>plot_digits_linkage.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_linkage_comparison.py'>plot_linkage_comparison.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_kmeans_plusplus.py'>plot_kmeans_plusplus.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_cluster_comparison.py'>plot_cluster_comparison.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_digits_agglomeration.py'>plot_digits_agglomeration.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_birch_vs_minibatchkmeans.py'>plot_birch_vs_minibatchkmeans.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_agglomerative_clustering_metrics.py'>plot_agglomerative_clustering_metrics.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_adjusted_for_chance_measures.py'>plot_adjusted_for_chance_measures.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_segmentation_toy.py'>plot_segmentation_toy.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_mini_batch_kmeans.py'>plot_mini_batch_kmeans.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_mean_shift.py'>plot_mean_shift.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_dict_face_patches.py'>plot_dict_face_patches.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_coin_segmentation.py'>plot_coin_segmentation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_ward_structured_vs_unstructured.py'>plot_ward_structured_vs_unstructured.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_face_compress.py'>plot_face_compress.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_kmeans_silhouette_analysis.py'>plot_kmeans_silhouette_analysis.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_kmeans_stability_low_dim_dense.py'>plot_kmeans_stability_low_dim_dense.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_kmeans_digits.py'>plot_kmeans_digits.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_kmeans_assumptions.py'>plot_kmeans_assumptions.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_coin_ward_segmentation.py'>plot_coin_ward_segmentation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_dbscan.py'>plot_dbscan.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_agglomerative_dendrogram.py'>plot_agglomerative_dendrogram.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cluster/plot_optics.py'>plot_optics.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- semi_supervised Submodule -->
			<details>
				<summary><b>semi_supervised</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.semi_supervised</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/semi_supervised/plot_self_training_varying_threshold.py'>plot_self_training_varying_threshold.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/semi_supervised/plot_label_propagation_structure.py'>plot_label_propagation_structure.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/semi_supervised/plot_label_propagation_digits_active_learning.py'>plot_label_propagation_digits_active_learning.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/semi_supervised/plot_semi_supervised_newsgroups.py'>plot_semi_supervised_newsgroups.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/semi_supervised/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/semi_supervised/plot_semi_supervised_versus_svm_iris.py'>plot_semi_supervised_versus_svm_iris.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/semi_supervised/plot_label_propagation_digits.py'>plot_label_propagation_digits.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- kernel_approximation Submodule -->
			<details>
				<summary><b>kernel_approximation</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.kernel_approximation</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/kernel_approximation/plot_scalable_poly_kernels.py'>plot_scalable_poly_kernels.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/kernel_approximation/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- callbacks Submodule -->
			<details>
				<summary><b>callbacks</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.callbacks</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/callbacks/plot_scoring_monitor.py'>plot_scoring_monitor.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/callbacks/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- calibration Submodule -->
			<details>
				<summary><b>calibration</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.calibration</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/calibration/plot_calibration.py'>plot_calibration.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/calibration/plot_compare_calibration.py'>plot_compare_calibration.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/calibration/plot_calibration_curve.py'>plot_calibration_curve.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/calibration/plot_calibration_multiclass.py'>plot_calibration_multiclass.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/calibration/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- gaussian_process Submodule -->
			<details>
				<summary><b>gaussian_process</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.gaussian_process</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/gaussian_process/plot_compare_gpr_krr.py'>plot_compare_gpr_krr.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/gaussian_process/plot_gpr_prior_posterior.py'>plot_gpr_prior_posterior.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/gaussian_process/plot_gpc_xor.py'>plot_gpc_xor.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/gaussian_process/plot_gpc_isoprobability.py'>plot_gpc_isoprobability.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/gaussian_process/plot_gpr_noisy.py'>plot_gpr_noisy.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/gaussian_process/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/gaussian_process/plot_gpc.py'>plot_gpc.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/gaussian_process/plot_gpc_iris.py'>plot_gpc_iris.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/gaussian_process/plot_gpr_co2.py'>plot_gpr_co2.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/gaussian_process/plot_gpr_noisy_targets.py'>plot_gpr_noisy_targets.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/gaussian_process/plot_gpr_on_structured_data.py'>plot_gpr_on_structured_data.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- compose Submodule -->
			<details>
				<summary><b>compose</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.compose</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/compose/plot_digits_pipe.py'>plot_digits_pipe.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/compose/plot_feature_union.py'>plot_feature_union.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/compose/plot_column_transformer.py'>plot_column_transformer.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/compose/plot_transformed_target.py'>plot_transformed_target.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/compose/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/compose/plot_column_transformer_mixed_types.py'>plot_column_transformer_mixed_types.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/compose/plot_compare_reduction.py'>plot_compare_reduction.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- datasets Submodule -->
			<details>
				<summary><b>datasets</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.datasets</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/datasets/plot_random_multilabel_dataset.py'>plot_random_multilabel_dataset.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/datasets/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- linear_model Submodule -->
			<details>
				<summary><b>linear_model</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.linear_model</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_quantile_regression.py'>plot_quantile_regression.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_bayesian_ridge_curvefit.py'>plot_bayesian_ridge_curvefit.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_ransac.py'>plot_ransac.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_logistic_l1_l2_sparsity.py'>plot_logistic_l1_l2_sparsity.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_ridge_coeffs.py'>plot_ridge_coeffs.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_sgd_early_stopping.py'>plot_sgd_early_stopping.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_sgd_separating_hyperplane.py'>plot_sgd_separating_hyperplane.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_ols_ridge.py'>plot_ols_ridge.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_polynomial_interpolation.py'>plot_polynomial_interpolation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_huber_vs_ridge.py'>plot_huber_vs_ridge.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_logistic_path.py'>plot_logistic_path.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_sparse_logistic_regression_mnist.py'>plot_sparse_logistic_regression_mnist.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_ard.py'>plot_ard.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_sgdocsvm_vs_ocsvm.py'>plot_sgdocsvm_vs_ocsvm.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_tweedie_regression_insurance_claims.py'>plot_tweedie_regression_insurance_claims.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_lasso_model_selection.py'>plot_lasso_model_selection.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.py'>plot_elastic_net_precomputed_gram_matrix_with_weighted_samples.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_sgd_iris.py'>plot_sgd_iris.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_ridge_path.py'>plot_ridge_path.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_poisson_regression_non_normal_loss.py'>plot_poisson_regression_non_normal_loss.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_multi_task_lasso_support.py'>plot_multi_task_lasso_support.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_sgd_penalties.py'>plot_sgd_penalties.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_theilsen.py'>plot_theilsen.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_lasso_and_elasticnet.py'>plot_lasso_and_elasticnet.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_sgd_weighted_samples.py'>plot_sgd_weighted_samples.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.py'>plot_lasso_lasso_lars_elasticnet_path.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_lasso_dense_vs_sparse_data.py'>plot_lasso_dense_vs_sparse_data.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_logistic_multinomial.py'>plot_logistic_multinomial.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_lasso_lars_ic.py'>plot_lasso_lars_ic.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_sgd_loss_functions.py'>plot_sgd_loss_functions.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_omp.py'>plot_omp.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_sparse_logistic_regression_20newsgroups.py'>plot_sparse_logistic_regression_20newsgroups.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_robust_fit.py'>plot_robust_fit.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/linear_model/plot_nnls.py'>plot_nnls.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- impute Submodule -->
			<details>
				<summary><b>impute</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.impute</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/impute/plot_missing_values.py'>plot_missing_values.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/impute/plot_iterative_imputer_variants_comparison.py'>plot_iterative_imputer_variants_comparison.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/impute/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- covariance Submodule -->
			<details>
				<summary><b>covariance</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.covariance</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/covariance/plot_mahalanobis_distances.py'>plot_mahalanobis_distances.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/covariance/plot_robust_vs_empirical_covariance.py'>plot_robust_vs_empirical_covariance.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/covariance/plot_covariance_estimation.py'>plot_covariance_estimation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/covariance/plot_lw_vs_oas.py'>plot_lw_vs_oas.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/covariance/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/covariance/plot_sparse_cov.py'>plot_sparse_cov.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- multioutput Submodule -->
			<details>
				<summary><b>multioutput</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.multioutput</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/multioutput/plot_classifier_chain_yeast.py'>plot_classifier_chain_yeast.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/multioutput/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- miscellaneous Submodule -->
			<details>
				<summary><b>miscellaneous</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.miscellaneous</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_multilabel.py'>plot_multilabel.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_outlier_detection_bench.py'>plot_outlier_detection_bench.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_johnson_lindenstrauss_bound.py'>plot_johnson_lindenstrauss_bound.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_anomaly_comparison.py'>plot_anomaly_comparison.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_kernel_ridge_regression.py'>plot_kernel_ridge_regression.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_isotonic_regression.py'>plot_isotonic_regression.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_metadata_routing.py'>plot_metadata_routing.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_roc_curve_visualization_api.py'>plot_roc_curve_visualization_api.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_set_output.py'>plot_set_output.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_pipeline_display.py'>plot_pipeline_display.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_kernel_approximation.py'>plot_kernel_approximation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_display_object_visualization.py'>plot_display_object_visualization.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_multioutput_face_completion.py'>plot_multioutput_face_completion.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/miscellaneous/plot_estimator_representation.py'>plot_estimator_representation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- feature_selection Submodule -->
			<details>
				<summary><b>feature_selection</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.feature_selection</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/feature_selection/plot_rfe_with_cross_validation.py'>plot_rfe_with_cross_validation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/feature_selection/plot_rfe_digits.py'>plot_rfe_digits.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/feature_selection/plot_feature_selection.py'>plot_feature_selection.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/feature_selection/plot_select_from_model_diabetes.py'>plot_select_from_model_diabetes.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/feature_selection/plot_f_test_vs_mi.py'>plot_f_test_vs_mi.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/feature_selection/plot_feature_selection_pipeline.py'>plot_feature_selection_pipeline.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/feature_selection/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- inspection Submodule -->
			<details>
				<summary><b>inspection</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.inspection</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/inspection/plot_partial_dependence.py'>plot_partial_dependence.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/inspection/plot_causal_interpretation.py'>plot_causal_interpretation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/inspection/plot_partial_dependence_visualization_api.py'>plot_partial_dependence_visualization_api.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/inspection/plot_permutation_importance_multicollinear.py'>plot_permutation_importance_multicollinear.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/inspection/plot_permutation_importance.py'>plot_permutation_importance.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/inspection/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/inspection/plot_linear_model_coefficient_interpretation.py'>plot_linear_model_coefficient_interpretation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- svm Submodule -->
			<details>
				<summary><b>svm</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.svm</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_separating_hyperplane.py'>plot_separating_hyperplane.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_custom_kernel.py'>plot_custom_kernel.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_svm_margin.py'>plot_svm_margin.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_iris_svc.py'>plot_iris_svc.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_svm_anova.py'>plot_svm_anova.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_rbf_parameters.py'>plot_rbf_parameters.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_separating_hyperplane_unbalanced.py'>plot_separating_hyperplane_unbalanced.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_oneclass.py'>plot_oneclass.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_svm_scale_c.py'>plot_svm_scale_c.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_svm_tie_breaking.py'>plot_svm_tie_breaking.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_svm_kernels.py'>plot_svm_kernels.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_svm_regression.py'>plot_svm_regression.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_linearsvc_support_vectors.py'>plot_linearsvc_support_vectors.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/svm/plot_weighted_samples.py'>plot_weighted_samples.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- manifold Submodule -->
			<details>
				<summary><b>manifold</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.manifold</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/manifold/plot_mds.py'>plot_mds.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/manifold/plot_compare_methods.py'>plot_compare_methods.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/manifold/plot_lle_digits.py'>plot_lle_digits.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/manifold/plot_manifold_sphere.py'>plot_manifold_sphere.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/manifold/plot_swissroll.py'>plot_swissroll.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/manifold/plot_t_sne_perplexity.py'>plot_t_sne_perplexity.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/manifold/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- applications Submodule -->
			<details>
				<summary><b>applications</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.applications</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_face_recognition.py'>plot_face_recognition.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_outlier_detection_wine.py'>plot_outlier_detection_wine.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_stock_market.py'>plot_stock_market.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_out_of_core_classification.py'>plot_out_of_core_classification.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_prediction_latency.py'>plot_prediction_latency.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_species_distribution_modeling.py'>plot_species_distribution_modeling.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/wikipedia_principal_eigenvector.py'>wikipedia_principal_eigenvector.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_cyclical_feature_engineering.py'>plot_cyclical_feature_engineering.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_model_complexity_influence.py'>plot_model_complexity_influence.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_tomography_l1_reconstruction.py'>plot_tomography_l1_reconstruction.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_time_series_lagged_features.py'>plot_time_series_lagged_features.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_digits_denoising.py'>plot_digits_denoising.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/applications/plot_topics_extraction_with_nmf_lda.py'>plot_topics_extraction_with_nmf_lda.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- mixture Submodule -->
			<details>
				<summary><b>mixture</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.mixture</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/mixture/plot_concentration_prior.py'>plot_concentration_prior.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/mixture/plot_gmm_covariances.py'>plot_gmm_covariances.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/mixture/plot_gmm.py'>plot_gmm.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/mixture/plot_gmm_selection.py'>plot_gmm_selection.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/mixture/plot_gmm_pdf.py'>plot_gmm_pdf.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/mixture/plot_gmm_init.py'>plot_gmm_init.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/mixture/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/mixture/plot_gmm_sin.py'>plot_gmm_sin.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- neural_networks Submodule -->
			<details>
				<summary><b>neural_networks</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.neural_networks</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neural_networks/plot_mlp_training_curves.py'>plot_mlp_training_curves.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neural_networks/plot_rbm_logistic_classification.py'>plot_rbm_logistic_classification.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neural_networks/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neural_networks/plot_mnist_filters.py'>plot_mnist_filters.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neural_networks/plot_mlp_alpha.py'>plot_mlp_alpha.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- release_highlights Submodule -->
			<details>
				<summary><b>release_highlights</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.release_highlights</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_1_3_0.py'>plot_release_highlights_1_3_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_1_2_0.py'>plot_release_highlights_1_2_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_1_5_0.py'>plot_release_highlights_1_5_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_1_9_0.py'>plot_release_highlights_1_9_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_1_8_0.py'>plot_release_highlights_1_8_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_1_4_0.py'>plot_release_highlights_1_4_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_1_7_0.py'>plot_release_highlights_1_7_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_1_6_0.py'>plot_release_highlights_1_6_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_0_24_0.py'>plot_release_highlights_0_24_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_0_23_0.py'>plot_release_highlights_0_23_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_1_1_0.py'>plot_release_highlights_1_1_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_1_0_0.py'>plot_release_highlights_1_0_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/release_highlights/plot_release_highlights_0_22_0.py'>plot_release_highlights_0_22_0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- preprocessing Submodule -->
			<details>
				<summary><b>preprocessing</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.preprocessing</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/preprocessing/plot_map_data_to_normal.py'>plot_map_data_to_normal.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/preprocessing/plot_target_encoder_cross_val.py'>plot_target_encoder_cross_val.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/preprocessing/plot_discretization_classification.py'>plot_discretization_classification.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/preprocessing/plot_discretization_strategies.py'>plot_discretization_strategies.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/preprocessing/plot_target_encoder.py'>plot_target_encoder.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/preprocessing/plot_scaling_importance.py'>plot_scaling_importance.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/preprocessing/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/preprocessing/plot_discretization.py'>plot_discretization.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/preprocessing/plot_all_scaling.py'>plot_all_scaling.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- text Submodule -->
			<details>
				<summary><b>text</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.text</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/text/plot_hashing_vs_dict_vectorizer.py'>plot_hashing_vs_dict_vectorizer.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/text/plot_document_clustering.py'>plot_document_clustering.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/text/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/text/plot_document_classification_20newsgroups.py'>plot_document_classification_20newsgroups.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- frozen Submodule -->
			<details>
				<summary><b>frozen</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.frozen</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/frozen/plot_frozen_examples.py'>plot_frozen_examples.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/frozen/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- model_selection Submodule -->
			<details>
				<summary><b>model_selection</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.model_selection</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_roc.py'>plot_roc.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_confusion_matrix.py'>plot_confusion_matrix.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_permutation_tests_for_classification.py'>plot_permutation_tests_for_classification.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_train_error_vs_test_error.py'>plot_train_error_vs_test_error.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_successive_halving_heatmap.py'>plot_successive_halving_heatmap.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_roc_crossval.py'>plot_roc_crossval.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_tuned_decision_threshold.py'>plot_tuned_decision_threshold.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_underfitting_overfitting.py'>plot_underfitting_overfitting.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_det.py'>plot_det.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_successive_halving_iterations.py'>plot_successive_halving_iterations.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_cv_predict.py'>plot_cv_predict.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_grid_search_stats.py'>plot_grid_search_stats.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_cv_indices.py'>plot_cv_indices.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_grid_search_text_feature_extraction.py'>plot_grid_search_text_feature_extraction.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_randomized_search.py'>plot_randomized_search.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_learning_curve.py'>plot_learning_curve.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_nested_cross_validation_iris.py'>plot_nested_cross_validation_iris.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_cost_sensitive_learning.py'>plot_cost_sensitive_learning.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_precision_recall.py'>plot_precision_recall.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_grid_search_refit_callable.py'>plot_grid_search_refit_callable.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_likelihood_ratios.py'>plot_likelihood_ratios.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_multi_metric_evaluation.py'>plot_multi_metric_evaluation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/model_selection/plot_grid_search_digits.py'>plot_grid_search_digits.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- multiclass Submodule -->
			<details>
				<summary><b>multiclass</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.multiclass</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/multiclass/plot_multiclass_overview.py'>plot_multiclass_overview.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/multiclass/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- decomposition Submodule -->
			<details>
				<summary><b>decomposition</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.decomposition</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/plot_incremental_pca.py'>plot_incremental_pca.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/plot_kernel_pca.py'>plot_kernel_pca.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/plot_faces_decomposition.py'>plot_faces_decomposition.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/plot_pca_vs_lda.py'>plot_pca_vs_lda.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/plot_image_denoising.py'>plot_image_denoising.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/plot_pca_vs_fa_model_selection.py'>plot_pca_vs_fa_model_selection.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/plot_pca_iris.py'>plot_pca_iris.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/plot_ica_blind_source_separation.py'>plot_ica_blind_source_separation.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/plot_varimax_fa.py'>plot_varimax_fa.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/plot_sparse_coding.py'>plot_sparse_coding.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/decomposition/plot_ica_vs_pca.py'>plot_ica_vs_pca.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- cross_decomposition Submodule -->
			<details>
				<summary><b>cross_decomposition</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.cross_decomposition</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cross_decomposition/plot_pcr_vs_pls.py'>plot_pcr_vs_pls.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cross_decomposition/plot_compare_cross_decomposition.py'>plot_compare_cross_decomposition.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/cross_decomposition/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- neighbors Submodule -->
			<details>
				<summary><b>neighbors</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ examples.neighbors</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_species_kde.py'>plot_species_kde.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_nca_classification.py'>plot_nca_classification.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_nearest_centroid.py'>plot_nearest_centroid.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_caching_nearest_neighbors.py'>plot_caching_nearest_neighbors.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_nca_dim_reduction.py'>plot_nca_dim_reduction.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_lof_outlier_detection.py'>plot_lof_outlier_detection.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_nca_illustration.py'>plot_nca_illustration.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_lof_novelty_detection.py'>plot_lof_novelty_detection.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_regression.py'>plot_regression.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_classification.py'>plot_classification.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_kde_1d.py'>plot_kde_1d.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/approximate_nearest_neighbors.py'>approximate_nearest_neighbors.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/examples/neighbors/plot_digits_kde_sampling.py'>plot_digits_kde_sampling.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- benchmarks Submodule -->
	<details>
		<summary><b>benchmarks</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ benchmarks</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_mnist.py'>bench_mnist.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/plot_tsne_mnist.py'>plot_tsne_mnist.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_rcv1_logreg_convergence.py'>bench_rcv1_logreg_convergence.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_neighbors.py'>bench_plot_neighbors.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_tsne_mnist.py'>bench_tsne_mnist.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_randomized_svd.py'>bench_plot_randomized_svd.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_hist_gradient_boosting_higgsboson.py'>bench_hist_gradient_boosting_higgsboson.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_isolation_forest.py'>bench_isolation_forest.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_hist_gradient_boosting_threading.py'>bench_hist_gradient_boosting_threading.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_omp_lars.py'>bench_plot_omp_lars.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_lasso.py'>bench_lasso.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_svd.py'>bench_plot_svd.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_pca_solvers.py'>bench_pca_solvers.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_polynomial_kernel_approximation.py'>bench_plot_polynomial_kernel_approximation.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_feature_expansions.py'>bench_feature_expansions.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_sample_without_replacement.py'>bench_sample_without_replacement.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_covertype.py'>bench_covertype.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_isotonic.py'>bench_isotonic.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_hist_gradient_boosting.py'>bench_hist_gradient_boosting.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_parallel_pairwise.py'>bench_plot_parallel_pairwise.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_fastkmeans.py'>bench_plot_fastkmeans.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_nmf.py'>bench_plot_nmf.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_ward.py'>bench_plot_ward.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_lasso_path.py'>bench_plot_lasso_path.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_hist_gradient_boosting_categorical_only.py'>bench_hist_gradient_boosting_categorical_only.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_tree.py'>bench_tree.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_hist_gradient_boosting_adult.py'>bench_hist_gradient_boosting_adult.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_incremental_pca.py'>bench_plot_incremental_pca.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_sparsify.py'>bench_sparsify.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_20newsgroups.py'>bench_20newsgroups.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_sgd_regression.py'>bench_sgd_regression.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_online_ocsvm.py'>bench_online_ocsvm.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_kernel_pca_solvers_time_vs_n_components.py'>bench_kernel_pca_solvers_time_vs_n_components.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_saga.py'>bench_saga.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_plot_hierarchical.py'>bench_plot_hierarchical.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_random_projections.py'>bench_random_projections.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_isolation_forest_predict.py'>bench_isolation_forest_predict.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_kernel_pca_solvers_time_vs_n_samples.py'>bench_kernel_pca_solvers_time_vs_n_samples.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_lof.py'>bench_lof.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_glmnet.py'>bench_glmnet.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_text_vectorizers.py'>bench_text_vectorizers.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/benchmarks/bench_glm.py'>bench_glm.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- build_tools Submodule -->
	<details>
		<summary><b>build_tools</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ build_tools</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/linting.sh'>linting.sh</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/shared.sh'>shared.sh</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/check-meson-openmp-dependencies.py'>check-meson-openmp-dependencies.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/get_comment.py'>get_comment.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/generate_authors_table.py'>generate_authors_table.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/codespell_ignore_words.txt'>codespell_ignore_words.txt</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/update_environments_and_lock_files.py'>update_environments_and_lock_files.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- wheels Submodule -->
			<details>
				<summary><b>wheels</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ build_tools.wheels</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/wheels/test_wheels.sh'>test_wheels.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/wheels/build_wheels.sh'>build_wheels.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/wheels/check_license.py'>check_license.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/wheels/LICENSE_linux.txt'>LICENSE_linux.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/wheels/LICENSE_windows.txt'>LICENSE_windows.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/wheels/LICENSE_macos.txt'>LICENSE_macos.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/wheels/cibw_before_build.sh'>cibw_before_build.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- github Submodule -->
			<details>
				<summary><b>github</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ build_tools.github</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pylatest_pip_openblas_pandas_environment.yml'>pylatest_pip_openblas_pandas_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pylatest_conda_forge_cuda_array-api_linux-64_virtual_package_spec.yml'>pylatest_conda_forge_cuda_array-api_linux-64_virtual_package_spec.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/build_minimal_windows_image.sh'>build_minimal_windows_image.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pylatest_conda_forge_cuda_array-api_linux-64_environment.yml'>pylatest_conda_forge_cuda_array-api_linux-64_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/upload_anaconda.sh'>upload_anaconda.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pylatest_free_threaded_environment.yml'>pylatest_free_threaded_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/vendor.py'>vendor.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/repair_windows_wheels.sh'>repair_windows_wheels.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/check_build_trigger.sh'>check_build_trigger.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/lint_lock.txt'>lint_lock.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pylatest_conda_forge_mkl_no_openmp_environment.yml'>pylatest_conda_forge_mkl_no_openmp_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/debian_32bit_lock.txt'>debian_32bit_lock.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/install.sh'>install.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/create_gpu_environment.sh'>create_gpu_environment.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/test_pytest_soft_dependency.sh'>test_pytest_soft_dependency.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pymin_conda_forge_arm_environment.yml'>pymin_conda_forge_arm_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pylatest_pip_scipy_dev_environment.yml'>pylatest_pip_scipy_dev_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/ubuntu_atlas_lock.txt'>ubuntu_atlas_lock.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/check_wheels.py'>check_wheels.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/combine_coverage_reports.sh'>combine_coverage_reports.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pymin_conda_forge_openblas_ubuntu_2204_environment.yml'>pymin_conda_forge_openblas_ubuntu_2204_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/autoclose_prs.py'>autoclose_prs.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pylatest_conda_forge_mkl_linux-64_environment.yml'>pylatest_conda_forge_mkl_linux-64_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pymin_conda_forge_openblas_environment.yml'>pymin_conda_forge_openblas_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/ubuntu_atlas_requirements.txt'>ubuntu_atlas_requirements.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pymin_conda_forge_openblas_min_dependencies_environment.yml'>pymin_conda_forge_openblas_min_dependencies_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/test_docs.sh'>test_docs.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/test_script.sh'>test_script.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/lint_requirements.txt'>lint_requirements.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/build_source.sh'>build_source.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/test_source.sh'>test_source.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/test_windows_wheels.sh'>test_windows_wheels.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/pylatest_conda_forge_osx-arm64_environment.yml'>pylatest_conda_forge_osx-arm64_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/github/debian_32bit_requirements.txt'>debian_32bit_requirements.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- circle Submodule -->
			<details>
				<summary><b>circle</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ build_tools.circle</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/circle/push_doc.sh'>push_doc.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/circle/doc_environment.yml'>doc_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/circle/list_versions.py'>list_versions.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/circle/download_documentation.sh'>download_documentation.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/circle/checkout_merge_commit.sh'>checkout_merge_commit.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/circle/doc_min_dependencies_environment.yml'>doc_min_dependencies_environment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/build_tools/circle/build_doc.sh'>build_doc.sh</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- .github Submodule -->
	<details>
		<summary><b>.github</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ .github</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/FUNDING.yml'>FUNDING.yml</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/labeler-module.yml'>labeler-module.yml</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/labeler-file-extensions.yml'>labeler-file-extensions.yml</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/dependabot.yml'>dependabot.yml</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- workflows Submodule -->
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ .github.workflows</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/autoclose-comment.yml'>autoclose-comment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/emscripten.yml'>emscripten.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/welcome-first-time-contributor.yml'>welcome-first-time-contributor.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/artifact-redirector.yml'>artifact-redirector.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/labeler-module.yml'>labeler-module.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/wheels.yml'>wheels.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/not-ready-for-pr-warning.yml'>not-ready-for-pr-warning.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/lint.yml'>lint.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/autoclose-schedule.yml'>autoclose-schedule.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/bot-lint-comment.yml'>bot-lint-comment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/update_tracking_issue.yml'>update_tracking_issue.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/codeql.yml'>codeql.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/needs-decision.yml'>needs-decision.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/publish_pypi.yml'>publish_pypi.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/check-changelog.yml'>check-changelog.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/label-blank-issue.yml'>label-blank-issue.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/unit-tests.yml'>unit-tests.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/cuda-ci.yml'>cuda-ci.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/codespell.yml'>codespell.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/cuda-label-remover.yml'>cuda-label-remover.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/check-sdist.yml'>check-sdist.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/update-lock-files.yml'>update-lock-files.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/workflows/labeler-title-regex.yml'>labeler-title-regex.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- scripts Submodule -->
			<details>
				<summary><b>scripts</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ .github.scripts</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/scripts/add_or_remove_no_pr_warning.py'>add_or_remove_no_pr_warning.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/scripts/label_title_regex.py'>label_title_regex.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- ISSUE_TEMPLATE Submodule -->
			<details>
				<summary><b>ISSUE_TEMPLATE</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ .github.ISSUE_TEMPLATE</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/ISSUE_TEMPLATE/feature_request.yml'>feature_request.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/ISSUE_TEMPLATE/bug_report.yml'>bug_report.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/ISSUE_TEMPLATE/doc_improvement.yml'>doc_improvement.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/.github/ISSUE_TEMPLATE/config.yml'>config.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- doc Submodule -->
	<details>
		<summary><b>doc</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ doc</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/install.rst'>install.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/jupyter-lite.json'>jupyter-lite.json</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/getting_started.rst'>getting_started.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/conftest.py'>conftest.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/documentation_team.rst'>documentation_team.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/data_interoperability.rst'>data_interoperability.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/roadmap.rst'>roadmap.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/jupyter_lite_config.json'>jupyter_lite_config.json</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/machine_learning_map.rst'>machine_learning_map.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/inspection.rst'>inspection.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/support.rst'>support.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/model_selection.rst'>model_selection.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/model_persistence.rst'>model_persistence.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/conf.py'>conf.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/communication_team.rst'>communication_team.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/callbacks.rst'>callbacks.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/contributor_experience_team_emeritus.rst'>contributor_experience_team_emeritus.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/governance.rst'>governance.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/visualizations.rst'>visualizations.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/index.rst.template'>index.rst.template</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/related_projects.rst'>related_projects.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/supervised_learning.rst'>supervised_learning.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/contributor_experience_team.rst'>contributor_experience_team.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/institutional_support.rst'>institutional_support.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/metadata_routing.rst'>metadata_routing.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/make.bat'>make.bat</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/maintainers_emeritus.rst'>maintainers_emeritus.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/api_reference.py'>api_reference.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/min_dependency_substitutions.rst.template'>min_dependency_substitutions.rst.template</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/presentations.rst'>presentations.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/communication_team_emeritus.rst'>communication_team_emeritus.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/install_instructions_conda.rst'>install_instructions_conda.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/data_transforms.rst'>data_transforms.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/datasets.rst'>datasets.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/maintainers.rst'>maintainers.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/user_guide.rst'>user_guide.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/unsupervised_learning.rst'>unsupervised_learning.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new.rst'>whats_new.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/faq.rst'>faq.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/common_pitfalls.rst'>common_pitfalls.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/computing.rst'>computing.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/glossary.rst'>glossary.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/min_dependency_table.rst.template'>min_dependency_table.rst.template</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/about.rst'>about.rst</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- whats_new Submodule -->
			<details>
				<summary><b>whats_new</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.whats_new</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v1.10.rst'>v1.10.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v1.5.rst'>v1.5.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v1.4.rst'>v1.4.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v1.6.rst'>v1.6.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.19.rst'>v0.19.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.18.rst'>v0.18.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v1.7.rst'>v1.7.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.24.rst'>v0.24.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v1.3.rst'>v1.3.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.20.rst'>v0.20.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.21.rst'>v0.21.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v1.2.rst'>v1.2.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v1.0.rst'>v1.0.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.23.rst'>v0.23.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/_contributors.rst'>_contributors.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.22.rst'>v0.22.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v1.1.rst'>v1.1.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.13.rst'>v0.13.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.15.rst'>v0.15.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.14.rst'>v0.14.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v1.9.rst'>v1.9.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.16.rst'>v0.16.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/older_versions.rst'>older_versions.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v0.17.rst'>v0.17.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/v1.8.rst'>v1.8.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/changelog_legend.inc'>changelog_legend.inc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- upcoming_changes Submodule -->
					<details>
						<summary><b>upcoming_changes</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ doc.whats_new.upcoming_changes</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/towncrier_template.rst.jinja2'>towncrier_template.rst.jinja2</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
							<!-- sklearn.model_selection Submodule -->
							<details>
								<summary><b>sklearn.model_selection</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.model_selection</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.model_selection/34250.api.rst'>34250.api.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- metadata-routing Submodule -->
							<details>
								<summary><b>metadata-routing</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.metadata-routing</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/metadata-routing/34224.fix.rst'>34224.fix.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/metadata-routing/34188.fix.rst'>34188.fix.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/metadata-routing/34201.fix.rst'>34201.fix.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.utils Submodule -->
							<details>
								<summary><b>sklearn.utils</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.utils</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.utils/34362.fix.rst'>34362.fix.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.tree Submodule -->
							<details>
								<summary><b>sklearn.tree</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.tree</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.tree/33810.feature.rst'>33810.feature.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.svm Submodule -->
							<details>
								<summary><b>sklearn.svm</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.svm</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.svm/34256.fix.rst'>34256.fix.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.impute Submodule -->
							<details>
								<summary><b>sklearn.impute</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.impute</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.impute/34214.api.rst'>34214.api.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- array-api Submodule -->
							<details>
								<summary><b>array-api</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.array-api</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/array-api/33573.feature.rst'>33573.feature.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.inspection Submodule -->
							<details>
								<summary><b>sklearn.inspection</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.inspection</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.inspection/34092.enhancement.rst'>34092.enhancement.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.metrics Submodule -->
							<details>
								<summary><b>sklearn.metrics</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.metrics</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.metrics/34236.efficiency.rst'>34236.efficiency.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.metrics/34083.fix.rst'>34083.fix.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.calibration Submodule -->
							<details>
								<summary><b>sklearn.calibration</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.calibration</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.calibration/33856.feature.rst'>33856.feature.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.pipeline Submodule -->
							<details>
								<summary><b>sklearn.pipeline</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.pipeline</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.pipeline/34263.fix.rst'>34263.fix.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.ensemble Submodule -->
							<details>
								<summary><b>sklearn.ensemble</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.ensemble</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.ensemble/34194.efficiency.rst'>34194.efficiency.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.ensemble/34248.efficiency.rst'>34248.efficiency.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.ensemble/34236.api.rst'>34236.api.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.ensemble/32911.efficiency.rst'>32911.efficiency.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.datasets Submodule -->
							<details>
								<summary><b>sklearn.datasets</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.datasets</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.datasets/34262.fix.rst'>34262.fix.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.linear_model Submodule -->
							<details>
								<summary><b>sklearn.linear_model</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.linear_model</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.linear_model/33759.enhancement.rst'>33759.enhancement.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.linear_model/34157.efficiency.rst'>34157.efficiency.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sklearn.neighbors Submodule -->
							<details>
								<summary><b>sklearn.neighbors</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.whats_new.upcoming_changes.sklearn.neighbors</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.neighbors/34187.efficiency.rst'>34187.efficiency.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/whats_new/upcoming_changes/sklearn.neighbors/34122.feature.rst'>34122.feature.rst</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- testimonials Submodule -->
			<details>
				<summary><b>testimonials</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.testimonials</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/testimonials/testimonials.rst'>testimonials.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/testimonials/README.txt'>README.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- images Submodule -->
					<details>
						<summary><b>images</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ doc.testimonials.images</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/testimonials/images/Makefile'>Makefile</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- sphinxext Submodule -->
			<details>
				<summary><b>sphinxext</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.sphinxext</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/sphinxext/doi_role.py'>doi_role.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/sphinxext/sphinx_issues.py'>sphinx_issues.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/sphinxext/dropdown_anchors.py'>dropdown_anchors.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/sphinxext/github_link.py'>github_link.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/sphinxext/MANIFEST.in'>MANIFEST.in</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/sphinxext/override_pst_pagetoc.py'>override_pst_pagetoc.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/sphinxext/allow_nan_estimators.py'>allow_nan_estimators.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/sphinxext/autoshortsummary.py'>autoshortsummary.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- binder Submodule -->
			<details>
				<summary><b>binder</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.binder</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/binder/requirements.txt'>requirements.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- images Submodule -->
			<details>
				<summary><b>images</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.images</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/images/ml_map.README.rst'>ml_map.README.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- js Submodule -->
			<details>
				<summary><b>js</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.js</b></code>
					<!-- scripts Submodule -->
					<details>
						<summary><b>scripts</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ doc.js.scripts</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/js/scripts/version-switcher.js'>version-switcher.js</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/js/scripts/api-search.js'>api-search.js</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/js/scripts/dropdown.js'>dropdown.js</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/js/scripts/sg_plotly_resize.js'>sg_plotly_resize.js</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/js/scripts/theme-observer.js'>theme-observer.js</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
							<!-- vendor Submodule -->
							<details>
								<summary><b>vendor</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ doc.js.scripts.vendor</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/js/scripts/vendor/svg-pan-zoom.min.js'>svg-pan-zoom.min.js</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- scss Submodule -->
			<details>
				<summary><b>scss</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.scss</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/scss/index.scss'>index.scss</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/scss/colors.scss'>colors.scss</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/scss/custom.scss'>custom.scss</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/scss/api.scss'>api.scss</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/scss/api-search.scss'>api-search.scss</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- datasets Submodule -->
			<details>
				<summary><b>datasets</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.datasets</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/datasets/loading_other_datasets.rst'>loading_other_datasets.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/datasets/real_world.rst'>real_world.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/datasets/sample_generators.rst'>sample_generators.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/datasets/toy_dataset.rst'>toy_dataset.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- api Submodule -->
			<details>
				<summary><b>api</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.api</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/api/deprecated.rst.template'>deprecated.rst.template</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/api/index.rst.template'>index.rst.template</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/api/module.rst.template'>module.rst.template</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- templates Submodule -->
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.templates</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/templates/numpydoc_docstring.rst'>numpydoc_docstring.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/templates/index.html'>index.html</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/templates/base.rst'>base.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/templates/funding_links.html'>funding_links.html</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/templates/redirects.html'>redirects.html</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- computing Submodule -->
			<details>
				<summary><b>computing</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.computing</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/computing/parallelism.rst'>parallelism.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/computing/computational_performance.rst'>computational_performance.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/computing/scaling_strategies.rst'>scaling_strategies.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- modules Submodule -->
			<details>
				<summary><b>modules</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.modules</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/df_output_transform.rst'>df_output_transform.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/kernel_approximation.rst'>kernel_approximation.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/compose.rst'>compose.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/isotonic.rst'>isotonic.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/neural_networks_unsupervised.rst'>neural_networks_unsupervised.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/learning_curve.rst'>learning_curve.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/svm.rst'>svm.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/density.rst'>density.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/gaussian_process.rst'>gaussian_process.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/impute.rst'>impute.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/lda_qda.rst'>lda_qda.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/cross_validation.rst'>cross_validation.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/preprocessing_targets.rst'>preprocessing_targets.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/sgd.rst'>sgd.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/semi_supervised.rst'>semi_supervised.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/decomposition.rst'>decomposition.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/ensemble.rst'>ensemble.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/array_api.rst'>array_api.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/classification_threshold.rst'>classification_threshold.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/kernel_ridge.rst'>kernel_ridge.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/neural_networks_supervised.rst'>neural_networks_supervised.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/linear_model.rst'>linear_model.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/clustering.rst'>clustering.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/biclustering.rst'>biclustering.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/naive_bayes.rst'>naive_bayes.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/cross_decomposition.rst'>cross_decomposition.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/tree.rst'>tree.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/pipeline.rst'>pipeline.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/model_evaluation.rst'>model_evaluation.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/metrics.rst'>metrics.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/covariance.rst'>covariance.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/multiclass.rst'>multiclass.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/neighbors.rst'>neighbors.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/preprocessing.rst'>preprocessing.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/mixture.rst'>mixture.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/partial_dependence.rst'>partial_dependence.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/unsupervised_reduction.rst'>unsupervised_reduction.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/random_projection.rst'>random_projection.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/calibration.rst'>calibration.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/permutation_importance.rst'>permutation_importance.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/feature_selection.rst'>feature_selection.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/outlier_detection.rst'>outlier_detection.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/manifold.rst'>manifold.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/grid_search.rst'>grid_search.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/modules/feature_extraction.rst'>feature_extraction.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- developers Submodule -->
			<details>
				<summary><b>developers</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ doc.developers</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/index.rst'>index.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/contributing.rst'>contributing.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/developing_callbacks.rst'>developing_callbacks.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/cython.rst'>cython.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/callbacks.rst'>callbacks.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/develop.rst'>develop.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/utilities.rst'>utilities.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/maintainer.rst.template'>maintainer.rst.template</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/tips.rst'>tips.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/plotting.rst'>plotting.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/bug_triaging.rst'>bug_triaging.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/development_setup.rst'>development_setup.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/minimal_reproducer.rst'>minimal_reproducer.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/misc_info.rst'>misc_info.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/callback_support.rst'>callback_support.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/scikit-learn/scikit-learn/blob/master/doc/developers/performance.rst'>performance.rst</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Conda, Pip

### Installation

Build scikit-learn from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/scikit-learn/scikit-learn
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd scikit-learn
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![conda][conda-shield]][conda-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [conda-shield]: https://img.shields.io/badge/conda-342B029.svg?style={badge_style}&logo=anaconda&logoColor=white -->
	<!-- [conda-link]: https://docs.conda.io/ -->

	**Using [conda](https://docs.conda.io/):**

	```sh
	❯ conda env create -f build_tools/github/pylatest_pip_openblas_pandas_environment.yml, build_tools/github/pylatest_conda_forge_cuda_array-api_linux-64_environment.yml, build_tools/github/pylatest_free_threaded_environment.yml, build_tools/github/pylatest_conda_forge_mkl_no_openmp_environment.yml, build_tools/github/pymin_conda_forge_arm_environment.yml, build_tools/github/pylatest_pip_scipy_dev_environment.yml, build_tools/github/pymin_conda_forge_openblas_ubuntu_2204_environment.yml, build_tools/github/pylatest_conda_forge_mkl_linux-64_environment.yml, build_tools/github/pymin_conda_forge_openblas_environment.yml, build_tools/github/pymin_conda_forge_openblas_min_dependencies_environment.yml, build_tools/github/pylatest_conda_forge_osx-arm64_environment.yml, build_tools/circle/doc_environment.yml, build_tools/circle/doc_min_dependencies_environment.yml
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r build_tools/github/ubuntu_atlas_requirements.txt, build_tools/github/lint_requirements.txt, build_tools/github/debian_32bit_requirements.txt, doc/binder/requirements.txt
	```

### Usage

Run the project with:

**Using [conda](https://docs.conda.io/):**
```sh
conda activate {venv}
python {entrypoint}
```
**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```

### Testing

Scikit-learn uses the {__test_framework__} test framework. Run the test suite with:

**Using [conda](https://docs.conda.io/):**
```sh
conda activate {venv}
pytest
```
**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## Contributing

- **💬 [Join the Discussions](https://github.com/scikit-learn/scikit-learn/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/scikit-learn/scikit-learn/issues)**: Submit bugs found or log feature requests for the `scikit-learn` project.
- **💡 [Submit Pull Requests](https://github.com/scikit-learn/scikit-learn/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/scikit-learn/scikit-learn
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/scikit-learn/scikit-learn/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=scikit-learn/scikit-learn">
   </a>
</p>
</details>

---

## License

Scikit-learn is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
