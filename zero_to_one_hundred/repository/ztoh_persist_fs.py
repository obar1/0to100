# pylint: disable=W0108
import logging
import os
import time

from zero_to_one_hundred.repository.a_persist_fs import APersistFS


class ZTOHPersistFS(APersistFS):
    """ZTOHPersistFS:
    deal with FS
    """

    @classmethod
    def done_section(cls, path):
        path = cls.abs_path(path)
        logging.info(f"done_section {path}")
        path = path + os.sep + ".done"
        logging.info(f"path {path}")
        os.makedirs(path, 0o777, True)
        with open("{}/.gitkeep".format(path), "a", encoding="utf-8"):
            os.utime("{}/.gitkeep".format(path), None)
        logging.info(f"created {path}")

    @classmethod
    def done_section_status(cls, abs_repo_path, path):
        logging.info(f"done_section_status {path}")
        path = abs_repo_path + os.sep + path + os.sep + ".done"
        logging.info(f"path {path}")
        exists = os.path.exists(path)
        if exists:
            return True
        return False

    @classmethod
    def get_biz_ts(cls, path):
        logging.info(f"path {path}")
        exists = os.path.exists(path)

        if exists:
            res = os.path.getmtime(path)
            return res
        return time.time()
