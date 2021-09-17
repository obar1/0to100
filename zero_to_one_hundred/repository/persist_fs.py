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
    def list_dirs(cls,repo_path) ->List[str]:
        os_walk = list(os.listdir(repo_path))
        return list(filter(lambda f : cls.HTTPS_ in str(f), os_walk))

    @classmethod
    def get_dir_name(cls, fn):
        """return  path dir name of the file"""
        return os.path.dirname(os.path.abspath(fn))

    @classmethod
    def load_file(cls, config_file):
        with open(config_file, "r") as stream:
            return yaml.safe_load(stream)

    @classmethod
    def write_file(cls,file_name, txt):
        if os.path.isfile(file_name):
            logging.info(f"skip {file_name}")
        else:
            with open(file_name, "w") as file1:
                # Writing data to a file
                file1.writelines(txt)
                logging.info(f"write {file_name}")

    @classmethod
    def make_dirs(cls, path):
        if os.path.isdir(path):
            logging.info(f"skip {path}")
        else:
            os.makedirs(path, 0o777, False)
            logging.info(f"create {path}")