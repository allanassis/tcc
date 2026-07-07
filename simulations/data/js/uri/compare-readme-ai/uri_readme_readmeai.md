<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# URI

<em>Master URLs with precision and effortless control</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/lil-js/uri?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/lil-js/uri?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/lil-js/uri?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/lil-js/uri?style=default&color=0080ff" alt="repo-language-count">

<!-- default option, no dependency badges. -->


<!-- default option, no dependency badges. -->

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

uri is a lightweight, chainable URI parser and builder designed to simplify URL manipulation in JavaScript projects. It enables developers to effortlessly parse, validate, and construct URIs with precision and ease.

**Why uri?**

This project streamlines URI handling by providing a robust, modular utility that integrates seamlessly across codebases. The core features include:

- **🔷 Lightweight & Modular:** Minimal footprint ensures fast performance and easy integration.
- **🟢 Chainable API:** Intuitive methods for building and modifying URIs fluently.
- **🟠 Comprehensive Parsing:** Accurate extraction and validation of all URI components.
- **🔴 Reliable Testing:** Automated browser-based tests guarantee consistent behavior.
- **🟣 Seamless Integration:** Designed to work smoothly within diverse development workflows.

---

## Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Modular JavaScript URI parsing and manipulation</li><li>Single responsibility functions for URI components</li><li>Supports both browser and Node.js environments</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>ES5+ JavaScript with clear function definitions</li><li>Consistent use of strict mode (`'use strict'`)</li><li>Readable, well-structured source files</li></ul> |
| 📄 | **Documentation** | <ul><li>Inline comments explaining key functions</li><li>README and metadata in `bower.json` and `package.json`</li><li>Minimal external documentation files</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Package management via Bower and npm (`bower.json`, `package.json`)</li><li>Testing integration with Mocha and Chai</li><li>Build and minification using UglifyJS and Terser</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Core URI logic separated into reusable modules</li><li>Supports extension via plugin-like patterns</li><li>Clear separation between parsing, formatting, and validation</li></ul> |
| 🧪 | **Testing**       | <ul><li>Unit tests written with Mocha and Chai</li><li>Test coverage includes parsing, formatting, and edge cases</li><li>Automated test scripts configured in `package.json`</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Minified builds available via UglifyJS and Terser</li><li>Optimized parsing algorithms for speed</li><li>Lightweight dependency footprint</li></ul> |
| 🛡️ | **Security**      | <ul><li>No direct dependencies with known vulnerabilities</li><li>Input validation for URI components to prevent injection</li><li>Regular dependency updates via npm and Bower</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Minimal runtime dependencies</li><li>Dev dependencies include `mocha`, `chai`, `uglify-js`, `terser`</li><li>Package metadata managed in `bower.json` and `package.json`</li></ul> |

---

## Project Structure

```sh
└── uri/
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── bower.json
    ├── package.json
    ├── test
    │   ├── runner.html
    │   └── uri.js
    ├── uri.js
    └── uri.min.js
```

### Project Index

