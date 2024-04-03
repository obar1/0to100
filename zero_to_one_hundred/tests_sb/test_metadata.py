from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.models.metadata import Metadata


def test_init(get_config_map, persist_fs, process_fs, http_url, isbn):
    actual = Metadata(
        get_config_map,
        persist_fs,
        process_fs,
        MetaBook.get_isbn,
        http_url,
    )
    assert str(actual.isbn).endswith(isbn)
    assert str(actual.http_url) == http_url
    assert actual.pages_tot == 0
    assert actual.page_curr == 0


def test_get_page_perc(get_config_map, persist_fs, process_fs, http_url):
    actual = Metadata(
        get_config_map,
        persist_fs,
        process_fs,
        MetaBook.get_isbn,
        http_url,
        99,
        999,
    )
    assert actual.get_page_perc == "9.9%"
