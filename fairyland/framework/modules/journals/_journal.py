# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 02 29, 2024
"""
import os
import sys
from loguru import logger


class Journal:
    """Log Module"""

    logger.remove()
    logger.add(
        sink=os.path.normpath("logs/services.log"),
        rotation="10 MB",
        retention="60 days",
        # format="[{time:YYYY-MM-DD HH:mm:ss} | {elapsed} | {level:<8}]: {message}",
        format="[{time:YYYY-MM-DD HH:mm:ss} | {level:<8}]: {message}",
        compression="gz",
        encoding="utf-8",
        # level: TRACE, DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL
        level="INFO",
        enqueue=True,
        colorize=True,
        backtrace=True,
    )
    logger.add(
        sink=sys.stdout,
        format="[<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level:<8}</level>]: {message}",
        level="TRACE",
        colorize=True,
    )
    __logs = logger
    __logs.critical(
        """

                                 _____       _               _                    _     _____        _                      
                                |  ___|__ _ (_) _ __  _   _ | |  __ _  _ __    __| |   |  ___|_   _ | |_  _   _  _ __  ___  
                                | |_  / _` || || '__|| | | || | / _` || '_ \  / _` |   | |_  | | | || __|| | | || '__|/ _ \ 
                                |  _|| (_| || || |   | |_| || || (_| || | | || (_| |   |  _| | |_| || |_ | |_| || |  |  __/ 
                                |_|   \__,_||_||_|    \__, ||_| \__,_||_| |_| \__,_|   |_|    \__,_| \__| \__,_||_|   \___| 
                                                      |___/                                                                 
"""
    )

    @classmethod
    def trace(cls, msg, *args, **kwargs) -> None:
        """
        Inherits the trace method from loguru.
        @param msg: Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.trace
        """
        return cls.__logs.trace(msg, *args, **kwargs)

    @classmethod
    def debug(cls, msg, *args, **kwargs) -> None:
        """
        Inherits the debug method from loguru.logger
        @param msg: Debug Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.debug
        :rtype: object
        """
        return cls.__logs.debug(msg, *args, **kwargs)

    @classmethod
    def info(cls, msg, *args, **kwargs) -> None:
        """
        Inherits the info method from loguru.
        @param msg: Info Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.info
        :rtype: object
        """
        return cls.__logs.info(msg, *args, **kwargs)

    @classmethod
    def success(cls, msg, *args, **kwargs) -> None:
        """
        Inherits the success method from loguru.
        @param msg: Success Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.success
        """
        return cls.__logs.success(msg, *args, **kwargs)

    @classmethod
    def warning(cls, msg, *args, **kwargs) -> None:
        """
        Inherits the warning method from loguru.
        @param msg: Warning Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.warning
        """
        return cls.__logs.warning(msg, *args, **kwargs)

    @classmethod
    def error(cls, msg, *args, **kwargs) -> None:
        """
        Inherits the error method from loguru.
        @param msg: Error Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.error
        """
        return cls.__logs.error(msg, *args, **kwargs)

    @classmethod
    def critical(cls, msg, *args, **kwargs) -> None:
        """
        Inherits the critical method from loguru.
        @param msg: Critical Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.critical
        """
        return cls.__logs.critical(msg, *args, **kwargs)

    @classmethod
    def exception(cls, msg, *args, **kwargs) -> None:
        """
        Inherits the exception method from loguru.
        @param msg: Exception Log messages: String
        @param args: Tuple
        @param kwargs: Dict
        @return: loguru.logger.exception
        """
        return cls.__logs.exception(msg, *args, **kwargs)
