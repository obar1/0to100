from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.tests_sb.moke import sb_persist_fs_fake, sb_process_fs_fake


def test_init(get_map_yaml_path, http_url):
    actual = MetaBook(
        SBConfigMap(get_map_yaml_path, sb_persist_fs_fake.SBPersistFSFake),
        sb_persist_fs_fake.SBPersistFSFake,
        sb_process_fs_fake,
        http_url,
    )
    assert str(actual.isbn).endswith("9780135956977")
    assert str(actual.contents_path).endswith("9780135956977")
    assert str(actual.path_pdf).endswith("9780135956977/9780135956977.pdf")
    assert str(actual.path_epub).endswith("9780135956977/9780135956977.epub")
    assert str(actual.path_img).endswith("9780135956977/9780135956977.png")


def test_write(get_map_yaml_path, http_url):
    actual = MetaBook(
        SBConfigMap(get_map_yaml_path, sb_persist_fs_fake.SBPersistFSFake),
        sb_persist_fs_fake.SBPersistFSFake,
        sb_process_fs_fake,
        http_url,
    )
    print(actual)


def test_build_from_dir(get_map_yaml_path):
    assert (
        MetaBook.build_from_dir(
            SBConfigMap(get_map_yaml_path, sb_persist_fs_fake.SBPersistFSFake),
            sb_persist_fs_fake.SBPersistFSFake,
            sb_process_fs_fake,
            "./books/9780135956977",
        ).isbn
        == "9780135956977"
    )


def test_is_valid_ebook_path():
    dirs = ["0123456789", "books", "ABC"]
    actual = [dir_ for dir_ in dirs if MetaBook.is_valid_ebook_path(dir_)]
    assert actual == ["0123456789"]
