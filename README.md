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
![](a0892483-ce6f-4ab1-bbd3-99f5ad7e7e8b.png)

- help

```bash
bash runme.sh help
```


## As developer:

### Installation:

check Makefile [here](./Makefile) to gets started
