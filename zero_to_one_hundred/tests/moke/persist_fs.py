from typing import List

from repository.persist_fs import PersistFS as _PersistFS

class PersistFS(_PersistFS):
    """PersistFS."""
    relative_path_starts_with = '../'
    HTTPS_ = 'https:§§'

    @classmethod
    def list_dirs(cls, repo_path) -> List[str]:
        return ['https:§§cloud.google.com§docs', 'https:§§cloud.google.com§products']

    @classmethod
    def get_dir_name(cls, fn):
        return fn

    @classmethod
    def load_file(cls,config_file:str):
        if config_file.endswith('unsupported_map.yaml'):
            return {'type': 'not_a_map', 'lib': {'path': './repo'}}
        if config_file.endswith('map.yaml'):
            return {'type': 'map', 'repo': {'path': './repo', 'map_md': 'map.md', 'sorted': True}}
        raise ValueError(f"{config_file} not supported")

    @classmethod
    def write_file(cls, readme_md, txt):
        return f"write_file {readme_md} {txt}"

    @classmethod
    def make_dirs(cls, path):
        return f"make_dirs {path}"

    @classmethod
    def read_file(cls, filename)-> List[str]:
        if filename.endswith('readme.md'):
            return """
        # https:§§cloud.google.com§docs\n
                \n
        > https://cloud.google.com/docs\n

https://cloud.google.com/products\n
                """.split('')
        else:
            raise ValueError(f"{filename} not supported")

