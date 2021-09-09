"""TODO:
"""
# pylint: disable=R0903,E0401,W0703,W1201
import pathlib


class Section:
    """Section."""

    def __init__(self, http_url: str,PersistFS):
        """
        Init
        Args:
            http_url: https://cloud.google.com/docs
        """
        self.http_url = http_url
        self.dir_name =self.__from_dir_to_http_url(http_url)
        self.PersistFS=PersistFS

    def __repr__(self):
        return f"Section {self.http_url}, {self.dir_name}"

    @classmethod
    def __from_dir_to_http_url(cls,http_url):
        return http_url.replace("/", "§")

    @classmethod
    def __from_http_url_to_dir(cls, dir):
        return dir.replace("§", "/")

    @classmethod
    def build_from_http(cls, http_url,PersistFS):
        return Section(http_url,PersistFS)

    @classmethod
    def build_from_dir(cls, dir,PersistFS):
        dir_name = pathlib.PurePath(dir).name
        return Section(cls.__from_http_url_to_dir(dir_name),PersistFS)

    def write(self):
        pass
