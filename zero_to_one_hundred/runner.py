# pylint: disable=W0106,R1710

from subprocess import CalledProcessError
import traceback
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

    except AssertionError:
        print("please, check the code")
    except FileNotFoundError:
        print("please, set env for MAP_YAML_PATH with map.yaml path")
    except (NotImplementedError, UnsupportedConfigMapError, CalledProcessError):
        print("please, check MAP_YAML_PATH env var contents")
    except ModuleNotFoundError:
        print("DDD have you installed all the dep")
    except (ValueError, TypeError, IndexError):
        traceback.print_exc()
    finally:
        factory.help_processor().process()
