# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging

from repository.persist_fs import PersistFS as persist_fs


def test_list_dirs(get_repo_path):
    actual = persist_fs.list_dirs(get_repo_path)
    logging.info(actual)
