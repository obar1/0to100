"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
from unittest.mock import Mock

import pytest

from processors.refresh_sections_processor import RefreshSectionsProcessor


@pytest.fixture
def section_processor(config_loader) -> RefreshSectionsProcessor:
    return RefreshSectionsProcessor(config_loader, Mock())


def test_refresh_sections_processor(section_processor):
    section_processor.process()

