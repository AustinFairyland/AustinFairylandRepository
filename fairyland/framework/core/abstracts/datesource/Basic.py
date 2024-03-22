# coding: utf8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 03 04, 2024
"""

from abc import abstractmethod
from typing import Optional, Tuple, Union, List, Any

from fairyland.framework.constants.typing import TypeSQLConnection
from fairyland.framework.constants.typing import TypeSQLCursor
from fairyland.framework.modules.journals.Journal import journal


class DataSource:
    """
    Abstract/Base class for database connection and operation.
    """

    def __init__(self):
        self.__init_connect()

    @abstractmethod
    def connect(self):
        """
        Connect to the database.

        :return: ...
        :rtype: ...
        """
        raise NotImplementedError("The method 'connect' must be implemented in the subclass.")

    def __connect(self) -> TypeSQLConnection:
        """
        Connect to the database.

        :return: ...
        :rtype: ...
        """
        return self.connect()

    def __init_connect(self) -> None:
        """
        Initialize the database connection and cursor.

        :return: ...
        :rtype: ...
        """
        self.__connection: TypeSQLConnection = self.__connect()
        self.cursor: TypeSQLCursor = self.__connection.cursor()

    def __close_cursor(self) -> None:
        """
        Close the database cursor.

        :return: ...
        :rtype: ...
        """
        if self.cursor:
            self.cursor.close()
            self.cursor = None
            journal.warning("Database has disconnected the cursor.")

    def __close_connection(self) -> None:
        """
        Close the database connection.

        :return: ...
        :rtype: ...
        """
        self.__close_cursor()
        if self.__connection:
            self.__connection.close()
            self.__connection = None

    def __reconnect(self) -> None:
        """
        Reconnect the database and cursor.

        :return: ...
        :rtype: ...
        """
        if not self.__connection:
            self.__connection = self.__connect()
            journal.warning("Database has been reconnected.")

        if not self.cursor:
            self.cursor = self.__connection.cursor()
            journal.warning("Database cursor has been reconnected.")
        else:
            journal.warning("The database and cursor are already connected.")

    @abstractmethod
    def execute(self, query, params) -> None:
        """
        Execute the SQL query.
            MySQL: self.cursor.execute(query=query, args=params)

            PostgreSQL: self.cursor.execute(query=query, vars=params)

        :param query: query statement
        :type query: ...
        :param params: query parameters
        :type params: ...
        :return: None
        :rtype: ...
        """
        raise NotImplementedError("The method 'execute' must be implemented in the subclass.")

    def __operate(self, sqls: Union[str, List[str], Tuple[str, ...]], params: Optional[Tuple[str, ...]] = None) -> Tuple[Any, ...]:
        """
        Execute the SQL query and return the results.

        :param sqls: SQL statement
        :type sqls: str or list or tuple
        :param params: SQL parameters
        :type params: tuple
        :return: Query results
        :rtype: tuple
        """
        try:
            self.__reconnect()
            if isinstance(sqls, str):
                journal.trace(f"SQL >> {sqls} | Params: {params}")
                self.execute(query=sqls, params=params)
                results = self.cursor.fetchall()
            elif isinstance(sqls, (list, tuple)):
                tmp_list = []
                for sql, param in zip(sqls, params):
                    journal.trace(f"SQL >> {sql} | Params: {param}")
                    self.execute(query=sql, params=param)
                    tmp_list.append(self.cursor.fetchall())
                results = tuple(tmp_list)
            else:
                raise TypeError("Wrong SQL statements type.")

            self.__connection.commit()
        except Exception as error:
            journal.warning("Failed to execute the rollback after an error occurred.")
            self.__connection.rollback()
            journal.error(f"Error occurred during SQL operation: {error}")
            raise error
        finally:
            self.__close_cursor()

        return results

    def operate(self, query: Union[str, List[str], Tuple[str, ...]], params: Optional[Tuple[str, ...]] = None) -> Tuple[Any, ...]:
        """
        Execute the SQL query and return the results.

        :param query: SQL statement
        :type query: str or list or tuple
        :param params: SQL parameters
        :type params: tuple
        :return: Query results
        :rtype: tuple
        """
        return self.__operate(query, params)

    def close(self) -> None:
        """
        Close the database connection.

        :return: ...
        :rtype: ...
        """
        self.__close_connection()
