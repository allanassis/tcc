# Git

## Overview

Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. It allows multiple developers to work on the same codebase concurrently without interfering with each other, providing strong support for non-linear development workflows with branches and merges. Git models the content and history of a project as snapshots and uses a powerful staging area to prepare changes before committing.

### Key Domain Concepts

- **Repository**: A collection of files and their history, either local or remote.
- **Commit**: A snapshot of the project at a point in time, with metadata.
- **Branch**: A pointer to a series of commits, facilitating parallel development.
- **Merge**: Combining changes from different branches.
- **Index (Staging area)**: A place where changes are prepared before committing.
- **Working directory**: Your local checkout of files.
- **Remote**: A version of the repository hosted elsewhere (GitHub, GitLab, etc.).

Git's design enables both centralized and decentralized workflows, allowing powerful branching and collaborative development.

---

## Installation

Git is available on most platforms including Linux, macOS, and Windows.

### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install git
```

### macOS

Install via Homebrew:

```bash
brew install git
```

Or via the standalone installer from [git-scm.com](https://git-scm.com/download/mac).

### Windows

Download and install Git for Windows from [git-scm.com](https://git-scm.com/download/win).

---

## Usage and Examples

Below are common patterns for using Git commands effectively.

### Initialize a New Repository

```bash
git init
```

Creates a new Git repository in the current directory.

### Clone an Existing Repository

```bash
git clone https://github.com/user/repo.git
```

Copies a remote repository locally.

### Check Repository Status

```bash
git status
```

Shows changes staged for commit, unstaged changes, and untracked files.

### Stage Files for Commit

```bash
git add <file>
git add .
```

Adds changes to the staging area.

### Commit Changes

```bash
git commit -m "Your descriptive commit message"
```

Records staged changes along with a message.

### View Commit History

```bash
git log
```

Shows the list of commits in the current branch.

### Create and Switch Branches

```bash
git branch <branch-name>
git checkout <branch-name>
```

Or combine:

```bash
git checkout -b <branch-name>
```

Starts work on a new branch.

### Merge Branches

```bash
git checkout main
git merge <branch-name>
```

Combines the changes from one branch into another.

### Push Changes to Remote

```bash
git push origin <branch-name>
```

Uploads commits to a remote repository.

### Pull Changes from Remote

```bash
git pull origin <branch-name>
```

Fetches and merges changes from a remote branch.

---

## API Reference (Command Line Interface)

Git consists primarily of commands executed via CLI. Below are key commands with their usage facts.

### `git init`

Creates a new repository. Must be run in a directory without an existing repository.

### `git clone <repo> [<dir>]`

Fetches a remote repository and creates a local copy. Optionally specify directory name.

### `git status`

Displays the state of the working directory and staging area.

### `git add <file>...`

Stages changes to files for the next commit. Use `git add .` to stage all changes.

### `git commit -m <message>`

Creates a new commit from staged changes with a descriptive message.

### `git log [options]`

Shows the commit history. Options allow filtering, formatting, and limiting output.

### `git branch [<branch-name>]`

Lists branches if no argument; creates a branch if `<branch-name>` is given.

### `git checkout <branch-or-commit>`

Switches working directory to the specified branch or commit.

### `git merge <branch>`

Merges specified branch into the current branch.

### `git push [<remote>] [<branch>]`

Updates the remote repository with local commits.

### `git pull [<remote>] [<branch>]`

Fetches from a remote and merges into the current branch.

---

## Contributing

Git is an open-source project hosted on GitHub.

- Fork the repository at [https://github.com/git/git](https://github.com/git/git).
- Create a feature or fix branch.
- Follow the coding guidelines provided in the documentation.
- Test changes thoroughly, including passing test suites.
- Submit pull requests with clear descriptions.

Contributions go through the Git mailing list and workflows; details are in the official Git documentation.

---

## License

Git is licensed under the GNU General Public License version 2 (GPLv2). See the LICENSE file in the repository for details.

---

## Contact

- Official website: [https://git-scm.com/](https://git-scm.com/)
- Source code and issue tracker: [https://github.com/git/git](https://github.com/git/git)
- Mailing lists and community: [https://git-scm.com/community](https://git-scm.com/community)
