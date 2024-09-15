#!/usr/bin/env python3
# coding: utf-8

import logging
import sys

from zero_to_one_hundred.exceptions.errors import UnsupportedOptionError
from zero_to_one_hundred.runner import run_core
from zero_to_one_hundred.validator.validator import Validator

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        args = sys.argv[1:]
        cmd , p1 , p2 = Validator.validate_args(args)
        match cmd:
            case 'zo':
                from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS as persist_fs
                from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as process_fs
                from zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
                run_core(args[1:], ZTOHFactoryProvider(persist_fs, process_fs))
            case 'sb':
                from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as persist_fs
                from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as process_fs
                from zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider
                run_core(args[1:], SBFactoryProvider(persist_fs, process_fs))
            case _:
                raise ValueError
    except (ValueError,IndexError, TypeError,UnsupportedOptionError) as e:
        from zero_to_one_hundred.repository.a_persist_fs import APersistFS as persist_fs
        from zero_to_one_hundred.factories.a_factory_provider import AFactoryProvider
        run_core(sys.argv, AFactoryProvider(persist_fs))
    except Exception as e:
        Validator.print_e(e)
  

