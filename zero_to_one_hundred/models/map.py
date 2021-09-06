"""TODO."""


# pylint: disable=R0903,E0401,W0703,W0238
from typing import List

from models.section import Section


class Map:
    """TODO."""

    def __init__(self, repo_path):
        self.__repo_path = repo_path

    def get_map_as_section(self, from_str) -> List[Section]:
        """
        Read the __repo_path and restrun section
        Args:
            from_str: def() to convert txt to Section

        Returns:
            list of Section
        """
        return []
