"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
from unittest.mock import Mock

import pytest
from typing import List
from factories.ztoh_factory import ZTOHFactory
from processors.create_section_processor import CreateSectionProcessor
from processors.refresh_sections_processor import RefreshSectionsProcessor


@pytest.fixture
def get_create_section_ztoh_factory(config_loader,get_create_section_params) -> ZTOHFactory:
    return ZTOHFactory(config_loader,get_create_section_params)


@pytest.fixture
def get_refresh_sections_ztoh_factory(config_loader,get_refresh_sections_params) -> ZTOHFactory:
    return ZTOHFactory(config_loader,get_refresh_sections_params)


def test_get_processor(get_create_section_ztoh_factory,get_refresh_sections_ztoh_factory):
   assert(isinstance( get_create_section_ztoh_factory.get_processor(), CreateSectionProcessor))
   assert(isinstance(get_refresh_sections_ztoh_factory.get_processor(), RefreshSectionsProcessor))


def test_create_section_processor(get_create_section_ztoh_factory):
    assert get_create_section_ztoh_factory.create_section_processor()


def test_refresh_sections_processor(get_refresh_sections_ztoh_factory):
    assert get_refresh_sections_ztoh_factory.refresh_sections_processor()




