"""TODO:
"""
# pylint: disable=R0903,E0401,W0703,W1201

from configs.config import ConfigMap
from models.map import Map


class RefreshSectionsProcessor():

    def __init__(self, config_map: ConfigMap, PersistFS):
        self.config_map = config_map
        self.PersistFS = PersistFS

    def process(self):
        """Scan the repo and for each section add it to  the map,  save the map file."""
        sections=Map.build_from_dirs(self.config_map, self.PersistFS, self.PersistFS.list_dirs(self.config_map.get_repo_path))
        map:Map = Map(self.config_map,self.PersistFS,sections)
        map.write()