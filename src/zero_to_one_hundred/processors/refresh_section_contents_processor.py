from src.zero_to_one_hundred.configs.ztoh_config_map import (
    ZTOHConfigMap,
)
from src.zero_to_one_hundred.models.map import Map
from src.zero_to_one_hundred.processors.a_processor import (
    AProcessor,
)
from src.zero_to_one_hundred.repository.ztoh_persist_fs import (
    ZTOHPersistFS,
)
from src.zero_to_one_hundred.validator.validator import Validator


class RefreshSectionContentsProcessor(AProcessor):
    """RefreshSectionContentsProcessor"""

    def __init__(
        self,
        config_map: ZTOHConfigMap,
        persist_fs: ZTOHPersistFS,
    ):
        self.config_map = config_map
        self.persist_fs = persist_fs

    def process(self):
        """Scan sections an update links."""
        sections = Map.build_from_dirs(
            self.persist_fs,
            self.config_map,
            self.persist_fs.list_dirs(self.config_map.get_repo_path),
        )
        for s in sections:
            try:
                s.look_for_materialized_https()
                s.delete_orphan_images()
            except Exception as e:
                Validator.print_e(e)
