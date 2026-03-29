# Git

## Overview

Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. Created by Linus Torvalds in 2005, Git allows multiple developers to collaborate on the same codebase while tracking changes, branching, and merging effectively. It is the de facto standard for source code management in modern software development.

### Domain Concepts

- **Repository:** A collection of files and their history tracked by Git.
- **Commit:** A snapshot of changes in the repository, identified by a SHA-1 hash.
- **Branch:** A pointer to a commit, allowing multiple lines of development.
- **Merge:** Combining changes from different branches.
- **Remote:** A version of the repository hosted on a server that multiple users can access.
- **Index (Staging Area):** Area where changes are prepared before committing.
- **Working Directory:** The current local directory where files are edited.
- **Checkout:** Switching between branches or commits.
- **Tag:** Marking specific commits as important or release points.

Git provides powerful tools to manage branches, resolve conflicts, inspect history, and collaborate across distributed teams.

---

## Installation

Git is available on almost all operating systems:

### On Windows

Download the official installer from https://git-scm.com/download/win and follow the setup wizard.

### On macOS

Install via Homebrew:

```bash
brew install git
```

Or use the Xcode Command Line Tools package:

```bash
xcode-select --install
```

### On Linux

Use the distribution package manager, for example on Ubuntu/Debian:

```bash
sudo apt-get update
sudo apt-get install git
```

On Fedora:

```bash
sudo dnf install git
```

Verify installation by running:

```bash
git --version
```

---

## Usage and Examples

### Setting Up a Repository

Initialize a new repository:

```bash
git init
```

Clone an existing repository:

```bash
git clone https://github.com/user/repo.git
```

### Basic Workflow

1. Check status of files:

```bash
git status
```

2. Stage files for commit:

```bash
git add <file1> <file2>
# Or to stage all changes
git add .
```

3. Commit staged files:

```bash
git commit -m "Descriptive commit message"
```

4. Push commits to remote repository:

```bash
git push origin main
```

### Branching and Merging

Create and switch to a new branch:

```bash
git checkout -b feature-branch
```

Merge branch into current branch:

```bash
git checkout main
git merge feature-branch
```

### Viewing History

Show commit history:

```bash
git log
```

Show changes in working directory:

```bash
git diff
```

### Undoing Changes

Unstage a file:

```bash
git reset <file>
```

Discard changes in working directory:

```bash
git checkout -- <file>
```

---

## API Reference

Git provides a rich command-line interface with numerous commands. Below are some of the core commands along with their key options:

### `git init [directory]`

Creates a new Git repository.

- If `[directory]` is omitted, initializes the repository in the current directory.

### `git clone [repository] [directory]`

Copies an existing Git repository to a new local directory.

- `[repository]`: URL or path to the source repository.
- `[directory]`: Optional name of the directory to create.

### `git status`

Displays the status of the working directory and staging area.

### `git add <pathspec>`

Stages changes for the next commit.

- `<pathspec>`: Files or directories to stage.

### `git commit -m <message>`

Records staged changes as a new commit with message.

- `-m <message>`: Commit message string.

### `git branch [branch-name]`

- With no arguments: lists branches.
- Creating: `git branch <branch-name>` creates a new branch.

### `git checkout [-b] [branch-name | commit]`

Switches branches or restores working tree files.

- `-b`: Creates and switches to a new branch.

### `git merge <branch>`

Merges specified branch into current branch.

### `git pull [remote] [branch]`

Fetches changes from a remote repository and merges.

- Defaults to `origin` and current branch.

### `git push [remote] [branch]`

Sends commits from local branch to remote repository.

### `git log [options]`

Shows commit logs.

- Options control output format and filtering.

---

## Additional Tools and Commands

- `git rebase`: Reapplies commits on top of another base tip.
- `git stash`: Temporarily shelves changes in working directory.
- `git remote`: Manages set of tracked repositories.
- `git tag`: Creates, lists, or deletes tags.
- `git config`: Configures Git settings and preferences.

---

## License

Git is distributed under the GNU General Public License version 2. See the [LICENSE](https://github.com/git/git/blob/master/COPYING) file for details.
