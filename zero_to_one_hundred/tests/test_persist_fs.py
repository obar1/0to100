import logging

from typing import List

from repository.persist_fs import PersistFS
from tests.conftest import get_sample_readme_md_path


def test_list_dirs( get_repo_path):
    actual = PersistFS.list_dirs(get_repo_path)
    logging.warning(actual)


def test_read_file(get_sample_readme_md_path):
    actual: List[str] = PersistFS.read_file(get_sample_readme_md_path)
    logging.warning(actual)





