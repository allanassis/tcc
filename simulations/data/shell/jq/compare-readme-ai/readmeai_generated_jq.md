<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# JQ

<em></em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/jqlang/jq?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/jqlang/jq?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/jqlang/jq?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/jqlang/jq?style=default&color=0080ff" alt="repo-language-count">

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



---

## Features

<code>❯ REPLACE-ME</code>

---

## Project Structure

```sh
└── jq/
    ├── .github
    │   ├── ISSUE_TEMPLATE
    │   ├── dependabot.yml
    │   └── workflows
    ├── AUTHORS
    ├── COPYING
    ├── ChangeLog
    ├── Dockerfile
    ├── KEYS
    ├── Makefile.am
    ├── NEWS.md
    ├── README.md
    ├── SECURITY.md
    ├── build
    │   └── .gitignore
    ├── compile-ios.sh
    ├── config
    │   ├── .gitignore
    │   └── m4
    ├── configure.ac
    ├── docs
    │   ├── Pipfile
    │   ├── Pipfile.lock
    │   ├── README.md
    │   ├── build_manpage.py
    │   ├── build_mantests.py
    │   ├── build_website.py
    │   ├── content
    │   ├── manual_schema.yml
    │   ├── public
    │   ├── templates
    │   └── validate_manual_schema.py
    ├── jq.1.prebuilt
    ├── jq.spec
    ├── libjq.pc.in
    ├── m4
    │   ├── ax_compare_version.m4
    │   ├── ax_prog_bison_version.m4
    │   └── ax_pthread.m4
    ├── scripts
    │   ├── crosscompile
    │   ├── gen_utf8_tables.py
    │   └── version
    ├── sig
    │   ├── jq-release-new.key
    │   ├── jq-release-old.key
    │   ├── v1.3
    │   ├── v1.4
    │   ├── v1.5
    │   ├── v1.5rc1
    │   ├── v1.5rc2
    │   ├── v1.6
    │   ├── v1.7
    │   ├── v1.7.1
    │   ├── v1.7rc1
    │   ├── v1.7rc2
    │   ├── v1.8.0
    │   ├── v1.8.1
    │   └── v1.8.2
    ├── src
    │   ├── builtin.c
    │   ├── builtin.h
    │   ├── builtin.jq
    │   ├── bytecode.c
    │   ├── bytecode.h
    │   ├── compile.c
    │   ├── compile.h
    │   ├── exec_stack.h
    │   ├── execute.c
    │   ├── inject_errors.c
    │   ├── jq.h
    │   ├── jq_parser.h
    │   ├── jq_test.c
    │   ├── jv.c
    │   ├── jv.h
    │   ├── jv_alloc.c
    │   ├── jv_alloc.h
    │   ├── jv_aux.c
    │   ├── jv_dtoa.c
    │   ├── jv_dtoa.h
    │   ├── jv_dtoa_tsd.c
    │   ├── jv_dtoa_tsd.h
    │   ├── jv_file.c
    │   ├── jv_parse.c
    │   ├── jv_print.c
    │   ├── jv_private.h
    │   ├── jv_thread.h
    │   ├── jv_unicode.c
    │   ├── jv_unicode.h
    │   ├── jv_utf8_tables.h
    │   ├── lexer.c
    │   ├── lexer.h
    │   ├── lexer.l
    │   ├── libm.h
    │   ├── linker.c
    │   ├── linker.h
    │   ├── locfile.c
    │   ├── locfile.h
    │   ├── main.c
    │   ├── opcode_list.h
    │   ├── parser.c
    │   ├── parser.h
    │   ├── parser.y
    │   ├── util.c
    │   └── util.h
    ├── tests
    │   ├── base64.test
    │   ├── base64test
    │   ├── jq-f-test.sh
    │   ├── jq.test
    │   ├── jq_fuzz_compile.c
    │   ├── jq_fuzz_execute.cpp
    │   ├── jq_fuzz_fixed.cpp
    │   ├── jq_fuzz_load_file.c
    │   ├── jq_fuzz_parse.c
    │   ├── jq_fuzz_parse_extended.c
    │   ├── jq_fuzz_parse_stream.c
    │   ├── jqtest
    │   ├── local.supp
    │   ├── man.test
    │   ├── manonig.test
    │   ├── manonigtest
    │   ├── mantest
    │   ├── modules
    │   ├── no-main-program.jq
    │   ├── onig.supp
    │   ├── onig.test
    │   ├── onigtest
    │   ├── optional.test
    │   ├── optionaltest
    │   ├── setup
    │   ├── shtest
    │   ├── torture
    │   ├── uri.test
    │   ├── uritest
    │   ├── utf8test
    │   └── yes-main-program.jq
    └── vendor
        ├── decNumber
```

