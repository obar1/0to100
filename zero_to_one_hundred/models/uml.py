"""UML:
sections rendered as mind map
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import os
from typing import List

from configs.config import ConfigMap
from models.section import Section


class UML:
    """UML"""

    ROOT = "ROOT"
    NODE_LEVEL_SYMBOL = "\t"

    def __init__(self, persist_fs, config_map: ConfigMap, sections: List[Section]):
        """init"""
        self.config_map = config_map
        self.uml_md = config_map.get_repo_path + "/" + config_map.get_repo_uml_md
        self.persist_fs = persist_fs
        self.sections = sections

    def __repr__(self):
        """repr"""
        return f"UML {self.uml_md}, {self.sections}"

    @staticmethod
    def __repr_flatten(rows: List[Section]) -> str:
        """built the md from sections"""
        rows_as_tree = UML.reorganize_as_tree(rows, UML.NODE_LEVEL_SYMBOL)
        return os.linesep.join(list(rows_as_tree))

    def write(self):
        """write to fs"""
        # init with list of sections found
        txt = []
        txt.append(
f"""
```mermaid
mindmap
{UML.ROOT}
{self.__repr_flatten(self.sections)}
```
"""
        )
        return self.persist_fs.write_file(self.uml_md, txt)

    @classmethod
    def reorganize_as_tree(cls, rows,node_level_symbol):
        http_url_rows = sorted(r.http_url + node_level_symbol for r in rows)
        for i in range(len(http_url_rows) - 1):
            for j in range(len(http_url_rows) - 1):
                if i != j:
                    if http_url_rows[j].startswith(http_url_rows[i].rstrip(node_level_symbol)):
                        http_url_rows[j]=http_url_rows[j]+node_level_symbol
        for row in http_url_rows:
            level = row.count(node_level_symbol)
            yield node_level_symbol * (level ) + row.replace(
                node_level_symbol, ""
            )
