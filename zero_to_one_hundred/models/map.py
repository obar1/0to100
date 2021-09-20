"""Map:
map md with list of sections as from fs
"""
# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103
import os
from typing import List

from configs.config import ConfigMap
from models.section import Section


class Map:
    """Map is a list of section"""

    def __init__(self, config_map: ConfigMap, persist_fs, sections: List[Section]):
        """init"""
        self.config_map = config_map
        self.readme_md = config_map.get_repo_path + "/" + config_map.get_repo_map_md
        self.persist_fs = persist_fs
        self.sections = sections

    def __repr__(self):
        """repr"""
        return f"Map {self.readme_md}, {self.sections}"

    @staticmethod
    def __repr_flatten(sections: List[Section], as_sorted: bool) -> str:
        """transf as"""
        # 1. <https://cloud.google.com/api-gateway/docs/about-ap
        # i-gateway> :ok: [`here`](../https:§§cloud.google.com§/readme.md)
        lambda_flatten_section = (
            lambda s: "1. <"
            + s.get_http_url
            + "> :o: [`here`](./"
            + s.get_dir_name
            + "/readme.md)"
            + os.linesep
        )
        flattened_sections = list(map(lambda_flatten_section, sections))
        return (
            "".join(sorted(flattened_sections))
            if as_sorted
            else "".join(flattened_sections)
        )

    def write(self, as_sorted):
        # init with list of sections found
        txt = []
        txt.append(
            """
# {}
> sorted:{}
{}
        """.format(
                self.readme_md,
                self.config_map.get_repo_sorted,
                self.__repr_flatten(self.sections, as_sorted),
            )
        )
        return self.persist_fs.write_file(self.readme_md, txt)

    @classmethod
    def build_from_dirs(cls, config_map, persist_fs, dirs: List[str]) -> List[Section]:
        """from a list of dirs created with Section() return the org Section()"""
        return [
            Section.build_from_dir(config_map, persist_fs, d)
            for d in dirs
            if d is not None
        ]
