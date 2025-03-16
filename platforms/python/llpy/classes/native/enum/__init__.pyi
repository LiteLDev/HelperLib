from typing import NoReturn

from ..types import (
    T_NativeTypeBool,
    T_NativeTypeChar,
    T_NativeTypeDouble,
    T_NativeTypeFloat,
    T_NativeTypeInt,
    T_NativeTypeLong,
    T_NativeTypeLongLong,
    T_NativeTypePointer,
    T_NativeTypeShort,
    T_NativeTypeUnsignedChar,
    T_NativeTypeUnsignedInt,
    T_NativeTypeUnsignedLong,
    T_NativeTypeUnsignedLongLong,
    T_NativeTypeUnsignedShort,
    T_NativeTypeVoid,
)

class NativeTypes:
    """原生函数类型枚举"""

    def __init__(self) -> NoReturn: ...

    Void: T_NativeTypeVoid
    Bool: T_NativeTypeBool
    Char: T_NativeTypeChar
    UnsignedChar: T_NativeTypeUnsignedChar
    Short: T_NativeTypeShort
    UnsignedShort: T_NativeTypeUnsignedShort
    Int: T_NativeTypeInt
    UnsignedInt: T_NativeTypeUnsignedInt
    Long: T_NativeTypeLong
    UnsignedLong: T_NativeTypeUnsignedLong
    LongLong: T_NativeTypeLongLong
    UnsignedLongLong: T_NativeTypeUnsignedLongLong
    Float: T_NativeTypeFloat
    Double: T_NativeTypeDouble
    Pointer: T_NativeTypePointer
