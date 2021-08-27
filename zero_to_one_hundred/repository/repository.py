"""Section repository.

Handle the persist
"""
# pylint: disable=R0903,W0238
from typing import List

from configs.config import Config
from models.section import Section


class Persist:
    """TODO."""

    def __init__(self, config: Config):
        self.__config = config

    def write(self, section: Section):
        """Write section."""

    def load_map(self) -> List[Section]:
        """Load section from map."""
