import logging

from repository.persist_fs import PersistFS


def test_list_dirs(wip,get_config_map):
    actual = PersistFS.list_dirs(get_config_map.get_repo_path)
    logging.warning(actual)

