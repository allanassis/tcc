# Standard README Evaluation Prompt

> Generic, tool-agnostic prompt for evaluating README files. It is not tied to
> any specific study, project sample, or generation tool. All study-specific
> values are supplied through the parameters below (for the TCC study, see
> `simulations/tcc-run-manifest.md`).

---

## Role

Act as a senior computer science researcher with expertise in software
documentation quality assessment. You will evaluate one or more README files
produced for a software project, applying a deterministic, rule-based rubric.
Your evaluation must be reproducible: another evaluator applying the same rules
to the same files must reach the same scores.

## Parameters

Fill these before executing:

| Parameter | Description |
|---|---|
| `{project_name}` | Name of the documented project |
| `{repository_url}` | URL of the project repository (ground-truth source) |
| `{core_functionality}` | One-line description of the project's expected primary functionality. If not provided, derive it from the repository before evaluating and record how it was derived. |
| `{readme_files}` | Ordered list of README file paths to evaluate |
| `{tool_name}` | Name of the tool/approach that generated the READMEs |
| `{output_folder}` | Folder where the five output files must be written |
| `{output_prefix}` | Filename prefix for the output files |

## Ground Rules

1. Evaluate **one README at a time**, in the order given by `{readme_files}`.
   Use explicit step-by-step reasoning for every rule.
2. Rely **only** on this rubric and the raw README files. Do not use any prior
   evaluation of these files.
3. Cross-check factual claims against `{repository_url}`, the project's
   official documentation, and the installed artifact. **Cite every source
   you cross-checked** in the reasoning documents.
4. **Execute** all installation commands and code snippets in a clean,
   isolated environment. Record commands, outputs, and pass/fail evidence.
5. Every rule is a binary check `V_i ∈ {0, 1}`. No partial credit within a
   rule.
6. Unresolved template placeholders (e.g., `{entrypoint}`,
   `INSERT-COMMAND-HERE`, `{venv}`) automatically fail any execution-related
   rule they appear in.
7. Content outside the rubric's sections (e.g., project file trees, badges,
   contribution workflows) is ignored, **except** when it is the only carrier
   of information a rubric section expects — in that case evaluate that
   content under the corresponding section and say so explicitly.
8. If a README lacks a section entirely, that section scores 0 in
   correctness and 0 in completeness.

---

## Dimension 1 — Structural Completeness

Check the presence of **seven elements**. An element counts as present (1)
only when the README presents the expected information — a heading alone is
not enough.

| # | Element | Expected information |
|---|---|---|
| 1 | Project Title | The project or tool name |
| 2 | Overview | Purpose, main goal, and functionality of the project |
| 3 | Installation | Steps to install the tool and set up the environment |
| 4 | Usage and Examples | Runnable examples demonstrating how to use the tool |
| 5 | API Reference | Main functions, classes, or endpoints with parameters |
| 6 | License | The license under which the project is distributed |
| 7 | Core Functionality | The README documents `{core_functionality}` |

Score per README: `completeness = (Σ S_i / 7) × 100`.

---

## Dimension 2 — Correctness

Each section is evaluated with deterministic verification rules. Section
scores are percentages; the overall score is the unweighted mean of the six
section scores:

```
C_R = (T + O + I + U + A + L) / 6
```

### Project Title (T) — 3 rules

1. The title exactly matches the repository name or officially documented
   project name.
2. The title does not describe a different project.
3. The title does not contain hallucinated terminology not present in the
   repository.

`T = (V1 + V2 + V3) / 3 × 100`

### Overview (O) — 5 rules

1. The primary functionality of the repository is correctly described.
2. The described functionality is supported by repository artifacts.
3. The overview does not describe unsupported features.
4. The overview correctly identifies the software domain.
5. The overview terminology matches the repository terminology.

`O = (Σ V_i / 5) × 100`

### Installation (I) — 5 rules (executed)

Execute all installation commands exactly as documented, in an isolated
environment.

1. All required dependencies are explicitly declared.
2. The installation commands execute without modification.
3. The installation produces no unresolved dependency errors.
4. The documented environment requirements are correct.
5. The installation process produces the expected executable artifact.

