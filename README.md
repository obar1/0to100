# readme

| SQ | CI |                                                                                                         
| -- | -- | 
| [![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=obar1_0to100)](https://sonarcloud.io/summary/new_code?id=obar1_0to100) | [![Makefile CI](https://github.com/obar1/0to100/actions/workflows/makefile.yml/badge.svg)](https://github.com/obar1/0to100/actions/workflows/makefile.yml) | 

## oto100

0 to 100 ... learn anything from webresources (and not)

We read training material from the web and learn from it by doing, but how do we keep that a bit organized? I came up with an idea: this small tool.
Given a 'url', it creates the entry in a markdown map and a folder and links them; in this way, you can easily jump between different sections inside your preferred ide. As you expand the map with new contents, you build some reference material, keep it local all the time, and searchable all the time on your daily coding.

current commands:
help:
['create_section', 'done_section', 'refresh_map', 'refresh_links', 'help']

> tip
in `create_section` you can override the default toc title adding another `#` hint below the one header created automatically in the section folder
ex
```markdown
# <https§§§www.cloudskillsboost.google§catalog>
> <https://www.cloudskillsboost.google/catalog>

# catalog
```

### 1st time usage:

```bash
# env
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# copy sample yaml conf
cp ./zero_to_one_hundred/tests/resources/map.yaml .
cat map.yaml
export MAP_YAML_PATH=$(pwd)/map.yaml
# tip:  add it to .bash_rc etc or some shell script

```

![](ab67dd2b-7c12-4cdf-a7a5-f773c2b67919.png)

```bash
chmod +x *.py
./main.py help
```

![](50a86373-910b-4a12-85ef-251b6d4f08f0.png)

### daily usage:

- create new section

```bash
url=https://cloud.google.com/docs
./main.py create_section $url

url=https://cloud.google.com/help
./main.py create_section $url
#...etc
```

![](9b873c30-eccb-4c17-9d36-1c302060f5c3.png)

## oto100 safari books :construction:

0 to 100 ... learn anything from safari books https://learning.oreilly.com/member/login/

some as above but it can uses dome external lib to grab file from oreilly

current commands:

help:
['create_meta_book', 'refresh_toc', 'help']

### 0th time usage:

> use what you prefer to  grab epub/pdf from oreilly 
check this 
https://github.com/lorenzodifuccia/safaribooks 
or just save as pdf section  by section with this 
https://chromewebstore.google.com/detail/reader-view/ecabifbgmdmgdllomnfinbmaellmclnh


### 1st time usage:

```bash
# env
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# copy sample yaml conf
cp ./zero_to_one_hundred/tests_sb/resources/map.yaml .
cat map.yaml
export MAP_YAML_PATH=$(pwd)/map.yaml
# tip:  add it to .bash_rc etc or some shell script
```

![](a4b09e11-9f1f-4098-a4e2-77d6df85226a.png)

```bash
vim map.yaml
# add your membership details :)
```

```bash
chmod +x *.py
./main_sb.py help
```

![](63fd79b5-ad41-45fd-a2dc-367f317bcc0c.png)

### daily usage:

- create new meta book

```bash
url=https://learning.oreilly.com/library/view/hunt-the-pragmatic-programmer/020161622X/
./main_sb.py create_meta_book $url
```

> add your membership details :) and it will work

![](c81254c5-058e-419a-b9c3-e967be2e5302.png)

> ex with mine :)

![](f5ac382b-dafe-4ba7-ba82-a3cabc01553e.png)

and you have a `toc.md` for free to use as index

![](d05502bb-4b90-422f-9624-568d9f02cd08.png)

## quick demo

> in you want to check this quickly ...

just open this repo in your GitHub Codespace
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/obar1/0to100?quickstart=1)
and run the 

```bash
demo.sh
```