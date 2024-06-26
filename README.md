# Learn-API-DataSources-Python

## Description

Python implementation to do CRUD operations on data sources

## Requirements

- Python 3 - On Mac: ```brew install python```
- virtualenv - On Mac: ```brew install virtualenv```
- [direnv](https://direnv.net/docs/installation.html) - On Mac ```brew install direnv```

### Intial Setup / Installation

Please install all the above requierements based on your distro.

### Python Virtual Environment

If you configured the direnv correctly, once you get into the cloned repository you can able see a warning to perform ```direnv allow```, please ignore it and go ahead with the python virtualenv setup.

To create an virtual environment.

```sh
virtualenv .env --python=python3
```

**Note:** Do not change the name of the virtual environment because it is configured by default with the name ```.env``` in direnv's ```.envrc``` file.

Now perform ```direnv allow```, This will activate the virtual environment and will continue to do it whenever you enters this repository.

#### Installing dependencies with pip

```sh
pip install -r requirements.txt
```

