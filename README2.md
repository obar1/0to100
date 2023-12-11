# safaribooks 0 to 100


[![Makefile CI](https://github.com/obar1/safaribooks-0to100/actions/workflows/makefile.yml/badge.svg)](https://github.com/obar1/safaribooks-0to100/actions/workflows/makefile.yml)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/obar1/safaribooks-0to100?quickstart=1)  

> safaribooks_zero_to_one_hundred 0 to 100 ... learn anything from [here](https://learning.oreilly.com/)

There are many tools available to download ebooks from your Safari Books membership; this cli enhances the experience by enabling you to create a simple toc offline of them and watch their progress.

- one cli where a few cmmands, such as crate meta book, can be run (download the ebook and save in a folder and add entry in the toc)
- toc to provide isbn, image from the actual cover, links to the epub and pdf versions, and some json where you can put whatever you want, in addition to number of tot ebooks and the most recent version date

![](0c924b28-4bca-4c60-8ccf-a0a4b76f3d97.png)

## As user:

### 1st time usage: (manual) setup

- create a new folder and get

```bash
wget -q https://raw.githubusercontent.com/obar1/safaribooks-0to100/master/setup.sh
```

- check latest tag values at https://github.com/obar1/safaribooks_zero_to_one_hundred/tags

or if you have [lynx](https://simple.wikipedia.org/wiki/Lynx_(web_browser)) or similar installed

```bash
lynx -dump https://github.com/obar1/safaribooks-0to100/tags | grep tags | uniq | sort | grep tar
```

- install :bowtie: the tag
```bash
bash setup.sh [tag]
```
> it uses the current folder

- install https://github.com/lorenzodifuccia/safaribooks and `*` it :)
> it dumps the books from the website ...

- install req
> add/set env if you wish

```bash
pip install -r safaribooks_zero_to_one_hundred-latest/requirements.txt

pip install -r safaribooks/requirements.txt
```

- check map.yaml contents

- run runme.sh

```bash
bash runme.sh
```

#### ex of working setup

> you need to setup the path and your credentials

```
mkdir /tmp/safaribooks_zero_to_one_hundred
cd /tmp/safaribooks_zero_to_one_hundred
# do setup

ls
```
![](3bddd16e-0765-46fc-ab01-e559c786c02f.png)

- edit oreilly_username and oreilly_userpassword with yours :)

- download a book
```bash
obar1➜  safaribooks_zero_to_one_hundred  ᐅ  bash runme.sh  create_meta_book 'https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/'
```
![](356cf6d5-53af-44bb-a095-472410e3061e.png)



### daily usage:

-  create new meta_book

```bash
url=https://learning.oreilly.com/library/view/hunt-the-pragmatic-programmer/020161622X/
bash runme.sh create_meta_book $url
```

- check the updated toc.md in a browser and bookmark it :)

```bash
# mac
open -a "Brave Browser" toc.md

# wsl ubuntu https://ubuntu.com/wsl
brave-browser toc.md
```

- opt but suggested
any md extension to see it nicer

https://chrome.google.com/webstore/detail/md-reader/medapdbncneneejhbgcjceippjlfkmkg/related


- help

```bash
bash runme.sh help
```

## As developer:

### Installation:

* Install python env: <https://github.com/pyenv/pyenv#getting-pyenv>
* Install req `requirements-dev.txt`

### Quick intergration :bowtie: test

use [runme](./zero_to_one_hundred/runme.sh) and set a copy of [map](./zero_to_one_hundred/tests/resources/map.yaml) with your account details

```bash
cd zero_to_one_hundred
touch map.yaml
bash runme.sh help
```


### Continuous pytest

```bash
export PYTHONPATH=. && ptw -c  -- --capture=tee-sys -o log_cli=true
```

## Example: my toc

![](./obar1_toc_md.png)
