# Jacksons Documentation

Jacksons is a Java library ecosystem developed by FasterXML designed for processing JSON data efficiently. It provides high-performance data-binding capabilities to convert between JSON and Java objects, streaming APIs for incremental JSON processing, and tree models for manipulating JSON content dynamically.

The Jacksons project encompasses multiple core modules, including `jackson-core`, `jackson-databind`, and various data format modules for working beyond JSON (e.g., Smile, CBOR, YAML). It is widely used for serialization and deserialization of Java objects in REST APIs, configuration files, and data exchange scenarios.

---

## Conceptual Introduction

### Domain Concepts

- **JSON (JavaScript Object Notation):** A lightweight data-interchange format widely used for communication between services and applications.
- **Serialization:** Converting Java objects to JSON.
- **Deserialization:** Parsing JSON text into Java objects.
- **Data-binding:** Mapping JSON structures directly to Java objects using annotations or configuration.
- **Streaming API:** Incrementally reading and writing JSON content using a low-level tokenized API.
- **Tree Model:** An in-memory JSON tree representation (`JsonNode`), allowing traversal and manipulation of JSON content.
- **Annotations:** Java annotations like `@JsonProperty`, `@JsonIgnore`, used to customize the serialization/deserialization behavior.
- **Modules:** Extensions to support additional data types, formats, or integration techniques (e.g., Joda-Time, afterburner for performance).

### Mapping to API Terms

- `ObjectMapper`: Primary class for data binding and tree model operations.
- `JsonFactory`: Factory class for constructing streaming parsers and generators.
- Serializer and deserializer classes provide customizable serialization logic.
- Annotations on Java classes and properties guide data binding.
- `JsonNode` model supports flexible JSON tree manipulation.
- Various modules extend capabilities with specialized formats or performance enhancements.

---

## Execution Facts

### Core Classes and Methods Overview

| Class / Interface | Inputs                                                      | Outputs                                           | Errors / Side Effects                                               | Defaults / Constraints                                         |
| ----------------- | ----------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------- |
| `ObjectMapper`    | JSON content string, `InputStream`, `File`, or Java objects | Java objects, JSON string, `JsonNode`             | Throws `JsonProcessingException` on invalid input or mapping errors | Uses default configuration; supports custom modules & features |
| `.readValue()`    | JSON input and target Java class/type                       | Java object instance                              | Parsing errors, mapping exceptions                                  | Configurable via mapper features                               |
| `.writeValue()`   | Java object and output destination                          | Writes JSON to stream, file, or returns as string | IOExceptions if output fails                                        | Supports pretty printing, filtering, views                     |
| `JsonFactory`     | None or config                                              | Streaming parsers and generators                  | IOExceptions during streaming                                       | Configurable for buffering, feature toggles                    |
| `JsonNode`        | None (created via ObjectMapper or builders)                 | JSON tree nodes                                   | N/A                                                                 | Immutable: to modify, create copies via builders               |

### Annotations

- `@JsonProperty`: Binds JSON property to Java field or getter/setter.
- `@JsonIgnore`: Ignores property during serialization/deserialization.
- `@JsonCreator`: Marks constructors/factory methods for deserialization.
- Other annotations include `@JsonInclude`, `@JsonFormat`, `@JsonTypeInfo` for advanced control.

### Modules and Extensions

- Jackson has multiple modules like `jackson-datatype-jsr310` (Java 8 Date/Time API), `jackson-module-afterburner` (performance).
- Modules must be registered with the `ObjectMapper` instance for effect.

### Constraints

- Carefully handle cycles or references to avoid infinite recursion.
- Customize configuration to suit application needs (e.g., visibility rules).
- Thread safety: `ObjectMapper` is thread-safe after configuration.

---

## API Usage Patterns

### Pattern 1: Basic Serialization / Deserialization

#### What the code does

Converts Java POJOs (Plain Old Java Objects) to JSON and back by mapping fields automatically.

#### How it does it

- Instantiate a default `ObjectMapper`.
- Use `.writeValueAsString(obj)` to serialize.
- Use `.readValue(jsonString, POJOclass.class)` to deserialize.
- Leverages annotations and default naming strategies.

#### Why it’s structured that way

- Simplifies JSON handling with minimal boilerplate.
- Supports flexible configuration for customization.
- Abstracts JSON parsing mechanics under simple API calls.

#### Variation Points

- Customize serialization with annotations or custom serializers.
- Change naming strategy (camelCase, snake_case).
- Handle polymorphic types using `@JsonTypeInfo`.

---

### Pattern 2: Streaming API for Large Data

#### What the code does

Reads or writes JSON content token by token for memory-efficient processing of large JSON files or streams.

#### How it does it

- Use `JsonFactory` to create `JsonParser` or `JsonGenerator`.
- Iterate over tokens for parsing or produce tokens for writing.
- Process JSON without loading full content into memory.

#### Why it’s structured that way

- Provides scalable JSON parsing/writing.
- Allows incremental JSON updates or partial reads.

#### Variation Points

- Use `ObjectMapper` on top of `JsonParser` for hybrid modes.
- Apply filters or conditional token skipping.

---

### Pattern 3: Manipulating JSON Tree Model

#### What the code does

Creates, traverses, and modifies a tree representation of JSON data dynamically.

#### How it does it

- Use `ObjectMapper` to parse JSON into `JsonNode`.
- Access or modify nodes using API of `JsonNode` subclasses (`ObjectNode`, `ArrayNode`).
- Write back modified tree as JSON.

#### Why it’s structured that way

- Supports complex changes not easily done via binding.
- Allows partial updates and inspections.

#### Variation Points

- Create new nodes programmatically with node factories.
- Combine tree model with data binding for mixed scenarios.

---

## Example Pattern: Serialize and Deserialize a Simple POJO

```java
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.annotation.JsonProperty;

public class User {
    @JsonProperty("id")
    private int userId;
    @JsonProperty("name")
    private String userName;

    // Constructors, getters and setters omitted for brevity
}

public class Example {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();

        User user = new User();
        user.setUserId(1);
        user.setUserName("Alice");

        // Serialize Java object to JSON string
        String jsonString = mapper.writeValueAsString(user);
        System.out.println("Serialized JSON: " + jsonString);

        // Deserialize JSON string back to Java object
        User deserializedUser = mapper.readValue(jsonString, User.class);
        System.out.println("Deserialized User ID: " + deserializedUser.getUserId());
        System.out.println("Deserialized User Name: " + deserializedUser.getUserName());
    }
}
```

- **What:** Converts a simple User POJO to JSON and back.
- **How:** Uses `ObjectMapper`'s `writeValueAsString()` and `readValue()` methods.
- **Why:** Demonstrates basic Jackson data binding workflow.
- **Variation:** Add annotations for custom property names; handle nested objects.

---

## Additional Developer Notes

- Jackson is highly configurable for diverse JSON data handling requirements.
- Register custom modules to extend types or performance.
- Use `ObjectMapper` instances carefully since configuration changes are not thread-safe.
- Refer to official FasterXML Jackson documentation for detailed module guides and advanced features.
- Consider performance implications: use streaming API for large data, afterburner for speed boosts.
- Support for other data formats (YAML, XML, CBOR) requires adding corresponding modules.

---

This documentation integrates the core domain concepts of JSON data processing and the Jacksons ecosystem, explicit execution facts detailing inputs, outputs, errors, and constraints of key APIs, and common usage patterns enabling developers to robustly use the library for a variety of data-binding and streaming scenarios in Java applications.
