# Bunker — Player Card Generator

A command-line Python tool that procedurally generates randomized player cards from a customizable parameter file, with optional AI-powered content generation via a local language model.

## Changelog

### v4.0
- Added AI-powered game generation — generates a full `Parameters.txt` with realistic survival attributes using a local LLM
- Added AI parameter generation — add a new attribute category to the game at any time using AI
- Added `setup.py` to automate dependency installation and optional AI model download
- Ollama server starts automatically in the background when an AI feature is first used
- Added `generateManyPlayers` command for batch player generation
- Added `deletePlayer`, `deleteAllPlayers`, and `deleteParameter` commands

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
- AI-powered content generation using a local LLM (no cloud API, no credits)
- Reads attribute pools from a plain-text `Parameters.txt` — no code changes needed to customize
- Interactive CLI shell with a self-documenting command system
- Clean separation between logic (`bunkerLogic.py`) and interface (`main.py`)

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) (optional, for AI features)

## Setup

Run the setup script — it installs dependencies and optionally downloads the AI model:

```bash
py setup.py
```

Then start the program:

```bash
py main.py start
```

## Parameters.txt Format

Define any number of sections separated by a blank line. Each section header is a plain text label on its own line, followed by one value per line:

```
Age
18
25
34
45
60

Gender
Male
Female
Non-binary

Skill
First Aid
Navigation
Survival
Engineering

Weakness
Claustrophobic
Fear of darkness
Low stamina
Trust issues

Background
Former soldier
Ex-doctor
Engineer
Farmer
```

The four base sections (`Age`, `Gender`, `Skill`, `Weakness`) are required. Additional sections are picked up automatically.

## Commands

| Command | Description |
|---|---|
| `generatePlayer` | Generates and prints a random player card |
| `generateManyPlayers` | Generates multiple random player cards |
| `generateNewAIGame` | Uses AI to generate a full new `Parameters.txt` |
| `addAIParameter` | Uses AI to add a new attribute section to `Parameters.txt` |
| `deletePlayer` | Deletes a player by index |
| `deleteAllPlayers` | Deletes all generated players |
| `deleteParameter` | Deletes a non-base parameter from `Parameters.txt` |
| `help` | Lists all available commands |
| `quit` | Exits the shell |

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
| `basicParameters` | The four protected base parameters |
| `parameters` | Full list of all parameters including custom ones |
| `clusters` | Internal line-index map used to locate attribute values in the file |
| `players` | List of all generated `Playercard` instances |
| `parsePars()` | Parses `Parameters.txt` and rebuilds `parameters` and `clusters` |
| `generateRandomPlayer()` | Randomly samples one value per feature and appends a new `Playercard` |
| `generateNewAIGame()` | Uses a local LLM to generate a full new `Parameters.txt` |
| `addAIParameter(name)` | Uses a local LLM to add a new parameter section to `Parameters.txt` |
| `deletePlayer(index)` | Removes a player by index |
| `deleteAllPlayers()` | Clears all players |
| `deleteParameter(parameter)` | Removes a non-base parameter from the file and rebuilds state |

## Architecture

The project follows the **MVP (Model-View-Presenter)** pattern:

- **Model** — `Playercard` holds the data
- **Presenter** — `PlayerCardGenerator` handles the logic
- **View** — `main.py` manages user interaction via the CLI

This separation keeps the core logic reusable and independent of the interface — swapping the CLI for a GUI or web frontend would only require changes to `main.py`.