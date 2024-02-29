# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 02 29, 2024
"""
from types import FunctionType, MethodType
from typing import Union, Any, Callable

import time

from fairyland.framework.modules.journals import Journal


class MethodRunTimeDecorators:
    """Methid runngin times"""

    def __new__(
        cls,
        function: Union[FunctionType, MethodType],
        *args: Any,
        **kwargs: Any,
    ) -> Callable[..., Any]:
        """
        Called when the decorators is applied to a function. Creates and returns a wrapper function.
        :param function: The function to be decorated.
        :type function: Union[FunctionType, MethodType]
        :param args: Positional arguments for the decorated function.
        :type args: Any
        :param kwargs: Keyword arguments for the decorated function.
        :type kwargs: Any
        :return: The wrapper function.
        :rtype: Callable[..., Any]
        """

        def warpper(*args: Any, **kwargs: Any) -> Any:
            """
            Wrapper function that logs the execution time of the decorated function.
            :param args: Positional arguments for the decorated function.
            :type args: Any
            :param kwargs: Keyword arguments for the decorated function.
            :type kwargs: Any
            :return: The return value of the decorated function.
            :rtype: Any
            """
            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            Journal.success(f"This method ran for {elapsed_time} seconds")
            return result

        return warpper


class MethodTipsDecorators:
    """Method tips"""

    def __init__(self, annotation: str = "A Method"):
        self.__annotation = annotation

    def __call__(
        self,
        function: Union[FunctionType, MethodType],
        *args: Any,
        **kwargs: Any,
    ) -> Callable[..., Any]:
        """
        The method decorators logic.
        :param function: The function to be decorated.
        :type function: Union[FunctionType, MethodType]
        :param args: Positional arguments for the decorated function.
        :type args: Any
        :param kwargs: Keyword arguments for the decorated function.
        :type kwargs: Any
        :return: The wrapper function.
        :rtype: Callable[..., Any]
        """

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Wrapper function that logs the execution status of the decorated function.
            :param args: Positional arguments for the decorated function.
            :type args: Any
            :param kwargs: Keyword arguments for the decorated function.
            :type kwargs: Any
            :return: The return value of the decorated function.
            :rtype: Any
            """
            try:
                Journal.debug(f"Action Running {self.__annotation}")
                results = function(*args, **kwargs)
                Journal.success(f"Success Running {self.__annotation}")
            except Exception as error:
                Journal.error(f"Failure Running {self.__annotation}")
                raise
            return results

        return wrapper
