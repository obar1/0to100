"""CreateSectionProcessor:
create a new section on fs from http address
"""
# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103
from typing import List

from configs.config import ConfigMap
from models.map import Map
from models.readme_md import ReadMeMD
from models.section import Section


class CreateSectionProcessor:
    """CreateSectionProcessor."""

    def __init__(self, config_map: ConfigMap, persist_fs, http_url: str):
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.config_map = config_map

    def process(self):
        """Process the section.
        - add new section
        - add def readme_md in section
        - add new sections to map at the end
        """
        section: Section = Section(self.config_map, self.http_url, self.persist_fs)
        section.write()
        readme_md: ReadMeMD = ReadMeMD(self.config_map, section, self.persist_fs)
        readme_md.write()

        dirs: List[str] = self.persist_fs.list_dirs(self.config_map.get_repo_path)
        dirs.remove(section.dir_name)
        sorted(dirs)
        dirs.append(section.dir_name)
        sections = Map.build_from_dirs(self.config_map, self.persist_fs, dirs)
        map_: Map = Map(self.config_map, self.persist_fs, sections)
        map_.write(False)
