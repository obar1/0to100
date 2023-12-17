from zero_to_one_hundred.configs.a_config_map import AConfigMap

MAP = "map"


class ConfigMap(AConfigMap):
    def __init__(self, persist_fs, map_yaml_path):
        super().__init__(map_yaml_path, persist_fs)

    @property
    def get_repo_path(self):
        return self.persist_fs.abs_path(self.load["repo"]["path"])

    @property
    def get_repo_map_md(self):
        return self.load["repo"]["map_md"]

    @property
    def get_repo_sorted(self) -> bool:
        return bool(self.load["repo"]["sorted"])
