"""PUML:
sections rendered as mind map
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import os
from typing import List

from configs.config import ConfigMap
from models.section import Section


class PUML:
    """PUML"""

    S = " *"
    NODE_LEVEL_SYMBOL = "+"

    def __init__(self, config_map: ConfigMap, persist_fs, sections: List[Section]):
        """init"""
        self.config_map = config_map
        self.readme_puml = (
            config_map.get_repo_path + "/" + config_map.get_repo_readme_puml
        )
        self.persist_fs = persist_fs
        self.sections = sections

    def __repr__(self):
        """repr"""
        return f"Map {self.readme_puml}, {self.sections}"

    @staticmethod
    def __repr_flatten(rows: List[Section]) -> str:
        """built the md from sections"""
        # 1. <https://cloud.google.com/api-gateway/docs/about-ap
        # i-gateway> :ok: [`here`](../https:§§cloud.google.com§bq/readme.md)

        rows_as_tree = PUML.reorganize_as_tree(rows)
        rows_puml = PUML.render_as_pum_tree(
            rows_as_tree, PUML.S, PUML.NODE_LEVEL_SYMBOL
        )
        return os.linesep.join(list(rows_puml))

    def write(self):
        """write to fs"""
        # init with list of sections found
        txt = []
        txt.append(
            f"""
@startmindmap

title LINKS

skinparam shadowing false
skinparam backgroundColor #EEEBDC
skinparam ArrowColor black
skinparam noteBorderColor black

{PUML.NODE_LEVEL_SYMBOL} 0
{self.__repr_flatten(self.sections)}

@endmindmap
        """
        )
        return self.persist_fs.write_file(self.readme_puml, txt)

    @classmethod
    def reorganize_as_tree(cls, rows):
        http_url_rows = sorted(r.http_url + PUML.S for r in rows)
        for i in range(len(http_url_rows) - 1):
            for k in range(i, len(http_url_rows) - 1):
                if http_url_rows[i].replace(PUML.S, "") in http_url_rows[k + 1]:
                    http_url_rows[k + 1] = (
                        http_url_rows[i].replace(PUML.S, "")
                        + http_url_rows[k + 1].replace(
                            http_url_rows[i].replace(PUML.S, ""), ""
                        )
                        + PUML.S
                    )
        return http_url_rows

    @classmethod
    def render_as_pum_tree(cls, rows_as_tree, symbol_level, node_symbole_level):
        """present in uml fashion"""
        for row in rows_as_tree:
            level = row.count(symbol_level)
            yield node_symbole_level * (level + 1) + "_" + " [[ " + row.replace(
                symbol_level, ""
            ) + " ]]"