### Project Index

<details open>
	<summary><b><code>JQ/</code></b></summary>
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
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/configure.ac'>configure.ac</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/ChangeLog'>ChangeLog</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/Dockerfile'>Dockerfile</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/jq.1.prebuilt'>jq.1.prebuilt</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/jq.spec'>jq.spec</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/compile-ios.sh'>compile-ios.sh</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/Makefile.am'>Makefile.am</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/COPYING'>COPYING</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/KEYS'>KEYS</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/libjq.pc.in'>libjq.pc.in</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- config Submodule -->
	<details>
		<summary><b>config</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ config</b></code>
			<!-- m4 Submodule -->
			<details>
				<summary><b>m4</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ config.m4</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/config/m4/check-math-func.m4'>check-math-func.m4</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/config/m4/find-func.m4'>find-func.m4</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/config/m4/find-func-no-libs.m4'>find-func-no-libs.m4</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/config/m4/misc.m4'>misc.m4</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/config/m4/find-func-no-libs2.m4'>find-func-no-libs2.m4</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- sig Submodule -->
	<details>
		<summary><b>sig</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ sig</b></code>
			<!-- v1.7.1 Submodule -->
			<details>
				<summary><b>v1.7.1</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.7.1</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-mips64r6el.asc'>jq-linux-mips64r6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-mips64r6.asc'>jq-linux-mips64r6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-mipsr6el.asc'>jq-linux-mipsr6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-i386.asc'>jq-linux-i386.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-armhf.asc'>jq-linux-armhf.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-mips64.asc'>jq-linux-mips64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-mips64el.asc'>jq-linux-mips64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-powerpc.asc'>jq-linux-powerpc.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-ppc64el.asc'>jq-linux-ppc64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-mipsel.asc'>jq-linux-mipsel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-win64.exe.asc'>jq-win64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-osx-amd64.asc'>jq-osx-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-mips.asc'>jq-linux-mips.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-mipsr6.asc'>jq-linux-mipsr6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-1.7.1.zip.asc'>jq-1.7.1.zip.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-arm64.asc'>jq-linux-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-macos-amd64.asc'>jq-macos-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-1.7.1.tar.gz.asc'>jq-1.7.1.tar.gz.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-windows-i386.exe.asc'>jq-windows-i386.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-macos-arm64.asc'>jq-macos-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-amd64.asc'>jq-linux-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux64.asc'>jq-linux64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-s390x.asc'>jq-linux-s390x.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-armel.asc'>jq-linux-armel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-windows-amd64.exe.asc'>jq-windows-amd64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7.1/jq-linux-riscv64.asc'>jq-linux-riscv64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.7rc1 Submodule -->
			<details>
				<summary><b>v1.7rc1</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.7rc1</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-mips64r6el.asc'>jq-linux-mips64r6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-mips64r6.asc'>jq-linux-mips64r6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-mipsr6el.asc'>jq-linux-mipsr6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-i386.asc'>jq-linux-i386.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-armhf.asc'>jq-linux-armhf.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-mips64.asc'>jq-linux-mips64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-mips64el.asc'>jq-linux-mips64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-powerpc.asc'>jq-linux-powerpc.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-ppc64el.asc'>jq-linux-ppc64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-mipsel.asc'>jq-linux-mipsel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-mips.asc'>jq-linux-mips.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-mipsr6.asc'>jq-linux-mipsr6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-arm64.asc'>jq-linux-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-macos-amd64.asc'>jq-macos-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-1.7rc1.zip.asc'>jq-1.7rc1.zip.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-windows-i386.exe.asc'>jq-windows-i386.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-macos-arm64.asc'>jq-macos-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-amd64.asc'>jq-linux-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-s390x.asc'>jq-linux-s390x.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-armel.asc'>jq-linux-armel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-windows-amd64.exe.asc'>jq-windows-amd64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-1.7rc1.tar.gz.asc'>jq-1.7rc1.tar.gz.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc1/jq-linux-riscv64.asc'>jq-linux-riscv64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.8.2 Submodule -->
			<details>
				<summary><b>v1.8.2</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.8.2</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-mips64r6el.asc'>jq-linux-mips64r6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-mips64r6.asc'>jq-linux-mips64r6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-mipsr6el.asc'>jq-linux-mipsr6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-i386.asc'>jq-linux-i386.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-armhf.asc'>jq-linux-armhf.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-mips64.asc'>jq-linux-mips64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-mips64el.asc'>jq-linux-mips64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-powerpc.asc'>jq-linux-powerpc.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-ppc64el.asc'>jq-linux-ppc64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-mipsel.asc'>jq-linux-mipsel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-win64.exe.asc'>jq-win64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-osx-amd64.asc'>jq-osx-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-mips.asc'>jq-linux-mips.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-mipsr6.asc'>jq-linux-mipsr6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-arm64.asc'>jq-linux-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-macos-amd64.asc'>jq-macos-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-1.8.2.zip.asc'>jq-1.8.2.zip.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-windows-i386.exe.asc'>jq-windows-i386.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-macos-arm64.asc'>jq-macos-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-attestation.json.asc'>jq-attestation.json.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-amd64.asc'>jq-linux-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux64.asc'>jq-linux64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-s390x.asc'>jq-linux-s390x.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-1.8.2.tar.gz.asc'>jq-1.8.2.tar.gz.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-armel.asc'>jq-linux-armel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-windows-amd64.exe.asc'>jq-windows-amd64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-windows-arm64.exe.asc'>jq-windows-arm64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.2/jq-linux-riscv64.asc'>jq-linux-riscv64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.5rc2 Submodule -->
			<details>
				<summary><b>v1.5rc2</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.5rc2</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5rc2/jq-linux-x86.asc'>jq-linux-x86.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5rc2/jq-win32.exe.asc'>jq-win32.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5rc2/jq-win64.exe.asc'>jq-win64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5rc2/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5rc2/jq-linux-x86_64.asc'>jq-linux-x86_64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5rc2/jq-osx-x86_64.asc'>jq-osx-x86_64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.7 Submodule -->
			<details>
				<summary><b>v1.7</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.7</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-mips64r6el.asc'>jq-linux-mips64r6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-mips64r6.asc'>jq-linux-mips64r6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-mipsr6el.asc'>jq-linux-mipsr6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-i386.asc'>jq-linux-i386.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-armhf.asc'>jq-linux-armhf.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-mips64.asc'>jq-linux-mips64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-win32.exe.asc'>jq-win32.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-mips64el.asc'>jq-linux-mips64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-powerpc.asc'>jq-linux-powerpc.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-ppc64el.asc'>jq-linux-ppc64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-mipsel.asc'>jq-linux-mipsel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-win64.exe.asc'>jq-win64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux32.asc'>jq-linux32.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-osx-amd64.asc'>jq-osx-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-mips.asc'>jq-linux-mips.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-mipsr6.asc'>jq-linux-mipsr6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-arm64.asc'>jq-linux-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-macos-amd64.asc'>jq-macos-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-1.7.tar.gz.asc'>jq-1.7.tar.gz.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-1.7.zip.asc'>jq-1.7.zip.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-windows-i386.exe.asc'>jq-windows-i386.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-macos-arm64.asc'>jq-macos-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-amd64.asc'>jq-linux-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux64.asc'>jq-linux64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-s390x.asc'>jq-linux-s390x.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-armel.asc'>jq-linux-armel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-windows-amd64.exe.asc'>jq-windows-amd64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7/jq-linux-riscv64.asc'>jq-linux-riscv64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.6 Submodule -->
			<details>
				<summary><b>v1.6</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.6</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.6/jq-win32.exe.asc'>jq-win32.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.6/jq-win64.exe.asc'>jq-win64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.6/jq-linux32.asc'>jq-linux32.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.6/jq-osx-amd64.asc'>jq-osx-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.6/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.6/jq-linux64.asc'>jq-linux64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.7rc2 Submodule -->
			<details>
				<summary><b>v1.7rc2</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.7rc2</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-mips64r6el.asc'>jq-linux-mips64r6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-mips64r6.asc'>jq-linux-mips64r6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-mipsr6el.asc'>jq-linux-mipsr6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-i386.asc'>jq-linux-i386.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-armhf.asc'>jq-linux-armhf.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-1.7rc2.tar.gz.asc'>jq-1.7rc2.tar.gz.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-mips64.asc'>jq-linux-mips64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-mips64el.asc'>jq-linux-mips64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-powerpc.asc'>jq-linux-powerpc.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-ppc64el.asc'>jq-linux-ppc64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-mipsel.asc'>jq-linux-mipsel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-mips.asc'>jq-linux-mips.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-mipsr6.asc'>jq-linux-mipsr6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-arm64.asc'>jq-linux-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-macos-amd64.asc'>jq-macos-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-windows-i386.exe.asc'>jq-windows-i386.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-macos-arm64.asc'>jq-macos-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-amd64.asc'>jq-linux-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-s390x.asc'>jq-linux-s390x.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-armel.asc'>jq-linux-armel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-windows-amd64.exe.asc'>jq-windows-amd64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-linux-riscv64.asc'>jq-linux-riscv64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.7rc2/jq-1.7rc2.zip.asc'>jq-1.7rc2.zip.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.8.1 Submodule -->
			<details>
				<summary><b>v1.8.1</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.8.1</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-mips64r6el.asc'>jq-linux-mips64r6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-1.8.1.tar.gz.asc'>jq-1.8.1.tar.gz.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-mips64r6.asc'>jq-linux-mips64r6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-mipsr6el.asc'>jq-linux-mipsr6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-i386.asc'>jq-linux-i386.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-armhf.asc'>jq-linux-armhf.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-mips64.asc'>jq-linux-mips64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-mips64el.asc'>jq-linux-mips64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-powerpc.asc'>jq-linux-powerpc.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-ppc64el.asc'>jq-linux-ppc64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-mipsel.asc'>jq-linux-mipsel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-win64.exe.asc'>jq-win64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-osx-amd64.asc'>jq-osx-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-mips.asc'>jq-linux-mips.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-mipsr6.asc'>jq-linux-mipsr6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-arm64.asc'>jq-linux-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-macos-amd64.asc'>jq-macos-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-windows-i386.exe.asc'>jq-windows-i386.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-macos-arm64.asc'>jq-macos-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-amd64.asc'>jq-linux-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux64.asc'>jq-linux64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-s390x.asc'>jq-linux-s390x.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-1.8.1.zip.asc'>jq-1.8.1.zip.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-armel.asc'>jq-linux-armel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-windows-amd64.exe.asc'>jq-windows-amd64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.1/jq-linux-riscv64.asc'>jq-linux-riscv64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.8.0 Submodule -->
			<details>
				<summary><b>v1.8.0</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.8.0</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-mips64r6el.asc'>jq-linux-mips64r6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-mips64r6.asc'>jq-linux-mips64r6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-mipsr6el.asc'>jq-linux-mipsr6el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-i386.asc'>jq-linux-i386.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-armhf.asc'>jq-linux-armhf.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-mips64.asc'>jq-linux-mips64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-mips64el.asc'>jq-linux-mips64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-powerpc.asc'>jq-linux-powerpc.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-ppc64el.asc'>jq-linux-ppc64el.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-mipsel.asc'>jq-linux-mipsel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-win64.exe.asc'>jq-win64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-osx-amd64.asc'>jq-osx-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-mips.asc'>jq-linux-mips.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-mipsr6.asc'>jq-linux-mipsr6.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-arm64.asc'>jq-linux-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-macos-amd64.asc'>jq-macos-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-1.8.0.tar.gz.asc'>jq-1.8.0.tar.gz.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-windows-i386.exe.asc'>jq-windows-i386.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-macos-arm64.asc'>jq-macos-arm64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-amd64.asc'>jq-linux-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-1.8.0.zip.asc'>jq-1.8.0.zip.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux64.asc'>jq-linux64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-s390x.asc'>jq-linux-s390x.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-armel.asc'>jq-linux-armel.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-windows-amd64.exe.asc'>jq-windows-amd64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.8.0/jq-linux-riscv64.asc'>jq-linux-riscv64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.5rc1 Submodule -->
			<details>
				<summary><b>v1.5rc1</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.5rc1</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5rc1/jq-win32.exe.asc'>jq-win32.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5rc1/jq-win64.exe.asc'>jq-win64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5rc1/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5rc1/jq-linux-x86_64-static.asc'>jq-linux-x86_64-static.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.4 Submodule -->
			<details>
				<summary><b>v1.4</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.4</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.4/jq-osx-x86.asc'>jq-osx-x86.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.4/jq-solaris11-32.asc'>jq-solaris11-32.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.4/jq-linux-x86.asc'>jq-linux-x86.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.4/jq-win32.exe.asc'>jq-win32.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.4/jq-win64.exe.asc'>jq-win64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.4/jq-solaris11-64.asc'>jq-solaris11-64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.4/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.4/jq-linux-x86_64.asc'>jq-linux-x86_64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.4/jq-osx-x86_64.asc'>jq-osx-x86_64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.3 Submodule -->
			<details>
				<summary><b>v1.3</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.3</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.3/jq-osx-x86.asc'>jq-osx-x86.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.3/jq-linux-x86.asc'>jq-linux-x86.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.3/jq-win32.exe.asc'>jq-win32.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.3/jq-win64.exe.asc'>jq-win64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.3/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.3/jq-linux-x86_64.asc'>jq-linux-x86_64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.3/jq-osx-x86_64.asc'>jq-osx-x86_64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- v1.5 Submodule -->
			<details>
				<summary><b>v1.5</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ sig.v1.5</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5/jq-win32.exe.asc'>jq-win32.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5/jq-win64.exe.asc'>jq-win64.exe.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5/jq-linux32.asc'>jq-linux32.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5/jq-osx-amd64.asc'>jq-osx-amd64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5/jq-linux32-no-oniguruma.asc'>jq-linux32-no-oniguruma.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5/sha256sum.txt'>sha256sum.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/sig/v1.5/jq-linux64.asc'>jq-linux64.asc</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- scripts Submodule -->
	<details>
		<summary><b>scripts</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ scripts</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/scripts/gen_utf8_tables.py'>gen_utf8_tables.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/scripts/version'>version</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/scripts/crosscompile'>crosscompile</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- .github Submodule -->
	<details>
		<summary><b>.github</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ .github</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/.github/dependabot.yml'>dependabot.yml</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- workflows Submodule -->
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ .github.workflows</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/.github/workflows/oniguruma.yml'>oniguruma.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/.github/workflows/manpage.yml'>manpage.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/.github/workflows/decnum.yml'>decnum.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/.github/workflows/scanbuild.yml'>scanbuild.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/.github/workflows/ci.yml'>ci.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/.github/workflows/website.yml'>website.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/.github/workflows/valgrind.yml'>valgrind.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- m4 Submodule -->
	<details>
		<summary><b>m4</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ m4</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/m4/ax_prog_bison_version.m4'>ax_prog_bison_version.m4</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/m4/ax_compare_version.m4'>ax_compare_version.m4</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/m4/ax_pthread.m4'>ax_pthread.m4</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- vendor Submodule -->
	<details>
		<summary><b>vendor</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ vendor</b></code>
			<!-- decNumber Submodule -->
			<details>
				<summary><b>decNumber</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ vendor.decNumber</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decNumberLocal.h'>decNumberLocal.h</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/example6.c'>example6.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decNumber.h'>decNumber.h</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decSingle.h'>decSingle.h</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/example8.c'>example8.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/example2.c'>example2.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decQuad.h'>decQuad.h</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decimal128.c'>decimal128.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/example5.c'>example5.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decimal32.c'>decimal32.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decPacked.c'>decPacked.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/example1.c'>example1.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decContext.h'>decContext.h</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decDPD.h'>decDPD.h</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decimal64.h'>decimal64.h</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decDouble.h'>decDouble.h</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/example4.c'>example4.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decSingle.c'>decSingle.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decBasic.c'>decBasic.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decNumber.c'>decNumber.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decimal128.h'>decimal128.h</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/ICU-license.html'>ICU-license.html</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decQuad.c'>decQuad.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/readme.txt'>readme.txt</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decPacked.h'>decPacked.h</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decCommon.c'>decCommon.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/example7.c'>example7.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/example3.c'>example3.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decimal32.h'>decimal32.h</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decDouble.c'>decDouble.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decimal64.c'>decimal64.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/vendor/decNumber/decContext.c'>decContext.c</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- src Submodule -->
	<details>
		<summary><b>src</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ src</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/bytecode.c'>bytecode.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/builtin.jq'>builtin.jq</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/compile.c'>compile.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_alloc.h'>jv_alloc.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_dtoa.c'>jv_dtoa.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/linker.c'>linker.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/util.c'>util.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/builtin.h'>builtin.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_thread.h'>jv_thread.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_unicode.c'>jv_unicode.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_parse.c'>jv_parse.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv.c'>jv.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/locfile.h'>locfile.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jq_test.c'>jq_test.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/parser.h'>parser.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_private.h'>jv_private.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/lexer.l'>lexer.l</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/execute.c'>execute.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_dtoa_tsd.c'>jv_dtoa_tsd.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_utf8_tables.h'>jv_utf8_tables.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/lexer.c'>lexer.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/opcode_list.h'>opcode_list.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_aux.c'>jv_aux.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_dtoa.h'>jv_dtoa.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_alloc.c'>jv_alloc.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/inject_errors.c'>inject_errors.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/compile.h'>compile.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/main.c'>main.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/bytecode.h'>bytecode.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jq_parser.h'>jq_parser.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv.h'>jv.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_unicode.h'>jv_unicode.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/locfile.c'>locfile.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/util.h'>util.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/builtin.c'>builtin.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/linker.h'>linker.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/lexer.h'>lexer.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/parser.y'>parser.y</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/exec_stack.h'>exec_stack.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/libm.h'>libm.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_print.c'>jv_print.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_dtoa_tsd.h'>jv_dtoa_tsd.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/parser.c'>parser.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jv_file.c'>jv_file.c</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/jqlang/jq/blob/master/src/jq.h'>jq.h</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** unknown
