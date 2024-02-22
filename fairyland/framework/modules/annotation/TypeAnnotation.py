# coding: utf8
""" 
@File: TypeAnnotation.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-02-05
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

from typing import Union

import pymysql
import psycopg2

from pymysql.connections import Connection as MySQLConnectionObject
from pymysql.cursors import Cursor as MySQLCursorObject
from psycopg2.extensions import connection as PostgreSQLConnectionObject
from psycopg2.extensions import cursor as PostgreSQLCursorObject

SQLConnectionObject = Union[pymysql.connections.Connection, psycopg2.extensions.connection, ...]
SQLCursorObject = Union[pymysql.cursors.Cursor.close(), psycopg2.extensions.cursor, ...]

from typing import Protocol, overload, Any, Tuple, Optional, Union, List


class DataBaseSourceConnectionProtocol(Protocol):
    def cursor(self) -> DataBaseSourceCursorProtocol: ...

    def commit(self) -> Any: ...

    def close(self) -> None: ...


class DataBaseSourceCursorProtocol(Protocol):
    @overload
    def execute(self, query: str, args: Optional[Tuple[Any, ...]] = None) -> int: ...

    @overload
    def execute(self, query: str, vars: Optional[Tuple[Any, ...]] = None) -> int: ...

    def execute(self, *args: Any, **kwargs: Any) -> Any: ...

    def fetchall(self) -> Union[List[Any, ...], Tuple[Any, ...]]: ...

    def close(self) -> None: ...
