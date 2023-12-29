import re

from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.metadata import Metadata
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS


class MetaBook:
    epub_suffix = ".epub"
    HTTP_OREILLY = "https://learning.oreilly.com/library/cover"
    GENERIC_HTTP_OREILLY = "https://learning.oreilly.com/library/"

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
        self.metadata = Metadata(
            self.config_map,
            self.persist_fs,
            self.process_fs,
            MetaBook.get_isbn,
            self.http_url,
        )
        self.isbn = MetaBook.get_isbn(http_url)
        self.contents_path = persist_fs.abs_path(f"{self.isbn}")
        self.path_epub = f"{self.contents_path}/{self.isbn}.epub"
        self.path_pdf = f"{self.contents_path}/{self.isbn}.pdf"
        self.path_img = f"{self.contents_path}/{self.isbn}.png"

    def __repr__(self):
        return f"MetaBook {self.http_url}, {self.isbn} {self.contents_path}"

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
            http_url=cls.GENERIC_HTTP_OREILLY + "/" + dir_name,
        )

    def write_img(self):
        self.process_fs.write_img(self.path_img, f"{self.HTTP_OREILLY}/{self.isbn}/")

    def write_epub(self):
        try:
            self.persist_fs.write_fake_epub(self.path_epub)
            self.process_fs.write_epub(self.config_map, self.path_epub, self.isbn)
            self.persist_fs.copy_file_to(self.get_epub_path, self.path_epub)
        except Exception as e:
            print(f"DDD issue with {e}")

    def write_json(self):
        self.metadata.write_json()

    @classmethod
    def is_valid_ebook_path(cls, ebook_folder):
        """check folder is 0123..9 like ISBN"""
        # https: // www.isbn.org / about_ISBN_standard
        return re.match(r"^[0-9]{13}", ebook_folder)

    def write(self):
        try:
            self.persist_fs.make_dirs(self.config_map.get_download_engine_books_path)
            self.persist_fs.make_dirs(self.contents_path)
        except Exception as e:
            print(f"DDD issue with {e}")
        try:
            self.write_img()
        except Exception as e:
            print(f"DDD issue with {e}")
        try:
            self.write_epub()
            self.metadata.write_json()
        except Exception as e:
            print(f"DDD issue with {e}")
        try:
            self.write_pdf(self.path_epub)
            self.write_splitter_pdf(self.path_pdf, self.config_map.get_split_pdf_pages)
        except Exception as e:
            print(f"DDD issue with {e}")

    def read_json(self):
        return self.metadata.read_json()

    @classmethod
    def get_isbn(cls, http_url):
        http_url = http_url.strip("/")
        return http_url[http_url.rfind("/") + 1 :]

    @property
    def get_epub_path(self):
        download_engine_books_path = self.config_map.get_download_engine_books_path
        isbn = self.isbn
        epub_suffix = MetaBook.epub_suffix
        return self.persist_fs.get_epub_path(
            download_engine_books_path, isbn, epub_suffix
        )

    def write_pdf(self, fn):
        self.persist_fs.write_pdf(fn, self.path_pdf)

    def write_splitter_pdf(self, fn, split_pdf_pages):
        self.persist_fs.write_splitter_pdf(fn, split_pdf_pages)
