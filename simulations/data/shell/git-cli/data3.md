# Git

## Overview

Git is a distributed version control system designed to manage source code history efficiently and securely. Created by Linus Torvalds in 2005, Git allows multiple developers to collaborate on projects by tracking changes, facilitating branching and merging workflows, and enabling versioning and recovery. It is widely recognized for its speed, data integrity, and support for non-linear development via branches.

### Domain Concepts

- **Repository (repo):** A data structure used by Git to store metadata and object database for a set of files and their history.
- **Commit:** A snapshot of changes in the repository, identified by a SHA-1 hash.
- **Branch:** A movable pointer to a commit, enabling parallel development.
- **Merge:** Integrating changes from different branches.
- **Clone:** Creating a copy of a remote repository locally.
- **Remote:** Versions of the project hosted on different servers.
- **Index (staging area):** Intermediate space for changes before committing.
- **HEAD:** Pointer to the current commit or reference.

Git abstracts the filesystem and history changes as objects (blobs, trees, commits, tags), providing a structured yet flexible model for source control.

---

## Installation

Git can be installed on most operating systems:

### On Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install git
```

### On macOS

Install via Homebrew:

```bash
brew install git
```

### On Windows

Download the installer from [https://git-scm.com/download/win](https://git-scm.com/download/win) and follow the setup wizard.

### Verify Installation

```bash
git --version
```

Expected output:

```
git version 2.x.x
```

---

## Usage and Examples

### Initialize a New Repository

```bash
git init
```

Creates a new Git repository in the current directory.

### Clone a Remote Repository

```bash
git clone https://github.com/user/repo.git
```

Downloads the full repository history locally.

### Check Repository Status

```bash
git status
```

Displays the state of the working directory and staging area.

### Stage Files for Commit

```bash
git add <file1> <file2>
```

Prepares changes for the next commit.

### Commit Changes

```bash
git commit -m "Descriptive commit message"
```

Records staged changes to the repository history.

### View Commit History

```bash
git log
```

Shows a list of commits on the current branch.

### Create and Switch Branches

```bash
git checkout -b feature-branch
```

Creates a new branch and switches to it.

### Merge Branches

```bash
git checkout main
git merge feature-branch
```

Integrates changes from `feature-branch` into `main`.

### Push Changes to Remote

```bash
git push origin main
```

Uploads local commits to the remote repository.

### Pull Changes from Remote

```bash
git pull
```

Fetches and merges changes from the remote repository.

---

## API Reference

Git primarily exposes a command-line interface (CLI) with numerous commands and options. Key commands include:

### `git init [directory]`

Initializes a new Git repository.

- `directory` (optional): The folder to create the repository in. Defaults to current directory.

### `git clone <repository> [directory]`

Clones a remote repository.

- `repository`: URL or path of the repository.
- `directory` (optional): Local directory name.

### `git add <pathspec>`

Stages changes in specified files.

- `pathspec`: Files or directories to stage.

### `git commit -m <message>`

Commits staged changes with a message.

- `message`: Commit description.

### `git status`

Shows the working tree status.

### `git log [options]`

Displays commit history.

- Common options: `--oneline`, `--graph`, `--decorate`.

### `git branch [branchname]`

Creates, lists, or deletes branches.

- Without arguments: lists branches.
- With `branchname`: creates a new branch.

### `git checkout <branch>`

Switches branches or restores working tree files.

### `git merge <branch>`

Merges changes from another branch.

### `git push [remote] [branch]`

Pushes commits to remote repository.

### `git pull [remote] [branch]`

Fetches and merges changes from the remote.

### Advanced commands detail:

- **Rebase**: `git rebase <branch>` - Reapplies commits on top of another base tip.
- **Reset**: `git reset [--soft|--mixed|--hard] <commit>` - Resets current HEAD to a specific state.
- **Tag**: `git tag <name>` - Marks specific commits as important.

---

## Contributing

Git is an open-source project managed via the Git SCM repository itself on [https://github.com/git/git](https://github.com/git/git).

### How to contribute

1. Fork the repository and clone locally.
2. Study the [Pro Git book](https://git-scm.com/book/en/v2) and Git internals.
3. Develop and test your features or fixes thoroughly.
4. Submit patches via mailing list or pull requests as per [CONTRIBUTING.md](https://github.com/git/git/blob/master/CONTRIBUTING.md).
5. Engage with the Git community for review and feedback.

Contributions require adherence to coding standards and signed-off commits.

---

## License

Git is distributed under the GNU General Public License version 2 (GPLv2). See the [LICENSE](https://github.com/git/git/blob/master/COPYING) file for details.

---

## Contact

- **Official website:** https://git-scm.com
- **GitHub repository:** https://github.com/git/git
- **Mailing list:** git@vger.kernel.org
- **Community and support:** https://git-scm.com/community

For issues and feature requests, utilize the Git mailing list or GitHub issues on the official repository.
