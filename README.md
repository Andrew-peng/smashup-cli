# Smash Up CLI

Smash Up CLI is a terminal utility for building Smash Up decks. It lets you
select expansions in a TUI and randomly assign factions to each player.

## Features

- TUI configuration to enable or disable expansions.
- Randomized faction assignment per player.
- Config stored at `~/.smashup/factions.toml`.

## Installation

```bash
pip install smashup-cli
```

## Usage

Configure which expansions are available:

```bash
smashup configure
```

Randomize factions for a game:

```bash
smashup randomize
```

## Development

```bash
pip install -e .
```

## License

MIT
