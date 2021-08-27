"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
from unittest.mock import Mock

import pytest

from processors.create_section_processor import CreateSectionProcessor


@pytest.fixture
def section_processor() -> CreateSectionProcessor:
    return Mock()


def test_process(section_processor):
    section_processor.process()
    assert True
