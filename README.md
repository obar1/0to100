# 0to100
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fobar1%2F0to100.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fobar1%2F0to100?ref=badge_shield)


> 0 to 100 to learn anything


## 1st time (manual) setup

check latest tag val latest at https://github.com/obar1/0to100/tags

or https://raw.githubusercontent.com/obar1/0to100/main/changelog.md like so

```bash
curl https://raw.githubusercontent.com/obar1/0to100/main/changelog.md | grep version | sort -r | head -1
```

in a any tmp folder get the `setup.sh` like so

```bash
wget -q https://raw.githubusercontent.com/obar1/0to100/main/setup.sh
```

and use it like so

```bash
# TODO: set vars
bash setup.sh $tag $target_dir
ex
bash setup.sh 1.5  .
```
> check contents `runme.sh`

ignore it so you can check in only the section in the new repo

```bash
touch .gitignore
```

add to it
```
0to100-latest/
```

## daily usage

-  create new section

```bash
url=https://cloud.google.com/docs
bash runme.sh create_section $url
url=https://cloud.google.com/help
bash runme.sh create_section $url
#...etc
```
-  refresh sections

```bash
bash runme.sh refresh_map
```
-  refresh links

```bash
bash runme.sh refresh_links
```
-  refresh puml

```bash
bash runme.sh refresh_puml
```
![](2021-09-18-01-08-45.png)

- help

```bash
bash runme.sh help
```


## Development

### Installation

* Install Poetry: <https://python-poetry.org/docs/#installation>
* Install python env: `pyenv install 3.7.0`
* Install virtual env: `pyenv virtualenv 3.7.0 pip_mse_ingestion`
* Activate virtual env: `pyenv activate py37`
* Install package and dependencies: `poetry install`
* Install pre-commit hooks: `poetry run pre-commit install`

### Run pre-commit hooks manually

All pre-commit hooks will be run automatically when pushing changes.
They can also be run on staged files or on all files manually:

```bash
# Run all hooks against currently staged files,
# this is what pre-commit runs by default when committing:
pre-commit run

# Run all the hooks against all the files:
pre-commit run --all-files

# Run a specific hook against all staged files:
pre-commit run black
pre-commit run flake8
pre-commit run isort
pre-commit run pylint
```


