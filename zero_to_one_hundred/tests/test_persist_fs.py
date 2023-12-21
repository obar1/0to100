from zero_to_one_hundred.tests.moke import persist_fs_fake


def test_list_dirs(get_resource_path):
    actual = persist_fs_fake.PersistFSFake.list_dirs(get_resource_path)
    print(actual)
