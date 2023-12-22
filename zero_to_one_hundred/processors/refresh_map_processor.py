from zero_to_one_hundred.configs.config_map import ConfigMap
from zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.processors.a_processor import AProcessor


class RefreshMapProcessor(AProcessor):
    """RefreshMapProcessor:
    refresh sections in map"""

    def __init__(self, persist_fs, process_fs, config_map: ConfigMap):
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.config_map = config_map

    def process(self):
        """Scan the repo and for each new_section add it to  the map,  save the map file."""
        map_: Map = Map(
            self.persist_fs,
            self.config_map,
            Map.build_from_dirs(
                self.persist_fs,
                self.process_fs,
                self.config_map,
                self.persist_fs.list_dirs(self.config_map.get_repo_path),
            ),
        )
        map_.write(self.config_map.get_repo_sorted)
