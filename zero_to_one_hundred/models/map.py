"""Map:
map md with list of sections as from fs
"""
# pylint: disable=R0903,E0401,W0703,W1201
import logging
import os
from typing import List

from configs.config import ConfigMap
from models.section import Section





class Map:
    """Map is a list of section """

    def __init__(self, config_map: ConfigMap, PersistFS, sections: List[Section]):
        self.config_map=config_map
        self.readme_md = config_map.get_repo_path + '/' + config_map.get_repo_map_md
        self.PersistFS = PersistFS
        self.sections = sections

    def __repr__(self):
        return  f"Map {self.readme_md}, {self.sections}"

    def __repr_flatten(self, sections:List[Section])->str:
        # 1. <https://cloud.google.com/api-gateway/docs/about-ap
        # i-gateway> :ok: [`here`](../https:§§cloud.google.com§api-gateway§docs§about-api-gateway/readme.md)
        lambda_flatten_section = lambda s: '1. <' + s.get_http_url + '> :o: [`here`](./' + s.get_dir_name +'/readme.md)'+ os.linesep
        flattened_sections = list(map(lambda_flatten_section, sections))
        return  ''.join(sorted(flattened_sections)) if self.config_map.get_repo_sorted else ''.join(flattened_sections)

    def write(self):
        # init with list of sections found
        txt = []
        txt.append(
            """
# {}
> sorted:{}
{}
        """.format(self.readme_md, self.config_map.get_repo_sorted, self.__repr_flatten(self.sections)))
        return self.PersistFS.write_file(self.readme_md, txt)


    @classmethod
    def build_from_dirs(cls, config_map, PersistFS, dirs:List[str]) -> List[Section]:
        """from a list of dirs created with Section() return the org Section()"""
        return [Section.build_from_dir(config_map, PersistFS, dir) for dir in dirs if dir is not None]