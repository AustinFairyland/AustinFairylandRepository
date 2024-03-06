# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 03 05, 2024
"""
from typing import Optional, Dict

import requests


class Requests:

    @staticmethod
    def get(
        url: str,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        cookies: Optional[Dict[str, str]] = None,
        verify: bool = False,
        timeout: int = 10,
    ):
        if not params:
            params = dict()
        if not headers:
            headers = {"Content-Type": "application/json"}
        try:
            response = requests.request(
                method="GET",
                url=url,
                params=params,
                headers=headers,
                cookies=cookies,
                verify=verify,
                timeout=timeout,
            )
            if response.status_code == 200:
                try:
                    results = response.json()
                except Exception as error:
                    journal.error(error)
                    try:
                        results = response.text
                    except Exception as error:
                        journal.error(error)
                        raise Exception("Failed to parse response")
            else:
                results = response.text
        except Exception as error:
            journal.error(error)
            raise Exception("Failed to get response")

        return results
