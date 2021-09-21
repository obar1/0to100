# 0to100

> 0 to 100 to learn anything


## Usage

### using the py scripts

#### 1-time (manual) setup

check latest tag val latest at https://github.com/obar1/0to100/tags

```bash
bash setup.sh tag target_dir
```
> check contents `runme.sh`

#### daily usage

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

### using the bash bash scripts

*OBSOLETE.....................*

* init the scripts in cmd line

```bash
(py37) √ 0to100.git % source ./_tools/runme.sh

```

* **use it to learn**

> we want to 1 level hierarchy and avoid the deep levels of the pages

- go to the https://cloud.google.com/

- get a section/link

```
ex
https://cloud.google.com/docs
```

- create local folder and some placeholder for the section/link automatically using the tools scripts

```bash
(py38) √ 0to100.git % do_section https://cloud.google.com/docs
https://cloud.google.com/docs
https:§§cloud.google.com§docs
https://cloud.google.com/docs
https:§§cloud.google.com§docs
# map
## wip
> flatview

1. <https://cloud.google.com/docs> :ok: [`here`](../https:§§cloud.google.com§api-gateway§docs/readme.md)1. <https://cloud.google.com/docs> :o: [`here`](../https:§§cloud.google.com§docs/readme.md)
1. <https://cloud.google.com/docs> :o: [`here`](../https:§§cloud.google.com§docs/readme.md)
https://cloud.google.com/docs
https:§§cloud.google.com§docs
copy pdf...
```
- go to the page https://cloud.google.com/docs and export as pdf in the folder created automatically

- hit a key

- the pdf is renamed and txt exported and vscode is called

![](1083eacc-b42e-489c-bed4-9e16cf3d64c5.png)

- `map.md` has automatically the section links to the local files and original link added

![](2bcf4234-8a4e-4263-be9d-e65210ef696e.png)

1. goto back ;) ... and expand your knowledge :*


## Useful tools

* install xpdf
```
brew install xpdf
```

* install vscode
```
brew install --cask visual-studio-code
```

* chrome extension to save pages in pdf
save the page with https://chrome.google.com/webstore/detail/print-friendly-pdf/ohlencieiipommannpdfcmfdpjjmeolj/related or https://chrome.google.com/webstore/detail/htmlurl-to-pdf-with-pdfma/dlmgniacaacmbccdegkadebbaphkonpb


## Development

### Installation

* Install Poetry: <https://python-poetry.org/docs/#installation>
* Install python env: `pyenv install 3.7.0`
* Install virtual env: `pyenv virtualenv 3.7.0 pip_mse_ingestion`
* Activate virtual env: `pyenv activate pip_mse_ingestion`
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
### local troubleshooting...

add to `setup.sh` something like
```
# DEBUG
cp -r $HOME/git/obar1/0to100.git/ "${DIR_TARGET_LATEST}" || true
```
so you can test local fix :)
