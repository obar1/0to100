"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
import pytest

from validator.validator import get_abs_path, is_valid_http


def test_get_valid_abs_path_abs():
    assert get_abs_path("/somepath", None) == "/somepath"


def test_get_valid_abs_path_relative(get_repo_root):
    assert get_abs_path(".", get_repo_root) == get_repo_root


def test_is_http():
    assert is_valid_http("https://code.google") == "https://code.google"
    with pytest.raises(AssertionError):
        assert is_valid_http("code.google")

