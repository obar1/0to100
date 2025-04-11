# readme

| SQ | CI |                                                                                                         
| -- | -- | 
| [![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=obar1_0to100)](https://sonarcloud.io/summary/new_code?id=obar1_0to100) | [![Makefile CI](https://github.com/obar1/0to100/actions/workflows/makefile.yml/badge.svg)](https://github.com/obar1/0to100/actions/workflows/makefile.yml) | 

We read training material from the web and learn from it by doing, but how do we keep that a bit organized? I came up with an idea: this small tool.
Given a 'url', it creates the entry in a markdown map and a folder and links them; in this way, you can easily jump between different sections inside your preferred ide. As you expand the map with new contents, you build some reference material, keep it local all the time, and searchable all the time on your daily coding and use it to fee your local `llm` :).

## quick demo

> in you want to check this quickly ...

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/obar1/0to100?quickstart=1)

just open this repo in your GitHub Codespace and run the demo as:

```bash
bash demo.sh zo
``` 

![](2dc4491c-fa27-4c5e-bd0c-71951b3ef0e5.png)
[here](./toc_zo.md)

```bash
bash demo.sh sb
```

![](z05502bb-4b90-422f-9624-568d9f02cd01.png)
[here](./toc_sb.md)


## oto100

0 to 100 ... learn anything from the web 

commands:

```
create_section = create a new section
section=https://www.cloudskillsboost.google/paths/16
./main.py zo create_section "$section"

done_section = tag a section as done
section=https://www.cloudskillsboost.google/paths/16
./main.py zo done_section "$section"

refresh_map = refresh the section map
./main.py zo refresh_map

refresh_section_contents = refresh links to sections in the readme.md(s) and delete orphaned image(s)
./main.py zo refresh_section_contents
```


in `create_section` you can override the default toc title adding another `#` hint below the one header created automatically in the section folder
ex
```markdown
# <https§§§www.cloudskillsboost.google§catalog>
> <https://www.cloudskillsboost.google/catalog>

# catalog
```

in `refresh_section_contents` you can expand links from other sections automatically 
ex
```markdown
# <https§§§www.cloudskillsboost.google§catalog>
> <https://www.cloudskillsboost.google/catalog>

https://www.cloudskillsboost.google/doc
```
expand the last link to point to the section for the doc - handy as anchor technique 

and it will delete img in the folder that have no reference in md readme anymore

```mermaid
graph TD
    
direction TB
A["Take Screenshot"] --> B["Add Context Text"]
B --> C{"Complete?"}
C -->|"No"| D["Continue Video"]
D --> A
C -->|"Yes"| E["End Documentation"]

direction TB
E["Review Content"] --> F{"Needs Update?"}
F -->|"Yes"| G["Update Image/Text"]
G --> H["Replace with Snippet"]
H --> I["Final Review"]
F -->|"No"| Complete([Complete])
I --> Complete
   
```

### setup and usage:

```bash
# env

make setup
source venv/bin/activate
pre-commit install # optional

# each time new code is ready for PRs :P
make refactor

# copy sample yaml conf
cp ./zero_to_one_hundred/tests/resources/map.yaml .
cat map.yaml
export MAP_YAML_PATH=map.yaml
# tip:  add it to .bash_rc etc or some shell script

chmod +x *.py
# run main
./main.py zo help
```

## oto100 safari books :construction:

0 to 100 ... learn anything from safari books https://learning.oreilly.com/member/login/

same as above but it can use some external lib to grab epub from oreilly

current commands:

```
snatch_book = snatch a book from safari
./main.py sb snatch_book https://learning.oreilly.com/library/view/rewire-your-brain/9781119895947

refresh_toc = refresh the toc with al the books info
./main.py sb refresh_toc
```

### setup and usage:

> use what you prefer to  grab epub/pdf from O'Reilly 
check this 
https://github.com/lorenzodifuccia/safaribooks 
or just save as pdf section  by section with this 
https://chromewebstore.google.com/detail/reader-view/ecabifbgmdmgdllomnfinbmaellmclnh


```bash
# copy sample yaml conf
cp ./zero_to_one_hundred/tests_sb/resources/map.yaml .
cat map.yaml
export MAP_YAML_PATH=map.yaml
# tip:  add it to .bash_rc etc or some shell script
```

![](a4b09e11-9f1f-4098-a4e2-77d6df85226a.png)

```bash
vim map.yaml
# add your membership details :)
```

> add your membership details :) and it will work

![](c81254c5-058e-419a-b9c3-e967be2e5302.png)

> ex with mine :)

![](f5ac382b-dafe-4ba7-ba82-a3cabc01553e.png)

```bash
chmod +x *.py
./main.py sb help
```

![](63fd79b5-ad41-45fd-a2dc-367f317bcc0c.png)


- create new meta-book

```bash
url=https://learning.oreilly.com/library/view/hunt-the-pragmatic-programmer/020161622X/
./main.py sb snatch_book $url
```

and you have a `toc.md` for free to use as your index (bookmark it)

> as I use myself Lorenzo's great utility `safaribooks` I added some code to convert the downloaded epub contents into a related pdf and split that in chunks so I can easily use it on ipad or better remarkable for studying and later sync back in a repo for hands-on code... they call that **learning by doing** 🖖🏻

