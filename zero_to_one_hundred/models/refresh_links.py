"""RefreshLinks:
a readme md with http and ref
"""
# pylint: disable=R0903,E0401,W0703,W1201
from typing import List

from configs.config import ConfigMap
from models.section import Section


def collect_links_str(sections:List[Section]):
    return []


class RefreshLinks:
    def __init__(self,config_map:ConfigMap, PersistFS, sections:List[Section]):
        self.config_map=config_map
        self.PersistFS=PersistFS
        self.sections=sections

    def __repr__(self):
        return f"RefreshLinks {self.config_map}, {self.sections}"

    def refresh_sections_links(self):
        links:List[str] = collect_links_str(self.sections)
