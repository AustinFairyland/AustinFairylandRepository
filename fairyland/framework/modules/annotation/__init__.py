# coding: utf8
""" 
@File: __init__.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-02-06
"""
from __future__ import annotations

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from typing import List

from .TypeAnnotation import MySQLConnectionObject
from .TypeAnnotation import MySQLCursorObject
from .TypeAnnotation import PostgreSQLConnectionObject
from .TypeAnnotation import PostgreSQLCursorObject

from .TypeAnnotation import DataBaseSourceConnectionProtocol
from .TypeAnnotation import DataBaseSourceCursorProtocol

__all__: List = [
    "MySQLConnectionObject",
    "MySQLCursorObject",
    "PostgreSQLConnectionObject",
    "PostgreSQLCursorObject",
    "DataBaseSourceConnectionProtocol",
    "DataBaseSourceCursorProtocol",
]