<details open>
	<summary><b><code>URI/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/lil-js/uri/blob/master/LICENSE'>LICENSE</a></b></td>
					<td style='padding: 8px;'>- Establishes the legal framework that governs the use, modification, and distribution of the entire software project<br>- Ensures contributors and users have clear permissions and limitations, promoting open collaboration while protecting authors from liability<br>- Serves as the foundational agreement that enables the project to be freely shared and adapted within the community.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/lil-js/uri/blob/master/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>- Automates build, test, versioning, and release workflows to streamline project maintenance and distribution<br>- Facilitates code bundling, minification, and running tests, while managing semantic version updates and Git tagging<br>- Integrates with the overall architecture by ensuring consistent version control and preparing optimized artifacts for deployment and publication.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/lil-js/uri/blob/master/bower.json'>bower.json</a></b></td>
					<td style='padding: 8px;'>- Defines essential metadata and configuration for the lil-uri project, facilitating package management, versioning, and distribution<br>- Serves as a central reference for project identity, dependencies, and keywords, supporting seamless integration within the broader codebase and ecosystem<br>- Enables streamlined development workflows and consistent project setup across environments.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/lil-js/uri/blob/master/package.json'>package.json</a></b></td>
					<td style='padding: 8px;'>- Defines the core metadata and configuration for the lil-uri project, establishing its identity as a compact URI parser and builder with a chainable API<br>- Facilitates project management, dependency handling, and script execution, thereby supporting the overall architecture by ensuring consistent versioning, licensing, and development workflows essential for building, testing, and distributing the library.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/lil-js/uri/blob/master/uri.min.js'>uri.min.js</a></b></td>
					<td style='padding: 8px;'>- Provides a lightweight URI parsing and manipulation utility that enables consistent handling, extraction, and reconstruction of URL components across the codebase<br>- Facilitates seamless integration and manipulation of URIs within the project architecture, supporting robust URL validation, decomposition, and query parameter management to enhance routing, networking, or resource identification functionalities.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/lil-js/uri/blob/master/uri.js'>uri.js</a></b></td>
					<td style='padding: 8px;'>- Provides a lightweight utility for parsing, manipulating, and constructing URIs within the codebase<br>- Facilitates consistent handling of URI components such as protocol, host, path, query parameters, and fragments, enabling seamless integration and manipulation of URLs across different modules<br>- Enhances the overall architecture by abstracting URI operations into a reusable, modular component.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- test Submodule -->
	<details>
		<summary><b>test</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ test</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/lil-js/uri/blob/master/test/runner.html'>runner.html</a></b></td>
					<td style='padding: 8px;'>- Facilitates automated testing by providing a browser-based interface to execute and display test results for the project’s core URI handling functionality<br>- Integrates testing frameworks to ensure code correctness and reliability within the overall architecture, supporting continuous validation and quality assurance throughout development.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/lil-js/uri/blob/master/test/uri.js'>uri.js</a></b></td>
					<td style='padding: 8px;'>- Validates and verifies the URI modules functionality within the codebase by testing URL parsing, validation, and construction capabilities<br>- Ensures accurate extraction and assembly of URI components such as protocol, host, port, path, query parameters, and hash fragments<br>- Supports maintaining reliability and correctness of URI handling, which is essential for consistent URL manipulation across the project architecture.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** JavaScript
- **Package Manager:** Bower, Npm

### Installation

Build uri from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/lil-js/uri
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd uri
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![bower][bower-shield]][bower-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [bower-shield]: None -->
	<!-- [bower-link]: None -->

	**Using [bower](None):**

	```sh
	❯ echo 'INSERT-INSTALL-COMMAND-HERE'
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![npm][npm-shield]][npm-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [npm-shield]: https://img.shields.io/badge/npm-CB3837.svg?style={badge_style}&logo=npm&logoColor=white -->
	<!-- [npm-link]: https://www.npmjs.com/ -->

	**Using [npm](https://www.npmjs.com/):**

	```sh
	❯ npm install
	```

### Usage

Run the project with:

**Using [bower](None):**
```sh
echo 'INSERT-RUN-COMMAND-HERE'
```
**Using [npm](https://www.npmjs.com/):**
```sh
npm start
```

### Testing

Uri uses the {__test_framework__} test framework. Run the test suite with:

**Using [bower](None):**
```sh
echo 'INSERT-TEST-COMMAND-HERE'
```
**Using [npm](https://www.npmjs.com/):**
```sh
npm test
```

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## Contributing

- **💬 [Join the Discussions](https://github.com/lil-js/uri/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/lil-js/uri/issues)**: Submit bugs found or log feature requests for the `uri` project.
- **💡 [Submit Pull Requests](https://github.com/lil-js/uri/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/lil-js/uri
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/lil-js/uri/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=lil-js/uri">
   </a>
</p>
</details>

---

## License

Uri is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
