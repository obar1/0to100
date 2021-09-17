"""RefreshLinks:
a readme md with http and ref
"""
# pylint: disable=R0903,E0401,W0703,W1201
from typing import List

from configs.config import ConfigMap
from models.readme_md import ReadMeMD
from models.section import Section



class RefreshLinks:
    def __init__(self,config_map:ConfigMap, PersistFS, sections:List[Section]):
        self.config_map=config_map
        self.PersistFS=PersistFS
        self.sections=sections

    def __repr__(self):
        return f"RefreshLinks {self.config_map}, {self.sections}"

    def refresh_sections_links(self):
        for section in self.sections:
            readme_md: ReadMeMD = ReadMeMD(self.config_map, section, self.PersistFS)
            txt = readme_md.read()
            txt_refreshed= readme_md.refresh_links(txt)

