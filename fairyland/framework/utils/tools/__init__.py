# coding: utf8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 03 06, 2024
"""

from typing import TypeVar, Dict, Any, Optional

_TypeVariableTools = TypeVar("_TypeVariableTools", bound="VariableTools")


class VariableTools:

    @classmethod
    def get_var_name(cls, _var: Any, _vars: Dict[str, Any]) -> Optional[str]:
        """
        Get var name

        :param _var: var
        :type _var: ...
        :param _vars: locals() or globals()
        :type _vars: dict
        :return: var name
        :rtype: str
        """
        for var_name, var_value in _vars.items():
            if var_value is _var:
                return var_name

        return None
