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
