# Survey Analysis

As a data scientist you are required to analyse the political landscape of Europe using the **Chapel Hill Expert Survery** dataset. The dataset provides insights into the positioning of **277 political parties** in Europe based on **55 different attributes**. The dataset can be downloaded [here](https://www.chesdata.eu/2019-chapel-hill-expert-survey) and the [codebook](https://static1.squarespace.com/static/5975c9bfdb29d6a05c65209b/t/5fa04ec05d3c8218b7c91450/1604341440585/2019_CHES_codebook.pdf) provides further information on the survey attributes.

This repository contains the necessary setup and codebase to help guide you in performing an analysis using different statistical methods.

## Project Setup

### Pre-requisites

Please make sure you have the following software installed:

- Python (3.9 - 3.12)
- [Poetry](https://python-poetry.org/docs/)

### Install all Python dependencies

Poetry is used for Python dependency management. To install the necessary Python dependencies run the following command:

```bash
poetry install
```

Alternatively, the `make` command defined in the Makefile can also be used:

```bash
make install
```

Similarly to add and install new Python packages to your Poetry virtual environment, use:

```bash
poetry add <python-package-name>
```

### Run tests & checks

The unit tests, linting checks, and type checks can be run either by using the `make` commands (given in the Makefile) or by using the corresponding commands for the respective packages. For example, unit tests can be executed using:

```bash
make test
```

or

```bash
poetry run pytest tests
```

For running linting checks using flake8, use:

```bash
poetry run flake8 src tests
```

or

```bash
make lint-check
```

## Gearing Up for the Pairing Session

Please be sure to complete the below tasks before the pairing session:

1. Get a high-level understanding of the dataset by looking into the [codebook](https://static1.squarespace.com/static/5975c9bfdb29d6a05c65209b/t/5fa04ec05d3c8218b7c91450/1604341440585/2019_CHES_codebook.pdf) and if necessary, downloading and inspecting the dataset.
2. Have your preferred text editor or IDE setup and ready to go.
3. Have your coding environment ready by installing Python and Poetry.
4. Ensure that you are able to run all commands mentioned in this README (note that a failing test from pytest is expected).

**Please note that you DO NOT have to complete the code/tasks inside the `src/` folder. These are intended to be completed collaboratively during the pairing session.**
