# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from pprint import pprint

from models.puml import PUML
from models.section import Section
from tests.moke.persist_fs import PersistFS as persist_fs
from tests.moke.process_fs import ProcessFS as process_fs

def test_reorganize_as_tree(get_config_map, dir_tree):
    sections = [
        Section.build_from_dir(get_config_map, persist_fs,process_fs,dir_)
        for dir_ in persist_fs.list_dirs(dir_tree)
        if dir_ is not None
    ]
    actual = PUML.reorganize_as_tree(sections)
    pprint(actual)


def test_render_as_pum_tree(get_config_map, dir_tree):
    sections = [
        Section.build_from_dir(get_config_map, persist_fs,process_fs,dir_)
        for dir_ in persist_fs.list_dirs(dir_tree)
        if dir_ is not None
    ]
    http_url_rows = PUML.reorganize_as_tree(sections)
    actual = PUML.render_as_pum_tree(http_url_rows, PUML.S, PUML.NODE_LEVEL_SYMBOL)
    pprint(list(actual))
