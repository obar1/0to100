"""Main ingestion execution methods.

Each of the factories methods does create
its own cloud function functionality.

"""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
import logging
import sys

from exceptions.section_value_error import SectionValueError
from factories.factory_provider import FactoryProvider


def run_section(argv):
    for arg in argv[1:]:
        logging.info(arg)
    factory = FactoryProvider(argv).provide()
    return factory.create_section_processor().process()


logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

if __name__ == "__main__":

    try:
        run_section(sys.argv)
    except SectionValueError as e:
        logging.error(e)
    except Exception as exp:
        logging.critical(exp)
