"""Section repository.

Handle the persist
"""
# pylint: disable=R0903,W0238,W1201
import logging
import os
import traceback
from typing import List

from configs.config import Config
from models.section import Section


class Persist:
    """TODO."""

    def __init__(self, config: Config):
        self.__config = config

    def write(self, section: Section):
        """Write section.

        Args:
            config: yaml config
            section: section
        """
        path = section.get_valid_path(self.__config.get_repo_path())
        assert os.path.isdir(path) is False

        try:
            os.makedirs(path)
        except ValueError:
            logging.error(traceback.format_exc())
        else:
            logging.info("Persist.write: done " + path)

    def load_map(self) -> List[Section]:
        """Load section from map."""
