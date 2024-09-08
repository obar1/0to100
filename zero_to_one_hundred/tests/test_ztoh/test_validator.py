"""Unit tests."""

import pytest

from zero_to_one_hundred.exceptions.errors import NotURLFormatError
from zero_to_one_hundred.validator.validator import Validator


def test_is_valid_http_pass0():
    assert Validator.is_valid_http("https" + "://code.google") is None


def test_is_valid_http_pass1():
    assert Validator.is_valid_http("http" + "://www.cloudskillsboost.google/") is None


def test_is_valid_http_fail():
    with pytest.raises(NotURLFormatError):
        Validator.is_valid_http("code.google")
