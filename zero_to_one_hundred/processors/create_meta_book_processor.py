"""CreateMetaBookProcessor:
create a new meta_book on fs from http address
"""


from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook


class CreateMetaBookProcessor:
    def __init__(self, config_map: SBConfigMap, persist_fs, http_url: str, process_fs):
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.config_map = config_map

    def process(self):
        meta_book: MetaBook = MetaBook(
            self.config_map, self.persist_fs, self.process_fs, self.http_url
        )
        meta_book.write()
