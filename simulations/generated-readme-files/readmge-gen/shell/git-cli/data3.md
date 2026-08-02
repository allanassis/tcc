# Git

## Overview

Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. It enables multiple developers to collaborate on source code history management, track changes, and merge contributions seamlessly. Git's domain revolves around concepts such as commits, branches, repositories, merges, remotes, and hooks.

### Core Domain Concepts

- **Repository (repo):** A directory structure containing all project files, including a history of changes.
- **Commit:** A snapshot of changes in the repository at a specific point in time.
- **Branch:** A movable pointer to a commit, representing independent lines of development.
- **Merge:** Combining changes from different branches.
- **Remote:** A version of the repository hosted on another server, often used for collaboration.
- **Index (staging area):** A preparation area for changes before committing.
- **Working Directory:** The checked-out project files where edits happen.
- **HEAD:** A pointer to the current branch or commit checked out.
- **Tag:** A named reference to a specific commit, often used for releases.

Git also supports concepts like rebasing, cherry-picking, submodules, and hooks.

---

## Installation

Git supports installation on multiple operating systems including Linux, macOS, and Windows.

### Linux

Install via package manager, e.g., on Debian/Ubuntu:

```bash
sudo apt update
sudo apt install git
```

### macOS

Install with Homebrew:

```bash
brew install git
```

Or install Xcode Command Line Tools which include Git:

```bash
xcode-select --install
```

### Windows

Download the installer from the official Git website:  
https://git-scm.com/download/win

Alternatively, install via package managers like `choco`:

```bash
choco install git
```

---

## Usage and Examples

Git is primarily used via its command-line interface.

### Initialize a repository

```bash
git init
```

Creates a new Git repository in the current directory.

### Clone an existing repository

```bash
git clone https://github.com/user/repo.git
```

Downloads a remote repository locally.

### Check repository status

```bash
git status
```

Shows changed, staged, and untracked files.

### Stage files for commit

```bash
git add filename.txt
```

Adds files to the staging area.

### Commit changes

```bash
git commit -m "Commit message"
```

Records staged changes in the repository.

### View commit history

```bash
git log
```

Shows the commit history.

### Branching

Create a new branch:

```bash
git branch feature-branch
```

Switch to a branch:

```bash
git checkout feature-branch
```

Create and switch in one step:

```bash
git checkout -b new-branch
```

### Merging branches

Merge a branch into the current branch:

```bash
git merge feature-branch
```

### Pushing changes

Push commits to remote repository:

```bash
git push origin main
```

### Pulling changes

Fetch and merge changes from remote:

```bash
git pull origin main
```

### Undo changes

Discard changes in working directory:

```bash
git checkout -- filename.txt
```

Unstage files:

```bash
git reset HEAD filename.txt
```

---

## API Reference

Git commands serve as the primary user API. Below are important commands with their main options that represent Git’s execution facts:

### `git init [directory]`

Initialize a new repository in the given directory (or current if none).

---

### `git clone [repository] [directory]`

Clone a remote repository into a new local directory.

- `repository`: URL or path of the repo to clone.
- `directory` (optional): Local directory name.

---

### `git status`

Display the current state of the working directory and staging area.

---

### `git add [file(s)]`

Add file changes to the staging area.

---

### `git commit -m "message"`

Save staged changes into a new commit with a message.

---

### `git log [options]`

Show commit logs. Options like `--oneline`, `--graph` visualize history compactly.

---

### `git branch [branch-name]`

Create a new branch. With `-d`, delete a branch.

---

### `git checkout [branch-or-commit]`

Switch branches or restore files.

---

### `git merge [branch]`

Merge another branch into the current one.

---

### `git push [remote] [branch]`

Push local branch changes to a remote repository.

---

### `git pull [remote] [branch]`

Fetch changes from a remote repo and merge to current branch.

---

### `git reset [options] [commit]`

Reset current HEAD to a specified state, with modes like soft, mixed, or hard.

---

## Examples

Initialize, add file, and commit:

```bash
git init
echo "Hello Git" > README.md
git add README.md
git commit -m "Add README"
```

Clone and switch branch:

```bash
git clone https://github.com/git/git.git
cd git
git checkout maint
```

Merge branch:

```bash
git checkout main
git merge feature-branch
```

Push changes to GitHub:

```bash
git push origin main
```

---

## License

Git is distributed under the GNU General Public License version 2 (GPLv2).  
For details see the LICENSE file in the Git source repository:  
https://github.com/git/git/blob/master/COPYING

---
