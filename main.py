#!/usr/bin/env python3
# coding: utf-8

import logging
import sys
from typing import List

from zero_to_one_hundred.src.zero_to_one_hundred.exceptions.errors import UnsupportedOptionError
from zero_to_one_hundred.src.zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider
from zero_to_one_hundred.src.zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
from zero_to_one_hundred.src.zero_to_one_hundred.validator.validator import Validator


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
                processor.process()
                
if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        args = sys.argv[1:]
        cmd , p1 , p2 = Validator.validate_args(args)
        match cmd:
            case 'zo':
                from zero_to_one_hundred.src.zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS as persist_fs
                from zero_to_one_hundred.src.zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as process_fs
                run_core(args[1:], ZTOHFactoryProvider(persist_fs, process_fs))
            case 'sb':
                from zero_to_one_hundred.src.zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as persist_fs
                from zero_to_one_hundred.src.zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as process_fs
                run_core(args[1:], SBFactoryProvider(persist_fs, process_fs))
            case _:
                raise ValueError
    except (ValueError,IndexError, TypeError,UnsupportedOptionError) as e:
        from zero_to_one_hundred.src.zero_to_one_hundred.repository.a_persist_fs import APersistFS as persist_fs
        from zero_to_one_hundred.src.zero_to_one_hundred.factories.a_factory_provider import AFactoryProvider
        run_core(sys.argv, AFactoryProvider(persist_fs))
    except Exception as e:
        Validator.print_e(e)
  

