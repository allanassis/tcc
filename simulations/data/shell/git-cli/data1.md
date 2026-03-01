# Git

## Overview

Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. Created by Linus Torvalds in 2005, Git enables multiple developers to collaborate seamlessly by tracking changes in source code during software development.

### Domain Concepts

- **Repository:** A directory or storage space where your project lives, containing all the project files and the entire history of changes.
- **Commit:** A snapshot of changes recorded in the repository history, representing a point in time.
- **Branch:** A movable pointer to a commit, enabling multiple lines of development.
- **Merge:** The process of combining changes from different branches.
- **Remote:** Versions of your project hosted on the Internet or network, allowing collaboration.
- **Index (Staging Area):** Intermediate storage where files are marked for the next commit.
- **Checkout:** Switching between different branches or commits.
- **Clone:** A copy of a remote repository on your local machine.
- **Pull & Push:** Commands to fetch changes from or send changes to a remote repository.

Git models these concepts through a content-addressable filesystem and SHA-1 hash identifiers, offering efficient branching and merging which are core strengths of the tool.

---

## Installation

Git runs on Linux, macOS, and Windows. Installation methods vary based on your platform.

### Windows

- Download and install from [https://git-scm.com/download/win](https://git-scm.com/download/win).

### macOS

Install via Homebrew:

```bash
brew install git
```

Alternatively, install Xcode Command Line Tools (includes Git):

```bash
xcode-select --install
```

### Linux

Install using your package manager:

- Debian/Ubuntu:

```bash
sudo apt-get update
sudo apt-get install git
```

- Fedora:

```bash
sudo dnf install git
```

- Arch:

```bash
sudo pacman -S git
```

### Verify Installation

```bash
git --version
```

Expected output:

```
git version 2.xx.x
```

---

## Usage and Examples

### Initializing a New Repository

```bash
git init
```

Creates a new Git repository in the current directory.

### Cloning a Repository

```bash
git clone https://github.com/user/repo.git
```

Copies a remote repository locally.

### Making Changes and Committing

```bash
# Track file changes
git add filename

# Commit changes with message
git commit -m "Your commit message"
```

### Basic Workflow

```bash
git status       # Show modified files
git diff         # Show changes between working directory and index
git add .        # Stage all changes
git commit -m "Commit message"
git push origin main  # Push changes to remote main branch
```

### Branching and Merging

Create and switch to a new branch:

```bash
git checkout -b feature-branch
```

Merge changes back to main branch:

```bash
git checkout main
git merge feature-branch
```

### Pulling Changes

Download and merge changes from remote:

```bash
git pull origin main
```

### Checking History

```bash
git log
```

Shows commit history.

---

## API Reference

Git primarily exposes its functionality via the `git` command line interface with numerous commands and options.

Below are key commands representing execution facts about their behavior and usage:

### `git init [directory]`

- Initializes a new empty Git repository or reinitializes an existing one.
- Creates `.git` directory containing repository metadata.
- If directory is omitted, current directory is used.

### `git clone [repository-url] [directory]`

- Creates a copy of an existing repository.
- Clones all branches and history locally.
- Directory is optional; defaults to the repository name.

### `git status`

- Shows the working tree status.
- Lists files staged for commit, modified, or untracked.

### `git add [file(s)]`

- Adds changes to the index (staging area).
- Supports individual files, directories, or `.` for all.

### `git commit -m "message" [options]`

- Records staged changes in a new commit.
- `-m` specifies commit message.
- Commits include author metadata and a SHA-1 hash.

### `git branch [branch-name]`

- Lists existing branches when no argument is given.
- Creates a new branch if branch-name is specified.

### `git checkout [branch|commit]`

- Switches branches or restores files.
- With branch name, moves HEAD to that branch.
- With commit hash, creates a detached HEAD state.

### `git merge [branch]`

- Combines changes from the named branch into the current one.
- May result in conflicts requiring manual resolution.

### `git pull [remote] [branch]`

- Fetches from remote and merges into current branch.
- Equivalent to `git fetch` plus `git merge`.

### `git push [remote] [branch]`

- Updates remote refs with local commits.
- Requires authentication for remote repos.

### `git log [options]`

- Displays commit history.
- Supports filtering by author, dates, and formatting.

---

## Contributing

Git is an open-source project maintained by a community of developers worldwide.

To contribute:

1. Fork the official Git repository: https://github.com/git/git
2. Clone your fork locally and create a branch for your feature or bugfix.
3. Make your changes with clear commit messages.
4. Compile and test your changes locally.
5. Submit a pull request to the official repository.
6. Adhere to coding standards and review feedback.

Refer to [Git’s official CONTRIBUTING.md](https://github.com/git/git/blob/master/CONTRIBUTING.md) for detailed guidelines.

---

## License

Git is distributed under the GNU General Public License version 2 (GPLv2).

See [LICENSE](https://github.com/git/git/blob/master/COPYING) for full details.

---

## Contact

- Official Website: https://git-scm.com/
- Source Code: https://github.com/git/git
- Mailing Lists: https://git-scm.com/community
- Issue Tracker: https://github.com/git/git/issues

For questions or support, visit the Git community resources above.
