"""PersistFS:
deal with FS
mocked in Test
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging
import os
from typing import List

import yaml


class PersistFS:
    """persist_fs."""

    relative_path_starts_with = "./"
    HTTPS_ = ":§§"

    @classmethod
    def list_dirs(cls, dir_name) -> List[str]:
        logging.info(os.path.dirname(os.path.abspath(__file__)))
        os_walk = list(os.listdir(dir_name))
        return list(filter(lambda f: cls.HTTPS_ in str(f), os_walk))

    @classmethod
    def get_dir_name(cls, filename):
        return os.path.dirname(os.path.abspath(filename))

    @classmethod
    def load_file(cls, config_file):
        with open(config_file, mode="r", encoding="UTF-8") as stream:
            return yaml.safe_load(stream)

    @classmethod
    def write_file(cls, file_name, txt):
        with open(file_name, mode="w", encoding="UTF-8") as outfile:
            outfile.write("".join(txt))
            logging.info(f"write_file {file_name} {txt}")

    @classmethod
    def make_dirs(cls, path):
        if os.path.isdir(path):
            logging.info(f"skip {path}")
        else:
            os.makedirs(path, 0o777, False)
            logging.info(f"create {path}")

    @classmethod
    def read_file(cls, filename) -> List[str]:
        logging.info(f"read {filename}")
        with open(filename, mode="r", encoding="UTF-8") as file_:
            lines = file_.readlines()
            return lines
