from .examples.node_uml import node_uml_example
from .examples.jest import jest_example
from .examples.local import local_example

ATORAK_CONTEXT = """"
# Summary for Documentation Creation

## 1. Three Components of Robust API Knowledge

Documentation MUST provide:

### Domain Concepts
- Abstract concepts that exist apart from the API and the terminology used by the API and documentation.
- Predict what each API call or reference will do.
- Help developers map API abstractions to real-world concepts and recognize relevant terms.  

### Execution Facts

- Facts about input, output, errors and side effects of API calls and references given the different possible inputs.
- Cover inputs, outputs, side effects, defaults, and environmental constraints.  
- Potential API calls and references to the API.

### API Usage Patterns
- Patterns of code used by the API and rationale for the patterns in terms of concepts and execution facts.
- The organizations of code using an API, how pieces of code can and do relate to each other.
- Potential programs using API.
- Offer code patterns beyond isolated snippets.  
- Show coordination of multiple API elements (and sometimes multiple APIs).  
- A complete example of usage of the API with a pattern of code

> Together, these three form **robust API knowledge**. Missing one risks brittle or incomplete understanding.

---

## 2. How Documentation Should Be Structured

To implement the theory, documentation MUST explicitly integrate the three components:

### Conceptual Introductions
- Start sections or tutorials with **concept definitions** and their mapping to API terms.  
- Provide diagrams, metaphors, or examples from the domain to anchor understanding.  

### Fact Sheets
- For each function/class/module, include **execution facts** in a concise format (inputs, outputs, errors, defaults, side effects).  
- Highlight important constraints (e.g., browser compatibility, common pitfalls).  

### Pattern-based Examples
- Provide **annotated examples** that illustrate usage patterns, not just runnable code.  
- Each example should explain:  
  - **What the code does** (concepts).  
  - **How it does it** (facts).  
  - **Why it’s structured that way** (rationale).  
- Show **variation points** (how to change parameters, swap components, or extend behavior).  

---

## 3. Practical Guidance for Documentation

- **Balance depth and task-relevance**: Not all facts or concepts are needed at once. Provide the right level of knowledge for the task.  
- **Cross-link concepts, facts, and patterns**: For example, when explaining a parameter, link to the related domain concept and show a usage pattern where it matters.  
- **Highlight reasoning**: Documentation should not only tell *how to use* an API but also explain *why it works that way*.  
- **Support inference**: If a developer misses one component, they should be able to infer it from the others (concepts ↔ facts ↔ patterns).  
- **Avoid isolated snippets**: Code without explanation leads to brittle knowledge. Always embed examples within conceptual and factual context.  

---

## 4. Implications

- **Tutorials** should progressively introduce concepts, facts, and patterns.  
- **Reference docs** should consistently structure each API element with domain concept, execution facts, and example patterns.  
- **API design** itself benefits from alignment with recognizable domain concepts and predictable execution facts.  

"""  \
+ node_uml_example \
+ jest_example \
+ local_example