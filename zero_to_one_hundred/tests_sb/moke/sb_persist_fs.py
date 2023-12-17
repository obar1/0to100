"""
PersistFS:
fs handling ops
"""


from typing import List

from zero_to_one_hundred.repository.sb_persist_fs import (
    SBPersistFS as _SBPersistFS,
)


class SBPersistFS(_SBPersistFS):
    @staticmethod
    def list_dirs(path: str) -> List[str]:
        print(f"list_dirs {path}")
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
        print(f"get_dir_name {filename}")

    @staticmethod
    def write_file(filename, txt):
        print(f"write_file {filename} {txt}")

    @classmethod
    def create_file(cls, filename):
        print(f"create_file {filename}")
        return cls.write_file(filename, [])

    @staticmethod
    def make_dirs(path):
        print(f"make_dirs {path}")

    @staticmethod
    def delete_folder(path):
        print(f"delete_folder {path}")

    @staticmethod
    def copy_file_to(file_path, path_to):
        print(f"copy_file_to {file_path} {path_to}")
