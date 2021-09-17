"""TODO:
"""
# pylint: disable=R0903,E0401,W0703,W1201
import logging
import os
from typing import List

import yaml




class PersistFS:
    """PersistFS."""
    relative_path_starts_with = './'
    HTTPS_ = 'https:§§'

    @classmethod
    def list_dirs(cls,get_repo_path) ->List[str]:
        logging.warning(os.path.dirname(os.path.abspath(__file__)))
        os_walk = list(os.listdir(get_repo_path))
        return list(filter(lambda f : cls.HTTPS_ in str(f), os_walk))

    @classmethod
    def get_dir_name(cls, fn):
        return os.path.dirname(os.path.abspath(fn))

    @classmethod
    def load_file(cls, config_file):
        with open(config_file, "r") as stream:
            return yaml.safe_load(stream)

    @classmethod
    def write_file(cls,file_name, txt:List[str]):
        with open(file_name, "w") as outfile:
            outfile.write("\n".join(txt))
            logging.info(f"write_file {file_name} {txt}")

    @classmethod
    def make_dirs(cls, path):
        if os.path.isdir(path):
            logging.info(f"skip {path}")
        else:
            os.makedirs(path, 0o777, False)
            logging.info(f"create {path}")

    @classmethod
    def read_file(cls, filename)-> List[str]:
        logging.info(f"read {filename}")
        with open(filename,'r') as f:
            lines = f.readlines()
        return lines



