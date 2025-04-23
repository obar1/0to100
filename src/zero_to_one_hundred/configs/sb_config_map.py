# pylint: disable=W0246

from src.zero_to_one_hundred.configs.a_config_map import AConfigMap
from src.zero_to_one_hundred.repository.sb_persist_fs import (
    SBPersistFS,
)

SAFARI_BOOKS_MAP = "safari-books-map"


class SBConfigMap(AConfigMap):
    """
    toc:
        path: "./0to100"
        fn_md: "toc_sb.md"
    """

    def __init__(self, persist_fs: SBPersistFS):
        super().__init__(persist_fs)

    @property
    def get_toc_path(self):
        return self.load["toc"]["path"]

    @property
    def get_toc_fn_md(self):
        return self.load["toc"]["fn_md"]
