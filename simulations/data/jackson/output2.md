# Jackson Library Documentation

Jackson is a high-performance, feature-rich Java library for processing JSON data. It provides a suite of data-binding tools for converting Java objects to and from JSON, along with streaming and tree-model APIs for efficient JSON parsing and generation. Jackson is widely used for JSON serialization and deserialization within Java applications due to its flexibility and speed.

---

## Conceptual Introduction

### Domain Concepts

- **JSON Processing:** Jackson enables Java applications to convert between Java objects and JSON (JavaScript Object Notation), a lightweight data interchange format.
- **Data Binding:** The process of mapping JSON data to Java objects (deserialization) and serializing Java objects into JSON strings.
- **Streaming API:** Provides forward-only, incremental reading and writing of JSON content, enabling low-level access and efficient processing of large JSON streams.
- **Tree Model:** Represents JSON content as a tree of nodes (JsonNode), allowing flexible in-memory manipulation without binding to POJOs.
- **Annotations:** Jackson offers annotations (e.g., `@JsonProperty`, `@JsonIgnore`) to customize serialization/deserialization behavior.
- **Modules:** Extend Jackson's capabilities to support additional data types, formats, and features (e.g., JavaTimeModule for Java 8 date/time classes).
- **ObjectMapper:** The primary class responsible for serialization and deserialization operations.

### Mapping to API Terms

- `ObjectMapper`: The main entry point for serialization and deserialization. Provides methods like `readValue()`, `writeValue()`.
- `JsonParser` and `JsonGenerator`: Core streaming API classes for reading and writing JSON tokens.
- `JsonNode`: Root of Jackson's Tree Model used to navigate and manipulate JSON as a tree.
- Annotation classes such as `@JsonProperty`, `@JsonCreator` control how Java properties map to JSON.
- Specialized modules (e.g., `jackson-datatype-jsr310`) can be registered with `ObjectMapper` to handle specific data types.

---

## Execution Facts

### Core Classes and Methods

| API Element                                   | Inputs                                                     | Outputs                                     | Errors / Side Effects                                | Defaults / Constraints                                  |
| --------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------- |
| `ObjectMapper.readValue(json, Class<T>)`      | JSON content as String/InputStream/File, target Java class | Instance of Java class (`T`)                | Throws `JsonProcessingException` on malformed JSON   | Requires properly configured mapper for custom classes  |
| `ObjectMapper.writeValue(File, Object)`       | Java object                                                | JSON written to File                        | Throws IOException for I/O errors                    | Default serialization includes all non-transient fields |
| `ObjectMapper.convertValue(Object, Class<T>)` | Java object, target class                                  | Converted Java object of target type        | Can throw `IllegalArgumentException` if incompatible | Useful for transforming objects within Java             |
| `JsonParser.nextToken()`                      | None                                                       | JSON token such as START_OBJECT, FIELD_NAME | Throws IOException on input failure                  | Used for incremental, streaming parsing                 |
| `JsonGenerator.writeStartObject()`            | None                                                       | Writes start object token to output         | Throws IOException on output failure                 | Must be paired correctly with writeEndObject()          |
| `JsonNode.get(String fieldName)`              | Field name                                                 | Child JsonNode or null                      | N/A                                                  | Null if field not present                               |

### Annotations

- `@JsonProperty`: Customize JSON property name.
- `@JsonIgnore`: Exclude property from serialization and/or deserialization.
- `@JsonCreator`: Define constructors or factory methods to use during deserialization.
- `@JsonInclude`: Control inclusion policies (e.g., non-null, non-empty).

### Modules and Extensions

- Register modules with `ObjectMapper.registerModule(Module module)` to add support for specialized types.
- Examples include `JavaTimeModule` for Java 8 date/time, `AfterburnerModule` for performance optimizations.

### Constraints and Environment

- Supports Java SE 6 and above; specific modules may require newer JDK versions.
- JSON input must conform to expected structure or mapping errors will occur.
- Streaming API requires careful token management to avoid malformed output.

