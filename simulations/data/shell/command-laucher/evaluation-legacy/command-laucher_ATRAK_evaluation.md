# command-laucher — ATORAK Adherence Evaluation

**Methodology:** Section 4.4.3 of *README-Gen: Evaluating A Large Language Model for API Documentation Synthesis* (Andrade & Ribeiro, UERJ).

**Scope of this evaluation:** Completeness only — whether each Knowledge Element is *present* in the README, regardless of factual correctness. Per the TCC §4.4.3, each element is binary: Ki ∈ {0, 1}.

**Theory of Robust API Knowledge (ATORAK)** [Thayer et al. 2021] defines three Knowledge Elements:

- **KD — Domain Concepts:** Conceptual vocabulary, entities, and relationships that define the problem domain the API operates in.
- **KE — Execution Facts:** Concrete, verifiable facts about how the API behaves at runtime — commands, parameters, return values, environment requirements, installation steps.
- **KU — Usage Patterns:** Recurring, purposeful combinations of API calls that solve real problems, including the *what*, *how*, and *why* of usage.

Each element is binary: Ki ∈ {0, 1}. The adherence score per README is:

```
Kpercentage = (KD + KE + KU) / 3 × 100
```

The final score across the three generated READMEs is:

```
Kavg = (K1 + K2 + K3) / 3
```

> **Important note on completeness vs. correctness:** This evaluation does NOT assess whether the content is factually correct. As established in the correctness evaluation (§4.4.2), all three READMEs hallucinated the technology stack (Python/Node.js instead of Go). However, the ATORAK adherence evaluation asks only: *does the README contain the knowledge element?* A hallucinated but structurally present Domain Concepts section still satisfies KD = 1.

---

## Ground Truth Reference (for context only — not used in scoring)

- Tool: **command-laucher** (criteo/command-launcher) — a Go binary CLI package manager/dispatcher
- Repository: https://github.com/criteo/command-launcher
- Domain: CLI tooling, command dispatching, package management
- Note: All three READMEs misidentified the technology stack but still produced structured documentation with domain concepts, execution facts, and usage patterns.

---

## data1.md Evaluation

### Step-by-step Reasoning

**data1.md claims:** Command Launcher is a lightweight Python tool for automating CLI tasks, with a decorator-based API (`CommandLauncher`, `@launcher.command`, `@argument`).

---

#### KD — Domain Concepts

The README must contain conceptual vocabulary, entities, and relationships that define the problem domain the API operates in.

**Evidence in data1.md:**

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **Command Registration:** "Defines shell commands with associated parameters and metadata." — A conceptual entity describing how commands are registered in the system. ✅ Present.
- **Argument Parsing:** "Uses structured schemas to parse and validate command-line input arguments." — A conceptual entity describing input handling. ✅ Present.
- **Execution Environment:** "Supports setting and managing environment variables and contextual information." — A conceptual entity describing runtime context. ✅ Present.
- **Command Execution:** "Runs shell commands with controlled input, output, error handling, and status reporting." — A conceptual entity describing the core operation. ✅ Present.
- **Extensibility:** "Designed so new commands can be added as Python functions decorated or registered to the launcher." — A conceptual entity describing the extension model. ✅ Present.

The Overview also frames the domain as "simplify and automate the execution of command-line tasks" — a domain description that contextualizes the tool's purpose.

**Assessment:** data1.md contains a dedicated "Domain Concepts" subsection with five named and defined conceptual entities. The domain is identified (CLI automation/command dispatching). The vocabulary is internally consistent. Regardless of factual accuracy (the tool is Go, not Python), the Knowledge Element KD is structurally and semantically present.

**KD = 1** ✅

---

#### KE — Execution Facts

The README must contain concrete facts about how the API behaves at runtime: commands, parameters, return values, environment requirements, installation steps.

**Evidence in data1.md:**

*Installation facts:*
- `pip install command-launcher` — an installation command with a specific package manager and package name. ✅ Present (even if incorrect).
- `git clone https://github.com/xZepyx/command-launcher.git` + `pip install .` — an alternative installation path. ✅ Present.
- "Python 3.7 or higher" — an environment requirement. ✅ Present.

