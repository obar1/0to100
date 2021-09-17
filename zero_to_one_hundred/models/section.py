"""TODO:
"""
# pylint: disable=R0903,E0401,W0703,W1201
import logging
import os
import pathlib

from configs.config import ConfigMap


class Section:
    """Section."""

    def __init__(self, config_map: ConfigMap, http_url: str, PersistFS):
        """
        Init
        Args:
            http_url: https://cloud.google.com/docs
        """

        self.config_map = config_map
        self.http_url = http_url
        self.dir_name = self.__from_dir_to_http_url(http_url)
        self.PersistFS = PersistFS
        self.dir_readme_md = self.dir_name+'/readme.md'

    def __repr__(self):
        return  f"Section {self.http_url}, {self.dir_name}"

    @property
    def get_http_url(self):
        return self.http_url

    @property
    def get_dir_name(self):
        return self.dir_name

    @classmethod
    def __from_dir_to_http_url(cls, http_url):
        return http_url.replace("/", "§")

    @classmethod
    def __from_http_url_to_dir(cls, dir):
        return dir.replace("§", "/")

    @classmethod
    def build_from_http(cls, config_map, http_url, PersistFS):
        return Section(config_map, http_url, PersistFS)

    @classmethod
    def build_from_dir(cls, config_map, PersistFS, dir_name):
        return Section(config_map, cls.__from_http_url_to_dir(dir_name), PersistFS)

    def write(self):
        return self.PersistFS.make_dirs(self.config_map.get_repo_path + '/' + self.dir_name)



