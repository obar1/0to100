#!/usr/bin/env python3
# coding: utf-8


import sys
from typing import List

from zero_to_one_hundred.factories.factory_provider import FactoryProvider
from zero_to_one_hundred.factories.ztoh_factory import ZTOHFactory
from zero_to_one_hundred.repository.persist_fs import PersistFS as persist_fs
from zero_to_one_hundred.repository.process_fs import ProcessFS as process_fs


def run_main(argv: List[str]):
    try:
        factory: ZTOHFactory = FactoryProvider(persist_fs, process_fs).provide()

        [p.process() for p in factory.get_processor(argv) if p]

    except AssertionError:
        print("set env for MAP_YAML_PATH with map.yaml path")
    except IndexError:
        print(f"check the params {sys.argv}")
    except ModuleNotFoundError:
        print("??? have you installed all the dep")
    except (ValueError, TypeError):
        print("help")
        return factory.help_processor().process()


if __name__ == "__main__":
    run_main(sys.argv)
