# AddBiomechanics CLI

This directory contains the Python command line interface for AddBiomechanics.

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

Use the development deployment (default):

```bash
addb -d dev ls
```

Use the production deployment:

```bash
addb -d prod ls
```

## Authentication

Most remote commands authenticate against AddBiomechanics and will prompt for your username and password if they are not provided on the command line.

Examples:

```bash
addb -u you@example.com -p 'your-password' ls
addb -u you@example.com upload ./my_dataset
```

Credentials are cached in `~/.addb_login.json` for reuse by later commands.

## Common commands

### Upload a dataset

```bash
addb upload ./path/to/dataset
```

Skip the confirmation prompt:

```bash
addb upload ./path/to/dataset --yes
```

Upload to the private workspace:

```bash
addb upload ./path/to/dataset --private
```

### Download processed data

Download subjects matching a regex:

```bash
addb download --pattern 'standardized/rajagopal_no_arms/.*'
```

Only include reviewed subjects:

```bash
addb download --pattern 'standardized/rajagopal_no_arms/.*' --reviewed-only
```

### Download files directly

```bash
addb download-files --prefix standardized/rajagopal_no_arms --pattern '.*_dynamics_trials_only\.b3d'
```

### Generate dataset credits

```bash
addb generate-credits --prefix standardized/
```

## Local-only utilities

Some commands operate on local files and do not require remote authentication, including utilities such as:

- `post-process`
- `export-csv`
- `stats`
- `plot`
- `compare`

Run `addb --help` to see the full command list and per-command options.
