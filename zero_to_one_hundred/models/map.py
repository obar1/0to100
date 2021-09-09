"""TODO:
"""
# pylint: disable=R0903,E0401,W0703,W1201
from typing import List

from models.section import Section


class Map:
    """Map is a list of section """

    def __init__(self, repo_path):
        self.__repo_path = repo_path


    @classmethod
    def from_dirs(cls, dirs:List[str]) -> List[Section]:
        """from a list of dirs created with Section() return the org Section()"""
        return [Section.build_from_dir(dir) for dir in dirs if dir is not None]
