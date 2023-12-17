from zero_to_one_hundred.exceptions.errors import UnsupportedConfigMapError
from zero_to_one_hundred.configs.config import Config

SAFARI_BOOKS = "safari-books"
MAP_YAML_PATH = "MAP_YAML_PATH"


class SBConfigMap(Config):
    def __init__(self, map_yaml_path, persist_fs):
        super().__init__(map_yaml_path, persist_fs)
        self.is_valid_type(self.get_type, SAFARI_BOOKS)

    @property
    def get_books_path(self):
        return "."

    @property
    def get_download_engine_path(self):
        return self.load["configs"]["download_engine_path"]

    @property
    def get_download_engine_books_path(self):
        return self.load["configs"]["download_engine_books_path"]

    @property
    def get_oreilly_username(self):
        return self.load["configs"]["oreilly_username"]

    @property
    def get_oreilly_userpassword(self):
        return self.load["configs"]["oreilly_userpassword"]

    @staticmethod
    def is_valid_type(type_, safari_books_type):
        if type_ is None or type_ != safari_books_type:
            raise UnsupportedConfigMapError(f"the {type_} should be {SAFARI_BOOKS}")
