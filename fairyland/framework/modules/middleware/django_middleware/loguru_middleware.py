# coding: utf8
""" 
@File: loguru_middleware.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-01-28
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

from typing import Union, Any, Callable
from types import FunctionType, MethodType
from django.http.request import HttpRequest
from django.http.response import HttpResponse
import traceback

from fairyland.framework.modules.journal import Journal


class DjangoLoguruMiddleware:
    def __init__(self, function: Union[FunctionType, MethodType]):
        self.__function = function

    def __call__(self, request: HttpRequest, *args: Any, **kwargs: Any):
        Journal.info(f"Request: {request.path}")
        response: HttpResponse = self.__function(request, *args, **kwargs)
        Journal.info(f"Response status code: {response.status_code}")
        return response

    def process_exception(self, request, exception):
        Journal.error(f"Unhandled exception: {exception}\n{traceback.format_exc()}")
