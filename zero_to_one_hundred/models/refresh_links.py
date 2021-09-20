"""RefreshLinks:
links fom a readme to  another are changed from http to http+dir/readme.md
"""
# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging
from typing import List

from configs.config import ConfigMap
from models.readme_md import ReadMeMD
from models.section import Section


class RefreshLinks:
    """RefreshLinks"""

    def __init__(self, config_map: ConfigMap, persist_fs, sections: List[Section]):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.sections = sections

    def __repr__(self):
        """repr"""
        return f"RefreshLinks {self.config_map}, {self.sections}"

    def refresh_map_links(self):
        """refresh_map_links"""
        for section in self.sections:
            try:
                readme_md: ReadMeMD = ReadMeMD(
                    self.config_map, section, self.persist_fs
                )
                txt = readme_md.read()
                readme_md.refresh_links(txt)
            except FileNotFoundError as e:
                logging.warning(f"Check {readme_md} {e}")
