# TCC Run Manifest — README-Gen vs README-AI

> Study-specific parameters for executing the generic prompts
> (`standard-readme-evaluation-prompt.md` and
> `readme-evaluation-comparison-prompt.md`) on the TCC / README-Gen study
> sample. The prompts themselves contain no study-specific values; this
> manifest supplies all of them.

## Study Sample — 12 Projects

Base path: `simulations/data/`. All popularity figures follow the study's
grouping: **popular** (>30k GitHub stars) vs **low-popularity** (<300 stars).

| # | `project_name` | Package folder | `repository_url` | `core_functionality` | Language | Popularity |
|---|---|---|---|---|---|---|
| 1 | Axios | `js/axios` | https://github.com/axios/axios | Execute HTTP requests | JavaScript | popular |
| 2 | jQuery | `js/jquey` | https://github.com/jquery/jquery | Query HTML elements | JavaScript | popular |
| 3 | Moment | `js/moment` | https://github.com/moment/moment | Parse and manipulate dates | JavaScript | popular |
| 4 | Uri | `js/uri` | https://github.com/lil-js/uri | Parse URIs | JavaScript | low |
| 5 | NumPy | `py/numpy` | https://github.com/numpy/numpy | Create and manipulate arrays | Python | popular |
| 6 | Rich | `py/rich` | https://github.com/Textualize/rich | Enhance Python console output | Python | popular |
| 7 | Scikit-learn | `py/scikit-learn` | https://github.com/scikit-learn/scikit-learn | Train machine learning models | Python | popular |
| 8 | SnakeMD | `py/snakemd` | https://github.com/TheRenegadeCoder/SnakeMD | Generate README files | Python | low |
| 9 | Git | `shell/git-cli` | https://github.com/git/git | Create and manage commits | Shell | popular |
| 10 | jq | `shell/jq` | https://github.com/jqlang/jq | Parse JSON data | Shell | popular |
| 11 | Notes-cli | `shell/notes-cli` | https://github.com/rhysd/notes-cli | Create and manage notes | Shell | low |
| 12 | CommandLauncher | `shell/command-laucher` | https://github.com/criteo/command-launcher | Install packages | Shell | low |

Core functionality definitions come from the TCC methodology section
(Table "Defined Core Functionalities of the Selected Repositories").

## Tools Under Evaluation

### Tool A — README-Gen (the TCC's approach)

- Generator: structured ATRAK-grounded prompting, model
  `gpt-4.1-mini-2025-04-14`
- `{readme_files}`: `data1.md`, `data2.md`, `data3.md` in each package folder
  (3 independent generation runs; aggregate = mean of the 3, with best/worst
  used as robustness checks)
- `{output_folder}`: `{package folder}/evaluation/`
- `{output_prefix}`: the package folder name (e.g., `numpy`, `jquey`,
  `git-cli`)

### Tool B — README-AI

- Generator: [README-AI](https://github.com/eli64s/readme-ai) v0.6.0rc1, same
  underlying model (`gpt-4.1-mini-2025-04-14`), identical command line per
  repository
- `{readme_files}`: single file per package, under
  `{package folder}/compare-readme-ai/` — see exact filenames below
- `{output_folder}`: `{package folder}/compare-readme-ai/evaluation/`
- `{output_prefix}`: `{package folder name}_readmeai` (e.g., `numpy_readmeai`)

### README-AI input filenames (naming quirks — do not rename)

| Package folder | README-AI file |
|---|---|
| `js/axios` | `axios_readme_readmeai.md` |
| `js/jquey` | `jquery_readme_readmeai.md` |
| `js/moment` | `moment_readme_readmeai.md` |
| `js/uri` | `uri_readme_readmeai.md` |
| `py/numpy` | `numpy_readme_readmeai.md` |
| `py/rich` | `rich_readme_readmeai.md` |
| `py/scikit-learn` | `scikit_readme_readmeai.md` |
| `py/snakemd` | `snakemd_readme_readmeai.md` |
| `shell/git-cli` | `git_readme_readmeai.md` |
| `shell/jq` | `jq_readme_readmeai.md` |
| `shell/notes-cli` | `notes_readme_readmeai.md` |
| `shell/command-laucher` | `command-launcher.md` |

## Comparison Parameters

For `readme-evaluation-comparison-prompt.md`:

- `{tool_a_name}` = `README-Gen`, `{tool_b_name}` = `README-AI`
- `{tool_a_eval_folders}` = the 12 `{package}/evaluation/` folders
- `{tool_b_eval_folders}` = the 12 `{package}/compare-readme-ai/evaluation/`
  folders
- `{grouping_dimensions}`:
  - **popularity**: popular = {Axios, jQuery, Moment, NumPy, Rich,
    Scikit-learn, Git, jq}; low = {Uri, SnakeMD, Notes-cli, CommandLauncher}
  - **language**: JavaScript = {Axios, jQuery, Moment, Uri}; Python = {NumPy,
    Rich, Scikit-learn, SnakeMD}; Shell = {Git, jq, Notes-cli,
    CommandLauncher}
- `{per_project_output}` =
  `{package folder}/compare-readme-ai/{package}_standard_comparison.csv`
- `{output_folder}` = `simulations/comparison/`

## Legacy Data (do not use as input)

- `{package}/evaluation-legacy/` — original README-Gen evaluations (pre-
  standardization)
- `{package}/compare-readme-ai/legacy/` — original ad-hoc comparison
  artifacts

Legacy data is retained for reference and for drift analysis between the
original and standardized evaluations. See `simulations/data/README.md`.
