# coding: utf8
""" 
@File: BasicInstantiation.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-10-12
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

from typing import Union, Tuple, Optional
import pymysql
import psycopg2
from pymysql.connections import Connection as MySQLConnection
from pymysql.cursors import Cursor as MySQLCursor
from psycopg2.extensions import connection as PostgreSQLConnection
from psycopg2.extensions import cursor as PostgreSQLCursor

from fairyland.framework.modules.journal import Journal


class MySQLSource:
    """MySQLSource"""

    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 3306,
        user: str = "root",
        password: Optional[str] = None,
        database: Optional[str] = None,
        charset: str = "utf8mb4",
        connect_timeout: int = 30,
    ):
        """
        Initialize datasource info.
        """
        self.host = host
        self.port = port
        self.user = user
        self.__password = password
        self.database = database
        self.charset = charset
        self.connect_timeout = connect_timeout
        self.__connection: Optional[MySQLConnection] = self.__connect()
        self.__cursor: Optional[MySQLCursor] = self.__connection.cursor()

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError
        self.__password = value

    def __connect(self) -> MySQLConnection:
        """
        Initialize datasource connection.
        @return: Database Connect Object.
        @rtype: DataBase Object.
        """
        try:
            connect = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.__password,
                database=self.database,
                charset=self.charset,
                connect_timeout=self.connect_timeout,
            )
        except Exception as error:
            Journal.error(error)
            raise
        return connect

    def __close_cursor(self) -> None:
        """
        Close the database cursor.
        @return: None
        @rtype: None
        """
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None
            Journal.warning("Database has disconnected the cursor.")

    def __close_connect(self) -> None:
        """
        Close the database connection.
        @return: None
        @rtype: None
        """
        if self.__connection:
            self.__connection.close()
            self.__connection = None
            Journal.warning("Database has been disconnected.")

    def __reconnect(self) -> None:
        """
        Reconnect to the database.
        @return: None
        @rtype: None
        """
        if self.__connection and self.__cursor:
            Journal.warning("The database and cursor are connected.")
        elif self.__connection and not self.__cursor:
            Journal.warning("Database is connected.")
            self.__cursor = self.__connection.cursor()
            Journal.warning("Database cursor has been reconnected.")
        else:
            self.__connection = self.__connect()
            Journal.warning("Database has been reconnected.")
            self.__cursor = self.__connection.cursor()
            Journal.warning("Database cursor has been reconnected.")

    def __close(self) -> None:
        """
        Completely close the database connection and cursor.
        @return: None
        @rtype: None
        """
        if self.__connection:
            self.__close_connect()
        if self.__cursor:
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

    def __execute(self, statement: str, parameters: Optional[str, tuple, list] = None) -> None:
        """
        Execute a SQL statement with optional parameters.
        @param statement: SQL statement to be executed.
        @type statement: str
        @param parameters: Parameters to be substituted into the SQL statement. Default is None.
        @type parameters: Union[str, tuple, list, None]
        @return: None
        @rtype: None
        """
        self.__cursor.execute(query=statement, args=parameters)

    def __operation(
        self,
        statements: Union[str, tuple, list, set],
        parameters: Optional[tuple, list, dict] = None,
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
                self.__execute(statement=statements, parameters=parameters)
                results = self.__cursor.fetchall()
            elif isinstance(statements, (tuple, list, set)):
                results_list = []
                for sql_statements, statements_parameters in zip(statements, parameters):
                    Journal.trace(self.__trace_sql_statement(sql_statements, statements_parameters))
                    self.__execute(statement=sql_statements, parameters=statements_parameters)
                    results_list.append(self.__cursor.fetchall())
            else:
                raise TypeError("Wrong SQL statements type.")
            self.__connection.commit()
        except Exception as error:
            Journal.warning("Failed to execute the rollback after an error occurred.")
            self.__connection.rollback()
            Journal.error(f"Error occurred during SQL operation: {error}")
            raise
        finally:
            self.__close_cursor()
        return results if "results" in locals() else tuple(results_list)

    def operation(
        self,
        statements: Union[str, tuple, list, set],
        parameters: Optional[tuple, list, dict] = None,
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


class PostgreSQLSource:
    """MySQLSource"""

    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 5432,
        user: str = "postgres",
        password: Optional[str] = None,
        database: Optional[str] = None,
    ):
        """
        Initialize datasource info.
        """
        self.host = host
        self.port = port
        self.user = user
        self.__password = password
        self.database = database
        self.__connection: Optional[PostgreSQLConnection] = self.__connect()
        self.__cursor: Optional[PostgreSQLCursor] = self.__connection.cursor()

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError
        self.__password = value

    def __connect(self) -> PostgreSQLConnection:
        """
        Initialize datasource connection.
        @return: Database Connect Object.
        @rtype: DataBase Object.
        """
        try:
            connect = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.__password,
                database=self.database,
            )
        except Exception as error:
            Journal.error(error)
            raise
        return connect

    def __close_cursor(self) -> None:
        """
        Close the database cursor.
        @return: None
        @rtype: None
        """
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None
            Journal.warning("Database has disconnected the cursor.")

    def __close_connect(self) -> None:
        """
        Close the database connection.
        @return: None
        @rtype: None
        """
        if self.__connection:
            self.__connection.close()
            self.__connection = None
            Journal.warning("Database has been disconnected.")

    def __reconnect(self) -> None:
        """
        Reconnect to the database.
        @return: None
        @rtype: None
        """
        if self.__connection and self.__cursor:
            Journal.warning("The database and cursor are connected.")
        elif self.__connection and not self.__cursor:
            Journal.warning("Database is connected.")
            self.__cursor = self.__connection.cursor()
            Journal.warning("Database cursor has been reconnected.")
        else:
            self.__connection = self.__connect()
            Journal.warning("Database has been reconnected.")
            self.__cursor = self.__connection.cursor()
            Journal.warning("Database cursor has been reconnected.")

    def __close(self) -> None:
        """
        Completely close the database connection and cursor.
        @return: None
        @rtype: None
        """
        if self.__connection:
            self.__close_connect()
        if self.__cursor:
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

    def __execute(self, statement: str, parameters: Optional[str, tuple, list] = None) -> None:
        """
        Execute a SQL statement with optional parameters.
        @param statement: SQL statement to be executed.
        @type statement: str
        @param parameters: Parameters to be substituted into the SQL statement. Default is None.
        @type parameters: Union[str, tuple, list, None]
        @return: None
        @rtype: None
        """
        self.__cursor.execute(query=statement, vars=parameters)

    def __operation(
        self,
        statements: Union[str, tuple, list, set],
        parameters: Optional[tuple, list, dict] = None,
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
                self.__execute(statement=statements, parameters=parameters)
                results = self.__cursor.fetchall()
            elif isinstance(statements, (tuple, list, set)):
                results_list = []
                for sql_statements, statements_parameters in zip(statements, parameters):
                    Journal.trace(self.__trace_sql_statement(sql_statements, statements_parameters))
                    self.__execute(statement=sql_statements, parameters=statements_parameters)
                    results_list.append(self.__cursor.fetchall())
            else:
                raise TypeError("Wrong SQL statements type.")
            self.__connection.commit()
        except Exception as error:
            Journal.warning("Failed to execute the rollback after an error occurred.")
            self.__connection.rollback()
            Journal.error(f"Error occurred during SQL operation: {error}")
            raise
        finally:
            self.__close_cursor()
        return results if "results" in locals() else tuple(results_list)

    def operation(
        self,
        statements: Union[str, tuple, list, set],
        parameters: Optional[tuple, list, dict] = None,
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
