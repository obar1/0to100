"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
from unittest.mock import Mock

import pytest

from factories.ztoh_factory import ZTOHFactory


@pytest.fixture
def ztoh_factory() -> ZTOHFactory:
    return Mock()


def test_create_section_processor(ztoh_factory):
    assert ztoh_factory.create_section_processor() is not None
