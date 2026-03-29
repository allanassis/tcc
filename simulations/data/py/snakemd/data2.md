# SnakeMD

## Overview

SnakeMD is a lightweight, markdown-based note-taking application inspired by the classic Snake game. It integrates note creation and navigation into an engaging, retro-style interface. The tool is designed to boost productivity by combining the familiarity and simplicity of markdown with an interactive game mechanic, allowing users to organize and edit notes seamlessly while enjoying an entertaining UI.

### Domain Concepts

- **Markdown Notes:** The core concept behind SnakeMD is managing notes written in Markdown, a lightweight markup language for formatting text.
- **Interactive Note Navigation:** Notes are navigated and managed through a game-like interface inspired by the classic Snake game, where users control a "snake" to select, add, or modify notes.
- **File-based Note Storage:** Notes are stored as markdown files in a directory, allowing easy access and organization outside the application.
- **Real-time Editing:** Users can edit note content in a text editor embedded or opened from the interface.
- **Cross-platform Behavior:** Designed to run in terminal environments across multiple operating systems.

---

## Installation

### Prerequisites

- Python 3.6 or higher
- Git (to clone the repository)
- Terminal with support for curses (Linux, macOS, Windows Subsystem for Linux recommended)

### Steps

1. Clone the repository:

```bash
git clone https://github.com/TheRenegadeCoder/SnakeMD.git
cd SnakeMD
```

2. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install any dependencies (the project is lightweight and may only require standard library):

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python snakemd.py
```

If a `requirements.txt` does not exist, all dependencies are likely from Python standard libraries.

---

## Usage and Examples

Run the main application script to start the SnakeMD interface, which opens in the terminal.

### Basic Navigation and Editing Pattern

1. **Navigate notes** – Control the snake with arrow keys (or WASD keys) to move the snake head to different notes (represented as blocks).
2. **Select a note** – Moving the snake over a note allows selection.
3. **Edit or create notes** – Press a designated key (like `Enter`) to open the selected note in the default system editor or an embedded editing mode.
4. **Save notes** – Save markdown files upon editing completion.
5. **Create new notes** – The snake can "eat" markers that trigger creation of new markdown notes.
6. **Delete notes** – Specific keys allow removing notes.

### Running the Application (Example)

```bash
python snakemd.py
```

You will see a snake moving on your terminal screen. Use arrow keys to navigate between notes, open and edit notes, and add new ones.

---

## API Reference

SnakeMD is primarily a terminal application with a focus on user interaction, but it exposes key modules and functions managing its behavior:

### Core Components

- `Game` class
  - Manages the game loop and snake movements.
  - Handles input processing and collision detection with notes.

- `NoteManager`
  - Responsible for loading, saving, creating, and deleting markdown notes.
  - Interfaces with the file system to read/write `.md` files.

- `Snake` class
  - Represents the snake controlled by the user.
  - Updates position based on input, detects note collisions.

- `Renderer`
  - Handles terminal output using curses.
  - Draws the snake, notes, and interface elements in real time.

### Important Functions

- `Game.run()`
  - Starts and maintains the game loop.
  - Processes user input, updates game state, and renders output until exit.

- `NoteManager.load_notes(directory)`
  - Loads all notes from a specified directory into the game.

- `NoteManager.save_note(note)`
  - Saves the content of a note to the filesystem.

- `Snake.move(direction)`
  - Moves the snake in the specified direction; updates game state accordingly.

- `Renderer.draw()`
  - Refreshes the terminal display with updated game and note information.

### Parameters and Data Flows

- Notes are stored as markdown files with filename identifiers.
- The snake's position is tracked as coordinates matched to notes' locations on the board.
- User inputs correspond to movement or action commands processed by `Game`.

---

## License

SnakeMD is distributed under the MIT License. See the [LICENSE](https://github.com/TheRenegadeCoder/SnakeMD/blob/master/LICENSE) file for details.
