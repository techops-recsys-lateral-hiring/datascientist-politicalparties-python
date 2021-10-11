# Survey Analysis

As a data scientist you are required to analyse the political landscape of Europe using the **Chapel Hill Expert Survery** dataset. The dataset provides insights into the positioning of **277 political parties** in Europe based on **55 different attributes**. The dataset can be downloaded [here](https://www.chesdata.eu/2019-chapel-hill-expert-survey) and the [codebook](https://static1.squarespace.com/static/5975c9bfdb29d6a05c65209b/t/5fa04ec05d3c8218b7c91450/1604341440585/2019_CHES_codebook.pdf) provides further information on the survey attributes.

This repository contains the necessary setup and code base to help guide you in performing an analysis using different statistical methods.

# Project Setup

## Pre-requisites

Please make sure you have the following software installed

- [Poetry](https://python-poetry.org/docs/)
- Python (3.7 or 3.8)

## Install all python dependencies

Poetry is used for python dependency management. To install the necessary python dependencies run the following command.

```bash
poetry install
```

Alternatively, the make command defined in the makefile can also be used.

```bash
make install
```

Similarly to add/install new python packages to your poetry virtual environment, use

```bash
poetry add <python-package-name>
```

## Run tests & checks

The unit tests, linting checks and type checks can be run either by using the make commands (given in the makefile) or by using the commands from the respective packages.
For example, unit tests can be executed using,

```bash
make test
```

or

```bash
poetry run pytest tests
```

For running linting checks using flake8, use

```bash
poetry run flake8 src tests
```

or

```bash
make lint-check
```

# Gearing Up for the Pairing Session

Please be sure to complete the below tasks before the pairing session.

1. Get a high-level understanding of the dataset by looking into the [codebook](https://static1.squarespace.com/static/5975c9bfdb29d6a05c65209b/t/5fa04ec05d3c8218b7c91450/1604341440585/2019_CHES_codebook.pdf) and if necessary downloading the dataset.
2. Have your coding environment ready by installing python and poetry.
3. Ensure that you are able to run all commands mentioned in this README (except for pytest errors)

**Please note that you DO NOT have to complete the code/tasks inside the `src/` folder. It is meant to be done together during pairing session.**
