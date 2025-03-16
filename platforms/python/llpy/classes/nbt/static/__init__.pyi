from typing import Any, NoReturn

from typing_extensions import deprecated

from llpy import NbtCompound

from ..types import (
    T_NbtClass,
    T_NbtType,
    T_NbtTypeByte,
    T_NbtTypeByteArray,
    T_NbtTypeCompound,
    T_NbtTypeDouble,
    T_NbtTypeEnd,
    T_NbtTypeFloat,
    T_NbtTypeInt,
    T_NbtTypeList,
    T_NbtTypeLong,
    T_NbtTypeShort,
    T_NbtTypeString,
)

class NBT:
    """NBT API"""

    End: T_NbtTypeEnd
    """NBT 类型枚举 | 用于标记标签的结尾"""
    Byte: T_NbtTypeByte
    """NBT 类型枚举 | 有符号字节 或 布尔值（8 位）"""
    Short: T_NbtTypeShort
    """NBT 类型枚举 | 有符号短整型（16 位）"""
    Int: T_NbtTypeInt
    """NBT 类型枚举 | 有符号整形（32位）"""
    Long: T_NbtTypeLong
    """NBT 类型枚举 | 有符号长整型（64位）"""
    Float: T_NbtTypeFloat
    """NBT 类型枚举 | 单精度浮点数"""
    Double: T_NbtTypeDouble
    """NBT 类型枚举 | 双精度浮点数"""
    ByteArray: T_NbtTypeByteArray
    """NBT 类型枚举 | 字节数组"""
    String: T_NbtTypeString
    """NBT 类型枚举 | UTF-8 字符串"""
    List: T_NbtTypeList
    """NBT 类型枚举 | NBT 列表（类似于 数组）"""
    Compound: T_NbtTypeCompound
    """NBT 类型枚举 | NBT 标签（类似于 键值对列表）"""

    def __init__(self) -> NoReturn: ...
    @staticmethod
    def parseSNBT(snbt: str) -> NbtCompound | None:
        """
        从 SNBT 字符串生成 NBT 标签对象

        Args:
            snbt: 你要解析的 SNBT 字符串。必须包含一个完整的 Compound

        Returns:
            生成的NBT对象。如返回值为 `None` 则表示解析失败
        """
    @staticmethod
    def parseBinaryNBT(nbt: bytearray) -> NbtCompound | None:
        """
        从二进制 NBT 数据生成 NBT 标签对象

        Args:
            nbt: 你要解析的二进制 NBT 数据

        Returns:
            生成的NBT对象。如返回值为 `None` 则表示解析失败
        """
    @deprecated("请使用各 NBT 对象的构造函数")
    @staticmethod
    def createTag(
        nbt_type: T_NbtType,
        default: Any,
    ) -> T_NbtClass | None: ...
    @staticmethod
    @deprecated("请使用各 NBT 对象的构造函数")
    def newTag(
        nbt_type: T_NbtType,
        default: Any,
    ) -> T_NbtClass | None: ...
