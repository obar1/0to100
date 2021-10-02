"""Unit tests."""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import pytest

from tests.moke.persist_fs import PersistFS as persist_fs
from validator.validator import Validator


def test_is_valid_http__pass__fail():
    # pass
    assert (
        Validator(persist_fs.relative_path_starts_with, None, None).is_valid_http(
            "https://code.google"
        )
        == "https://code.google"
    )
    # fail
    with pytest.raises(AssertionError):
        assert Validator(
            persist_fs.relative_path_starts_with, None, None
        ).is_valid_http("code.google")
