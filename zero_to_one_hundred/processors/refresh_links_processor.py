"""RefreshLinks:
in each md there are links to http://
when some of them are added as new_section
replace them with the location of the new_section ...
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from typing import List

from configs.config import ConfigMap
from models.map import Map
from models.refresh_links import RefreshLinks
from models.section import Section


class RefreshLinksProcessor:
    """RefreshLinksProcessor"""

    def __init__(self, config_map: ConfigMap, persist_fs,process_fs):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def process(self):
        """Scan sections an update links."""
        sections: List[Section] = Map.build_from_dirs(
            self.config_map,
            self.persist_fs,
            self.process_fs,
            self.persist_fs.list_dirs(self.config_map.get_repo_path),
        )
        refresh_links: RefreshLinks = RefreshLinks(
            self.config_map, self.persist_fs, sections,self.process_fs
        )
        refresh_links.refresh_map_links()
