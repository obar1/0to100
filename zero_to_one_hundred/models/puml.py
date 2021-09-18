"""PUML:
sections rendered as mind map
"""
# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,C0209,W1203,C0200,C0103
import os
from typing import List

from configs.config import ConfigMap
from models.section import Section


class PUML:
    """PUML"""

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

        rows = sorted(map(lambda s: " * " + s.get_dir_name, rows))

        for f in range(len(rows)):
            # print('\n>'+str(f)+rows[f])
            for b in range(f + 1, len(rows)):
                # print('='+str(b)+rows[b])
                if str(rows[b]).startswith(str(rows[f])):
                    rows[b] = str(rows[b]).replace(str(rows[f]), "  * ")
                # else:
                #     print('*'+str(rows[f]))

        for f in range(len(rows)):
            print(rows[f])
        return os.linesep.join(rows)

    def write(self):
        """write to fs"""
        # init with list of sections found
        txt = []
        txt.append(
            """
@startmindmap puml
* root
{}

@endmindmap
        """.format(
                self.__repr_flatten(self.sections)
            )
        )
        return self.persist_fs.write_file(self.readme_puml, txt)
