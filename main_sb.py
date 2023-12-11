"""MAIN:
main
"""


import logging
import sys
from typing import List
from zero_to_one_hundred.factories.sb_factory import SBFactory
from zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as persist_fs
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as process_fs


def run_main(argv: List[str]):
    try:
        factory: SBFactory = SBFactoryProvider(persist_fs, process_fs).provide()
        [p.process() for p in factory.get_processor(argv) if p]

    except AssertionError:
        logging.error("set env for MAP_YAML_PATH with map.yaml path")
    except IndexError:
        logging.critical(f"check the params {sys.argv}")
    except ModuleNotFoundError:
        logging.critical("??? have you installed all the dep")
    except (ValueError, TypeError):
        logging.debug("help")
        return factory.help_processor().process()


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
    run_main(sys.argv)
