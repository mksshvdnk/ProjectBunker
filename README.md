# Bunker — Player Card Generator

A command-line Python tool that procedurally generates randomized player cards from a customizable parameter file.

## Changelog

### v3.0
- Player cards now support any number of custom attributes — just add a new section to `Parameters.txt`, no code changes needed
- `Parameters.txt` sections can appear in any order without affecting output
- Minor improvements to value parsing and internal refactoring

### v2.0
- Added an interactive CLI shell — the tool now runs as a persistent session rather than a single command
- `help` command lists all available commands automatically
- Minor improvements including player numbering and unknown command feedback

### v1.0
- Initial release with basic random player generation from `Parameters.txt`
- Minor: `writePars()` for console output, no third-party dependencies

## Features

- Randomly generates player cards with any number of custom attributes
- Reads attribute pools from a plain-text `Parameters.txt` file — no code changes needed to add new features
- Sections can appear in any order in `Parameters.txt`
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

Define any number of sections separated by blank lines. Each section header must be on its own line, followed by values prefixed with `- `. The four base sections are `Age`, `Gender`, `Skill`, and `Weakness`, but any additional sections will be picked up automatically.

```
Age
- 18
- 25
- 34
- 45

Gender
- Male
- Female
- Non-binary

Skill
- Fast runner
- Medical knowledge
- Survival expert
- Military training

Weakness
- Claustrophobic
- Fear of darkness
- Low stamina
- Trust issues

Personality
- Optimistic
- Stubborn
- Loyal
- Impulsive
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
Age : 34
Gender : Female
Skill : Medical knowledge
Weakness : Claustrophobic
Personality : Loyal
```

## Classes

### `Playercard` (`bunkerLogic.py`)

Data container for a single player's attributes.

| Member | Description |
|---|---|
| `index` | Player number, increments automatically |
| `parameters` | Dictionary of all attributes, built dynamically from `Parameters.txt` |
| `writePars()` | Prints all attributes to the console |

### `PlayerCardGenerator` (`bunkerLogic.py`)

Parses `Parameters.txt` and generates player cards.

| Member | Description |
|---|---|
| `parametersPath` | Path to the located `Parameters.txt` file |
| `players` | List of all generated `Playercard` instances |
| `parameters` | List of feature names parsed from `Parameters.txt` |
| `clusters` | Internal line-index map used to locate attribute values in the file |
| `generateRandomPlayer()` | Randomly samples one value per feature and appends a new `Playercard` to `players` |

## Architecture

The project follows the **MVP (Model-View-Presenter)** pattern:

- **Model** — `Playercard` holds the data
- **Presenter** — `PlayerCardGenerator` handles the logic
- **View** — `main.py` manages user interaction via the CLI

This separation keeps the core logic reusable and independent of the interface — swapping the CLI for a GUI or web frontend would only require changes to `main.py`.