# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from pprint import pprint

from models.uml import UML
from models.section import Section
from repository.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs
from configs.config import ConfigMap


def test_reorganize_as_tree(get_config_map: ConfigMap, get_repo_path: str):
    sections = [
        Section.build_from_dir(persist_fs, process_fs, get_config_map, dir_)
        for dir_ in persist_fs.list_dirs(get_repo_path)
        if dir_ is not None
    ]
    actual = list(UML.reorganize_as_tree(sections, UML.NODE_LEVEL_SYMBOL))
    pprint((actual))
