# AddBiomechanics CLI

This branch provides a **local-only** CLI workflow for AddBiomechanics utilities.
Cloud account features are intentionally disabled here.

## Install

From the repository root:

```bash
pip install ./cli
```

To install in editable mode while developing:

```bash
pip install -e ./cli
```

## Basic usage

Show the available commands:

```bash
addb --help
```

## Local-only behavior

The local CLI does **not** include:
- AWS/Cognito login
- deployment selection (`-d`)
- cached credentials (`~/.addb_login.json`)
- cloud commands like upload/download/list/analytics

It only exposes local file-processing commands, including:

- `post-process`
- `export-csv`
- `stats`
- `plot`
- `compare`
- `view`
- `view-energy`
- `transfer-markerset`
- `transfer-reviews`
- `create-b3d`
- `clean-up`
- `describe-dataset`

Run `addb --help` to see the available local commands and per-command options.
