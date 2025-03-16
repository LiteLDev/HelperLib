from typing import TypedDict


class T_TimeObj(TypedDict):
    """`system.getTimeObj()` 获取到的时间对象"""

    Y: int
    """年份数值（4位）"""
    M: int
    """月份数值"""
    D: int
    """天数数值"""
    h: int
    """小时数值（24小时制）"""
    m: int
    """分钟数值"""
    s: int
    """秒数值"""
    ms: int
    """毫秒数值"""
