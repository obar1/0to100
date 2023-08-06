"""PersistFS:
deal with FS
mocked in Test
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging
import os
from datetime import datetime
from shutil import copyfile
from typing import List

import yaml


class PersistFS:
    """persist_fs."""

    relative_path_starts_with = "./"
    HTTPS_ = ":§§"

    @classmethod
    def list_dirs(cls, path) -> List[str]:
        logging.info(f"list_dirs {path}")
        return [
            name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))
        ]

    @classmethod
    def get_dir_name(cls, filename):
        logging.info(f"get_dir_name {filename}")
        return os.path.dirname(os.path.abspath(filename))

    @classmethod
    def load_file(cls, config_file):
        logging.info(f"load_file {config_file}")
        with open(config_file, mode="r", encoding="UTF-8") as stream:
            return yaml.safe_load(stream)

    @classmethod
    def write_file(cls, filename, txt):
        logging.info(f"write_file {filename}")
        with open(filename, mode="w", encoding="UTF-8") as outfile:
            return outfile.write("".join(txt))

    @classmethod
    def create_file(cls, filename):
        logging.info(f"create_file {filename}")
        return cls.write_file(filename, [])

    @classmethod
    def make_dirs(cls, path):
        logging.info(f"make_dirs {path}")
        if os.path.isdir(path):
            logging.info(f"_skip {path}")
            return None
        logging.info(f"_create {path}")
        return os.makedirs(path, 0o777, False)

    @classmethod
    def read_file(cls, filename) -> List[str]:
        logging.info(f"read {filename}")
        with open(filename, mode="r", encoding="UTF-8") as file_:
            lines = file_.readlines()
            return lines

    @classmethod
    def delete_folder(cls, path):
        logging.info(f"delete_folder {path}")
        return os.rmdir(path)

    @classmethod
    def copy_file_to(cls, file_path, path_to):
        logging.info(f"copy_file_to {file_path} {path_to}")
        return copyfile(file_path, path_to)

    @classmethod
    def abs_path(cls, path):
        abs_path = os.path.abspath(path)
        assert abs_path is not None
        logging.info(f"abs_path {abs_path}")
        return abs_path

    @classmethod
    def get_now(cls):
        now = datetime.now()
        return now.strftime("%Y/%m/%d-%H:%M:%S")

    @classmethod
    def done_section(cls, path):
        logging.info(f"done_section {path}")
        if os.path.isdir(path):
            path = path + os.sep + ".done"
            logging.info(f"path {path}")
            if os.path.exists(path):
                logging.info(f"skip {path}")
            else:
                os.makedirs(path, 0o777, False)
                logging.info(f"created {path}")
            return True

    @classmethod
    def done_section_status(cls, path):
        logging.info(f"done_section_status {path}")
        if path := cls.abs_path(path):
            path = path + os.sep + ".done"
            logging.info(f"path {path}")
            exists = os.path.exists(path)
            logging.info(f"exists {exists}")
            return exists
