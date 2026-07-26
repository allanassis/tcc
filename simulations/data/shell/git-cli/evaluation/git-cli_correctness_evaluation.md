# Correctness Evaluation — README-Gen (project: git-cli)

Repository (ground truth): https://github.com/git/git
Core functionality: Create and manage commits
Installed artifact used for cross-check: `git version 2.55.0` (Homebrew, macOS 26.5.2, arm64)

## Execution Methodology (applies to all READMEs)

- **Environment:** throwaway repositories created under `/tmp` (`git init`); host
  git 2.55.0. `--global` config commands were treated as valid but not run against
  the host to avoid mutating host state.
- **Installation paths:** the macOS `brew install git` path was executed on-host;
  `xcode-select --install` was validated as a valid command with the Command Line
  Tools already present (`xcode-select -p` → `/Library/Developer/CommandLineTools`).
  OS-specific paths that cannot run on macOS (Windows installer, `apt-get`, `dnf`,
  `pacman`, `choco`) were validated by confirming the documented package/URL exists
  in the respective official repository (HTTP 200 + genuine package page title).
- **Snippet unit:** one fenced code block = one snippet.
- **Placeholder policy (rubric rule 6):** a snippet containing an unresolved
  meta-placeholder that cannot be executed verbatim (`<file>`, `<file1> <file2>`,
  `INSERT-…-HERE`, `{…}`) FAILS the execution rules.
- **Illustrative argument values:** conventional example values that are valid git
  syntax and behave exactly as the prose describes when a real value is supplied
  (e.g. `https://github.com/user/repo.git`, remote `origin`, branch `main`) are
  NOT treated as failures — they are not generation placeholders and the command
  form and documented behavior are correct. This policy is applied uniformly.

## Cross-checked sources

- Repository & license: https://github.com/git/git , `COPYING` (raw) — confirms
  "GNU General Public License … v2".
- Official docs: https://git-scm.com/docs and local `git help <cmd>` (2.55.0).
- Installer/package existence:
  - https://git-scm.com/download/win → 200
  - https://packages.ubuntu.com/noble/git → 200 ("Details of package git in noble")
  - https://packages.debian.org/stable/git → 200
  - https://packages.fedoraproject.org/pkgs/git/git/ → 200 ("git - Fedora Packages")
  - https://archlinux.org/packages/extra/x86_64/git/ → 200
  - https://community.chocolatey.org/packages/git → 200 ("Git 2.55.0.3")
- API flags verified in installed git: `git remote` (add/rename/remove/show),
  `git reset --soft|--mixed|--hard`, `git branch -d/-D`, `git commit -a/-m`,
  `git checkout -b`; `maint` branch exists on git/git
  (`git ls-remote --heads … maint` → `e9019fc…`).

---

# README 1 — data1.md

## Project Title (T)
- V1 title matches repo/officially-documented name: "Git" = repo `git`. **1**
- V2 does not describe a different project. **1**
- V3 no hallucinated terminology. **1**
- **T = 3/3 = 100%**

## Overview (O)
Claims: "distributed version control system … Linus Torvalds 2005 … de facto
standard for source code management." Domain-concept glossary (repository, commit,
branch, merge, remote, index, working directory, checkout, tag) all accurate.
- V1 primary functionality correctly described (distributed VCS). **1**
- V2 supported by repository artifacts. **1**
- V3 no unsupported features described. **1**
- V4 correct software domain (version control). **1**
- V5 terminology matches repository terminology. **1**
- **O = 5/5 = 100%**

## Installation (I) — executed / validated
Paths documented: Windows installer, macOS `brew install git`, macOS
`xcode-select --install`, Ubuntu/Debian `apt-get`, Fedora `dnf`; verify `git --version`.
- V1 required dependencies declared — package-manager paths resolve deps
  automatically; no manual dependency omitted. **1**
- V2 commands execute without modification — `brew install git` executed
  (idempotent: "already installed and up-to-date"); `git --version` → 2.55.0;
  `xcode-select` valid; apt/dnf packages confirmed to exist. **1**
- V3 no unresolved dependency errors (brew resolved cleanly). **1**
- V4 environment requirements correct — no false version claim; "available on
  almost all OS" is accurate. **1**
- V5 expected executable artifact produced — `git` binary (`git --version` works). **1**
- **I = 5/5 = 100%**

## Usage and Examples (U) — 12 snippets executed
| # | Snippet | Executes | Behaves as described | E_i |
|---|---|---|---|---|
| 1 | `git init` | yes | yes | 1 |
| 2 | `git clone https://github.com/user/repo.git` | yes (real URL clones; illustrative remote) | yes | 1 |
| 3 | `git status` | yes | yes | 1 |
| 4 | `git add <file1> <file2>` + `git add .` | **no** — `<file1> <file2>` placeholder | — | 0 |
| 5 | `git commit -m "Descriptive commit message"` | yes | yes | 1 |
| 6 | `git push origin main` | yes (valid; illustrative remote) | yes | 1 |
| 7 | `git checkout -b feature-branch` | yes | yes | 1 |
| 8 | `git checkout main` + `git merge feature-branch` | yes | yes | 1 |
| 9 | `git log` | yes | yes | 1 |
| 10 | `git diff` | yes | yes | 1 |
| 11 | `git reset <file>` | **no** — `<file>` placeholder | — | 0 |
| 12 | `git checkout -- <file>` | **no** — `<file>` placeholder | — | 0 |

