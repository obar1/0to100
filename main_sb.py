#!/usr/bin/env python3
# coding: utf-8

import sys
from zero_to_one_hundred.factories.sb_factory_provider import SBFactoryProvider
from zero_to_one_hundred.repository.sb_persist_fs import SBPersistFS as persist_fs
from zero_to_one_hundred.repository.sb_process_fs import SBProcessFS as process_fs
from zero_to_one_hundred.runner import run_core

if __name__ == "__main__":
    run_core(sys.argv, SBFactoryProvider(persist_fs, process_fs))
