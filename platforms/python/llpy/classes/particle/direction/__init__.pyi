from typing import NoReturn

from ..types import (
    T_PosDirection_NEG_X,
    T_PosDirection_NEG_Y,
    T_PosDirection_NEG_Z,
    T_PosDirection_POS_X,
    T_PosDirection_POS_Y,
    T_PosDirection_POS_Z,
)

class Direction:
    """粒子生成器方向枚举"""

    def __init__(self) -> NoReturn: ...

    NEG_Y: T_PosDirection_NEG_Y
    """粒子方向枚举 | -Y"""
    POS_Y: T_PosDirection_POS_Y
    """粒子方向枚举 | +Y"""
    NEG_Z: T_PosDirection_NEG_Z
    """粒子方向枚举 | -Z"""
    POS_Z: T_PosDirection_POS_Z
    """粒子方向枚举 | +Z"""
    NEG_X: T_PosDirection_NEG_X
    """粒子方向枚举 | -X"""
    POS_X: T_PosDirection_POS_X
    """粒子方向枚举 | +X"""