- **U = 9/12 = 75%**

## API Reference (A) — 11 primary elements + 5 supplementary, all validated
Documented: `git init [directory]`, `git clone [repository] [directory]`,
`git status`, `git add <pathspec>`, `git commit -m <message>`,
`git branch [branch-name]`, `git checkout [-b] [branch-name|commit]`,
`git merge <branch>`, `git pull [remote] [branch]`, `git push [remote] [branch]`,
`git log [options]`; plus `git rebase`, `git stash`, `git remote`, `git tag`,
`git config`.
Every element passes all 6 rules: exists in repo (git-scm.com/docs + `git help`),
names correct, parameter notation correct, return/behavior correct, behavior
consistent with execution (init/add/commit/checkout/merge/log/diff executed
above), none deprecated. **A = 100%**

## License (L)
- V1 matches repo `COPYING` (GPL v2). **1**
- V2 valid identifier (GPL-2.0). **1**
- V3 no conflicting license info. **1**
- **L = 3/3 = 100%**

**C_R(data1) = (100+100+100+75+100+100)/6 = 95.83%**

---

# README 2 — data2.md

## Project Title (T): "Git" → **T = 100%**

## Overview (O)
"distributed VCS … Linus Torvalds 2005 … snapshots over differences, immutable
history, distributed workflows." All accurate. V1–V5 all 1. **O = 100%**

## Installation (I) — executed / validated
Paths: Linux `apt`, `dnf`, `pacman`; macOS `brew`; `xcode-select`; Windows
installer. `brew install git` executed; apt/dnf/pacman packages and installer
URL all confirmed to exist. No false requirements. V1–V5 all 1. **I = 100%**

## Usage and Examples (U) — 12 snippets, none contain placeholders
| # | Snippet | E_i |
|---|---|---|
| 1 | `git config --global user.name/user.email` | 1 |
| 2 | `mkdir my-project; cd my-project; git init` | 1 |
| 3 | `git clone …/user/repo.git; cd repo` | 1 |
| 4 | `git status` | 1 |
| 5 | `git add file1.txt file2.txt` | 1 |
| 6 | `git commit -m "Describe your changes"` | 1 |
| 7 | `git checkout -b feature-branch` | 1 |
| 8 | `git checkout main; git merge feature-branch` | 1 |
| 9 | `git remote add origin …` | 1 |
| 10 | `git push origin main` | 1 |
| 11 | `git pull origin main` | 1 |
| 12 | `git log --oneline --graph --all` | 1 |

All use real filenames/literal values (no `<…>` placeholders); each is valid git
syntax and behaves as described (verified equivalents executed in throwaway repos).
**U = 12/12 = 100%**

## API Reference (A)
`git init`, `git clone`, `git add`, `git commit [-m][-a]`, `git status`,
`git branch`, `git checkout`, `git merge`, `git remote [add|remove|show]`,
`git push`, `git pull`, `git log`. `git remote add/remove/show` and `git commit -a`
confirmed in installed git. All pass 6 rules. **A = 100%**

## License (L): GPL v2, link to gnu.org gpl-2.0; matches `COPYING`. **L = 100%**

**C_R(data2) = (100+100+100+100+100+100)/6 = 100%**

---

# README 3 — data3.md

## Project Title (T): "Git" → **T = 100%**

## Overview (O)
"distributed VCS … commits, branches, repositories, merges, remotes, hooks …
rebasing, cherry-picking, submodules, hooks." All real git concepts/features.
V1–V5 all 1. **O = 100%**

## Installation (I) — executed / validated
Paths: Linux `apt`; macOS `brew`; `xcode-select`; Windows installer;
`choco install git`. `brew install git` executed; apt, installer URL, and
Chocolatey package ("Git 2.55.0.3") all confirmed. V1–V5 all 1. **I = 100%**

## Usage and Examples (U) — 18 snippets, none contain placeholders
Usage section (14): `git init`, `git clone …/user/repo.git`, `git status`,
`git add filename.txt`, `git commit -m "Commit message"`, `git log`,
`git branch feature-branch`, `git checkout feature-branch`,
`git checkout -b new-branch`, `git merge feature-branch`, `git push origin main`,
`git pull origin main`, `git checkout -- filename.txt`,
`git reset HEAD filename.txt`.
Examples section (4): `git init; echo … > README.md; git add README.md;
git commit -m "Add README"`; `git clone https://github.com/git/git.git; cd git;
git checkout maint`; `git checkout main; git merge feature-branch`;
`git push origin main`.
All are valid git syntax with real/literal values; the `README.md` workflow and
`git checkout maint` (branch confirmed to exist on git/git) execute as described.
**U = 18/18 = 100%**

## API Reference (A)
`git init`, `git clone`, `git status`, `git add`, `git commit -m`, `git log`,
`git branch [-d]`, `git checkout`, `git merge`, `git push`, `git pull`,
`git reset [soft|mixed|hard]`. `git reset --soft/--mixed/--hard` and `git branch -d`
confirmed in installed git. All pass 6 rules. **A = 100%**

## License (L): GPL v2 (GPLv2); link to `COPYING`; matches repo. **L = 100%**

**C_R(data3) = (100+100+100+100+100+100)/6 = 100%**

---

## Section averages (over 3 READMEs)
- Title 100, Overview 100, Installation 100, Usage (75+100+100)/3 = 91.67,
  API 100, License 100.
- **Correctness average = (95.83+100+100)/3 = 98.61%**
