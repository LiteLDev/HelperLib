from typing import Generic, TypeVar, overload

from ..types import (
    T_NbtType,
    T_NbtTypeByte,
    T_NbtTypeByteArray,
    T_NbtTypeDouble,
    T_NbtTypeEnd,
    T_NbtTypeFloat,
    T_NbtTypeInt,
    T_NbtTypeLong,
    T_NbtTypeShort,
    T_NbtTypeString,
)

_T_PyType = TypeVar("_T_PyType")
_T_NbtType = TypeVar("_T_NbtType", bound=T_NbtType)

class _T_BaseNbt(Generic[_T_PyType, _T_NbtType]):
    @overload
    def __init__(self) -> None:
        """
        创建新的 NBT 数据对象

        如果创建失败，将抛出异常
        """
    @overload
    def __init__(self, default: _T_PyType) -> None:
        """
        创建新的 NBT 数据对象

        如果创建失败，将抛出异常

        Args:
            default: 初始数据
        """
    def set(self, data: _T_PyType) -> bool:
        """
        设置对象的数据

        Args:
            data: 要写入的数据

        Returns:
            是否成功写入
        """
    def get(self) -> _T_PyType:
        """
        读取对象的数据

        Returns:
            对象中储存的数据
        """
    def getType(self) -> _T_NbtType: ...
    def toString(self, indent: int = -1) -> str: ...

class NbtEnd(_T_BaseNbt[None, T_NbtTypeEnd]):
    """用于标记标签的结尾 NBT"""

class NbtByte(_T_BaseNbt[int, T_NbtTypeByte]):
    """有符号字节 或 布尔值（8 位）NBT"""

class NbtShort(_T_BaseNbt[int, T_NbtTypeShort]):
    """有符号短整型（16 位）NBT"""

class NbtInt(_T_BaseNbt[int, T_NbtTypeInt]):
    """有符号整形（32位）NBT"""

class NbtLong(_T_BaseNbt[int, T_NbtTypeLong]):
    """有符号长整型（64位）NBT"""

class NbtFloat(_T_BaseNbt[float, T_NbtTypeFloat]):
    """单精度浮点数 NBT"""

class NbtDouble(_T_BaseNbt[float, T_NbtTypeDouble]):
    """双精度浮点数 NBT"""

class NbtByteArray(_T_BaseNbt[bytearray, T_NbtTypeByteArray]):
    """字节数组 NBT"""

class NbtString(_T_BaseNbt[str, T_NbtTypeString]):
    """UTF-8 字符串 NBT"""
