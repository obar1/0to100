# 0to100

> 0 to 100 ... learn anything from webresources (and not)

## As user:

### 1st time usage: (manual) setup

- create a new folder and get

```bash
wget -q https://raw.githubusercontent.com/obar1/0to100/main/setup.sh
```

- check latest tag values at https://github.com/obar1/0to100/tags

or if you have [lynx](https://simple.wikipedia.org/wiki/Lynx_(web_browser)) or similar installed

```bash
lynx -dump https://github.com/obar1/0to100/tags | grep tags | uniq | sort
```

- install :bowtie: the tag

```bash
bash setup.sh [tag] [target_dir]
```
> [target_dir] can be set to `.` to use the current folder

- install req
> add/set env if you wish

```bash
pip install -r "0to100-latest/requirements.txt"
```

- check runme.sh

```bash
bash runme.sh help
```

- optional get

```bash
wget -q https://raw.githubusercontent.com/obar1/0to100/main/test_setup/.gitignore
```

### daily usage:

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


## As developer:

### Installation:

* Install python env: <https://github.com/pyenv/pyenv#getting-pyenv>
* Install Poetry: <https://python-poetry.org/docs/#installation>

### Export to pip req

so you can just use pip  to run the thing ...

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```
