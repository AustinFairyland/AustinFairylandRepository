# coding: utf8
""" 
@File: test.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-07
"""
from __future__ import annotations

import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import setuptools
import re

from fairyland.framework.utils.datetimes import DatetimeUtils
from fairyland.framework.modules.enumeration import DateTimeFormatEnum
from fairyland.framework.core.source.enumeration import ProjectEnum
from fairyland.framework.core.source.enumeration import PackageEnum

if __name__ == "__main__":
    print()
    for i in setuptools.find_packages():
        print(i)
    print(PackageEnum.release_version.value)
    print(PackageEnum.name.value)
