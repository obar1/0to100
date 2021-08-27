"""Main ingestion execution methods.

Each of the factories methods does create
its own cloud function functionality.

"""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401

from factories.factory_provider import FactoryProvider


def run_section(args):
    """TODO."""
    factory = FactoryProvider(args).provide()
    return factory.create_section_processor().process()


if __name__ == "__main__":
    import sys

    for arg in sys.argv[1:]:
        print(arg)
    run_section(args=sys.argv)
