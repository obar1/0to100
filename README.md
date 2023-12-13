# readme

| SQ                                                                                                                                                    | CI                                                                            | CodeSpace                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| [![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=obar1_0to100)](https://sonarcloud.io/summary/new_code?id=obar1_0to100) | ![](https://github.com/obar1/0to100/actions/workflows/makefile.yml/badge.svg) | [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/obar1/0to100?quickstart=1) |

## oto100

0 to 100 ... learn anything from webresources (and not)

### 1st time usage:

```bash
# env
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# copy sample yaml conf
cp ./zero_to_one_hundred/tests/resources/map.yaml .
cat map.yaml
```

![](ab67dd2b-7c12-4cdf-a7a5-f773c2b67919.png)

```bash
# tip:  add it to .bash_rc etc or some shell script
export MAP_YAML_PATH=$(pwd)/map.yaml
python ./main.py help

```

![](50a86373-910b-4a12-85ef-251b6d4f08f0.png)

### daily usage:

- create new section

```bash
export MAP_YAML_PATH='map.yaml'

url=https://cloud.google.com/docs
python ./main.py create_section $url

url=https://cloud.google.com/help
python ./main.py create_section $url
#...etc
```

![](9b873c30-eccb-4c17-9d36-1c302060f5c3.png)

## oto100 safari books :construction:

0 to 100 ... learn anything from safari books https://learning.oreilly.com/member/login/

### 0th time usage:

https://github.com/lorenzodifuccia/safaribooks

> just a sample
> ![](a1aef2bb-ce75-4288-8051-512ca8865522.png)

### 1st time usage:

```bash
# env
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# copy sample yaml conf
cp ./zero_to_one_hundred/tests_sb/resources/map.yaml .
cat map.yaml

```

![](a4b09e11-9f1f-4098-a4e2-77d6df85226a.png)

```bash
vim map.yaml
# add your membership details :)

export MAP_YAML_PATH='map.yaml' && python ./main_sb.py help

# tip:  add it to .bash_rc etc or some shell script
```

![](63fd79b5-ad41-45fd-a2dc-367f317bcc0c.png)

### daily usage:

- create new meta book

```bash
export MAP_YAML_PATH='map.yaml'

url=https://learning.oreilly.com/library/view/hunt-the-pragmatic-programmer/020161622X/
python ./main_sb.py create_meta_book $url


```

> add your membership details :) and it will work

![](c81254c5-058e-419a-b9c3-e967be2e5302.png)

> ex with mine :)

![](f5ac382b-dafe-4ba7-ba82-a3cabc01553e.png)

and you have a `toc.md` for free to use as index

![](d05502bb-4b90-422f-9624-568d9f02cd08.png)
