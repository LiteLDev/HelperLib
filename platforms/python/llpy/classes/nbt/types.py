from typing import Literal

from .base import (
    NbtByte,
    NbtByteArray,
    NbtDouble,
    NbtEnd,
    NbtFloat,
    NbtInt,
    NbtLong,
    NbtShort,
    NbtString,
)
from .compound import NbtCompound
from .list import NbtList

T_NbtTypeEnd = Literal[0]
T_NbtTypeByte = Literal[1]
T_NbtTypeShort = Literal[2]
T_NbtTypeInt = Literal[3]
T_NbtTypeLong = Literal[4]
T_NbtTypeFloat = Literal[5]
T_NbtTypeDouble = Literal[6]
T_NbtTypeByteArray = Literal[7]
T_NbtTypeString = Literal[8]
T_NbtTypeList = Literal[9]
T_NbtTypeCompound = Literal[10]
T_NbtType = (
    T_NbtTypeEnd
    | T_NbtTypeByte
    | T_NbtTypeShort
    | T_NbtTypeInt
    | T_NbtTypeLong
    | T_NbtTypeFloat
    | T_NbtTypeDouble
    | T_NbtTypeByteArray
    | T_NbtTypeString
    | T_NbtTypeList
    | T_NbtTypeCompound
)

T_NbtBaseClass = (
    NbtEnd
    | NbtByte
    | NbtShort
    | NbtInt
    | NbtLong
    | NbtFloat
    | NbtDouble
    | NbtByteArray
    | NbtString
)
T_NbtClass = T_NbtBaseClass | NbtCompound | NbtList

T_ToNbtBase = int | float | str | bytearray | None
T_ToNbtList = list["T_ToNbtType"]
T_ToNbtDict = dict[str, "T_ToNbtType"]
T_ToNbtType = T_ToNbtBase | T_ToNbtList | T_ToNbtDict
