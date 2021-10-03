"""RefreshLinks:
links fom a readme to  another are changed from http to http+dir/readme.md
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging
from typing import List

from configs.config import ConfigMap
from models.readme_md import ReadMeMD
from models.section import Section


class RefreshLinks:
    """RefreshLinks"""

    def __init__(
        self, persist_fs, process_fs, config_map: ConfigMap, sections: List[Section]
    ):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.sections = sections

    def __repr__(self):
        """repr"""
        return f"RefreshLinks {self.config_map}, {self.sections}"

    def refresh_map_links(self):
        """refresh_map_links"""
        for section in self.sections:
            readme_md: ReadMeMD = ReadMeMD(
                self.persist_fs, self.process_fs, self.config_map, section
            )
            try:
                txt = readme_md.read()
                readme_md.refresh_links(txt)
            except FileNotFoundError as e:
                logging.info(f"Check {readme_md} {e}")
