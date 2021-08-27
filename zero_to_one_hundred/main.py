"""Main ingestion execution methods.

Each of the factories methods does create
its own cloud function functionality.

"""
# pylint: disable=redefined-outer-name,missing-function-docstring,E0401
import logging
import sys

from typing import List

from exceptions.section_value_error import SectionValueError
from factories.factory_provider import FactoryProvider


def run_main(argv:List[str]):
    """run main section"""
    factory = FactoryProvider(argv).provide()
    return factory.get_processor().process()



if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    run_main(sys.argv)


