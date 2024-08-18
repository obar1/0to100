from zero_to_one_hundred.configs.a_config_map import AConfigMap
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS

ZTOH_MAP = "ztoh-map"


class ZTOHConfigMap(AConfigMap):
    def __init__(self, persist_fs: ZTOHPersistFS):
        super().__init__(persist_fs)

    @property
    def get_repo_path(self):
        return self.load["repo"]["path"]

    @property
    def get_repo_map_md(self):
        return self.load["repo"]["map_md"]

    @property
    def get_repo_sorted(self) -> bool:
        return self.load["repo"].get("sorted")

    @property
    def get_repo_legend_type(self) -> str | None:
        return self.load["repo"].get("legend_type")
