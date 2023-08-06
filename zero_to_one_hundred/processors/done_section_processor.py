"""DoneSectionProcessor:
done section on fs from http address
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from configs.config import ConfigMap
from models.section import Section


class DoneSectionProcessor:
    """DoneSectionProcessor."""

    def __init__(self, persist_fs, process_fs, config_map: ConfigMap, http_url: str):
        """init"""
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.config_map = config_map

    def process(self):
        """Close section"""
        section: Section = Section(
            self.persist_fs,
            self.process_fs,
            self.config_map,
            self.http_url,
            is_done=True,
        )
        section.write()
