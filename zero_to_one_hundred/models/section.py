"""Section:
new_section od disk
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from configs.config import ConfigMap


class Section:
    """Section."""

    epub_suffix = ".epub"
    HTTP_OREILLY = "https://learning.oreilly.com/library/cover"
    GENERIC_HTTP_OREILLY = "https://learning.oreilly.com/library/"

    def __init__(self, persist_fs, process_fs, config_map: ConfigMap, http_url: str):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.http_url = http_url
        self.dir_name = self.__from_dir_to_http_url(http_url)
        self.dir_readme_md = self.dir_name + "/readme.md"

    def __repr__(self):
        """repr"""
        return f"Section {self.http_url}, {self.dir_name}"

    @property
    def get_http_url(self):
        return self.http_url

    @property
    def get_dir_name(self):
        return self.dir_name

    @classmethod
    def __from_dir_to_http_url(cls, http_url):
        return (
            http_url.replace("/", "§")
            .replace("<", "§")
            .replace(">", "§")
            .replace(":", "§")
            .replace("?", "§")
            .replace("*", "§")
            .replace("\\", "§")
        )

    @classmethod
    def from_http_url_to_dir(cls, dir_):
        return dir_.replace("§", "/")

    @classmethod
    def build_from_http(cls, config_map, http_url, persist_fs, process_fs):
        return Section(persist_fs, process_fs, config_map, http_url)

    @classmethod
    def build_from_dir(cls, persist_fs, process_fs, config_map, dir_name):
        return Section(
            persist_fs, process_fs, config_map, cls.from_http_url_to_dir(dir_name)
        )

    def write(self):
        return self.persist_fs.make_dirs(
            self.config_map.get_repo_path + "/" + self.dir_name
        )

    @classmethod
    def is_valid_dir(cls, curr_dir):
        logging.info(curr_dir)
        return True
