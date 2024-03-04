# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 02 29, 2024
"""
from ._journal import JournalSingleton
from ._journal import logger

journal: JournalSingleton = JournalSingleton()
