

import json
import re

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap


class MetaBook:
    

    epub_suffix = ".epub"
    HTTP_OREILLY = "https://learning.oreilly.com/library/cover"
    GENERIC_HTTP_OREILLY = "https://learning.oreilly.com/library/"

    def __init__(self, config_map: SBConfigMap, persist_fs, process_fs, http_url: str):
        self.config_map = config_map
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.isbn = self.__get_isbn(http_url)
        self.contents_path = f"{self.isbn}"
        self.dir_json = f"{self.contents_path}/{self.isbn}.json"
        self.dir_epub = f"{self.contents_path}/{self.isbn}.epub"
        self.dir_pdf = f"{self.contents_path}/{self.isbn}.pdf"
        self.dir_img = f"{self.contents_path}/{self.isbn}.png"

    def __repr__(self):
        return f"MetaBook {self.http_url}, {self.isbn} {self.contents_path}"

    @classmethod
    def build_from_dir(cls, config_map, persist_fs, process_fs, dir_name):
        "
        return MetaBook(
            config_map,
            persist_fs,
            process_fs,
            http_url=cls.GENERIC_HTTP_OREILLY + "/" + dir_name,
        )

    def write_img(self):
        "
        self.process_fs.write_img(self.dir_img, f"{self.HTTP_OREILLY}/{self.isbn}/")

    def write_epub(self):
        "
        self.process_fs.write_epub(self.config_map, self.dir_epub, self.isbn)
        self.persist_fs.copy_file_to(self.get_epub_path(), self.dir_epub)

    def write_json(self):
        """write json
        {
            "isbn": "0596007124",
            "http_url": "https://learning.oreilly.com/library/view/head-first-design/0596007124/"
        }
        """
        txt = []
        txt.append(
            "{"
            + ' "isbn" : "'
            + self.isbn
            + '" '
            + ' ,"url" : "'
            + self.http_url
            + '" '
            + "}"
        )
        self.persist_fs.write_file(
            self.dir_json, json.dumps(json.loads("".join(txt)), indent=4)
        )

    @staticmethod
    def is_valid_ebook_path(ebook_folder):
        """check folder is 0123..9 like ISBN"""
        return re.match(r"^[0-9]+", ebook_folder)

    def write(self):
        self.persist_fs.make_dirs(self.contents_path)
        self.write_json()
        self.write_epub()
        self.write_fake_pdf()
        self.write_img()

    def read_json(self):
        lines = "{}"
        try:
            lines = self.persist_fs.read_file(self.dir_json)
            return json.dumps(json.loads("".join(lines)), indent=4)
        except:
            return lines

    @staticmethod
    def __get_isbn(http_url):
        """get isbn
        it's the last 0123456..9
        """
        http_url = http_url.strip("/")
        return http_url[http_url.rfind("/") + 1 :]

    def get_epub_path(self):
        """find the actual path into the path given the isbn
        dirs are supposed to be like
        download_engine_books_path/books title (isbn)
        """
        download_engine_books_path = self.config_map.get_download_engine_books_path
        isbn = self.isbn
        dirs = self.persist_fs.list_dirs(download_engine_books_path)
        dir_isbn = [dir_ for dir_ in dirs if "(" + isbn + ")" in dir_]
        return (
            download_engine_books_path
            + "/"
            + dir_isbn[0]
            + "/"
            + isbn
            + MetaBook.epub_suffix
        )

    def write_fake_pdf(self):
        self.persist_fs.create_file(self.dir_pdf)