*API Reference facts:*
- `CommandLauncher` class — documented with methods `command(name: str)` (decorator) and `run(args: list = None)`. Parameter names and types are specified. ✅ Present.
- `argument` decorator — documented with parameters `name` (str), `type` (type), `default` (optional), `help` (str). ✅ Present.
- Return behavior: `run()` "Parses input arguments and executes corresponding command." ✅ Present.

*CLI execution facts:*
- `command-launcher <command> [options] [arguments]` — a CLI invocation pattern with argument structure. ✅ Present.
- `command-launcher --help` — a specific executable command. ✅ Present.

**Assessment:** data1.md contains installation commands, environment requirements, API method signatures with typed parameters, and CLI invocation patterns. These are all execution facts — concrete, specific, and actionable (even if factually wrong). The Knowledge Element KE is structurally and semantically present.

**KE = 1** ✅

---

#### KU — Usage Patterns

The README must present recurring, purposeful combinations of API calls that solve real problems, communicating *what*, *how*, and *why*.

**Evidence in data1.md:**

The "Usage and Examples" section presents the following patterns:

1. **Basic CLI invocation** — `command-launcher <command> [options]` / `command-launcher --help`: Shows the fundamental invocation pattern. *What*: invoke a registered command. *How*: use the CLI with command name and options. *Why*: simple user interface for on-demand command execution. ✅ Present.

2. **Defining a Command (Usage Pattern)** — Full code example showing `CommandLauncher()`, `@launcher.command('greet')`, `@argument('name', ...)`, function definition, `launcher.run()`, and terminal invocation `python myscript.py greet --name John` with expected output `Hello, John!`: Shows the complete command definition and execution lifecycle. *What*: define and run a custom command. *How*: decorator pattern + `launcher.run()`. *Why*: structured way to add new commands. ✅ Present.

3. **Running Shell Commands** — Prose description of defining commands to execute shell instructions with environment variable support and I/O redirection. *What*: execute shell instructions. *How*: via launcher environment. *Why*: supports environment variables and I/O redirection. ✅ Present (prose pattern, not code).

**Assessment:** data1.md presents two code-based usage patterns and one prose pattern. Each pattern communicates a purposeful combination of API calls with context about what it does and how to execute it. The *why* is implied through section headings and contextual descriptions. The patterns cover the core workflow (define → run). The Knowledge Element KU is structurally and semantically present.

**KU = 1** ✅

---

### data1.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data1.md ATORAK Score: 100**

---

## data2.md Evaluation

### Step-by-step Reasoning

**data2.md claims:** `command-launcher` is a lightweight Python library for running shell commands from Python scripts, with `CommandLauncher` and `CommandResult` classes.

---

#### KD — Domain Concepts

**Evidence in data2.md:**

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **Command Execution:** "Running shell commands or external programs from Python." — A conceptual entity describing the core operation. ✅ Present.
- **Process Management:** "Starting and handling subprocesses with control over input/output." — A conceptual entity describing subprocess lifecycle. ✅ Present.
- **Result Handling:** "Capturing the standard output (stdout), standard error (stderr), and exit status of commands." — A conceptual entity describing output capture. ✅ Present.
- **Timeouts:** "Ability to limit the execution time of the commands." — A conceptual entity describing execution control. ✅ Present.

The Overview also states: "These core concepts allow the user to integrate shell command functionality seamlessly into Python applications, encouraging robust error handling and output processing." — This sentence explicitly frames the relationship between the concepts and the domain purpose.

**Assessment:** data2.md contains a dedicated "Domain Concepts" subsection with four named and defined conceptual entities. The domain is identified (shell command execution / subprocess management). The vocabulary is internally consistent and the relationships between concepts are articulated. The Knowledge Element KD is structurally and semantically present.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data2.md:**

*Installation facts:*
- `pip install command-launcher` — installation command. ✅ Present.
- "Python 3.6 or later" — environment requirement. ✅ Present.

*API Reference facts:*
- `CommandLauncher.run(command: str, timeout: Optional[int] = None, input_data: Optional[str] = None) -> CommandResult` — full method signature with typed parameters and return type. ✅ Present.
- `CommandResult` class with attributes: `stdout` (str), `stderr` (str), `exit_code` (int), `timed_out` (bool) — typed attribute list. ✅ Present.
- Parameter descriptions: `command` (str), `timeout` (int, optional), `input_data` (str, optional) — all with types and descriptions. ✅ Present.

