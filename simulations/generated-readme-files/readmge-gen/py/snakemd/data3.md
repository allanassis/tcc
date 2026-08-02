# SnakeMD

## Overview

SnakeMD is a Markdown parser designed to transform Markdown content into stylized terminal output. It enables users to write rich text documentation, README files, or notes using Markdown syntax and display them beautifully within command-line interfaces (CLI). The tool focuses on faithfully representing Markdown elements such as headings, code blocks, lists, links, and text styles (bold, italics) with colored and formatted terminal output.

### Domain Concepts

- **Markdown Syntax:** A lightweight markup language for formatting text, including headers, emphasis, code snippets, lists, blockquotes, and links.
- **Terminal Rendering:** Displaying styled text in terminal environments using colors, fonts, and layout approximations.
- **Text Parsing and Tokenization:** The process of analyzing raw Markdown content, recognizing syntactic structures, and converting them into a format suitable for terminal output.
- **Themes and Styling:** Applying color schemes and text styles to different Markdown elements for better readability.

SnakeMD abstracts these concepts into an API that allows users to render Markdown dynamically, enhancing CLI application documentation, help menus, and other text-based user interactions.

---

## Installation

### Prerequisites

- Node.js (version 12 or later)
- npm (Node Package Manager)

### Install via npm

```bash
npm install -g snakemd
```

This global installation adds the `snakemd` command-line tool to your environment.

### Install as a local dependency

```bash
npm install snakemd
```

When installed locally, you can import and use SnakeMD in your JavaScript or TypeScript projects.

---

## Usage and Examples

### Using SnakeMD as a CLI Tool

Render a Markdown file directly in the terminal:

```bash
snakemd README.md
```

This command reads the `README.md` file and outputs the formatted content in the terminal, styled according to SnakeMD's default theme.

### Rendering from Standard Input

You can pipe Markdown content into SnakeMD:

```bash
cat README.md | snakemd
```

This is useful for dynamic content rendering and integration into scripts.

### Using SnakeMD Programmatically

Import and use SnakeMD in a Node.js application:

```js
const snakemd = require("snakemd");
const fs = require("fs");

const markdownText = fs.readFileSync("README.md", "utf-8");

const styledText = snakemd(markdownText);
console.log(styledText);
```

This snippet reads a Markdown file and converts it into styled terminal output.

---

## API Reference

### `snakemd(markdown: string): string`

- **Purpose:** Parses the given Markdown string and returns a string formatted with terminal escape codes to render colors and styles.

- **Parameters:**
  - `markdown` (`string`): The raw Markdown content to parse and render.

- **Returns:** A terminal-formatted string with styles and colors applied according to Markdown semantics.

### Key Execution Facts

- The `snakemd` function processes Markdown elements including:
  - Headers (levels 1 to 6)
  - Bold, Italic, and Strikethrough text
  - Inline code and code blocks
  - Ordered and unordered lists
  - Blockquotes
  - Links (displaying URLs in styled format)
- The return string includes ANSI escape sequences compatible with most terminals.
- Syntax highlighting is applied to code blocks if the language is specified.
- Errors during parsing fallback gracefully to return the original Markdown string.

---

## License

SnakeMD is licensed under the MIT License. See the [LICENSE](https://github.com/TheRenegadeCoder/SnakeMD/blob/master/LICENSE) file for details.
