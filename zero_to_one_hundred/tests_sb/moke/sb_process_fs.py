"""ProcessFS:
deal with Process
mocked in Test
"""

import logging

from zero_to_one_hundred.repository.sb_process_fs import (
    SBProcessFS as _SBProcessFS,
)


class SBProcessFS(_SBProcessFS):
    """Process_fs."""

    @classmethod
    def write_img(cls, dir_img, http_url_img):
        logging.info(f"write_img  {dir_img} {http_url_img}")

    @classmethod
    def write_epub(cls, config_map, dir_epub, isbn):
        logging.info(f"write_epub {config_map} {dir_epub} {isbn}")

    @staticmethod
    def get_now():
        return "2021/01/01-00:00:00"
