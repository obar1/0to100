#!/usr/bin/env python3
# coding: utf-8

import sys
from typing import List

from zero_to_one_hundred.factories.ztoh_factory_provider import ZTOHFactoryProvider
from zero_to_one_hundred.repository.ztoh_persist_fs import ZTOHPersistFS as persist_fs
from zero_to_one_hundred.repository.ztoh_process_fs import ZTOHProcessFS as process_fs
from zero_to_one_hundred.runner import run_core


if __name__ == "__main__":
    run_core(sys.argv, ZTOHFactoryProvider(persist_fs, process_fs))
