"""RefreshPUMLProcessor:
add uml like mind-map of the sections
"""
# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-section,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from configs.config import ConfigMap
from models.map import Map
from models.puml import PUML


class RefreshPUMLProcessor:
    """RefreshPUMLProcessor"""

    def __init__(self, config_map: ConfigMap, persist_fs):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs

    def process(self):
        """Scan the repo and for each new_section add it to the puml, save the map file."""
        sections = Map.build_from_dirs(
            self.config_map,
            self.persist_fs,
            self.persist_fs.list_dirs(self.config_map.get_repo_path),
        )
        puml: PUML = PUML(self.config_map, self.persist_fs, sections)
        puml.write()
