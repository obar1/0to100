"""Main ingestion execution methods.

Each of the factories methods does create
its own cloud function functionality.

"""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401

from factories.factory_provider import FactoryProvider


def run_section():
    """TODO."""
    factory = FactoryProvider().provide()
    return factory.create_section_processor().process()


if __name__ == "__main__":
    run_section()
