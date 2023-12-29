# pylint: disable=W0246
from abc import ABC
import os

from zero_to_one_hundred.repository.a_persist_fs import APersistFS


class AConfigMap(ABC):
    MAP_YAML_PATH = "MAP_YAML_PATH"

    def __init__(self, persist_fs: APersistFS):
        self.map_yaml_path = os.getenv(AConfigMap.MAP_YAML_PATH)
        assert self.map_yaml_path is not None
        self.persist_fs = persist_fs

    def __repr__(self):
        return (
            f"{AConfigMap.MAP_YAML_PATH} from {self.map_yaml_path} type {self.get_type}"
        )

    @property
    def load(self):
        return self.persist_fs.load_map_yaml_path(self.map_yaml_path)

    @property
    def get_type(self):
        return self.load["type"]