---

## API Usage Patterns

### Pattern 1: Basic Serialization and Deserialization with ObjectMapper

#### What the code does

Converts between Java objects and JSON strings or files, enabling data interchange or persistence.

#### How it does it

- Uses the central `ObjectMapper` instance.
- Calls `readValue()` with JSON input and target class to deserialize.
- Calls `writeValue()` to serialize Java object back to JSON format.

#### Why it’s structured that way

- Provides straightforward conversion with minimal configuration for common use cases.
- Abstracts low-level JSON parsing details.
- Supports customization via modules and annotations.

#### Variation Points

- Customize serialization behaviors using annotations on POJOs.
- Use configuration options on `ObjectMapper` (e.g., date formatting, visibility).
- Handle different input/output sources (String, File, InputStream).

---

### Pattern 2: Streaming JSON Parsing and Generation

#### What the code does

Efficiently reads or writes JSON content token by token, suitable for large streaming data.

#### How it does it

- Instantiate `JsonParser` to pull JSON tokens from input.
- Use token-based logic to process JSON content incrementally.
- Use `JsonGenerator` to write JSON tokens to output stream.

#### Why it’s structured that way

- Minimizes memory usage compared to tree or data binding models.
- Allows complex or manual JSON processing workflows.

#### Variation Points

- Combine with data binding for hybrid approaches.
- Customize token handling for partial object processing.

---

### Pattern 3: Tree Model Manipulation with JsonNode

#### What the code does

Represents JSON content as a mutable tree of nodes for flexible inspection or modification.

#### How it does it

- Parse JSON content into a `JsonNode` tree via `ObjectMapper.readTree()`.
- Traverse or modify nodes using methods like `get()`, `path()`, and setters.
- Serialize changed tree back to JSON when needed.

#### Why it’s structured that way

- Supports cases where structures are dynamic or not directly mapped to POJOs.
- Enables selective updates without full binding.

#### Variation Points

- Use `ObjectNode` or `ArrayNode` subclasses for specific node types.
- Combine with `ObjectMapper` to convert between trees and objects.

---

## Example Pattern: Basic Object Serialization and Deserialization

```java
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.annotation.JsonProperty;

public class User {
    @JsonProperty("username")
    private String name;
    private int age;

    // Constructors, getters, setters
    public User() {}
    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}

public class JacksonExample {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();

        // Serialization: Java object to JSON string
        User user = new User("johndoe", 30);
        String jsonString = mapper.writeValueAsString(user);
        System.out.println(jsonString);
        // Output: {"username":"johndoe","age":30}

        // Deserialization: JSON string to Java object
        String inputJson = "{\"username\":\"janedoe\",\"age\":25}";
        User userObj = mapper.readValue(inputJson, User.class);
        System.out.println(userObj.getName() + ", " + userObj.getAge());
        // Output: janedoe, 25
    }
}
```

- **What:** Illustrates converting a Java User object to JSON string and back.
- **How:** Uses `ObjectMapper.writeValueAsString()` and `readValue()` for serialization and deserialization.
- **Why:** Demonstrates typical Jackson usage for data binding.
- **Variation:** Customize JSON property names with `@JsonProperty`.

---

## Additional Developer Notes

- Jackson is modular; core databind is usually paired with jackson-core and jackson-annotations libraries.
- Many extensions are available to handle formats like XML, YAML, CBOR, Smile.
- Performance can be enhanced with the AfterburnerModule.
- Pay attention to thread-safety: reuse `ObjectMapper` instances rather than creating new ones.
- Review configuration options on `ObjectMapper` for features like FAIL_ON_UNKNOWN_PROPERTIES to control deserialization strictness.
- Consult official docs for detailed annotation usage, custom serializers/deserializers, and advanced streaming API.

---

This documentation integrates domain concepts of JSON processing and data binding, execution facts about key classes and their behavior, and usage patterns illustrating how to serialize, deserialize, and manipulate JSON with Jackson, providing developers a robust guide for effective JSON handling in Java.
