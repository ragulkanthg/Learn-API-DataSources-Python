# Learn-API-DataSources-Python

## Description

Python implementation to perform CRUD operations on data sources

## Requirements

- Python 3 - On Mac: ```brew install python```
- virtualenv - On Mac: ```brew install virtualenv```
- [direnv](https://direnv.net/docs/installation.html) - On Mac ```brew install direnv```

### Intial Setup / Installation

Please install all the above requierements based on your distribution/OS.

### Python Virtual Environment

If you have configured the direnv correctly, upon entering the cloned repository, you will see a warning to perform ```direnv allow```. please ignore this warning initially and proceed with the Python virtualenv setup.

To create an virtual environment, run:

```sh
virtualenv .env --python=python3
```

**Note:** Do not change the name of the virtual environment, as it is configured by default with the name ```.env``` in direnv's ```.envrc``` file.

Now run ```direnv allow```, This will activate the virtual environment and continue to do so whenever you enter this repository.

#### Installing dependencies with pip

```sh
pip install -r requirements.txt
```