**Assessment:** data2.md contains installation commands, environment requirements, a fully typed method signature with parameter descriptions, a return type, and a result class with typed attributes. These are all execution facts. The Knowledge Element KE is structurally and semantically present.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data2.md:**

The "Usage and Examples" section presents the following patterns:

1. **Basic Usage Example** — `CommandLauncher()` → `launcher.run("echo Hello, World!")` → `result.stdout` / `result.stderr` / `result.exit_code` with expected output block: Shows the fundamental run-and-capture pattern. *What*: run a command and capture output. *How*: instantiate launcher, call `run()`, access result attributes. *Why*: simple interface for on-demand command execution. ✅ Present.

2. **Running a Command with a Timeout** — `launcher.run("sleep 5", timeout=2)` → `result.timed_out` check: Shows the timeout handling pattern. *What*: run a command with a time limit. *How*: pass `timeout` parameter, check `timed_out` attribute. *Why*: "handling cases where the command takes too long." ✅ Present (explicit *why* stated in prose).

3. **Running Commands with Input Data** — `launcher.run("cat", input_data="Hello from stdin\n")` → `result.stdout`: Shows the stdin piping pattern. *What*: pipe data to a command's stdin. *How*: pass `input_data` parameter. *Why*: "pipes the string to the command's standard input." ✅ Present.

**Assessment:** data2.md presents three distinct usage patterns, each with a code example, expected output or behavior description, and an explicit *why* statement. The patterns cover the core workflows (basic execution, timeout handling, stdin piping). The Knowledge Element KU is structurally and semantically present.

**KU = 1** ✅

---

### data2.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data2.md ATORAK Score: 100**

---

## data3.md Evaluation

### Step-by-step Reasoning

**data3.md claims:** `command-launcher` is a simple Node.js utility for launching external commands from JavaScript, with callback, Promise, and synchronous APIs.

---

#### KD — Domain Concepts

**Evidence in data3.md:**

The "Overview" section contains an explicit "Domain Concepts" subsection listing:

- **Command Execution:** "Running shell commands or executables from a script." — A conceptual entity describing the core operation. ✅ Present.
- **Process Management:** "Handling asynchronous command execution, capturing standard output, standard error, and managing exit codes." — A conceptual entity describing subprocess lifecycle. ✅ Present.
- **Cross-Platform Compatibility:** "Ensuring commands execute correctly on supported operating systems." — A conceptual entity describing portability. ✅ Present.
- **Callback and Promise APIs:** "Supporting both callback functions and Promises for handling command execution results." — A conceptual entity describing the async programming model. ✅ Present.

The Overview also describes the tool as "especially useful for developers who want to automate or integrate command line processes within their Node.js applications" — a domain framing statement.

**Assessment:** data3.md contains a dedicated "Domain Concepts" subsection with four named and defined conceptual entities. The domain is identified (command execution / process management in Node.js). The vocabulary is internally consistent. The Knowledge Element KD is structurally and semantically present.

**KD = 1** ✅

---

#### KE — Execution Facts

**Evidence in data3.md:**

*Installation facts:*
- `npm install command-launcher` — installation command. ✅ Present.
- `yarn add command-launcher` — alternative installation command. ✅ Present.
- "Node.js 10 or later" — environment requirement. ✅ Present.

*API Reference facts:*
- `commandLauncher(command: string, args?: string[], callback?: function)` — full function signature with typed parameters, optional markers, and callback signature `(error, stdout, stderr)`. ✅ Present.
- `commandLauncher.exec(command: string, args?: string[]): Promise<{stdout: string, stderr: string}>` — async method with typed return. ✅ Present.
- `commandLauncher.execSync(command: string, args?: string[]): Buffer` — sync method with typed return and throws behavior. ✅ Present.
- Return value descriptions: child process instance, Promise resolving to `{stdout, stderr}`, Buffer. ✅ Present.

**Assessment:** data3.md contains installation commands (two package managers), environment requirements, three fully typed function signatures with parameter descriptions, return types, and error behavior. These are all execution facts. The Knowledge Element KE is structurally and semantically present.

**KE = 1** ✅

---

#### KU — Usage Patterns

**Evidence in data3.md:**

The "Usage and Examples" section presents the following patterns:

1. **Basic Usage with Callbacks** — `commandLauncher("ls", ["-l", "/usr"], (error, stdout, stderr) => {...})`: Shows the callback-based invocation pattern. *What*: run a command and handle output via callback. *How*: pass command, args array, and callback function. *Why*: "prints the output or any errors." ✅ Present.

