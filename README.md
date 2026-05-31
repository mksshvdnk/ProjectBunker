# Bunker — Player Card Generator

A command-line Python tool that procedurally generates randomized player cards from a customizable parameter file.

## Changelog

### v2.0
- Added interactive CLI shell with command routing via dictionary, replacing single-command Typer setup
- Added `quit` and `help` commands; `help` builds itself automatically from the command dictionary
- Added `index` field to `Playercard` — players are now numbered automatically
- Added unknown command feedback in the shell
- Separated CLI logic into `main.py`, keeping `bunkerLogic.py` free of interface concerns
- Added Typer as a dependency

### v1.0
- Initial release with basic random player generation
- `PlayerCardGenerator` parses `Parameters.txt` into feature clusters
- `Playercard` data container with `age`, `gender`, `skill`, and `weakness` attributes
- `writePars()` method for formatted console output
- No third-party dependencies

## Features

- Randomly generates player cards with age, gender, skill, and weakness attributes
- Reads attribute pools from a plain-text `Parameters.txt` file — no code changes needed to customize values
- Interactive CLI shell with a self-documenting command system
- Clean separation between logic (`bunkerLogic.py`) and interface (`main.py`)

## Requirements

- Python 3.10+
- [Typer](https://typer.tiangolo.com/) (`pip install typer`)

## Project Structure

```
TopDeveloper/
├── bunkerLogic.py      # Core logic — Playercard and PlayerCardGenerator classes
├── main.py             # CLI shell and command routing
├── Parameters.txt      # Attribute definitions (customizable)
└── .gitignore
```

## Parameters.txt Format

Define four sections separated by blank lines. Section headers must be exactly `Age`, `Gender`, `Skill`, and `Weakness` (case-sensitive). Sections can appear in any order.

```
Age
Child
Teen
Adult
Senior

Gender
Male
Female
Non-binary

Skill
Swordsmanship
Archery
Magic
Stealth

Weakness
Fire
Water
Light
Darkness
```

## Usage

Start the interactive shell:

```bash
py main.py start
```

Available commands:

| Command | Description |
|---|---|
| `generateRandomPlayer` | Generates and prints a random player card |
| `help` | Lists all available commands |
| `quit` | Exits the shell |

Example output:

```
Player 1
Age Adult
Gender Female
Skill Magic
Weakness Fire
```

## Classes

### `Playercard` (`bunkerLogic.py`)

Data container for a single player's attributes.

| Member | Description |
|---|---|
| `index` | Player number, increments automatically |
| `age` | Randomly selected age category |
| `gender` | Randomly selected gender |
| `skill` | Randomly selected skill |
| `weakness` | Randomly selected weakness |
| `writePars()` | Prints all attributes to the console |

### `PlayerCardGenerator` (`bunkerLogic.py`)

Parses `Parameters.txt` and generates player cards.

| Member | Description |
|---|---|
| `parametersPath` | Path to the located `Parameters.txt` file |
| `players` | List of all generated `Playercard` instances |
| `clusters` | Internal line-index map used to locate attribute values in the file |
| `generateRandomPlayer()` | Randomly samples one value per feature and appends a new `Playercard` to `players` |

## Architecture

The project follows the **MVP (Model-View-Presenter)** pattern:

- **Model** — `Playercard` holds the data
- **Presenter** — `PlayerCardGenerator` handles the logic
- **View** — `main.py` manages user interaction via the CLI

This separation keeps the core logic reusable and independent of the interface — swapping the CLI for a GUI or web frontend would only require changes to `main.py`.