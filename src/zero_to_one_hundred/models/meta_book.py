import logging
import re

from zero_to_one_hundred.configs.sb_config_map import (
    SBConfigMap,
)
from zero_to_one_hundred.models.metadata import Metadata
from zero_to_one_hundred.repository.sb_persist_fs import (
    SBPersistFS,
)
from zero_to_one_hundred.repository.sb_process_fs import (
    SBProcessFS,
)
from zero_to_one_hundred.validator.validator import Validator


class MetaBook:
    epub_suffix = ".epub"
    HTTP_OREILLY_COVER = "https://learning.oreilly.com/library/cover"
    HTTP_OREILLY_LIBRARY = "https://learning.oreilly.com/library"

    def __init__(
        self,
        config_map: SBConfigMap,
        persist_fs: SBPersistFS,
        process_fs: SBProcessFS,
        http_url: str,
    ):
        self.config_map = config_map
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.isbn = MetaBook.get_isbn(http_url)
        self.contents_path = f"{self.config_map.get_toc_path}/{self.isbn}"
        self.path_img = f"{self.contents_path}/{self.isbn}.png"
        self.metadata = Metadata(
            self.config_map,
            self.persist_fs,
            self.process_fs,
            MetaBook.get_isbn,
            self.http_url,
        )

    def __repr__(self):
        return f"MetaBook {self.isbn} {self.http_url} {self.contents_path}"

    @classmethod
    def build_from_dir(
        cls,
        config_map: SBConfigMap,
        persist_fs: SBPersistFS,
        process_fs: SBProcessFS,
        dir_name,
    ):
        return MetaBook(
            config_map,
            persist_fs,
            process_fs,
            http_url=cls.HTTP_OREILLY_LIBRARY + "/" + dir_name,
        )

    def write_img(self):
        self.process_fs.write_img(
            self.path_img, f"{self.HTTP_OREILLY_COVER}/{self.isbn}/"
        )

    def write_metadata(self):
        self.metadata.write()

    @classmethod
    def is_valid_ebook_path(cls, ebook_folder):
        """check folder is 0123..9 like ISBN"""
        # https: // www.isbn.org / about_ISBN_standard
        return re.match(r"^[0-9]{13}", ebook_folder)

    def write(self):
        try:
            self.persist_fs.make_dirs(self.contents_path)
            self.write_img()
            self.write_metadata()
        except Exception as e:
            Validator.print_e(e)

    @classmethod
    def get_isbn(cls, http_url) -> str | None:
        isbn10_pattern = (
            r"(?<![0-9])[0-9]{1,5}[-\s]?[0-9]{1,7}[-\s]?[0-9]{1,6}[-\s]?[0-9X](?![0-9])"
        )
        isbns = re.findall(isbn10_pattern, http_url)
        return isbns[0] if len(isbns) > 0 else None

    def path_as_md(self, a_path):
        """
        use relative path and convert " " to %20
        """
        return a_path.replace(" ", "%20")

    @property
    def get_matching_icon_as_md(self):
        icons = self.config_map.get_legend_icons

        res = [i.icon for i in icons if re.search(i.regex, self.http_url)]
        return " ".join(res)
