# pylint: disable=W0108
import json
import logging
import os
from abc import ABC
from typing import List, Union

import yaml


class APersistFS(ABC):
    @classmethod
    def list_dirs(cls, path) -> List[str]:
        logging.debug(f"list_dirs {path}")
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
        logging.debug(f"write_file {filename}")
        with open(filename, mode="w", encoding="UTF-8") as outfile:
            return outfile.write("".join(txt))

    @classmethod
    def write_file_json(cls, filename, json_dict):
        json_txt = json.dumps(json_dict, indent=4)
        logging.debug(f"write_file {filename}")
        with open(filename, mode="w", encoding="UTF-8") as outfile:
            return outfile.write(json_txt)

    @classmethod
    def create_empty_file(cls, filename):
        logging.debug(f"create_empty_file {filename}")
        return cls.write_file(filename, [])

    @classmethod
    def make_dirs(cls, path):
        logging.debug(f"make_dirs {path}")
        try:
            os.makedirs(path, 0o777, True)
            return True
        except FileExistsError:
            return False

    @classmethod
    def read_file(cls, filename) -> Union[List[str], None]:  # Replace | with Union
        # logging.debug(f"read_file {filename}")
        lines = None
        try:
            with open(filename, mode="r", encoding="UTF-8") as f:
                lines = f.readlines()
        except Exception as e:
            logging.debug(e)  # we dont care
        return lines

    @classmethod
    def delete_folder(cls, path):
        logging.debug(f"delete_folder {path}")
        return os.rmdir(path)

    @classmethod
    def abs_path(cls, path) -> str:
        return os.path.abspath(path)
