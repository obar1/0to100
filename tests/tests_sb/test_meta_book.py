from zero_to_one_hundred.models.meta_book import MetaBook


# pylint: disable=W0613
def test_init(get_config_map, persist_fs, process_fs, http_oreilly_1):
    """
    test with
    "https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/"

    """
    actual = MetaBook(
        get_config_map,
        persist_fs,
        process_fs,
        http_oreilly_1,
    )
    assert actual.isbn == "9780135956977"
    assert actual.contents_path == "./0to100/9780135956977"
    assert actual.path_img == "./0to100/9780135956977/9780135956977.png"


def test_build_from_dir(get_config_map, persist_fs, process_fs):
    assert (
        MetaBook.build_from_dir(
            get_config_map,
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
