from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.processors.a_processor import AProcessor
from zero_to_one_hundred.validator.validator import Validator
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as persist_fs
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as process_fs


class CreateMetaBookProcessor(AProcessor):
    """CreateMetaBookProcessor:
    create a new meta_book on fs from http address"""

    def __init__(self, config_map: SBConfigMap, persist_fs: persist_fs, http_url: str, process_fs:process_fs):
        Validator.is_valid_http(http_url)
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.process_fs = process_fs
        self.config_map = config_map

    def process(self):
        meta_book: MetaBook = MetaBook(
            self.config_map, self.persist_fs, self.process_fs, self.http_url
        )
        meta_book.write()
