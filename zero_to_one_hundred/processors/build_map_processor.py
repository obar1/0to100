"""TODO:
"""
# pylint: disable=R0903,E0401,W0703,W1201
from typing import List

from configs.config import Config
from models.map import Map
from repository.persist_fs import PersistFS


class BuildMapProcessor:
    """BuildMapProcessor"""

    def __init__(self, config: Config, persist: PersistFS):
        self.__config = config
        self.__persist = persist

    def process(self):
        """Scan the repo and for each section add it to  the map,  save the map file."""
        repo_path = self.__config.get_repo_path()
        dirs: List[str] = self.__persist.list_dirs
        map: Map = Map.from_dirs(dirs)
        return map
