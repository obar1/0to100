"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
import pytest

from validator.validator import is_path, is_valid_http


def test_is_path():
    assert is_path("/somepath") == "/somepath"
    with pytest.raises(AssertionError):
        assert is_path("somepath")


def test_is_http():
    assert is_valid_http("https://code.google") == "https://code.google"
    with pytest.raises(AssertionError):
        assert is_valid_http("code.google")
