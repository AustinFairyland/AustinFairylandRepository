# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 03 03, 2024
"""

from typing import Any

from fairyland.framework.utils.generals import DefaultConstantUtils


class SingletonPattern:

    def __init__(self, __cls):
        self.__cls = __cls
        self.__instance = DefaultConstantUtils.dict()

    def __call__(self, *args: Any, **kwargs: Any):
        if not self.__instance:
            self.__instance.update(__instance=self.__cls(*args, **kwargs))
            return self.__instance.get("__instance")
        else:
            return self.__instance.get("__instance")
