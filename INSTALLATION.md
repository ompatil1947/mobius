# Installation

## Requirements

- Python 3.11 or newer
- a virtual environment is recommended

## Setup

Create an environment and install Mobius:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Build and test

```bash
mobius build
pytest
```

## Development commands

- `scripts/build.sh` builds the site
- `scripts/clean.sh` removes generated output
- `scripts/dev.sh` serves the site with live rebuilding
