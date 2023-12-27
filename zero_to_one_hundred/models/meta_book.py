import re


from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.metadata import Metadata


class MetaBook:
    epub_suffix = ".epub"
    HTTP_OREILLY = "https://learning.oreilly.com/library/cover"
    GENERIC_HTTP_OREILLY = "https://learning.oreilly.com/library/"

    def __init__(self, config_map: SBConfigMap, persist_fs, process_fs, http_url: str):
        self.config_map = config_map
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.metadata = Metadata(
            MetaBook.get_isbn,
            self.config_map,
            self.persist_fs,
            self.process_fs,
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
    def build_from_dir(cls, config_map, persist_fs, process_fs, dir_name):
        return MetaBook(
            config_map,
            persist_fs,
            process_fs,
            http_url=cls.GENERIC_HTTP_OREILLY + "/" + dir_name,
        )

    def write_img(self):
        self.process_fs.write_img(self.path_img, f"{self.HTTP_OREILLY}/{self.isbn}/")

    def write_epub(self):
        self.process_fs.write_epub(self.config_map, self.path_epub, self.isbn)
        self.persist_fs.copy_file_to(self.get_epub_path(), self.path_epub)

    def write_json(self):
        self.metadata.write_json()

    @classmethod
    def is_valid_ebook_path(cls, ebook_folder):
        """check folder is 0123..9 like ISBN"""
        return re.match(r"^[0-9]+", ebook_folder)

    def write(self):
        self.persist_fs.make_dirs(self.contents_path)
        self.metadata.write_json()
        self.write_img()
        self.write_epub()
        self.write_pdf(self.path_epub)
        self.write_splitter_pdf(self.path_pdf, self.config_map.get_split_pdf_pages)

    def read_json(self):
        self.metadata.read_json()

    @classmethod
    def get_isbn(cls, http_url):
        http_url = http_url.strip("/")
        return http_url[http_url.rfind("/") + 1 :]

    def get_epub_path(self):
        download_engine_books_path = self.config_map.get_download_engine_books_path
        isbn = self.isbn
        epub_suffix = MetaBook.epub_suffix
        return self.persist_fs.get_epub_path(
            download_engine_books_path, isbn, epub_suffix
        )

    def write_pdf(self, fn):
        self.persist_fs(fn)

    def write_splitter_pdf(self, fn, split_pdf_pages):
        self.write_splitter_pdf(fn, split_pdf_pages)
