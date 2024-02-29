# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 02 29, 2024
"""


class NoneDataUtils:
    """NoneDataUtils"""

    @staticmethod
    def api_results():
        results = {"status": "failure", "code": 500, "data": None}
        return results

    @staticmethod
    def data_string():
        results = str()
        return results

    @staticmethod
    def data_integer():
        results = int()
        return results

    @staticmethod
    def data_float():
        results = float()
        return results

    @staticmethod
    def data_boolean():
        results = bool()
        return results

    @staticmethod
    def data_list():
        results = []
        return results

    @staticmethod
    def data_tuple():
        results = ()
        return results

    @staticmethod
    def data_set():
        results = set()
        return results

    @staticmethod
    def data_dict():
        results = {}
        return results

    @staticmethod
    def data_none():
        return None

    @staticmethod
    def data_byte():
        results = bytes()
        return results

    @staticmethod
    def data_bytearray():
        results = bytearray()
        return results

    @staticmethod
    def data_complex():
        results = complex()
        return results
