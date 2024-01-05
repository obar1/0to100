from zero_to_one_hundred.configs.sb_config_map import SBConfigMap
from zero_to_one_hundred.models.meta_book import MetaBook


# pylint: disable=W0613
def test_init(get_config_map, persist_fs, process_fs, http_url):
    actual = MetaBook(
        SBConfigMap(persist_fs),
        persist_fs,
        process_fs,
        http_url,
    )
    assert str(actual.isbn).endswith("9780135956977")
    assert str(actual.contents_path).endswith("9780135956977")
    assert str(actual.path_pdf).endswith("9780135956977/9780135956977.pdf")
    assert str(actual.path_epub).endswith("9780135956977/9780135956977.epub")
    assert str(actual.path_img).endswith("9780135956977/9780135956977.png")


def test_build_from_dir(get_config_map, persist_fs, process_fs):
    assert (
        MetaBook.build_from_dir(
            SBConfigMap(persist_fs),
            persist_fs,
            process_fs,
            "./books/9780135956977",
        ).isbn
        == "9780135956977"
    )


def test_is_valid_ebook_path():
    dirs = ["0123456789", "1234567890123", "books", "ABC"]
    actual = [d for d in dirs if MetaBook.is_valid_ebook_path(d)]
    assert actual == ["1234567890123"]
