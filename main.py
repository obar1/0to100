#!/usr/bin/env python3
# coding: utf-8

import sys
from typing import List
from src.zero_to_one_hundred.exceptions.errors import UnsupportedOptionError
from src.zero_to_one_hundred.factories.a_factory_provider import AFactoryProvider
from src.zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider
from src.zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
from src.zero_to_one_hundred.validator.validator import Validator
from loguru import logger as logging


def run_core(argv: List[str], factory_provider: AFactoryProvider):
    """given params and factory provider it runs the core logic

    Args:
        argv (List[str]): args from cmd line
        factory_provider (AFactoryProvider): a factory_type

    """

    factory = factory_provider.provide()
    if factory:
        for processor in factory.get_processor(argv):
            if processor:
                logging.warning(f"processor {processor.__class__.__name__} argv {argv}")
                processor.process()


if __name__ == "__main__":
    logging.remove()
    logging.add(sys.stderr, level="WARNING")
    try:
        args = sys.argv[1:]
        cmd, p1, p2 = Validator.validate_args(args)
        match cmd:
            case "zo":
                from src.zero_to_one_hundred.repository.ztoh_persist_fs import (
                    ZTOHPersistFS as persist_fs,
                )

                run_core(args[1:], ZTOHFactoryProvider(persist_fs))
            case "sb":
                from src.zero_to_one_hundred.repository.sb_persist_fs import (
                    SBPersistFS as persist_fs,
                )

                run_core(args[1:], SBFactoryProvider(persist_fs))
            case _:
                raise ValueError(f"args = {args}")
    except (ValueError, IndexError, TypeError, UnsupportedOptionError):
        from src.zero_to_one_hundred.repository.a_persist_fs import (
            APersistFS as persist_fs,
        )

        run_core(sys.argv, AFactoryProvider(persist_fs))
    except Exception as e:
        Validator.print_e(e)