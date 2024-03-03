# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 02 29, 2024
"""
from typing import Any

from fairyland.framework.core.abstracts.enumerate import StringEnum


class DateTimeFormatEnumModule(StringEnum):
    """Format Datetime Enum Module"""

    date = "%Y-%m-%d"
    time = "%H:%M:%S"
    datetime = "%Y-%m-%d %H:%M:%S"

    date_CN = "%Y年%m月%d日"
    time_CN = "%H时%M分%S秒"
    datetime_CN = "%Y年%m月%d日 %H时%M分%S秒"

    @classmethod
    def default(cls) -> str:
        return cls.datetime.value
