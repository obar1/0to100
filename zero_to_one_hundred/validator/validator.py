import logging
import traceback
import re


from zero_to_one_hundred.exceptions.errors import NotURLFormatError


class Validator:
    @classmethod
    def is_valid_http(cls, url: str):
        pattern = r"^[^https?:\/\/].*"
        if re.match(pattern, url) is not None:
            raise NotURLFormatError(f"{url} not valid")

    @classmethod
    def print_e(cls, e: Exception):
        logging.exception(traceback.format_exc())
        logging.exception(f"#DDD issue with {e}")