- **Package Manager:** Autotools
- **Container Runtime:** Docker

### Installation

Build jq from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/jqlang/jq
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd jq
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![docker][docker-shield]][docker-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [docker-shield]: https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white -->
	<!-- [docker-link]: https://www.docker.com/ -->

	**Using [docker](https://www.docker.com/):**

	```sh
	❯ docker build -t jqlang/jq .
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![autotools][autotools-shield]][autotools-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [autotools-shield]: None -->
	<!-- [autotools-link]: None -->

	**Using [autotools](None):**

	```sh
	❯ echo 'INSERT-INSTALL-COMMAND-HERE'
	```

### Usage

Run the project with:

**Using [docker](https://www.docker.com/):**
```sh
docker run -it {image_name}
```
**Using [autotools](None):**
```sh
echo 'INSERT-RUN-COMMAND-HERE'
```

### Testing

Jq uses the {__test_framework__} test framework. Run the test suite with:

**Using [autotools](None):**
```sh
echo 'INSERT-TEST-COMMAND-HERE'
```

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## Contributing

- **💬 [Join the Discussions](https://github.com/jqlang/jq/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/jqlang/jq/issues)**: Submit bugs found or log feature requests for the `jq` project.
- **💡 [Submit Pull Requests](https://github.com/jqlang/jq/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/jqlang/jq
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
   <a href="https://github.com{/jqlang/jq/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=jqlang/jq">
   </a>
</p>
</details>

---

## License

Jq is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
