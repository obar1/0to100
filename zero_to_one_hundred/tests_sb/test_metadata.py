import json
from zero_to_one_hundred.models.meta_book import MetaBook
from zero_to_one_hundred.models.metadata import Metadata
from zero_to_one_hundred.tests.conftest import str_relaxed

# pylint: disable=C0303


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


def test_get_page_perc(get_config_map, persist_fs, process_fs, http_url):
    actual = Metadata.get_page_perc({"page_curr": 99, "page_tot": 999})
    assert actual == "9.9%"

    actual = Metadata.get_page_perc({"page_curr": 0, "page_tot": 999})
    assert actual == "0.0%"
    actual = Metadata.get_page_perc({"page_curr": 1, "page_tot": 0})
    assert actual == "n/a"


def test_asMarkDown(get_config_map, persist_fs, process_fs, http_url, isbn):
    actual = Metadata(
        get_config_map,
        persist_fs,
        process_fs,
        MetaBook.get_isbn,
        http_url,
    )

    assert str_relaxed(actual.asMarkDown()) == str_relaxed(
        """
    {
        "isbn":"9780135956977",<br/>
        "pages_perc":"n/a",<br/>
        "url":"https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/"
    }
    """
    )
    # some rand values from json

    data = '{ "abc": "123", "def": "456"}'
    actual.metadata = json.loads(data)

    assert str_relaxed(actual.asMarkDown()) == str_relaxed(
        """
    {
        "abc": "123",<br/>
        "def": "456",<br/>
        "isbn":"9780135956977",<br/>
        "pages_perc":"n/a",<br/>
        "url":"https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/"
    }
    """
    )

    # calculate pages
    data = """ 
    {
        "abc": "123",
        "page_curr": 10,
        "page_tot": 100
    }
    """
    actual.metadata = json.loads(data)
    print(actual.asMarkDown())
    assert str_relaxed(actual.asMarkDown()) == str_relaxed(
        """
    {
        "abc": "123",  <br/>
        "isbn":"9780135956977",<br/>
        "page_curr": 10,<br/>
        "page_tot": 100,<br/>
        "pages_perc":"10.0%",<br/>
        "url":"https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/"
    }
    """
    )
