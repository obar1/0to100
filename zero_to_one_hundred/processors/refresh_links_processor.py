"""RefreshLinks:
in each md there are links to http://
when some of them are added as section
replace them with the location of the section ...
"""
# pylint: disable=R0903,E0401,W0703,W1201
from typing import List

from configs.config import ConfigMap
from models.map import Map
from models.refresh_links import RefreshLinks
from models.section import Section


class RefreshLinksProcessor():

    def __init__(self, config_map: ConfigMap, PersistFS):
        self.config_map = config_map
        self.PersistFS = PersistFS

    def process(self):
        """Scan sections an update links."""
        sections:List[Section] = Map.build_from_dirs(self.config_map, self.PersistFS,
                                       self.PersistFS.list_dirs(self.config_map.get_repo_path))
        refresh_links: RefreshLinks = RefreshLinks(self.config_map, self.PersistFS, sections)
        refresh_links.refresh_sections_links()


