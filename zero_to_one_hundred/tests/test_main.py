"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401


def test_version(get_root):
    expected = "0.0.3"
    with open(get_root + "/../../version", mode="r", encoding="UTF-8") as file_handle:
        assert file_handle.read().lower().strip("\n") == expected
