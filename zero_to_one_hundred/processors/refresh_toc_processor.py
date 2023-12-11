"""RefreshMapProcessor:
refresh meta_books in map
"""


from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.models.toc import Toc


class RefreshTocProcessor:
    """RefreshMapProcessor"""

    def __init__(self, config_map: SBConfigMap, persist_fs, process_fs):
        """init"""
        self.config_map = config_map
        self.persist_fs = persist_fs
        self.process_fs = process_fs

    def process(self):
        """Scan the repo and for each meta_book add it to  the map, save the toc file."""
        dirs = self.persist_fs.list_dirs(self.config_map.get_books_path)
        valid_dirs = [dir_ for dir_ in dirs if MetaBook.is_valid_ebook_path(dir_)]
        meta_books = Toc.build_from_dirs(
            self.config_map, self.persist_fs, self.process_fs, valid_dirs
        )
        toc: Toc = Toc(self.config_map, self.persist_fs, self.process_fs, meta_books)
        toc.write()