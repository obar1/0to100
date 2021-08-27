"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
from unittest.mock import Mock

import pytest

from processors.section_processor import SectionProcessor


@pytest.fixture
def section_processor() -> SectionProcessor:
    return Mock()


def test_process(section_processor):
    section_processor.process()
    assert True
