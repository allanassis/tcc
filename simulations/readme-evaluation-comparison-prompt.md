# README Evaluation Comparison Prompt

> Generic, tool-agnostic prompt for comparing two README generation tools
> based on their **standardized evaluation data**. It is not tied to any
> specific study or project sample. All study-specific values are supplied
> through the parameters below (for the TCC study, see
> `simulations/tcc-run-manifest.md`).
>
> Prerequisite: both tools must have been evaluated with
> `simulations/standard-readme-evaluation-prompt.md`, so that each project has
> the standard five-file evaluation output per tool.

---

## Role

Act as a senior computer science researcher specializing in empirical software
engineering. You will compare two README generation tools using previously
produced evaluation data. You are an analyst, **not** a judge of READMEs: the
evaluation data is the ground truth.

## Parameters

| Parameter | Description |
|---|---|
| `{tool_a_name}` / `{tool_b_name}` | Names of the two compared tools |
| `{tool_a_eval_folders}` | Per-project standardized evaluation folders for tool A |
| `{tool_b_eval_folders}` | Per-project standardized evaluation folders for tool B |
| `{grouping_dimensions}` | Optional: named project groupings to break results down by (e.g., popularity, language), each with its project membership list |
| `{output_folder}` | Folder for the aggregate outputs |
| `{per_project_output}` | Path template for the per-project comparison CSV |

## Ground Rules

1. Rely **exclusively** on the standardized evaluation CSVs
   (`*_completeness.csv`, `*_correctness_results.csv`,
   `*_completeness_ATRAK.csv`). Do **not** read or re-judge the README files
   themselves, and do not use any legacy or ad-hoc evaluation data.
2. For a tool evaluated with multiple runs per project, report three
   aggregations: **mean** over runs (primary), **best** run, and **worst** run
   (robustness check), where best/worst are selected by overall correctness.
3. For a tool evaluated with a single run per project, use that single score
   for all aggregations.
4. Completeness per run is derived from the binary completeness CSV as
   `(Σ elements / number of element columns) × 100`.
5. Show every computation step (which rows were read, which numbers were
   averaged) so the comparison is fully auditable.
6. Do not invent numbers. If an input file is missing or malformed, stop and
   report it instead of estimating.

## Outputs

### 1. Per-project comparison CSV — `{per_project_output}`

One file per project, columns:

```
project,tool,aggregation,completeness_score,atrak_score,title_score,overview_score,installation_score,usage_score,api_score,license_score,correctness_score,winner_correctness
```

- `aggregation ∈ {mean, best, worst, single}`
- `winner_correctness`: the tool with the higher correctness under the row's
  aggregation vs the other tool's primary aggregation (mark only on the
  primary rows; leave empty otherwise)

### 2. Aggregate summary CSV — `{output_folder}/summary_<tool_a>_vs_<tool_b>.csv`

Sections (use a `scope` column to distinguish them):

- `project` rows: one per project — each tool's primary correctness,
  completeness, and ATRAK scores, and the winner
- `overall` rows: per tool — mean completeness, mean ATRAK, mean correctness,
  and the standard deviation of correctness across projects
- one row group per grouping dimension in `{grouping_dimensions}`: per-group,
  per-tool mean correctness (and completeness/ATRAK)
- `win_count` rows: number of projects where each tool has strictly higher
  correctness, computed twice — under tool A's mean aggregation and under its
  worst-run aggregation (and symmetrically if tool B is multi-run)

### 3. Aggregate reasoning report — `{output_folder}/comparison_reasoning.md`

Must contain, in order:

1. **Methodology recap** — what data was consumed, aggregation rules, and the
   provenance of every number.
2. **Aggregate table** — the overall per-tool results.
3. **Per-project analysis** — winner per project, with the score deltas.
4. **Group patterns** — results per grouping dimension, and any interaction
   worth noting (e.g., gap narrowing in a particular group).
5. **Dispersion analysis** — standard deviation of each tool's scores across
   projects and what it suggests about the tools' behavior.
6. **Fairness caveats** — explicitly state any dimension where one tool is
   favored **by construction** (for example: a tool whose generation prompt
   enforces the very sections the completeness rubric checks; or a rubric
   scoped to user-oriented content while a tool targets
   maintainer/repository-structure content). State what the comparison
   does and does not measure.

## Final Step

Verify all aggregate numbers against the per-project CSVs (recompute means and
win counts) before finishing, and state that the verification was done.
