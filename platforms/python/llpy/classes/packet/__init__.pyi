from typing import NoReturn

from llpy import FloatPos, NativePointer
from llpy.classes.nbt.compound import NbtCompound

class LLSE_Packet:
    """数据包对象"""

    def __init__(self) -> NoReturn: ...
    def asPointer(self) -> NativePointer: ...
    def getName(self) -> str: ...
    def getId(self) -> int: ...

Packet = LLSE_Packet

class BinaryStream:
    """二进制流对象"""

    def __init__(self) -> None:
        """创建一个二进制流对象"""
    def reset(self) -> bool:
        """
        重置二进制流

        Returns:
            是否成功
        """
    def reserve(self, size: int) -> bool:
        """
        给二进制流分配空间

        Args:
            size: 分配的字节数

        Returns:
            是否成功
        """
    def writeBool(self, value: bool) -> bool:
        """
        向二进制流写入 布尔值

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeByte(self, value: int) -> bool:
        """
        向二进制流写入 字节

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeDouble(self, value: float) -> bool:
        """
        向二进制流写入 双精度浮点

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeFloat(self, value: float) -> bool:
        """
        向二进制流写入 单精度浮点

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeSignedBigEndianInt(self, value: int) -> bool:
        """
        向二进制流写入 大端格式 有符号 整数

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeSignedInt(self, value: int) -> bool:
        """
        向二进制流写入 有符号 整数

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeSignedInt64(self, value: int) -> bool:
        """
        向二进制流写入 有符号 长整数

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeSignedShort(self, value: int) -> bool:
        """
        向二进制流写入 有符号 短整数

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeString(self, value: str) -> bool:
        """
        向二进制流写入 字符串

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeUnsignedChar(self, value: int) -> bool:
        """
        向二进制流写入 无符号 字符

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeUnsignedInt(self, value: int) -> bool:
        """
        向二进制流写入 无符号 整数

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeUnsignedInt64(self, value: int) -> bool:
        """
        向二进制流写入 无符号 长整数

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeUnsignedShort(self, value: int) -> bool:
        """
        向二进制流写入 无符号 短整数

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeUnsignedVarInt(self, value: int) -> bool:
        """
        向二进制流写入 无符号 变长 整数

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeUnsignedVarInt64(self, value: int) -> bool:
        """
        向二进制流写入 无符号 变长 长整数

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeVarInt(self, value: int) -> bool:
        """
        向二进制流写入 变长 整数

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeVarInt64(self, value: int) -> bool:
        """
        向二进制流写入 变长 长整数

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeVec3(self, value: FloatPos) -> bool:
        """
        向二进制流写入 三维向量（坐标）

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def writeCompoundTag(self, value: NbtCompound) -> bool:
        """
        向二进制流写入 NBT 标签

        Args:
            value: 写入的数据

        Returns:
            是否成功
        """
    def createPacket(self, pkt_id: int) -> LLSE_Packet:
        """
        通过二进制流构建数据包

        Args:
            pkt_id: 数据包 ID

        Returns:
            数据包对象
        """
    def getData(self) -> str: ...
