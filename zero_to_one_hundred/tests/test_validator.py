"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
import pytest

from tests.moke.persist_fs import PersistFS
from validator.validator import Validator

def test_build_full_path__pass__fail(get_resource_path):
    # abs path
    assert Validator(PersistFS.relative_path_starts_with, "/somepath", None) \
               .build_full_path == "/somepath"
    # relative path
    assert Validator(PersistFS.relative_path_starts_with, get_resource_path, None) \
               .build_full_path == get_resource_path


def test_is_valid_http__pass__fail():
    # pass
    assert Validator(PersistFS.relative_path_starts_with, None, None) \
               .is_valid_http("https://code.google") == "https://code.google"
    # fail
    with pytest.raises(AssertionError):
        assert Validator(PersistFS.relative_path_starts_with, None, None) \
            .is_valid_http("code.google")
