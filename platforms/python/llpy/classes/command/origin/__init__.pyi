from typing import NoReturn

from llpy import FloatPos, IntPos, LLSE_Entity, LLSE_Player, NbtCompound

from ..types import T_OriginType

class LLSE_CommandOrigin:
    """指令执行主体对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def type(self) -> T_OriginType:
        """类型"""
    @property
    def typeName(self) -> str:
        """类型名称"""
    @property
    def name(self) -> str:
        """名称"""
    @property
    def pos(self) -> FloatPos:
        """坐标"""
    @property
    def blockPos(self) -> IntPos:
        """方块坐标"""
    @property
    def entity(self) -> LLSE_Entity | None:
        """执行的实体"""
    @property
    def player(self) -> LLSE_Player | None:
        """执行的玩家"""
    def getNbt(self) -> NbtCompound: ...
    def toString(self) -> str: ...

CommandOrigin = LLSE_CommandOrigin
