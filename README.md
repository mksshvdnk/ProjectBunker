# Player Card Generator

A lightweight Python utility that randomly generates player cards by sampling attributes from a structured text file (`Parameters.txt`).

## Requirements

- Python 3.10+ (uses structural pattern matching via `match`/`case`)
- A `Parameters.txt` file somewhere in the working directory tree (see format below)

No third-party dependencies — only the standard library (`pathlib`, `random`).

## Parameters.txt Format

The file must define four sections, each headed by an exact label on its own line, followed by one value per line, and separated from the next section by a blank line:

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

The section headers must be exactly: `Age`, `Gender`, `Skill`, `Weakness` (case-sensitive). The sections can appear in any order.

## Usage

```python
from player_card_generator import PlayerCardGenerator

generator = PlayerCardGenerator()

# Generate a single random player
generator.generateRandomPlayer()

# Generate multiple players
for _ in range(5):
    generator.generateRandomPlayer()

# Access the generated player cards
for player in generator.players:
    print(player.age, player.gender, player.skill, player.weakness)

# Print a player's stats to the console
generator.players[0].writePars()
```

## Classes

### `PlayerCardGenerator`

Parses `Parameters.txt` on construction and manages a collection of generated player cards.

| Member | Description |
|---|---|
| `parametersPath` | `Path` to the located `Parameters.txt` file |
| `players` | List of generated `Playercard` instances |
| `clusters` | 8-element list storing start/end line indices for each feature |
| `generateRandomPlayer()` | Randomly selects one value per feature and appends a new `Playercard` to `players` |

### `Playercard`

A simple data container for a single player's attributes.

| Attribute | Description |
|---|---|
| `age` | Randomly selected age category |
| `gender` | Randomly selected gender |
| `skill` | Randomly selected skill |
| `weakness` | Randomly selected weakness |

| Method | Description |
|---|---|
| `writePars()` | Prints all four attributes to the console |