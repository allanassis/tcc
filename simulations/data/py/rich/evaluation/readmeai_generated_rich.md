<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# RICH

<em></em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/Textualize/rich?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/Textualize/rich?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/Textualize/rich?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/Textualize/rich?style=default&color=0080ff" alt="repo-language-count">

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
└── rich/
    ├── .github
    │   ├── FUNDING.yml
    │   ├── ISSUE_TEMPLATE
    │   ├── dependabot.yml
    │   ├── pull_request_template.md
    │   └── workflows
    ├── AI_POLICY.md
    ├── CHANGELOG.md
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── CONTRIBUTORS.md
    ├── FAQ.md
    ├── LICENSE
    ├── Makefile
    ├── README.cn.md
    ├── README.de-ch.md
    ├── README.de.md
    ├── README.es.md
    ├── README.fa.md
    ├── README.fr.md
    ├── README.hi.md
    ├── README.id.md
    ├── README.it.md
    ├── README.ja.md
    ├── README.kr.md
    ├── README.md
    ├── README.pl.md
    ├── README.pt-br.md
    ├── README.ru.md
    ├── README.sv.md
    ├── README.tr.md
    ├── README.zh-tw.md
    ├── SECURITY.md
    ├── assets
    │   ├── logo.ai
    │   ├── logo.svg
    │   └── logo.txt
    ├── asv.conf.json
    ├── asvhashfile
    ├── benchmarks
    │   ├── README.md
    │   ├── __init__.py
    │   ├── benchmarks.py
    │   ├── results
    │   └── snippets.py
    ├── docs
    │   ├── Makefile
    │   ├── images
    │   ├── make.bat
    │   ├── requirements.txt
    │   └── source
    ├── examples
    │   ├── README.md
    │   ├── attrs.py
    │   ├── bars.py
    │   ├── columns.py
    │   ├── cp_progress.py
    │   ├── downloader.py
    │   ├── dynamic_progress.py
    │   ├── exception.py
    │   ├── export.py
    │   ├── file_progress.py
    │   ├── fullscreen.py
    │   ├── group.py
    │   ├── group2.py
    │   ├── highlighter.py
    │   ├── jobs.py
    │   ├── justify.py
    │   ├── justify2.py
    │   ├── layout.py
    │   ├── link.py
    │   ├── listdir.py
    │   ├── live_progress.py
    │   ├── log.py
    │   ├── overflow.py
    │   ├── padding.py
    │   ├── print_calendar.py
    │   ├── rainbow.py
    │   ├── recursive_error.py
    │   ├── repr.py
    │   ├── save_table_svg.py
    │   ├── screen.py
    │   ├── spinners.py
    │   ├── status.py
    │   ├── suppress.py
    │   ├── table.py
    │   ├── table_movie.py
    │   ├── top_lite_simulator.py
    │   └── tree.py
    ├── faq.yml
    ├── imgs
    │   ├── columns.png
    │   ├── downloader.gif
    │   ├── features.png
    │   ├── hello_world.png
    │   ├── inspect.png
    │   ├── log.png
    │   ├── logging.png
    │   ├── logo.svg
    │   ├── markdown.png
    │   ├── print.png
    │   ├── progress.gif
    │   ├── progress.png
    │   ├── repl.png
    │   ├── spinners.gif
    │   ├── status.gif
    │   ├── syntax.png
    │   ├── table.png
    │   ├── table2.png
    │   ├── table_movie.gif
    │   ├── traceback.png
    │   ├── tree.png
    │   └── where_there_is_a_will.png
    ├── make.bat
    ├── poetry.lock
    ├── pyproject.toml
    ├── questions
    │   ├── README.md
    │   ├── ansi_escapes.question.md
    │   ├── emoji_broken.question.md
    │   ├── highlight_incorrect.question.md
    │   ├── highlighting_unexpected.question.md
    │   ├── jupyter.question.md
    │   ├── log_renderables.question.md
    │   ├── logging_color.question.md
    │   ├── rich_spinner.question.md
    │   ├── square_brackets.question.md
    │   └── tracebacks_installed.question.md
    ├── rich
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── _emoji_codes.py
    │   ├── _emoji_replace.py
    │   ├── _export_format.py
    │   ├── _extension.py
    │   ├── _fileno.py
    │   ├── _inspect.py
    │   ├── _log_render.py
    │   ├── _loop.py
    │   ├── _null_file.py
    │   ├── _palettes.py
    │   ├── _pick.py
    │   ├── _ratio.py
    │   ├── _spinners.py
    │   ├── _stack.py
    │   ├── _timer.py
    │   ├── _unicode_data
    │   ├── _win32_console.py
    │   ├── _windows.py
    │   ├── _windows_renderer.py
    │   ├── _wrap.py
    │   ├── abc.py
    │   ├── align.py
    │   ├── ansi.py
    │   ├── bar.py
    │   ├── box.py
    │   ├── cells.py
    │   ├── color.py
    │   ├── color_triplet.py
    │   ├── columns.py
    │   ├── console.py
    │   ├── constrain.py
    │   ├── containers.py
    │   ├── control.py
    │   ├── default_styles.py
    │   ├── diagnose.py
    │   ├── emoji.py
    │   ├── errors.py
    │   ├── file_proxy.py
    │   ├── filesize.py
    │   ├── highlighter.py
    │   ├── json.py
    │   ├── jupyter.py
    │   ├── layout.py
    │   ├── live.py
    │   ├── live_render.py
    │   ├── logging.py
    │   ├── markdown.py
    │   ├── markup.py
    │   ├── measure.py
    │   ├── padding.py
    │   ├── pager.py
    │   ├── palette.py
    │   ├── panel.py
    │   ├── pretty.py
    │   ├── progress.py
    │   ├── progress_bar.py
    │   ├── prompt.py
    │   ├── protocol.py
    │   ├── py.typed
    │   ├── region.py
    │   ├── repr.py
    │   ├── rule.py
    │   ├── scope.py
    │   ├── screen.py
    │   ├── segment.py
    │   ├── spinner.py
    │   ├── status.py
    │   ├── style.py
    │   ├── styled.py
    │   ├── syntax.py
    │   ├── table.py
    │   ├── terminal_theme.py
    │   ├── text.py
    │   ├── theme.py
    │   ├── themes.py
    │   ├── traceback.py
    │   └── tree.py
    ├── setup.py
    ├── tests
    │   ├── __init__.py
    │   ├── _card_render.py
    │   ├── conftest.py
    │   ├── pytest.ini
    │   ├── render.py
    │   ├── test_align.py
    │   ├── test_ansi.py
    │   ├── test_bar.py
    │   ├── test_block_bar.py
    │   ├── test_box.py
    │   ├── test_card.py
    │   ├── test_cells.py
    │   ├── test_color.py
    │   ├── test_color_triplet.py
    │   ├── test_columns.py
    │   ├── test_columns_align.py
    │   ├── test_console.py
    │   ├── test_constrain.py
    │   ├── test_containers.py
    │   ├── test_control.py
    │   ├── test_emoji.py
    │   ├── test_file_proxy.py
    │   ├── test_filesize.py
    │   ├── test_getfileno.py
    │   ├── test_highlighter.py
    │   ├── test_inspect.py
    │   ├── test_json.py
    │   ├── test_jupyter.py
    │   ├── test_layout.py
    │   ├── test_live.py
    │   ├── test_live_render.py
    │   ├── test_log.py
    │   ├── test_logging.py
    │   ├── test_markdown.py
    │   ├── test_markdown_no_hyperlinks.py
    │   ├── test_markup.py
    │   ├── test_measure.py
    │   ├── test_null_file.py
    │   ├── test_padding.py
    │   ├── test_palette.py
    │   ├── test_panel.py
    │   ├── test_pick.py
    │   ├── test_pretty.py
    │   ├── test_progress.py
    │   ├── test_prompt.py
    │   ├── test_protocol.py
    │   ├── test_ratio.py
    │   ├── test_repr.py
    │   ├── test_rich_print.py
    │   ├── test_rule.py
    │   ├── test_rule_in_table.py
    │   ├── test_screen.py
    │   ├── test_segment.py
    │   ├── test_spinner.py
    │   ├── test_stack.py
    │   ├── test_status.py
    │   ├── test_style.py
    │   ├── test_styled.py
    │   ├── test_syntax.py
    │   ├── test_table.py
    │   ├── test_text.py
    │   ├── test_theme.py
    │   ├── test_tools.py
    │   ├── test_traceback.py
    │   ├── test_tree.py
    │   ├── test_unicode_data.py
    │   ├── test_win32_console.py
    │   └── test_windows_renderer.py
    ├── tools
    │   ├── README.md
    │   ├── cats.json
    │   ├── make_emoji.py
    │   ├── make_width_tables.py
    │   ├── movies.md
    │   ├── profile_divide.py
    │   ├── profile_pretty.py
    │   └── stress_test_pretty.py
    └── tox.ini
