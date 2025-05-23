from src.zero_to_one_hundred.configs.sb_config_map import (
    SBConfigMap,
)
from src.zero_to_one_hundred.models.meta_book import MetaBook
from src.zero_to_one_hundred.models.toc import Toc
from src.zero_to_one_hundred.processors.a_processor import (
    AProcessor,
)


class RefreshTocProcessor(AProcessor):
    """RefreshMapProcessor:
    refresh meta_books in map"""

    def __init__(self, config_map: SBConfigMap, persist_fs):
        self.config_map = config_map
        self.persist_fs = persist_fs

    def process(self):
        """Scan the repo and for each meta_book add it to  the map, save the toc file."""
        dirs = self.persist_fs.list_dirs(self.config_map.get_toc_path)
        valid_ebook_folders = [
            ebook_folder
            for ebook_folder in dirs
            if MetaBook.is_valid_ebook_path(ebook_folder)
        ]
        meta_books = Toc.build_from_dirs(
            self.config_map, self.persist_fs, valid_ebook_folders
        )
        toc = Toc(self.config_map, self.persist_fs, meta_books)
        toc.write()