`I = (Σ V_i / 5) × 100`

### Usage and Examples (U) — 5 rules per snippet (executed)

Execute each code snippet independently in a clean environment. A snippet
passes (E_i = 1) **only if all five rules hold**:

1. The snippet executes successfully without manual modification
   (adding missing imports is the only permitted intervention, and must be
   recorded).
2. All required imports and dependencies are explicitly documented.
3. The snippet produces the documented output (if an output is documented).
4. The snippet does not generate runtime exceptions.
5. The snippet behavior matches the surrounding textual description.

`U = (Σ E_i / k) × 100`, where `k` is the number of executable snippets. The E_i from `0` to `k`.

### API Reference (A) — 6 rules per element

Validate each documented function, class, method, or endpoint against the
repository source code and official API documentation. An element passes
(A_i = 1) **only if all six rules hold**:

1. The documented API element exists in the repository.
2. Function and parameter names are correct.
3. Parameter types match the implementation.
4. Return values match the implementation behavior.
5. The documented behavior is consistent with execution results.
6. The element is not a deprecated or removed API documented as current.

`A = (Σ A_i / n) × 100`, where `n` is the number of documented API elements. The A_i from `0` to `n`.

### License (L) — 3 rules

1. The documented license matches the repository LICENSE file.
2. The license identifier is valid.
3. The README does not contain conflicting licensing information.

`L = (V1 + V2 + V3) / 3 × 100`

---

## Dimension 3 — Adherence to the Theory of Robust API Knowledge (ATRAK)

Check the binary presence of the three Knowledge Elements
[Thayer et al. 2021]. This dimension assesses **presence, not correctness**.

- **K_D — Domain Concepts:** the fundamental entities and abstractions of the
  problem domain, with the conceptual vocabulary needed to understand what the
  software represents.
- **K_E — Execution Facts:** verifiable facts about runtime behavior — inputs,
  outputs, return types, dependencies, configuration, installation,
  constraints.
- **K_U — Usage Patterns:** purposeful demonstrations of how the software is
  applied — code examples, tutorials, what/how/why of use.

**"Listed" is not "communicated":** a feature bullet list or table that only
names concepts, without defining them or teaching the conceptual vocabulary,
does **not** satisfy K_D. Broken or placeholder commands do **not** satisfy
K_E. Examples that do not show real API usage do **not** satisfy K_U.

`K = (K_D + K_E + K_U) / 3 × 100` per README.

---

## Output Contract

Write exactly **five files** to `{output_folder}`. When multiple READMEs are
evaluated, the `average` row is the arithmetic mean over all of them; with a
single README, the `average` row equals that README's row.

### 1. `{output_prefix}_completeness.csv`

```
Project Title,Overview,Installation,Usage and Examples,API Reference,License,Core functionality
<one binary row per README, in the order of {readme_files}>
```

### 2. `{output_prefix}_correctness_results.csv`

```
project,readme,title_score,overview_score,installation_score,usage_score,api_score,license_score,correctness_score
<one row per README>
<project>,average,<per-column means>
```

### 3. `{output_prefix}_correctness_evaluation.md`

Step-by-step reasoning: for each README, every section's rules with pass/fail
evidence, snippet execution tables (snippet, execution result, output match,
score), API element validation tables, the section score computations, and the
list of cross-checked documentation sources.

### 4. `{output_prefix}_completeness_ATRAK.csv`

```
project,readme,domain_concepts,execution_facts,usage_patterns,atrak_score
<one row per README>
<project>,average,<per-column means>
```

### 5. `{output_prefix}_ATRAK_evaluation.md`

Reasoning document: a Ground Truth Reference block (project, repository,
domain, core domain entities, core execution facts), then per-README evidence
and verdict for each of K_D, K_E, K_U.

---

## Final Step

After all READMEs are evaluated, print a summary table (README × completeness,
correctness, ATRAK) and verify every `average` row is arithmetically
consistent with the per-README rows before finishing.
