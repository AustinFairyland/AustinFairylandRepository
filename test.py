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
import time
from datetime import date, datetime

from fairyland import framework
from fairyland.framework import core
from fairyland.framework import modules
from fairyland.framework import utils
from fairyland.web import djangoweb
from fairyland.framework.core import general
from fairyland.framework.core import inheritance
from fairyland.framework.core import instantiation
from fairyland.framework.core import source
from fairyland.framework.modules import abnormal
from fairyland.framework.utils import datetimes
from fairyland.framework.core.general import *
from fairyland.framework.core.inheritance import datasource
from fairyland.framework.core.inheritance import enumsource
from fairyland.framework.core.instantiation import datasource
from fairyland.framework.core.source import enumeration
from fairyland.framework.core.source import packaging
from fairyland.framework.core.inheritance.datasource import DataBaseSource
from fairyland.framework.core.inheritance.enumsource import BaseEnum
from fairyland.framework.core.inheritance.enumsource import StringEnum
from fairyland.framework.core.inheritance.enumsource import IntegerEnum
from fairyland.framework.core.instantiation.datasource import MySQLSource
from fairyland.framework.core.instantiation.datasource import PostgreSQLSource
from fairyland.framework.core.source.enumeration import ProjectEnum
from fairyland.framework.core.source.enumeration import PackageEnum
from fairyland.framework.core.source.packaging import InstallPackageSource
from fairyland.framework.modules.abnormal import ProjectError
from fairyland.framework.modules.abnormal import ParameterError
from fairyland.framework.modules.abnormal import DataSourceError
from fairyland.framework.modules.abnormal import ReadFileError
from fairyland.framework.modules.abnormal import SQLExecutionError
from fairyland.framework.modules.annotation import SQLConnectionType
from fairyland.framework.modules.annotation import SQLCursorType
from fairyland.framework.modules.decorators import MethodRunTimeDecorators
from fairyland.framework.modules.decorators import MethodTipsDecorators
from fairyland.framework.modules.enumeration import DateTimeFormatEnum
from fairyland.framework.modules.journal import Journal
from fairyland.framework.utils.datetimes import DateTimeUtils
from fairyland.framework.utils.general import DataTypeUtils
from fairyland.web.djangoweb import configuration
from fairyland.web.djangoweb import middleware
from fairyland.web.djangoweb.configuration import DjangoPublicConfiguration
from fairyland.web.djangoweb.middleware import DjangoLoguruMiddleware

if __name__ == "__main__":
    print()
    for i in setuptools.find_packages():
        print(i)

