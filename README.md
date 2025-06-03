# Survey Analysis

As a data scientist you are required to analyse the political landscape of Europe using
the **Chapel Hill Expert Survery** dataset. The dataset provides insights into the
positioning of **277 political parties** in Europe based on **55 different
attributes**. The dataset can be downloaded
[here](https://www.chesdata.eu/2019-chapel-hill-expert-survey) and the
[codebook](https://static1.squarespace.com/static/5975c9bfdb29d6a05c65209b/t/5fa04ec05d3c8218b7c91450/1604341440585/2019_CHES_codebook.pdf)
provides further information on the survey attributes.

This repository contains the necessary setup and codebase to help guide you in
performing an analysis using different statistical methods.

## Pre-requisites

Please make sure you have the following software installed:

- Python (3.9 - 3.13)
- [Poetry](https://python-poetry.org/docs/)


## Install project and dependencies

Poetry is used for Python dependency management. To install the necessary Python
dependencies run the following command:

```bash
poetry install
```

Alternatively, the `make` command defined in the Makefile can also be used:

```bash
make install
```

## Development

Installing this project with Poetry will install the development dependencies by default.

### Running the tests

The unit tests can be run either by using the `make` command (given in the Makefile) or
by running `pytest` directly:

```bash
make test
```

or

```bash
poetry run pytest tests
```

### Installing pre-commit hooks

This project uses [pre-commit](https://pre-commit.com) to manage a collection of
pre-commit hooks that help maintain source code quality. If you are going to make
contributions to this codebase, please ensure you have install the pre-commit hooks
before committing any code, by running the following:

```bash
poetry run pre-commit install
```

To modify or update hooks, see the file `.pre-commit-config.yaml`.


## Gearing Up for the Pairing Session

Please be sure to complete the below tasks before the pairing session:

1. Get a high-level understanding of the dataset by looking into the [codebook](https://static1.squarespace.com/static/5975c9bfdb29d6a05c65209b/t/5fa04ec05d3c8218b7c91450/1604341440585/2019_CHES_codebook.pdf) and if necessary, downloading and inspecting the dataset.
2. Have your preferred text editor or IDE setup and ready to go.
3. Have your coding environment ready by installing Python and Poetry.
4. Ensure that you are able to run all commands mentioned in this README (note that a failing test from pytest is expected).


**Please note that you DO NOT have to complete the code/tasks inside the `src/`
folder. These are intended to be completed collaboratively during the pairing session.**
