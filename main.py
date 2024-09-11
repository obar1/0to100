#!/usr/bin/env python3
# coding: utf-8

import sys
import logging

from zero_to_one_hundred.runner import run_core

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    err_msg = f'zt or sb available, passed {str(sys.argv)}'
    try:
        arg1= sys.argv[1]
        match arg1:
            case 'zt':
                from zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
                from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS as persist_fs
                from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as process_fs
                run_core(sys.argv, ZTOHFactoryProvider(persist_fs, process_fs))
            case 'sb':
                from zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider
                from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as persist_fs
                from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as process_fs
                run_core(sys.argv, SBFactoryProvider(persist_fs, process_fs))
            case _:
                raise ValueError(err_msg)
    except Exception as  e:
        logging.info(err_msg)

