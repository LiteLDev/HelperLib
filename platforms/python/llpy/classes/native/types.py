from typing import Literal

T_NativeTypeVoid = Literal[0]
T_NativeTypeBool = Literal[1]
T_NativeTypeChar = Literal[2]
T_NativeTypeUnsignedChar = Literal[3]
T_NativeTypeShort = Literal[4]
T_NativeTypeUnsignedShort = Literal[5]
T_NativeTypeInt = Literal[6]
T_NativeTypeUnsignedInt = Literal[7]
T_NativeTypeLong = Literal[8]
T_NativeTypeUnsignedLong = Literal[9]
T_NativeTypeLongLong = Literal[10]
T_NativeTypeUnsignedLongLong = Literal[11]
T_NativeTypeFloat = Literal[12]
T_NativeTypeDouble = Literal[13]
T_NativeTypePointer = Literal[14]
T_NativeType = (
    T_NativeTypeVoid
    | T_NativeTypeBool
    | T_NativeTypeChar
    | T_NativeTypeUnsignedChar
    | T_NativeTypeShort
    | T_NativeTypeUnsignedShort
    | T_NativeTypeInt
    | T_NativeTypeUnsignedInt
    | T_NativeTypeLong
    | T_NativeTypeUnsignedLong
    | T_NativeTypeLongLong
    | T_NativeTypeUnsignedLongLong
    | T_NativeTypeFloat
    | T_NativeTypeDouble
    | T_NativeTypePointer
)
