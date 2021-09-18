# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,C0209,W1203,C0200,C0103
import logging
from typing import List

from repository.persist_fs import PersistFS as persist_fs


def test_list_dirs(get_repo_path):
    actual = persist_fs.list_dirs(get_repo_path)
    logging.warning(actual)


def test_read_file(get_sample_readme_md_path):
    actual: List[str] = persist_fs.read_file(get_sample_readme_md_path)
    logging.warning(actual)