```

### Project Index

<details open>
	<summary><b><code>RICH/</code></b></summary>
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
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/faq.yml'>faq.yml</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/LICENSE'>LICENSE</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/Makefile'>Makefile</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/setup.py'>setup.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/asv.conf.json'>asv.conf.json</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/make.bat'>make.bat</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/tox.ini'>tox.ini</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/asvhashfile'>asvhashfile</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- tools Submodule -->
	<details>
		<summary><b>tools</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ tools</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/tools/make_width_tables.py'>make_width_tables.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/tools/profile_pretty.py'>profile_pretty.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/tools/stress_test_pretty.py'>stress_test_pretty.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/tools/cats.json'>cats.json</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/tools/profile_divide.py'>profile_divide.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/tools/make_emoji.py'>make_emoji.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- examples Submodule -->
	<details>
		<summary><b>examples</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ examples</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/dynamic_progress.py'>dynamic_progress.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/link.py'>link.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/screen.py'>screen.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/file_progress.py'>file_progress.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/tree.py'>tree.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/exception.py'>exception.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/recursive_error.py'>recursive_error.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/justify.py'>justify.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/group2.py'>group2.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/print_calendar.py'>print_calendar.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/downloader.py'>downloader.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/save_table_svg.py'>save_table_svg.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/table_movie.py'>table_movie.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/log.py'>log.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/cp_progress.py'>cp_progress.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/layout.py'>layout.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/overflow.py'>overflow.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/export.py'>export.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/repr.py'>repr.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/live_progress.py'>live_progress.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/suppress.py'>suppress.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/jobs.py'>jobs.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/columns.py'>columns.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/spinners.py'>spinners.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/justify2.py'>justify2.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/fullscreen.py'>fullscreen.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/highlighter.py'>highlighter.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/group.py'>group.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/bars.py'>bars.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/table.py'>table.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/top_lite_simulator.py'>top_lite_simulator.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/attrs.py'>attrs.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/listdir.py'>listdir.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/padding.py'>padding.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/status.py'>status.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/examples/rainbow.py'>rainbow.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- benchmarks Submodule -->
	<details>
		<summary><b>benchmarks</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ benchmarks</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/snippets.py'>snippets.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/benchmarks.py'>benchmarks.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- results Submodule -->
			<details>
				<summary><b>results</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ benchmarks.results</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/benchmarks.json'>benchmarks.json</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- darrenburns-2022-mbp Submodule -->
					<details>
						<summary><b>darrenburns-2022-mbp</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ benchmarks.results.darrenburns-2022-mbp</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/0a3fcb9c-virtualenv-py3.10-setuptools59.2.0.json'>0a3fcb9c-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/b391635e-virtualenv-py3.10.json'>b391635e-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/99831099-virtualenv-py3.10.json'>99831099-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/8a7f5d82-virtualenv-py3.10.json'>8a7f5d82-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/58bfa48f-virtualenv-py3.10-setuptools59.2.0.json'>58bfa48f-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/038e22eb-virtualenv-py3.10.json'>038e22eb-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/8e649fea-virtualenv-py3.10-setuptools59.2.0.json'>8e649fea-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/464e4e33-virtualenv-py3.10-setuptools59.2.0.json'>464e4e33-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/2ea7e586-virtualenv-py3.10.json'>2ea7e586-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/9abc0292-virtualenv-py3.10.json'>9abc0292-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/83756d62-virtualenv-py3.10-setuptools59.2.0.json'>83756d62-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/0d2aeb75-virtualenv-py3.10-setuptools59.2.0.json'>0d2aeb75-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/e9e72000-virtualenv-py3.10.json'>e9e72000-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/21432b4c-virtualenv-py3.10-setuptools59.2.0.json'>21432b4c-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/aaea99f7-virtualenv-py3.10.json'>aaea99f7-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/a81230bc-virtualenv-py3.10.json'>a81230bc-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/5fafb92f-virtualenv-py3.10-setuptools59.2.0.json'>5fafb92f-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/bf728dbc-virtualenv-py3.10-setuptools59.2.0.json'>bf728dbc-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/95d8bf98-virtualenv-py3.10.json'>95d8bf98-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/e7de32a0-virtualenv-py3.10-setuptools59.2.0.json'>e7de32a0-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/36efcb5a-virtualenv-py3.10.json'>36efcb5a-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/3f7d3e4e-virtualenv-py3.10.json'>3f7d3e4e-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/4020d5a9-virtualenv-py3.10.json'>4020d5a9-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/4dc1d4cb-virtualenv-py3.10-setuptools59.2.0.json'>4dc1d4cb-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/5f03e3ba-virtualenv-py3.10.json'>5f03e3ba-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/aca0b60b-virtualenv-py3.10.json'>aca0b60b-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/d9d59c6e-virtualenv-py3.10.json'>d9d59c6e-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/690507d4-virtualenv-py3.10.json'>690507d4-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/53d9eeaf-virtualenv-py3.10.json'>53d9eeaf-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/41279bca-virtualenv-py3.10-setuptools59.2.0.json'>41279bca-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/f2af8c9d-virtualenv-py3.10.json'>f2af8c9d-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/5f021978-virtualenv-py3.10.json'>5f021978-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/11c00224-virtualenv-py3.10.json'>11c00224-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/189a2a3f-virtualenv-py3.10-setuptools59.2.0.json'>189a2a3f-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/b9e0014a-virtualenv-py3.10.json'>b9e0014a-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/f82a4ccf-virtualenv-py3.10-setuptools59.2.0.json'>f82a4ccf-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/9f2a426e-virtualenv-py3.10.json'>9f2a426e-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/23aa7177-virtualenv-py3.10.json'>23aa7177-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/3473658d-virtualenv-py3.10.json'>3473658d-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/7edd619f-virtualenv-py3.10-setuptools59.2.0.json'>7edd619f-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/a27a3ee2-virtualenv-py3.10.json'>a27a3ee2-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/79ea1c1d-virtualenv-py3.10-setuptools59.2.0.json'>79ea1c1d-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/4f8908a6-virtualenv-py3.10-setuptools59.2.0.json'>4f8908a6-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/e338ab14-virtualenv-py3.10.json'>e338ab14-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/5f55063b-virtualenv-py3.10.json'>5f55063b-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/88b07b3e-virtualenv-py3.10.json'>88b07b3e-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/666d0cf2-virtualenv-py3.10.json'>666d0cf2-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/f5ed5bde-virtualenv-py3.10-setuptools59.2.0.json'>f5ed5bde-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/c24ab497-virtualenv-py3.10.json'>c24ab497-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/edcb6f9e-virtualenv-py3.10-setuptools59.2.0.json'>edcb6f9e-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/55e11902-virtualenv-py3.10.json'>55e11902-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/bd34e0a1-virtualenv-py3.10-setuptools59.2.0.json'>bd34e0a1-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/27ab1732-virtualenv-py3.10-setuptools59.2.0.json'>27ab1732-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/aa4546ac-virtualenv-py3.10-setuptools59.2.0.json'>aa4546ac-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/5f021978-virtualenv-py3.10-setuptools59.2.0.json'>5f021978-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/d06540a2-virtualenv-py3.10-setuptools59.2.0.json'>d06540a2-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/ac1a33da-virtualenv-py3.10.json'>ac1a33da-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/f2845e12-virtualenv-py3.10-setuptools59.2.0.json'>f2845e12-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/64755d41-virtualenv-py3.10.json'>64755d41-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/aa7926c1-virtualenv-py3.10-setuptools59.2.0.json'>aa7926c1-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/c3d0e358-virtualenv-py3.10-setuptools59.2.0.json'>c3d0e358-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/76620730-virtualenv-py3.10-setuptools59.2.0.json'>76620730-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/c9afafdd-virtualenv-py3.10.json'>c9afafdd-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/0fd6bc56-virtualenv-py3.10-setuptools59.2.0.json'>0fd6bc56-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/c57e1f50-virtualenv-py3.10.json'>c57e1f50-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/11c305e1-virtualenv-py3.10.json'>11c305e1-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/f84d5dee-virtualenv-py3.10.json'>f84d5dee-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/64471afc-virtualenv-py3.10-setuptools59.2.0.json'>64471afc-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/7d00fa83-virtualenv-py3.10.json'>7d00fa83-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/a81230bc-virtualenv-py3.10-setuptools59.2.0.json'>a81230bc-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/ae5865eb-virtualenv-py3.10-setuptools59.2.0.json'>ae5865eb-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/30498f59-virtualenv-py3.10-setuptools59.2.0.json'>30498f59-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/8a7f5d82-virtualenv-py3.10-setuptools59.2.0.json'>8a7f5d82-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/43a26c0a-virtualenv-py3.10.json'>43a26c0a-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/53cda574-virtualenv-py3.10-setuptools59.2.0.json'>53cda574-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/03392a1b-virtualenv-py3.10-setuptools59.2.0.json'>03392a1b-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/550d3911-virtualenv-py3.10.json'>550d3911-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/0ac4e308-virtualenv-py3.10-setuptools59.2.0.json'>0ac4e308-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/c3d0e358-virtualenv-py3.10.json'>c3d0e358-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/15623c5a-virtualenv-py3.10.json'>15623c5a-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/932e26b6-virtualenv-py3.10.json'>932e26b6-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/48da2791-virtualenv-py3.10.json'>48da2791-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/1daa1771-virtualenv-py3.10-setuptools59.2.0.json'>1daa1771-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/4d6a6d88-virtualenv-py3.10.json'>4d6a6d88-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/911d305f-virtualenv-py3.10.json'>911d305f-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/2d3ec69f-virtualenv-py3.10.json'>2d3ec69f-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/e7849495-virtualenv-py3.10.json'>e7849495-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/0db0cbd0-virtualenv-py3.10.json'>0db0cbd0-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/ea049ffc-virtualenv-py3.10.json'>ea049ffc-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/ea2ed337-virtualenv-py3.10.json'>ea2ed337-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/e21ac11a-virtualenv-py3.10-setuptools59.2.0.json'>e21ac11a-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/eab3fe8e-virtualenv-py3.10-setuptools59.2.0.json'>eab3fe8e-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/1f3f7f1e-virtualenv-py3.10.json'>1f3f7f1e-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/bd34e0a1-virtualenv-py3.10.json'>bd34e0a1-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/e78acae6-virtualenv-py3.10-setuptools59.2.0.json'>e78acae6-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/2ea7e586-virtualenv-py3.10-setuptools59.2.0.json'>2ea7e586-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/6d7ba589-virtualenv-py3.10.json'>6d7ba589-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/2d3152a2-virtualenv-py3.10-setuptools59.2.0.json'>2d3152a2-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/573125e9-virtualenv-py3.10.json'>573125e9-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/7441bf27-virtualenv-py3.10.json'>7441bf27-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/b9e0014a-virtualenv-py3.10-setuptools59.2.0.json'>b9e0014a-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/3be88c08-virtualenv-py3.10-setuptools59.2.0.json'>3be88c08-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/3db6396a-virtualenv-py3.10.json'>3db6396a-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/2356d7c0-virtualenv-py3.10.json'>2356d7c0-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/646d933d-virtualenv-py3.10-setuptools59.2.0.json'>646d933d-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/71135d19-virtualenv-py3.10-setuptools59.2.0.json'>71135d19-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/dc3f0623-virtualenv-py3.10-setuptools59.2.0.json'>dc3f0623-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/52d159aa-virtualenv-py3.10-setuptools59.2.0.json'>52d159aa-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/26fe4667-virtualenv-py3.10-setuptools59.2.0.json'>26fe4667-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/24743154-virtualenv-py3.10.json'>24743154-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/008854c4-virtualenv-py3.10.json'>008854c4-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/ba5d0c2c-virtualenv-py3.10.json'>ba5d0c2c-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/588f0331-virtualenv-py3.10-setuptools59.2.0.json'>588f0331-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/416033ff-virtualenv-py3.10-setuptools59.2.0.json'>416033ff-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/ef80460f-virtualenv-py3.10.json'>ef80460f-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/3f7d3e4e-virtualenv-py3.10-setuptools59.2.0.json'>3f7d3e4e-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/972dedff-virtualenv-py3.10.json'>972dedff-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/03a52134-virtualenv-py3.10.json'>03a52134-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/177958c5-virtualenv-py3.10-setuptools59.2.0.json'>177958c5-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/877c53d9-virtualenv-py3.10-setuptools59.2.0.json'>877c53d9-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/ecf3d7f1-virtualenv-py3.10.json'>ecf3d7f1-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/a6d1d784-virtualenv-py3.10.json'>a6d1d784-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/44f54dd8-virtualenv-py3.10.json'>44f54dd8-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/07d51ffc-virtualenv-py3.10.json'>07d51ffc-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/c3ee3b05-virtualenv-py3.10.json'>c3ee3b05-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/5f82274a-virtualenv-py3.10-setuptools59.2.0.json'>5f82274a-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/8c3e6be4-virtualenv-py3.10-setuptools59.2.0.json'>8c3e6be4-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/9a4fbf83-virtualenv-py3.10.json'>9a4fbf83-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/06922006-virtualenv-py3.10.json'>06922006-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/8b185610-virtualenv-py3.10.json'>8b185610-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/2aea8526-virtualenv-py3.10-setuptools59.2.0.json'>2aea8526-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/2c93dce9-virtualenv-py3.10-setuptools59.2.0.json'>2c93dce9-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/b15bc18c-virtualenv-py3.10-setuptools59.2.0.json'>b15bc18c-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/96ea5fed-virtualenv-py3.10.json'>96ea5fed-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/4bf3f19c-virtualenv-py3.10.json'>4bf3f19c-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/837b6d7e-virtualenv-py3.10.json'>837b6d7e-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/4b3b6531-virtualenv-py3.10-setuptools59.2.0.json'>4b3b6531-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/4b123ddf-virtualenv-py3.10.json'>4b123ddf-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/43d4c4e5-virtualenv-py3.10-setuptools59.2.0.json'>43d4c4e5-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/1cdcd1ae-virtualenv-py3.10.json'>1cdcd1ae-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/1442dd77-virtualenv-py3.10.json'>1442dd77-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/machine.json'>machine.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/a8d2bb20-virtualenv-py3.10-setuptools59.2.0.json'>a8d2bb20-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/a2f6688e-virtualenv-py3.10-setuptools59.2.0.json'>a2f6688e-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/52d159aa-virtualenv-py3.10.json'>52d159aa-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/cefafdc1-virtualenv-py3.10.json'>cefafdc1-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/7e4a2db4-virtualenv-py3.10.json'>7e4a2db4-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/8b47f338-virtualenv-py3.10.json'>8b47f338-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/d1ea01d0-virtualenv-py3.10.json'>d1ea01d0-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/656b7a18-virtualenv-py3.10-setuptools59.2.0.json'>656b7a18-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/0e8df8cd-virtualenv-py3.10-setuptools59.2.0.json'>0e8df8cd-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/9bfb6190-virtualenv-py3.10-setuptools59.2.0.json'>9bfb6190-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/7bad81d5-virtualenv-py3.10-setuptools59.2.0.json'>7bad81d5-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/489fafc6-virtualenv-py3.10-setuptools59.2.0.json'>489fafc6-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/43d4c4e5-virtualenv-py3.10.json'>43d4c4e5-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/d6e6a762-virtualenv-py3.10.json'>d6e6a762-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/20024635-virtualenv-py3.10.json'>20024635-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/7ef7ffee-virtualenv-py3.10.json'>7ef7ffee-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/2ba277ac-virtualenv-py3.10.json'>2ba277ac-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/e5246436-virtualenv-py3.10.json'>e5246436-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/ad6e3dea-virtualenv-py3.10.json'>ad6e3dea-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/25a1bf06-virtualenv-py3.10.json'>25a1bf06-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/579a29c8-virtualenv-py3.10.json'>579a29c8-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/19e26c94-virtualenv-py3.10-setuptools59.2.0.json'>19e26c94-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/7d02d29b-virtualenv-py3.10.json'>7d02d29b-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/3827b4ae-virtualenv-py3.10.json'>3827b4ae-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/cf606f0a-virtualenv-py3.10.json'>cf606f0a-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/0d69004c-virtualenv-py3.10-setuptools59.2.0.json'>0d69004c-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/06aa1271-virtualenv-py3.10-setuptools59.2.0.json'>06aa1271-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/e0a1fd30-virtualenv-py3.10.json'>e0a1fd30-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/a6ea9890-virtualenv-py3.10-setuptools59.2.0.json'>a6ea9890-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/e34eadb3-virtualenv-py3.10.json'>e34eadb3-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/1ffbd443-virtualenv-py3.10.json'>1ffbd443-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/d9d59c6e-virtualenv-py3.10-setuptools59.2.0.json'>d9d59c6e-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/972dedff-virtualenv-py3.10-setuptools59.2.0.json'>972dedff-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/949e1f72-virtualenv-py3.10.json'>949e1f72-virtualenv-py3.10.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/benchmarks/results/darrenburns-2022-mbp/60dadaf2-virtualenv-py3.10-setuptools59.2.0.json'>60dadaf2-virtualenv-py3.10-setuptools59.2.0.json</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
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
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/.github/FUNDING.yml'>FUNDING.yml</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/.github/dependabot.yml'>dependabot.yml</a></b></td>
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
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/.github/workflows/pythonpackage.yml'>pythonpackage.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/.github/workflows/codeql.yml'>codeql.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/.github/workflows/comment.yml'>comment.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/.github/workflows/readmechanged.yml'>readmechanged.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/.github/workflows/codespell.yml'>codespell.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/.github/workflows/newissue.yml'>newissue.yml</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- rich Submodule -->
	<details>
		<summary><b>rich</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ rich</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/themes.py'>themes.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/screen.py'>screen.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/logging.py'>logging.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/measure.py'>measure.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/tree.py'>tree.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/console.py'>console.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/live_render.py'>live_render.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_emoji_codes.py'>_emoji_codes.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/box.py'>box.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/color.py'>color.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_timer.py'>_timer.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_fileno.py'>_fileno.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/align.py'>align.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/theme.py'>theme.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/style.py'>style.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/default_styles.py'>default_styles.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_wrap.py'>_wrap.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_log_render.py'>_log_render.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/emoji.py'>emoji.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/layout.py'>layout.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/containers.py'>containers.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_emoji_replace.py'>_emoji_replace.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/traceback.py'>traceback.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/region.py'>region.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/protocol.py'>protocol.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_loop.py'>_loop.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/control.py'>control.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/filesize.py'>filesize.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_null_file.py'>_null_file.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_palettes.py'>_palettes.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_pick.py'>_pick.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/file_proxy.py'>file_proxy.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/palette.py'>palette.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/markup.py'>markup.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_ratio.py'>_ratio.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/repr.py'>repr.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/constrain.py'>constrain.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/pretty.py'>pretty.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/diagnose.py'>diagnose.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/columns.py'>columns.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/rule.py'>rule.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_inspect.py'>_inspect.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/markdown.py'>markdown.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/pager.py'>pager.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/text.py'>text.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/highlighter.py'>highlighter.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_spinners.py'>_spinners.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/terminal_theme.py'>terminal_theme.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/bar.py'>bar.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/live.py'>live.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/py.typed'>py.typed</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/syntax.py'>syntax.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/table.py'>table.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_export_format.py'>_export_format.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/progress_bar.py'>progress_bar.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/errors.py'>errors.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/prompt.py'>prompt.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/segment.py'>segment.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/ansi.py'>ansi.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/progress.py'>progress.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_stack.py'>_stack.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_windows.py'>_windows.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/cells.py'>cells.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_win32_console.py'>_win32_console.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/panel.py'>panel.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/styled.py'>styled.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/spinner.py'>spinner.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_windows_renderer.py'>_windows_renderer.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/json.py'>json.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/padding.py'>padding.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/__main__.py'>__main__.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/scope.py'>scope.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_extension.py'>_extension.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/status.py'>status.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/abc.py'>abc.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/jupyter.py'>jupyter.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/color_triplet.py'>color_triplet.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- _unicode_data Submodule -->
			<details>
				<summary><b>_unicode_data</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ rich._unicode_data</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode15-0-0.py'>unicode15-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode5-2-0.py'>unicode5-2-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode15-1-0.py'>unicode15-1-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode17-0-0.py'>unicode17-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode6-1-0.py'>unicode6-1-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode8-0-0.py'>unicode8-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode13-0-0.py'>unicode13-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode11-0-0.py'>unicode11-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode4-1-0.py'>unicode4-1-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode6-0-0.py'>unicode6-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode6-3-0.py'>unicode6-3-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode14-0-0.py'>unicode14-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode16-0-0.py'>unicode16-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode6-2-0.py'>unicode6-2-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode12-0-0.py'>unicode12-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode9-0-0.py'>unicode9-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode5-0-0.py'>unicode5-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode7-0-0.py'>unicode7-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode5-1-0.py'>unicode5-1-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode12-1-0.py'>unicode12-1-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/unicode10-0-0.py'>unicode10-0-0.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Textualize/rich/blob/master/rich/_unicode_data/_versions.py'>_versions.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Tox, Poetry

### Installation

Build rich from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/Textualize/rich
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd rich
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![tox][tox-shield]][tox-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [tox-shield]: None -->
	<!-- [tox-link]: None -->

	**Using [tox](None):**

	```sh
	❯ echo 'INSERT-INSTALL-COMMAND-HERE'
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![poetry][poetry-shield]][poetry-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [poetry-shield]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json -->
	<!-- [poetry-link]: https://python-poetry.org/ -->

	**Using [poetry](https://python-poetry.org/):**

	```sh
	❯ poetry install
	```

### Usage

Run the project with:

**Using [tox](None):**
```sh
echo 'INSERT-RUN-COMMAND-HERE'
```
**Using [poetry](https://python-poetry.org/):**
```sh
poetry run python {entrypoint}
```

### Testing

Rich uses the {__test_framework__} test framework. Run the test suite with:

**Using [tox](None):**
```sh
echo 'INSERT-TEST-COMMAND-HERE'
```
**Using [poetry](https://python-poetry.org/):**
```sh
poetry run pytest
```

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## Contributing

- **💬 [Join the Discussions](https://github.com/Textualize/rich/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Textualize/rich/issues)**: Submit bugs found or log feature requests for the `rich` project.
- **💡 [Submit Pull Requests](https://github.com/Textualize/rich/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Textualize/rich
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
   <a href="https://github.com{/Textualize/rich/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Textualize/rich">
   </a>
</p>
</details>

---

## License

Rich is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
