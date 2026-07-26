# README-Gen vs README-AI — Comparison Reasoning

Produced per `simulations/readme-evaluation-comparison-prompt.md`, parameterized
by `simulations/tcc-run-manifest.md`. Numbers computed by
`simulations/comparison/run_comparison.py` (audit trail in its stdout; re-run
to reproduce).

## 1. Methodology Recap

- **Inputs consumed:** exclusively the standardized evaluation CSVs produced by
  `simulations/standard-readme-evaluation-prompt.md`:
  `{pkg}/evaluation/{pkg}_{correctness_results,completeness,completeness_ATRAK}.csv`
  (README-Gen, 3 runs) and
  `{pkg}/compare-readme-ai/evaluation/{pkg}_readmeai_*.csv` (README-AI, 1 run)
  for the 12 manifest projects. No README file was re-judged; no legacy data
  was used.
- **Aggregations:** README-Gen = mean of its 3 runs (primary), plus best and
  worst run (selected by overall correctness C_R) as robustness checks;
  README-AI = its single run.
- **Completeness per run** = (Σ of the 7 binary elements / 7) × 100, derived
  from the completeness CSVs.
- **Outputs:** one `{pkg}_standard_comparison.csv` per project (mean/best/worst
  vs single), plus `summary_readme_gen_vs_readme_ai.csv` (this folder).
- **Evaluation rubric reminder:** ATRAK is presence-only (hallucinated content
  counts as present; absent only for empty sections, name-only lists, or
  unresolved placeholders); correctness requires executing installation paths
  and snippets and validating API elements against source/official docs.

## 2. Aggregate Results

| Metric | README-Gen (mean of 3 runs) | README-AI (single run) |
|---|---|---|
| Structural completeness | **97.62** | 65.48 |
| ATRAK adherence | **100.00** | 75.00 |
| Correctness (all 12) | **77.77** | 47.57 |
| Correctness (popular, 8) | **93.37** | 45.70 |
| Correctness (low-popularity, 4) | 46.56 | **51.32** |
| Correctness std dev across projects | 23.16 | 9.39 |
| Wins (vs README-Gen mean) | **11 / 12** | 1 / 12 |
| Wins (vs README-Gen worst run) | **9 / 12** | 2 / 12 (1 tie) |

## 3. Per-Project Analysis

| Project | README-Gen mean C_R | README-AI C_R | Δ | Winner |
|---|---|---|---|---|
| axios | 96.58 | 63.89 | +32.69 | README-Gen |
| jquey (jQuery) | 99.66 | 43.89 | +55.77 | README-Gen |
| moment | 100.00 | 48.89 | +51.11 | README-Gen |
| uri | 57.22 | 53.06 | +4.16 | README-Gen |
| numpy | 90.18 | 38.89 | +51.29 | README-Gen |
| rich | 87.94 | 50.00 | +37.94 | README-Gen |
| scikit-learn | 82.85 | 42.22 | +40.63 | README-Gen |
| snakemd | 36.66 | 66.67 | −30.01 | **README-AI** |
| git-cli | 98.61 | 38.89 | +59.72 | README-Gen |
| jq | 91.11 | 38.89 | +52.22 | README-Gen |
| notes-cli | 53.49 | 48.89 | +4.60 | README-Gen |
| command-laucher | 38.89 | 36.67 | +2.22 | README-Gen |

Robustness check (README-Gen worst run vs README-AI): README-Gen still wins
9/12. The three changes are snakemd (already a README-AI win), **uri** (worst
run 50.00 < 53.06) and **command-laucher** (worst run 36.67 = 36.67, a tie) —
all three in the low-popularity group, where README-Gen's margins are thin.

README-AI's only outright win, snakemd (66.67 vs 36.66), is the repository
where README-Gen hallucinated entire projects across its runs (a resume/CV
tool, a note-taking snake game, a Node terminal renderer): the model had no
usable prior exposure to the real SnakeMD, while README-AI's
repository-parsing pipeline extracted a genuinely correct project description
and a working `git clone` + `poetry install` flow.

README-AI's recurring correctness failures are structural and repeat across
projects: empty Overview sections (partially rescued when a Features table
carries a description), unresolved template placeholders in Usage
(`python {entrypoint}`, `{__test_framework__}`, `INSERT-RUN-COMMAND-HERE`),
absent API Reference sections (A = 0 in 11 of 12 projects), and License
sections that never name the actual license (L = 33.33 in 9 of 12).

## 4. Group Patterns

- **Popularity.** README-Gen's correctness is strongly stratified by
  popularity (93.37 popular vs 46.56 low, a 46.8-point drop). README-AI is
  nearly flat (45.70 vs 51.32 — slightly *higher* on obscure projects). On
  the low-popularity group the ranking inverts: README-AI's mean (51.32)
  edges out README-Gen's (46.56). Since README-AI parses the repository at
  generation time while README-Gen relies on the model's prior knowledge of
  the identified project, this is direct evidence that artifact injection
  compensates for missing training exposure — and that README-Gen's advantage
  comes from the model's prior knowledge, not from its structure alone.
- **Language.** README-Gen leads in all three: JavaScript 88.36 vs 52.43,
  Python 74.41 vs 49.45, Shell 70.53 vs 40.84. Language differences mainly
  reflect where the low-popularity projects sit, not language-specific
  ability.

## 5. Dispersion Analysis

README-Gen's correctness varies widely across projects (std 23.16): it is
near-perfect on popular repositories and collapses on obscure ones. README-AI
is far more stable (std 9.39) and uncorrelated with popularity: its content is
derived from parsing the repository, so its quality is bounded by its pipeline
(placeholders, missing sections) rather than by the project's presence in the
training corpus. Its best scores occur on the two smallest codebases
(snakemd 66.67, uri 53.06), consistent with per-file summarization covering a
larger fraction of small projects.

## 6. Fairness Caveats

These must accompany any use of the aggregate numbers:

1. **Construction advantage — completeness and ATRAK.** README-Gen's
   generation prompt enforces exactly the six sections that the completeness
   rubric checks and maps them one-to-one to the ATRAK Knowledge Elements.
   Its near-perfect completeness (97.62) and perfect ATRAK (100) are therefore
   expected by construction, and those two rows should not be read as an
   independent quality finding. The informative contrast is correctness.
2. **Scope of the rubric.** The rubric measures the user-oriented purpose the
   documentation literature assigns to READMEs (install, use, API, license).
   README-AI spends much of its generative effort on repository-structure
   content (per-file project index, badges, contribution workflow) that the
   rubric intentionally ignores. The comparison measures fitness for the
   user-oriented purpose, not overall tool quality.
3. **Run asymmetry.** README-Gen is averaged over 3 generations; README-AI was
   executed once. The worst-run robustness check (README-Gen still wins 9/12)
   bounds the impact of README-Gen's variability, but README-AI's own run-to-
   run variance is unmeasured — its score-determining failures (empty
   sections, unresolved placeholders) are structural, so low variance is
   expected.
4. **ATRAK is presence-only.** Under this rubric, hallucinated-but-present
   content earns ATRAK credit for both tools (accuracy is scored separately
   under correctness). README-AI's 75% ATRAK therefore reads higher than under
   a stricter "communicated-knowledge" standard; its failures are genuinely
   absent content (empty Overviews, placeholder-only Usage).

## 7. Verification

All aggregate numbers in Section 2 were recomputed from the per-project
comparison CSVs after generation (means, group means, standard deviations, and
win counts) and matched the summary CSV exactly. Per-run provenance is printed
by `run_comparison.py` as an audit trail (which rows were read per project,
which run was selected as best/worst).
