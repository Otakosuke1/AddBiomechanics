# AddBiomechanics CLI (Local-only)

This directory contains a local-only Python command line interface for AddBiomechanics.

Cloud-backed features such as AWS access, remote uploads/downloads, and account authentication are not supported on this branch.

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

## Local commands

This branch is focused on commands that operate on local files.

Examples:

```bash
addb post-process <source_data_folder> <destination_data_folder>
addb export-csv <source_bin_file> <destination_csv_file>
addb stats <path>
addb plot <path>
addb compare <file_a> <file_b>
```

Common local-only utilities include:

- `post-process`
- `export-csv`
- `stats`
- `plot`
- `compare`
- `debug`
- `view`
- `view-energy`
- `transfer-markerset`
- `describe-dataset`
- `transfer-reviews`
- `create-b3d`
- `clean-up`

## Removed cloud features

The following cloud-oriented capabilities are intentionally disabled or removed from this local-only branch:

- login/authentication
- AWS/Cognito/S3 access
- remote dataset listing
- remote uploads
- remote downloads
- remote analytics
- remote credit generation

If you need remote AddBiomechanics service integration, use an upstream cloud-enabled branch instead.
