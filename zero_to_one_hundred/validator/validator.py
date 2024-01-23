import traceback
from zero_to_one_hundred.exceptions.errors import NotURLFormatError


class Validator:
    @classmethod
    def is_valid_http(cls, url: str):
        if not url.startswith("https://"):
            raise NotURLFormatError(f"{url} not valid")

    @classmethod
    def print_DDD(cls, e: Exception):
        print(traceback.format_exc())
        print(f"DDD issue with {e}")
