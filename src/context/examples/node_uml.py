node_uml_example = """
## 5.1 Example

### Input 
```
Generate API documentation for the package in the following address https://github.com/allanassis/node-uml. You can search on the web to understand what are the most importants parts to be added in the documentation.
You MUST output ONLY the documentation in Markdown format, no more data.
```

### Output

```.md
# node-uml Documentation

Node-uml is a Node.js package that allows developers to generate UML (Unified Modeling Language) models by utilizing the PlantUML server. This library abstracts the process of creating UML diagrams programmatically and integrates with the PlantUML online service for rendering diagrams.

---

## Conceptual Introduction

### Domain Concepts

- **UML (Unified Modeling Language):** A standardized modeling language in software engineering that provides a way to visualize a system's architectural blueprints.
- **PlantUML:** An open-source tool that allows the creation of UML diagrams from plain text descriptions.
- **Node.js Package:** A library designed to be used in Node.js environments to facilitate UML diagram generation.
- **UML Models:** Visual diagrams representing various aspects of software systems like class diagrams, sequence diagrams, use case diagrams, etc.

### Mapping to API Terms

- The library uses PlantUML server to convert text-based UML descriptions into images or diagrams.
- Developers interact with the library by providing UML syntax (text) which the library sends to the PlantUML server and obtains UML models.
- The focus is on simplifying communication with PlantUML to programmatically generate diagrams in Node.js applications.

---

## Execution Facts

### Overview

#### Methods

- `generate(umlText, options).then()`: This method receives two parameters, the text representing the UML diagram and an object contains options to the method.

##### Method Input
- umlText: A string containing the textual UML description in PlantUML syntax.
- options: An object containing options for the method. The options include:
    options.type: The type of image, can be any value in the list ["png", "gif", "jpeg"]
    options.outputName: The name of the image file that will be generated
    options.path: The path that the image will be generated

##### Method Input
The generated image with the UML diagram rendered.


### Constraints

- Requires Internet connection to access the PlantUML server.
- Depends on the uptime and response of the PlantUML server.
- Generated diagrams depend entirely on the correctness of provided PlantUML syntax.

---

## API Usage Patterns

### Typical Use Case: Generating UML Diagrams in Node.js

#### What the code does

- It takes a user-defined UML text description.
- Sends it to the PlantUML server through the node-uml package.
- Retrieves a image output which can be embedded or displayed.

#### How it does it

- Encapsulates HTTP request to PlantUML server.
- Encodes UML text appropriately for PlantUML decoding.
- Returns diagram links or data buffers for rendering.

#### Why it's structured that way

- Decouples UML diagram generation from the rendering engine.
- Provides an abstraction layer so that developers focus on UML text.
- Leverages PlantUML's powerful diagram parsing and rendering without managing a local server.

#### Variation Points

- Switch between output formats like PNG, SVG, or ASCII depending on developer needs.
- Use synchronous or asynchronous methods based on application flow.

---

## Example Pattern

```javascript
const uml = require('node-uml');

const umlText = `
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
@enduml
`;

// Generate UML diagram URL
uml.generateDiagram(umlText)
  .then(url => {
    console.log('UML diagram URL:', url);
  })
  .catch(error => {
    console.error('Error generating UML:', error);
  });
```

- **What:** This example generates a.uml diagram URL based on a simple sequence diagram.
- **How:** It calls a method that sends the UML text to PlantUML server and returns a diagram URL.
- **Why:** Shows simple integration with the library to produce visual UML from text.
- **Variation:** Change `umlText` to create different UML diagram types; can handle error scenarios for stability.

---

## Additional Notes for Developers

- Ensure UML text follows PlantUML syntax strictly for valid output.
- Consider caching diagram URLs for performance in repeated requests.
- Explore different rendering options provided by PlantUML through customization in the library if supported.

---

This documentation integrates domain concepts, execution facts, and usage patterns to create a robust understanding of the node-uml package for developers wishing to generate UML diagrams programmatically with Node.js.
```


"""