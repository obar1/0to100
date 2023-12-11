from zero_to_one_hundred.configs.config import Config

MAP = "map"
MAP_YAML_PATH = "MAP_YAML_PATH"


class ConfigMap(Config):
    """ConfigMap specific to  actual impl"""

    def __init__(self, persist_fs, map_yaml_path):
        """init"""
        super().__init__(map_yaml_path, persist_fs)

    @property
    def get_repo_path(self):
        """T Returns path."""
        return self.persist_fs.abs_path(self.load["repo"]["path"])

    @property
    def get_repo_map_md(self):
        """T Returns map_md."""
        return self.load["repo"]["map_md"]

    @property
    def get_repo_sorted(self) -> bool:
        """T Returns sorted."""
        return bool(self.load["repo"]["sorted"])
