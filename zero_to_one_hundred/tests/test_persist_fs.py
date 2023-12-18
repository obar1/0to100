from zero_to_one_hundred.tests.moke.persist_fs_fake import (
    PersistFSFake as persist_fs_fake,
)


def test_list_dirs(get_resource_path):
    actual = persist_fs_fake.list_dirs(get_resource_path)
    print(actual)
