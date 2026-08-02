# Git

## Overview

Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. Created by Linus Torvalds in 2005, it enables multiple developers to coordinate their work on source code, tracking changes, managing branches, and merging modifications seamlessly. Git models the domain concepts of commits, branches, repositories, and merges, allowing developers to manage source code evolution reliably.

### Domain Concepts

- **Repository:** A data structure storing all versions of files and metadata about the project history.
- **Commit:** A snapshot of changes with a unique SHA-1 identifier, representing project states.
- **Branch:** A movable pointer to a commit, enabling parallel lines of development.
- **Merge:** Integration of changes from different branches, resolving conflicts if any.
- **Index (Staging Area):** A preparatory area where changes are gathered before committing.
- **Remote:** A version of the repository hosted elsewhere, facilitating collaboration.
- **Working Directory:** The current files checked out from the repository for editing.

Git emphasizes snapshots over differences, immutable history, and distributed workflows.

---

## Installation

Git is available on major platforms including Linux, macOS, and Windows.

### Linux

Install Git via package managers:

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install git

# Fedora
sudo dnf install git

# Arch Linux
sudo pacman -S git
```

### macOS

Install Git via Homebrew:

```bash
brew install git
```

Alternatively, install Xcode Command Line Tools which includes Git:

```bash
xcode-select --install
```

### Windows

Download the installer from the official [Git website](https://git-scm.com/download/win) and follow the setup wizard.

---

## Usage and Examples

Git is primarily used via command-line interface (CLI). Below are common usage patterns illustrating basic and advanced workflows.

### Setup User Identity

Configure your user name and email before using Git:

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

### Initialize a Repository

Create a new Git repository in a folder:

```bash
mkdir my-project
cd my-project
git init
```

### Clone an Existing Repository

Download a remote repository:

```bash
git clone https://github.com/user/repo.git
cd repo
```

### Track Changes

Check status of your repository:

```bash
git status
```

Add files to staging area:

```bash
git add file1.txt file2.txt
```

Commit staged changes with a message:

```bash
git commit -m "Describe your changes"
```

### Branching and Merging

Create a new branch and switch to it:

```bash
git checkout -b feature-branch
```

Merge a branch into current branch:

```bash
git checkout main
git merge feature-branch
```

### Working with Remote Repositories

Add a remote:

```bash
git remote add origin https://github.com/user/repo.git
```

Push changes to remote:

```bash
git push origin main
```

Fetch and merge remote changes:

```bash
git pull origin main
```

### Viewing History

Show commit history:

```bash
git log --oneline --graph --all
```

---

## API Reference

Git’s primary public interface is through its CLI commands, which follow consistent syntax patterns. Below are key commands with important parameters and behavior focused on execution facts.

### `git init [directory]`

Initializes a new Git repository.

- `directory` (optional): Directory to initialize. Defaults to current directory.
- Creates `.git` metadata folder storing repository data.

### `git clone <repository> [directory]`

Copies a remote repository.

- `repository`: URL or path of remote repository.
- `directory` (optional): Target directory name.

Clones entire history and sets `origin` remote.

### `git add <pathspec>`

Stages changes for next commit.

- `pathspec`: Files or directories to add.

Supports patterns and recursive adds.

### `git commit [-m <message>] [-a]`

Records staged changes as a new commit.

- `-m <message>`: Commit message.
- `-a`: Automatically stage tracked files before committing.

Creates a commit object linking to parent commit(s).

### `git status`

Shows changes in working directory and staging area compared to last commit.

- Displays modified, untracked, and staged files.

### `git branch [branch-name]`

Lists branches or creates a new branch.

- Without argument: Lists local branches.
- With `branch-name`: Creates a branch pointing to current commit.

### `git checkout <branch|commit|file>`

Switches branches or restores files.

- `<branch>`: Move HEAD to branch.
- `<commit>`: Detach HEAD at commit.
- `<file>`: Restore file from HEAD or specified commit.

### `git merge <branch>`

Integrates changes from specified branch into current branch.

- Performs a three-way merge.
- May require conflict resolution if changes overlap.

### `git remote [add|remove|show]`

Manages tracked remote repositories.

- `add <name> <url>`: Adds a new remote.
- `remove <name>`: Removes a remote.
- `show <name>`: Shows remote details.

### `git push [remote] [branch]`

Uploads commits to a remote repository.

- `remote`: Remote name (e.g. origin).
- `branch`: Branch to push.

Rejected pushes may require pull or merge.

### `git pull [remote] [branch]`

Fetches and integrates changes from remote branch.

- Equivalent to `git fetch` followed by `git merge`.

### `git log [options]`

Shows commit logs.

- Common options:
  - `--oneline`: One line per commit.
  - `--graph`: ASCII graph of branch history.
  - `--all`: Show all refs.

---

## License

Git is distributed under the [GNU General Public License version 2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).

---
