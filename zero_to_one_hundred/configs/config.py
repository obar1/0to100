"""Config:

like

config:
  type: map
repo:
  path: ./repo
  map_md: map.md
  sorted : true

"""
# pylint: disable=R0903,W0238



class Config:
    """Config"""

    def __init__(self, map_yaml_path,PersistFS):
        """

        Args:
            map_yaml_path:
            persist_fs_load_file: f()  to load file as dict[]
        """
        self.map_yaml_path =  map_yaml_path
        self.PersistFS =PersistFS

    def __repr__(self):
        return f"map_yaml_path:{self.map_yaml_path}"

    @property
    def load(self):
        return self.PersistFS.load_file(self.map_yaml_path)

    @property
    def get_type(self):
        """Returns config type."""
        return self.load["type"]



class ConfigMap(Config):

    def __init__(self,map_yaml_path,PersistFS):
        super().__init__(map_yaml_path,PersistFS)

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


