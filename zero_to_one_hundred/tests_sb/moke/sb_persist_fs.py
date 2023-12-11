"""
PersistFS:
fs handling ops
"""


import logging
from typing import List

from zero_to_one_hundred.repository.sb_persist_fs import (
    SBPersistFS as _SBPersistFS,
)


class SBPersistFS(_SBPersistFS):
    """persist_fs."""

    @staticmethod
    def list_dirs(path: str) -> List[str]:
        logging.debug(f"list_dirs {path}")
        if path == ".":
            return ["ABC (9781948580793)", "CDF (9780135956977)"]
        if path == "./safaribooks.git/Books":
            return [
                "The Concise Coaching Handbook (9781948580793)",
                "The Pragmatic Programmer (9780135956977)",
            ]
        raise ValueError(f"{path} not supported")

    @staticmethod
    def get_dir_name(filename):
        logging.info(f"get_dir_name {filename}")

    @staticmethod
    def write_file(filename, txt):
        logging.debug(f"write_file {filename} {txt}")

    @classmethod
    def create_file(cls, filename):
        logging.debug(f"create_file {filename}")
        return cls.write_file(filename, [])

    @staticmethod
    def make_dirs(path):
        logging.debug(f"make_dirs {path}")

    @staticmethod
    def delete_folder(path):
        logging.debug(f"delete_folder {path}")

    @staticmethod
    def copy_file_to(file_path, path_to):
        logging.debug(f"copy_file_to {file_path} {path_to}")
