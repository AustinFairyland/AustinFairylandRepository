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
from fairyland.framework.utils.generals import DefaultDataUtils
from fairyland.framework.utils.generals import DatetimeUtils
from fairyland.framework.utils.publish import PackageInfo
from fairyland.framework.utils.generals import DecodingUtils


class Test:

    @classmethod
    def run(cls) -> None:
        cls.test_1()
        cls.test_2()
        cls.test_3()
        cls.test_4()
        cls.test_5()
        return

    @classmethod
    def test_1(cls):
        class DatetimeEnum(BaseEnum):
            data = {"a": 1}

        Journal.debug(f"测试枚举继承方法: {DatetimeEnum.values()}")

    @classmethod
    def test_2(cls):
        Journal.debug(f"日期时间格式化枚举值: {DateTimeFormatEnumModule.values()}")

    @classmethod
    def test_3(cls):
        Journal.debug(f"当前时间时间戳: {DatetimeUtils.normtimestamp()}")
        a = DefaultDataUtils.data_dict()
        a.update(测试时间=DatetimeUtils.normdatetime_to_str())
        Journal.debug(f"测试字典: {a}")

    @classmethod
    def test_4(cls):
        Journal.debug(f"包名: {PackageInfo.name}")
        Journal.debug(f"版本号: {PackageInfo.version}")

    @classmethod
    def test_5(cls):
        b_str = b"\xd3\xd0\xb9\xd8\xc4\xb3\xb8\xf6\xc3\xfc\xc1\xee\xb5\xc4\xcf\xea\xcf\xb8\xd0\xc5\xcf\xa2\xa3\xac\xc7\xeb\xbc\xfc\xc8\xeb HELP \xc3\xfc\xc1\xee\xc3\xfb\r\nASSOC"
        a = DecodingUtils.decode_binary_string(b_str, encodings=["UTF-8", "gb18030", "big5"])
        Journal.debug(f"解码: {a}")

if __name__ == "__main__":
    Test.run()
