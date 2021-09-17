"""MAIN:
"""
# pylint: disable=R0903,E0401,W0703,W1201

import logging
import sys

from typing import List

from factories.factory_provider import FactoryProvider
from factories.ztoh_factory import ZTOHFactory
from repository.persist_fs import PersistFS


def run_main(argv: List[str]):
    """run main section"""
    factory: ZTOHFactory = FactoryProvider(PersistFS).provide()
    return factory.get_processor(argv).process()

if __name__ == "__main__":
    try:
        logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
        run_main(sys.argv[1:])
    except IndexError:
        logging.info(f"check the params {sys.argv}")