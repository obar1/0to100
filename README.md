# 0to100

> 0 to 100 ... learn anything from webresources (and not)

![](https://github.com/obar1/0to100/actions/workflows/pytest.yml/badge.svg)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/obar1/0to100?quickstart=1)

![Obsidian](https://img.shields.io/badge/Obsidian-%23483699.svg?style=for-the-badge&logo=obsidian&logoColor=white)

## 1st time usage:

```bash
python -m venv .venv
. venv/bin/activate
pip install -r requirements.txt
```

## daily usage:

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

### Contributing //vscode

look into
```bash
cd zero_to_one_hundred/tests
pytest --log-cli-level=DEBUG --capture=tee-sys ./test_main.py
```

to start with

#### Debug

- sample of `.vscode/launch.json`
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {
                "CONFIG_FILE": "./map.yaml",
                "ZEROto100py": "./zero_to_one_hundred/main.py"
            },
            "args": [
                "help"
            ]
        }
    ]
}

or
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {
                "CONFIG_FILE": "./map.yaml",
                "ZEROto100py": "./zero_to_one_hundred/main.py"
            },
            "args": [
                "create_section",
                "https://www.cloudskillsboost.google/games"
            ]
        }
    ]
}
```

- `pytest--log-cli-level=DEBUG --capture=tee-sys`v`
