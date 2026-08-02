# Results Section Rewrite Prompt

> Prompt to rewrite `tcc-overleaf/sections/results.tex` of the README-Gen TCC
> into a concise, data-driven, uniformly patterned results section.

---

## Role

Act as a scientific writer specialized in empirical software engineering.
You will rewrite the Results section of a LaTeX document. You are a data
presenter, not a narrator: every subsection exists to show data and state its
final result. No storytelling, no repeated methodology, no interpretation
beyond the single final-result sentence of each subsection (interpretation
belongs only in the Final Considerations and Research Questions subsections).

## Inputs (ground truth — never invent numbers)

- Human evaluation data: `simulations/data/{lang}/{pkg}/evaluation-legacy/`
  (human CSVs) and the values already validated in the current TCC.
- Automated README-Gen evaluation: `simulations/data/{lang}/{pkg}/evaluation/`
  (standardized 5-file contract, 3 runs + average).
- Automated README-AI evaluation:
  `simulations/data/{lang}/{pkg}/compare-readme-ai/evaluation/` (1 run).
- Comparison data (best/worst/mean vs single):
  `simulations/data/{lang}/{pkg}/compare-readme-ai/{pkg}_standard_comparison.csv`
  and `simulations/comparison/summary_readme_gen_vs_readme_ai.csv`.
- Verified aggregates: human correctness mean 75.33 (popular 99.05 / low
  27.89), completeness 98.01, ATRAK 100; automated README-Gen correctness
  mean 77.77 (popular 93.37 / low 46.56), best 81.92, worst 74.28,
  completeness 97.62, ATRAK 100; automated README-AI correctness 47.57
  (popular 45.70 / low 51.32), completeness 65.48, ATRAK 75.00; human-vs-
  automated mean difference +2.44 (popular −5.68, low +18.67), 12/12 verdict
  agreement at a 70% usability threshold; README-Gen best wins 11/12,
  worst wins 9/12 with 1 tie (loses SnakeMD and URI, ties CommandLauncher).

## Required structure (exactly these subsections, in this order)

1. **Human Evaluation** (of README-Gen)
2. **Automated README-Gen Evaluation**
3. **Automated README-AI Evaluation**
4. **Human vs. Automated README-Gen Evaluation**
5. **Automated README-Gen vs. Automated README-AI Evaluation**
6. **Overall View and Final Considerations** — the three evaluations in one
   grouped bar chart + closing considerations
7. **Answering the Research Questions**

## Uniform pattern — evaluation subsections (1–3)

Each of subsections 1–3 MUST have exactly the same shape; only the data and
the final result change:

- One intro sentence naming the evaluator, the target tool, and the number of
  runs aggregated.
- One table: rows = the 12 repositories (+ average row); columns =
  completeness, correctness, ATRAK. Same column order, same caption pattern
  ("<Evaluator> evaluation of <tool> (%, <aggregation>)").
- One final-result sentence: the three averages, and at most one clause on
  the dominant pattern (e.g., popularity stratification or the recurring
  failure mode). Nothing else.

## Uniform pattern — comparison subsections (4–5)

Same shape for both; only data and final result change:

- One intro sentence naming the two datasets being contrasted and the
  aggregation used.
- One table: subsection 4 = per-repository human vs. automated correctness
  with a difference column (+ average); subsection 5 = the best/worst/README-AI
  metric table (completeness, ATRAK, correctness overall/popular/low, win
  counts).
- One final-result sentence stating the agreement or the winner. For
  subsection 4 it must include: mean difference +2.44, direction (−5.68
  popular / +18.67 low), and the 12/12 verdict agreement at the 70%
  threshold. For subsection 5: best wins 11/12, worst wins 9/12 (1 tie), and
  the low-popularity inversion in one clause.
- FORBIDDEN: rank-correlation statistics (Spearman, Kendall) anywhere.

## Subsection 6 — Overall View and Final Considerations

- One grouped pgfplots bar chart (`pgfplots` is already loaded): 12
  repositories on the x-axis (popular group first, then low-popularity),
  three series — Human README-Gen, Automated README-Gen, Automated README-AI
  correctness.
- One short final-considerations paragraph (max ~6 sentences) synthesizing
  the three datasets: structure/ATRAK guaranteed by construction; correctness
  driven by popularity for README-Gen; README-AI flat across popularity and
  losing everywhere except where prior exposure is absent; the two evaluators
  agreeing on every verdict.

## Subsection 7 — Answering the Research Questions

Answer RQ1, RQ1.1, RQ2, RQ3 in bold-labeled paragraphs of at most 3 sentences
each, every claim cited to a table or the figure by `\ref`. RQ1.1 must use the
best/worst framing.

## Constraints

- Keep `\section{Results}\label{results}` and reference
  `Section~\ref{sec:baseline-comparison}` for the comparison protocol and
  `Section~\ref{sec:automated-eval}` for the rubric — do not restate either.
- Keep the footnote to the public project repository in the section intro.
- Total prose budget: every subsection is intro sentence + table/figure +
  final-result sentence (subsections 6–7 as specified above). If a sentence
  does not present data or state a result, delete it.
- Preserve compilability: booktabs-style tables consistent with the rest of
  the document, `\resizebox{\textwidth}{!}` for wide tables, labels unique.
- After writing, recompile the document and verify: 0 TeX errors, no
  undefined references, all table averages match the input aggregates.
