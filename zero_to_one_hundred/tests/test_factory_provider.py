"""Unit tests."""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
from unittest.mock import Mock

import pytest

from factories.factory_provider import FactoryProvider


@pytest.fixture
def factory_provider() -> FactoryProvider:
    return Mock()


def test_provide(factory_provider):
    factory_provider.provide()
    assert True
