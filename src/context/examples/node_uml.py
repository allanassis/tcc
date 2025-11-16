node_uml_example = """
## 5.1 Example

### Input 
```
Generate API documentation for the package in the following address https://github.com/allanassis/node-uml. You can search on the web to understand what are the most importants parts to be added in the documentation.
You MUST output ONLY the documentation in Markdown format, no more data.
```

### Output

```.md
# node-uml

## Overview

`node-uml` is a Node.js package designed to generate UML (Unified Modeling Language) diagrams from plain text descriptions. It is a lightweight tool that helps developers and teams visualize and document software designs and architectures by converting textual UML descriptions into graphical diagrams. The tool supports generating various types of UML diagrams and outputs them in popular image formats such as SVG and PNG.

The main domain concepts involved in `node-uml` include:

- **UML Diagrams:** Visual representations of software system elements, such as classes, relationships, and interactions.
- **PlantUML Syntax:** A plain text language used to describe UML diagrams that the tool interprets.
- **Diagram Generation:** Transforming plain text UML descriptions into graphical formats using PlantUML rendering.

`node-uml` streamlines diagram creation, making it easier to maintain up-to-date software documentation, reverse engineer designs from code, and communicate architecture among teams.

---

## Installation

To use `node-uml`, you need Node.js installed on your system (version 10 or higher is recommended).

### Install via npm globally

```bash
npm install -g node-uml
```

### Install as a local dependency

```bash
npm install node-uml
```

`node-uml` works cross-platform (Linux, macOS, Windows) as long as Node.js is installed.

---

## Usage and Examples

### Usage as a Command-line Tool

Once installed globally, you can generate UML diagrams from a PlantUML text description file:

```bash
node-uml -i input.uml -o output.svg
```

Where:

- `-i` or `--input`: Path to the UML text file.
- `-o` or `--output`: Filename of the generated diagram image (SVG, PNG, or TXT).

### Usage in JavaScript Code

To generate UML diagrams programmatically:

```javascript
const generate = require('node-uml')

const umlText = `
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
@enduml
`

generate(umlText, { path: '.', outputName: 'diagram.svg', type: 'svg' })
  .then(() => {
    console.log('UML diagram generated successfully.')
  })
  .catch(err => {
    console.error('Error generating UML:', err)
  })
```

### Parameters for `generate` function:

- `text` (string): UML description in PlantUML syntax.
- `options` (object):
  - `path` (string): Directory path where output files will be saved.
  - `outputName` (string): Filename for the generated diagram.
  - `type` (string): Image format type (`svg`, `png`, or `txt`).

The promise resolves when diagram generation completes successfully.

---

## API Reference

### `generate(text, options)`

Generates a UML diagram based on the given PlantUML text.

- **Parameters:**
  - `text` (string): The PlantUML text description of the UML diagram.
  - `options` (object):
    - `type` (string): The format of the output diagram image. Values include `"png"`, `"svg"`, and `"txt"`.
    - `outputName` (string): The name of the output file for the generated diagram.
    - `path` (string): The directory path to save the output file.

- **Returns:** A `Promise` that resolves when the diagram is successfully generated, or rejects with an error if the generation fails.

### Example

```js
generate(umlText, { path: '.', outputName: 'diagram.svg', type: 'svg' })
  .then(() => console.log('Diagram created'))
  .catch(err => console.error(err))
```

---

## Contributing

Contributions to `node-uml` are welcome! To contribute improvements, fix bugs, or add features:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bugfix (`git checkout -b feature-name`).
3. Make your changes and add tests if applicable.
4. Commit your work (`git commit -m 'Add feature'`).
5. Push to your fork (`git push origin feature-name`).
6. Open a Pull Request describing your changes.

Please ensure your code follows the existing style and that you test your changes before submitting.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/allanassis/node-uml/blob/master/LICENSE) file for details.

---

## Contact

- **Author:** Allan Assis
- **Repository:** [https://github.com/allanassis/node-uml](https://github.com/allanassis/node-uml)
- **Issues and feature requests:** Use the [GitHub Issues](https://github.com/allanassis/node-uml/issues) page to report problems or suggest enhancements.

```


"""