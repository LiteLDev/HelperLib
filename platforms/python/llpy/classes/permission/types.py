from typing import TypedDict

from llpy.types import T_ToJsonDict


class T_PermInfo(TypedDict):
    """权限信息"""

    name: str
    """权限名称"""
    enabled: bool
    """是否启用"""
    extra: T_ToJsonDict | None
    """额外数据"""
