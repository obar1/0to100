"""Section repository.

Handle the persist
"""
# pylint: disable=R0903,W0238,W1201
import logging
import os
import traceback
from typing import List

from configs.config import Config
from exceptions.section_value_error import SectionValueError
from models.section import Section


class ReadMe:

    def __init__(self,repo_path, section: Section):
        self.readme=repo_path+"/readme.md"
        self.__section=section


    def write(self):
        file1 = open(self.readme, "w")  # write mode
        # # https:§§cloud.google.com§api-gateway§docs
        # > https: // cloud.google.com / api - gateway / docs
        txt = """
# {}
        
> {}
        """.format(self.__section.get_section(),self.__section.get_http())
        file1.write(txt)
        file1.close()


class PersistFS:
    """PersistFS."""

    def __init__(self, config: Config):
        self.__config = config

    def write(self, section: Section):
        """write section"""
        repo_path = section.get_valid_path(self.__config.get_repo_path())
        os.makedirs(repo_path, exist_ok=True)
        ReadMe(repo_path,section).write()
        logging.info("PersistFS.write: done " + section.__str__())

    def load_map(self) -> List[Section]:
        """Load section from map."""
        return []
        # TODO: tio implement
