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

`node-uml` is a Node.js package designed to generate UML diagrams from your plain text descriptions. The tool helps developers and teams visually represent and document system architecture, classes, and relationships through UML diagrams automatically. It supports various diagram types including class diagrams and supports importing code to generate UML models.

The primary goal of `node-uml` is to simplify the process of creating and maintaining UML diagrams linked directly to source code, enabling better system understanding, design validation, and communication among developers.

## Features and Capabilities

- Support for generating output in SVG and other visual formats.
- Supports customization of output and diagram configuration.
- Useful for documentation, reverse engineering, and design validation.

## Installation

To install `node-uml`, you need Node.js installed on your system.

### Using npm

```bash
npm install -g node-uml
```

### Alternative: Use with npx (without global install)

```bash
npx node-uml <options>
```

The package works cross-platform on Linux, macOS, and Windows as long as Node.js is available.

## Usage and Examples

```javascript
const generate = require('node-uml')

const umlText = 'Bob -> Alice : hello'

generate(umlText, { path: '.', outputName: 'diagram.svg' }).then((resp) => console.log(resp))
```

## API Reference 

### generate

- Parameters:

  - `text` (string): Text representing the plantuml text
  - `options` (object):
  - - `options.type`: The type of image, can be any value in the list ["png", "svg", "txt"]
  - - `options.outputName`: The name of the image file that will be generated
  - - `options.path`: The path that the image will be generated

- Returns: Promise that resolves when generation completes.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request describing your modifications.

Ensure your code follows the existing style and includes tests for new functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/allanassis/node-uml/blob/master/LICENSE) file for details.

## Contact

- Author: Allan Assis
- Repository: [https://github.com/allanassis/node-uml](https://github.com/allanassis/node-uml)
- Issues and feature requests: [GitHub Issues](https://github.com/allanassis/node-uml/issues)

---

This README provides a focused overview for users and developers to understand what `node-uml` does, how to install and use it, and how to contribute or get support effectively.

```


"""