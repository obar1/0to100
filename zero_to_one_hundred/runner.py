# pylint: disable=W0106,R1710
from typing import List

from zero_to_one_hundred.exceptions.errors import SomeError
from zero_to_one_hundred.factories.a_factory import AFactory
from zero_to_one_hundred.factories.a_factory_provider import AFactoryProvider
from zero_to_one_hundred.validator.validator import Validator


def run_core(argv: List[str], factory_provider: AFactoryProvider):
    """given params and factory provider it runs the core logic

    Args:
        argv (List[str]): args from cmd line
        factory_provider (AFactoryProvider): a factory_type

    """
    factory: AFactory
    try:
        factory = factory_provider.provide()
        [processor.process() for processor in factory.get_processor(argv) if processor]
    except SomeError as e:
        Validator.print_DDD(e)
        return
    except FileNotFoundError as e:
        Validator.print_DDD(e)
        return
    except Exception as e:
        Validator.print_DDD(e)
        factory.help_processor().process()
