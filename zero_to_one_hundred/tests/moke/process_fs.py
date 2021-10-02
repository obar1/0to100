"""ProcessFS:
deal with Process
mocked in Test
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from repository.process_fs import ProcessFS as _ProcessFS


class ProcessFS(_ProcessFS):
    """Process_fs."""

    @classmethod
    def write_img(cls, dir_img, http_url_img):
        logging.info(f"write_img  {dir_img} {http_url_img}")

    @classmethod
    def write_epub(cls, config_map, dir_epub, isbn):
        logging.info(f"write_epub  {dir_epub} {isbn}")
