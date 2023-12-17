from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs


def test_list_dirs(get_resource_path):
    actual = persist_fs.list_dirs(get_resource_path)
    print(actual)
