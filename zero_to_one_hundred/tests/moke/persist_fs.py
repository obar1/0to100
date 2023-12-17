"""
PersistFS:
fs handling ops
"""
# pylint: disable=R1714,W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203


from typing import List

from repository.persist_fs import PersistFS as _PersistFS


class PersistFS(_PersistFS):
    @classmethod
    def list_dirs(cls, path) -> List[str]:
        print(f"list_dirs {path}")
        if path == "https§§§cloud.google.com§sections" or path == "./repo":
            return [
                "https§§§cloud",
                "https§§§cloud§1",
                "https§§§cloud§1§3",
                "https§§§cloud§1§1",
                "https§§§cloud§1§2",
                "https§§§cloud§2",
                "https§§§cloud§2§1",
                "https§§§cloud§2§1§1",
            ]
        if path == "https§§§cloud.google.com§docs":
            return [
                "https§§§cloud.google.com§docs",
                "https§§§cloud.google.com§products",
            ]
        raise ValueError(f"{path} not supported")

    @classmethod
    def get_dir_name(cls, filename):
        print(f"get_dir_name {filename}")

    @classmethod
    def load_file(cls, MAP_YAML_PATH):
        print(f"load_file {MAP_YAML_PATH}")
        if MAP_YAML_PATH.endswith("unsupported_map.yaml"):
            return {"type": "not_a_map", "lib": {"path": "./repo"}}
        if MAP_YAML_PATH.endswith("map.yaml"):
            return {
                "type": "map",
                "repo": {"path": "./repo", "map_md": "map.md", "sorted": True},
            }
        raise ValueError(f"{MAP_YAML_PATH} not supported")

    @classmethod
    def write_file(cls, filename, txt):
        print(f"write_file {filename} {txt}")

    @classmethod
    def create_file(cls, filename):
        print(f"create_file {filename}")
        return cls.write_file(filename, [])

    @classmethod
    def make_dirs(cls, path):
        print(f"make_dirs {path}")

    @classmethod
    def read_file(cls, filename) -> List[str]:
        print(f"read {filename}")
        if filename.endswith("readme.md"):
            return """
        # https§§§cloud.google.com§docs\n
                \n
        > https://cloud.google.com/docs\n

https://cloud.google.com/products\n
                """.split(
                "\n"
            )
        raise ValueError(f"{filename} not supported")

    @classmethod
    def delete_folder(cls, path):
        print(f"delete_folder {path}")

    @classmethod
    def copy_file_to(cls, file_path, path_to):
        print(f"copy_file_to {file_path} {path_to}")

    @classmethod
    def abs_path(cls, path):
        print(f"abs_path {path}")
        return path

    @classmethod
    def done_section(cls, path):
        print(f"close_section {path}")
