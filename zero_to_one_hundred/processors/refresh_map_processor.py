from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS

from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS

from zero_to_one_hundred.configs.ztoh_config_map import ZTOHConfigMap
from zero_to_one_hundred.models.map import Map
from zero_to_one_hundred.processors.a_processor import AProcessor


class RefreshMapProcessor(AProcessor):
    """RefreshMapProcessor:
    refresh sections in map"""

    def __init__(
        self,
        config_map: ZTOHConfigMap,
        persist_fs: ZTOHPersistFS,
        process_fs: ZTOHProcessFS,
    ):
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.config_map = config_map

    def process(self):
        """Scan the repo and for each new_section add it to  the map,  save the map file."""
        actual: Map = Map(
            self.config_map,
            self.persist_fs,
            Map.build_from_dirs(
                self.persist_fs,
                self.process_fs,
                self.config_map,
                self.persist_fs.list_dirs(self.config_map.get_repo_path),
            ),
        )
        actual.write(self.config_map.get_repo_sorted)
