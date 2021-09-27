"""Config:

like

config:
  type: map
repo:
  path: ./repo
  map_md: map.md
  sorted : true

"""
# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-section,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203


class Config:
    """Config"""

    def __init__(self, map_yaml_path, persist_fs):
        """persist_fs_load_file: f()  to load file as dict[]"""
        self.map_yaml_path = map_yaml_path
        self.persist_fs = persist_fs

    def __repr__(self):
        """repr"""
        return f"map_yaml_path:{self.map_yaml_path}"

    @property
    def load(self):
        """load yaml file"""
        return self.persist_fs.load_file(self.map_yaml_path)

    @property
    def get_type(self):
        """Returns config type."""
        return self.load["type"]


class ConfigMap(Config):
    """ConfigMap specific to  actual impl"""

    def __init__(self, map_yaml_path, persist_fs):
        """init"""
        super().__init__(map_yaml_path, persist_fs)
        self.get_repo_readme_puml = "readme.puml"
        # TODO: put in the yaml

    @property
    def get_repo_path(self):
        """T Returns path."""
        return self.load["repo"]["path"]

    @property
    def get_repo_map_md(self):
        """T Returns map_md."""
        return self.load["repo"]["map_md"]

    @property
    def get_repo_sorted(self) -> bool:
        """T Returns sorted."""
        return bool(self.load["repo"]["sorted"])
