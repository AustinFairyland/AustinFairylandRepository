# coding: utf8
"""
@File: DataSourceInheritance.py
@Editor: PyCharm
@Author: Austin (From Chengdu, China) https://fairy.host
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

from typing import Union, Tuple, Optional
from abc import ABC, abstractmethod

from fairyland.framework.modules.journal import Journal

from fairyland.framework.modules.annotation import DataBaseSourceConnectionProtocol
from fairyland.framework.modules.annotation import DataBaseSourceCursorProtocol


class DataBaseSource(ABC):
    """DataBaseSource"""

    def __init__(self, drive: Optional[str] = None):
        """
        Initialize datasource info.
        """
        if not drive:
            raise 
        self.connection = self.__connect()
        self.cursor = self.__create_cursor()

    @abstractmethod
    def connect(self):
        """
        Initialize datasource connection.
        @return: Database Connect Object.
        @rtype: DataBase Object.
        """
        raise NotImplementedError

    def __connect(self) -> DataBaseSourceConnectionProtocol:
        """
        Initialize datasource connection.
        @return: Database Connect Object.
        @rtype: DataBase Object.
        """
        return self.connect()

    def __create_cursor(self) -> DataBaseSourceCursorProtocol:
        """
        Create the database cursor.
        @return: DataBase Cursor Object.
        @rtype: DataBase Cursor Object.
        """
        return self.connection.cursor()

    def __close_cursor(self) -> None:
        """
        Close the database cursor.
        @return: None
        @rtype: None
        """
        if self.cursor:
            self.cursor.close()
            self.cursor = None
            Journal.warning("Database has disconnected the cursor.")

    def __close_connect(self) -> None:
        """
        Close the database connection.
        @return: None
        @rtype: None
        """
        if self.connection:
            self.connection.close()
            self.connection = None
            Journal.warning("Database has been disconnected.")

    def __reconnect(self) -> None:
        """
        Reconnect to the database.
        @return: None
        @rtype: None
        """
        if self.connection and self.cursor:
            Journal.warning("The database and cursor are connected.")
        elif self.connection and not self.cursor:
            Journal.warning("Database is connected.")
            self.cursor = self.__create_cursor()
            Journal.warning("Database cursor has been reconnected.")
        else:
            self.connection = self.__connect()
            Journal.warning("Database has been reconnected.")
            self.cursor = self.__create_cursor()
            Journal.warning("Database cursor has been reconnected.")

    def __close(self) -> None:
        """
        Completely close the database connection and cursor.
        @return: None
        @rtype: None
        """
        if self.connection:
            self.__close_connect()
        if self.cursor:
            self.__close_cursor()
        Journal.warning("Database has been disconnected completely.")

    def close(self) -> None:
        """
        Close the database connection and cursor.
        @return: None
        @rtype: None
        """
        self.__close()

    def __trace_sql_statement(self, statement: str, parameters: Union[tuple, list, None]) -> str:
        """
        Generate and return a debug SQL statement with parameters.
        @param statement: SQL statement.
        @type statement: str
        @param parameters: SQL statement parameters.
        @type parameters: Union[tuple, list, None]
        @return: Debug information.
        @rtype: str
        """
        return f"SQL Statement -> {statement} | Parameters -> {parameters}"

    @abstractmethod
    def execute(self, statement: str, parameters: Union[str, tuple, list, None] = None) -> None:
        """
        Execute a SQL statement with optional parameters.
        @param statement: SQL statement to be executed.
        @type statement: str
        @param parameters: Parameters to be substituted into the SQL statement. Default is None.
        @type parameters: Union[str, tuple, list, None]
        @return: None
        @rtype: None
        """
        raise NotImplementedError

    def __operation(
        self,
        statements: Union[str, tuple, list, set],
        parameters: Union[tuple, list, dict, None] = None,
    ) -> Tuple:
        """
        Execute SQL operations.
        @param statements: SQL statement(s).
        @type statements: Union[str, tuple, list, set]
        @param parameters: SQL parameters.
        @type parameters: Union[tuple, list, dict, None]
        @return: Operation result.
        @rtype: Depends on the SQL operation
        """
        try:
            self.__reconnect()
            if isinstance(statements, str):
                Journal.trace(self.__trace_sql_statement(statements, parameters))
                self.execute(statement=statements, parameters=parameters)
                results = self.cursor.fetchall()
            elif isinstance(statements, (tuple, list, set)):
                results_list = []
                for sql_statements, statements_parameters in zip(statements, parameters):
                    Journal.trace(self.__trace_sql_statement(sql_statements, statements_parameters))
                    self.execute(statement=sql_statements, parameters=statements_parameters)
                    results_list.append(self.cursor.fetchall())
            else:
                raise TypeError("Wrong SQL statements type.")
            self.connection.commit()
        except Exception as error:
            Journal.warning("Failed to execute the rollback after an error occurred.")
            self.connection.rollback()
            Journal.error(f"Error occurred during SQL operation: {error}")
            raise
        finally:
            self.__close_cursor()
        return results if "results" in locals() else tuple(results_list)

    def operation(
        self,
        statements: Union[str, tuple, list, set],
        parameters: Union[tuple, list, dict, None] = None,
    ) -> Tuple:
        """
        Execute single or multiple SQL statements.
        @param statements: SQL statements or a set of statements.
        @type statements: Union[str, tuple, list, set]
        @param parameters: Parameters for the SQL statements(s).
        @type parameters: Union[tuple, list, dict, None]
        @return: Execution result.
        @rtype: Depends on the SQL operation
        """
        if not isinstance(statements, str) and isinstance(statements, (list, tuple, set)) and not parameters:
            parameters = tuple([None for _ in range(len(statements))])
        return self.__operation(statements=statements, parameters=parameters)
