# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 02 29, 2024
"""
import sys

sys.dont_write_bytecode = True

from fairyland.framework.modules.journals import Journal
from fairyland.framework.core.abstracts.enumerate import BaseEnum
from fairyland.framework.modules.generals import DateTimeFormatEnumModule
from fairyland.framework.modules.exceptions import ProjectError
from fairyland.framework.utils.generals import NoneDataUtils
from fairyland.framework.utils.generals import DatetimeUtils
from fairyland.framework.utils.publish import PackageInfo


class DatetimeEnum(BaseEnum):
    data = {"a": 1}


class Test:

    @classmethod
    def run(cls) -> None:
        return

    @classmethod
    def test_1(cls) -> None:
        print(DatetimeEnum.values())
        return

    @classmethod
    def test_2(cls):
        Journal.debug(DateTimeFormatEnumModule.values())

    @classmethod
    def test_3(cls):
        Journal.debug(DatetimeUtils.normtimestamp())
        a = NoneDataUtils.data_dict()
        a.update(AA="11")
        Journal.debug(f"a = {a}")

    @classmethod
    def test_4(cls):
        Journal.debug(PackageInfo.name)
        Journal.debug(PackageInfo.version)


if __name__ == "__main__":
    Test.run()
    Test.test_1()
    Test.test_2()
    Test.test_3()
    Test.test_4()
