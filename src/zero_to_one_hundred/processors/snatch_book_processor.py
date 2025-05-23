from src.zero_to_one_hundred.configs.sb_config_map import (
    SBConfigMap,
)
from src.zero_to_one_hundred.models.meta_book import MetaBook
from src.zero_to_one_hundred.processors.a_processor import (
    AProcessor,
)
from src.zero_to_one_hundred.repository.sb_persist_fs import (
    SBPersistFS,
)
from src.zero_to_one_hundred.validator.validator import Validator


class SnatchBookProcessor(AProcessor):
    """SnatchBookProcessor:
    create a new meta_book on fs from http address"""

    def __init__(
        self,
        config_map: SBConfigMap,
        persist_fs: SBPersistFS,
        http_url: str,
    ):
        Validator.is_valid_http(http_url)
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.config_map = config_map

    def process(self):
        meta_book = MetaBook(self.config_map, self.persist_fs, self.http_url)
        meta_book.write()
