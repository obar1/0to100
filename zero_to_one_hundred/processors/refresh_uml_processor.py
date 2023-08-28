"""RefreshUMLProcessor:
add uml like mind-map of the sections
"""
# pylint: disable=R0801,W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from configs.config import ConfigMap
from models.map import Map
from models.uml import UML


class RefreshUMLProcessor:
    """RefreshUMLProcessor"""

    def __init__(self, persist_fs, process_fs, config_map: ConfigMap):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def process(self):
        """Scan the repo and for each new_section add it to the uml, save the map file."""
        uml: UML = UML(
            self.persist_fs,
            self.config_map,
            Map.build_from_dirs(
                self.persist_fs,
                self.process_fs,
                self.config_map,
                self.persist_fs.list_dirs(self.config_map.get_repo_path),
            ),
        )
        uml.write()
