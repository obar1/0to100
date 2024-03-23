# pylint: disable=W0106,R1710

import traceback
from subprocess import CalledProcessError
from typing import List

from zero_to_one_hundred.exceptions.errors import UnsupportedConfigMapError
from zero_to_one_hundred.factories.a_factory import AFactory
from zero_to_one_hundred.factories.a_factory_provider import AFactoryProvider


def run_core(argv: List[str], factory_provider: AFactoryProvider):
    """given params and factory provider it runs the core logic

    Args:
        argv (List[str]): args from cmd line
        factory_provider (AFactoryProvider): a factory_type

    """
    factory: AFactory = None
    try:
        factory = factory_provider.provide()
        assert factory is not None
        [processor.process() for processor in factory.get_processor(argv) if processor]

    except ModuleNotFoundError:
        print("Please cheek if have you installed all the dep")
        traceback.print_exc()
    except (NotImplementedError, UnsupportedConfigMapError, CalledProcessError):
        print("Please check MAP_YAML_PATH env var contents")
        traceback.print_exc()
    except AssertionError:
        print("Please check the below")
        traceback.print_exc()
    except:
        traceback.print_exc()
        factory.help_processor().process()
