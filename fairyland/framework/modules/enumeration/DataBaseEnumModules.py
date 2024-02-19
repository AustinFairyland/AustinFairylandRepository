# coding: utf8
"""
@ File: DataBaseEnumModules.py
@ Editor: PyCharm
@ Author: Austin (From Chengdu.China) https://fairy.host
@ HomePage: https://github.com/AustinFairyland
@ OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@ CreatedTime: 2024/2/19
"""
from __future__ import annotations

import abc
import os
import sys
import warnings
import platform
import asyncio
from typing import Tuple

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fairyland.framework.core.inheritance.enumsource import StringEnum


class DataBaseSourceDrive(StringEnum):

    MySQL = "MySQL"
    PostgreSQL = "PostgreSQL"
