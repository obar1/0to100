"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
import pytest

from validator.validator import is_path


def test_is_path():
    assert is_path("/somepath") == "/somepath"
    with pytest.raises(AssertionError):
        assert is_path("somepath") is False
