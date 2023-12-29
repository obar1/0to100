# pylint: disable=W0108
from abc import ABC
from typing import List
import os
import yaml


class APersistFS(ABC):
    @classmethod
    def list_dirs(cls, path) -> List[str]:
        print(f"list_dirs {path}")
        files = [
            os.path.join(path, name)
            for name in os.listdir(path)
            if os.path.isdir(os.path.join(path, name))
        ]
        files.sort(key=lambda x: os.path.getmtime(x))
        return [f[len(path) + 1 :] for f in files]

    @classmethod
    def get_dir_name(cls, filename):
        return os.path.dirname(os.path.abspath(filename))

    @classmethod
    def load_map_yaml_path(cls, MAP_YAML_PATH):
        with open(MAP_YAML_PATH, mode="r", encoding="UTF-8") as stream:
            return yaml.safe_load(stream)

    @classmethod
    def write_file(cls, filename, txt):
        print(f"write_file {filename}")
        with open(filename, mode="w", encoding="UTF-8") as outfile:
            return outfile.write("".join(txt))

    @classmethod
    def create_empty_file(cls, filename):
        print(f"create_empty_file {filename}")
        return cls.write_file(filename, [])

    @classmethod
    def make_dirs(cls, path):
        print(f"make_dirs {path}")
        return os.makedirs(path, 0o777, True)

    @classmethod
    def read_file(cls, filename) -> List[str] | None:
        print(f"read_file {filename}")
        lines = None
        try:
            with open(filename, mode="r", encoding="UTF-8") as f:
                lines = f.readlines()
        except:
            pass  # we dont care
        return lines

    @classmethod
    def delete_folder(cls, path):
        print(f"delete_folder {path}")
        return os.rmdir(path)

    @classmethod
    def abs_path(cls, path):
        return os.path.abspath(path)

    @classmethod
    def get_pkg_info(cls):
        res: str = "--"
        try:
            res = " ".join(cls.read_file("0to100.egg-info/PKG-INFO")[:4])
        except:
            pass  # we dont care
        return res
