"""CreateSectionProcessor:
create a new new_section on fs from http address
"""
# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
from typing import List

from configs.config import ConfigMap
from models.map import Map
from models.readme_md import ReadMeMD
from models.section import Section


class CreateSectionProcessor:
    """CreateSectionProcessor."""

    def __init__(self, config_map: ConfigMap, persist_fs, http_url: str):
        """init"""
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.config_map = config_map

    def process(self):
        """Process the new_section.
        - add new new_section
        - add def readme_md in new_section
        - add new sections to map at the end
        """
        section: Section = Section(self.config_map, self.http_url, self.persist_fs)
        section.write()
        readme_md: ReadMeMD = ReadMeMD(self.config_map, section, self.persist_fs)
        readme_md.write()
        map_: Map = Map(self.config_map, self.persist_fs, self.get_sections(section))
        map_.write(False)

    def get_sections(self, new_section):
        """Get all the sections (sorted) and add the new new_section at the bottom"""
        dirs: List[str] = self.persist_fs.list_dirs(self.config_map.get_repo_path)
        dirs.remove(new_section.dir_name)
        if self.config_map.get_repo_sorted:
            sorted(dirs)
        dirs.append(new_section.dir_name)
        return Map.build_from_dirs(self.config_map, self.persist_fs, dirs)