2. **Usage with Promises** — `async function runCommand() { const { stdout, stderr } = await commandLauncher.exec("node", ["--version"]); }`: Shows the async/await pattern. *What*: run a command using Promise-based API. *How*: `await commandLauncher.exec()` inside try/catch. *Why*: "async/await usage." ✅ Present.

3. **Running Commands Synchronously** — `const result = commandLauncher.execSync("echo", ["Hello World"])`: Shows the synchronous execution pattern. *What*: run a command synchronously. *How*: `commandLauncher.execSync()`. *Why*: "If synchronous execution is needed (blocking the event loop)." ✅ Present (explicit *why* stated in prose).

**Assessment:** data3.md presents three distinct usage patterns, each with a complete code example and contextual description. The patterns cover the three execution modes (callback, Promise, synchronous). Each pattern communicates *what* it does, *how* to execute it, and *why* it is useful. The Knowledge Element KU is structurally and semantically present.

**KU = 1** ✅

---

### data3.md ATORAK Score

| Knowledge Element | Present | Score |
|-------------------|---------|-------|
| KD — Domain Concepts | ✅ Yes | 1 |
| KE — Execution Facts | ✅ Yes | 1 |
| KU — Usage Patterns | ✅ Yes | 1 |

```
Kpercentage = (1 + 1 + 1) / 3 × 100 = 100
```

**data3.md ATORAK Score: 100**

---

## Summary: All Three command-laucher READMEs — ATORAK Adherence

| README | KD (Domain Concepts) | KE (Execution Facts) | KU (Usage Patterns) | Kpercentage |
|--------|---------------------|---------------------|---------------------|-------------|
| data1.md | 1 | 1 | 1 | **100** |
| data2.md | 1 | 1 | 1 | **100** |
| data3.md | 1 | 1 | 1 | **100** |

### Final Average Score (Equation 16 from TCC §4.4.3)

```
Kavg = (100 + 100 + 100) / 3 = 100
```

**command-laucher ATORAK Average Score: 100**

---

## Analysis and Observations

**Why all three score 100 on ATORAK adherence despite catastrophic correctness failure:**

This result reveals a critical dissociation between ATORAK adherence and factual correctness. The correctness evaluation (§4.4.2) assigned all three READMEs a score of 33.33 — the lowest possible score given only title and license were correct. Yet all three score 100 on ATORAK adherence.

**KD (Domain Concepts) — all three score 1:**
All three READMEs include an explicit "Domain Concepts" subsection in the Overview. Each README defines 4–5 named conceptual entities with descriptions. The entities are internally consistent and domain-appropriate for the technology the LLM hallucinated (Python subprocess wrapper, Python CLI framework, Node.js child process utility). The presence of a structured domain vocabulary satisfies KD regardless of whether it describes the correct tool.

**KE (Execution Facts) — all three score 1:**
All three READMEs provide installation commands with specific package managers and version requirements, API method signatures with typed parameters and return values, and CLI invocation patterns. These are all execution facts — concrete, specific, and actionable. The fact that they describe a hallucinated API does not affect the presence of the knowledge element.

**KU (Usage Patterns) — all three score 1:**
All three READMEs present multiple named usage patterns with complete code examples, expected outputs, and contextual descriptions explaining *what*, *how*, and *why*. Each pattern is a purposeful combination of API calls that solves a real problem within the hallucinated domain. The patterns are well-structured and cover the core workflows of the described (hallucinated) tool.

**Key insight — completeness vs. correctness divergence:**
The command-laucher case is the most extreme example of ATORAK completeness being decoupled from correctness. The LLM generated structurally complete, well-organized READMEs that fully satisfy all three ATORAK knowledge elements — but for entirely fictional tools. This suggests that the ATORAK adherence metric measures the *structural quality* of the documentation format, not the *semantic accuracy* of its content.

**Implication for the TCC:**
A README can score 100 on ATORAK adherence and 33.33 on correctness simultaneously. This validates the TCC's decision to treat these as separate evaluation dimensions (§4.4.1, §4.4.2, §4.4.3). The ATORAK score reflects whether the LLM understood *how to structure* API documentation; the correctness score reflects whether it understood *what to document*.
