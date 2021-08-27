"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401

from zero_to_one_hundred import __version__


def test_version():
    assert __version__ == "0.0.2"
