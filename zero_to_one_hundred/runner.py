# pylint: disable=W0106,R1710

from typing import List

from zero_to_one_hundred.exceptions.errors import UnsupportedConfigMapError
from zero_to_one_hundred.factories.factory_provider import FactoryProvider


def run_core(argv: List[str], factory_provider: FactoryProvider):
    """given params and factory provider it runs the core logic

    Args:
        argv (List[str]): args from cmd line
        factory_provider (AFactoryProvider): a factory_type

    """
    try:
        factory = factory_provider.provide()
        assert factory is not None
        [processor.process() for processor in factory.get_processor(argv) if processor]

    except AssertionError:
        print("check the code")
    except FileNotFoundError:
        print("set env for MAP_YAML_PATH with map.yaml path")
    except (NotImplementedError, UnsupportedConfigMapError):
        print("check MAP_YAML_PATH env var contents")
    except ModuleNotFoundError:
        print("??? have you installed all the dep")
    except (ValueError, TypeError, IndexError):
        print("help")
        return factory.help_processor().process()
