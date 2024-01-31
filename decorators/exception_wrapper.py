from typing import Callable
from typing import Optional
from typing import ParamSpec
from typing import Type
from typing import TypeVar


def log_exception(func_name: str, exc: Exception):
    import logging

    logging.error('Error in "%s" routine, details: %s', func_name, str(exc))


T = TypeVar('T')
P = ParamSpec('P')


def exception_catch(
    exception_range: tuple[Type[Exception], ...] = (Exception,),
    exception_value: Optional[T] = None,
    callback: Callable[[str, Exception], None] = log_exception,
) -> Callable[[Callable[P, Optional[T]]], Callable[P, Optional[T]]]:
    """
    Exception wrapper decorator with parameters

    :param exception_range: tuple with catch exception types
    :param exception_value: what should you return on raised exception. Default - None
    :param callback: exception callback, executed on fired exception.
                     Default exception callback - simple logging routine
    :return: decorated function
    """

    def args_wrapper(func: Callable[P, Optional[T]]) -> Callable[P, Optional[T]]:
        def wrapper(*args, **kwargs) -> Optional[T]:
            try:
                return func(*args, **kwargs)
            except exception_range as e:
                callback(func.__name__, e)
                return exception_value

        return wrapper

    return args_wrapper
