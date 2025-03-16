from typing import NoReturn

from llpy import LLSE_Container, LLSE_Entity, LLSE_Item, LLSE_Player

from ..stdstring import NativeStdString

class NativePointer:
    """原生指针 API"""

    def __init__(self) -> NoReturn: ...
    @property
    def byte(self) -> str:
        """
        读取 byte

        此属性读写通过十六进制字符串完成
        """
    @byte.setter
    def byte(self, val: str): ...
    @property
    def int8(self) -> int:
        """读取 int8"""
    @int8.setter
    def int8(self, val: int): ...
    @property
    def uint8(self) -> int:
        """读取 uint8"""
    @uint8.setter
    def uint8(self, val: int): ...
    @property
    def int16(self) -> int:
        """读取 int16"""
    @int16.setter
    def int16(self, val: int): ...
    @property
    def uint16(self) -> int:
        """读取 uint16"""
    @uint16.setter
    def uint16(self, val: int): ...
    @property
    def int32(self) -> int:
        """读取 int32"""
    @int32.setter
    def int32(self, val: int): ...
    @property
    def uint32(self) -> int:
        """读取 uint32"""
    @uint32.setter
    def uint32(self, val: int): ...
    @property
    def long(self) -> int:
        """读取 long"""
    @long.setter
    def long(self, val: int): ...
    @property
    def ulong(self) -> int:
        """读取 ulong"""
    @ulong.setter
    def ulong(self, val: int): ...
    @property
    def int64(self) -> int:
        """读取 int64"""
    @int64.setter
    def int64(self, val: int): ...
    @property
    def uint64(self) -> int:
        """读取 uint64"""
    @uint64.setter
    def uint64(self, val: int): ...
    @property
    def float(self) -> float:
        """读取 float"""
    @float.setter
    def float(self, val: float): ...
    @property
    def double(self) -> float:
        """读取 double"""
    @double.setter
    def double(self, val: float): ...
    @property
    def string(self) -> str:
        """
        读取 string

        此属性表示 `std::string*`
        """
    @string.setter
    def string(self, val: str): ...
    @property
    def bool(self) -> bool:
        """读取 bool"""
    @bool.setter
    def bool(self, val: bool): ...
    @staticmethod
    def fromSymbol(symbol: str) -> NativePointer:
        """
        获得符号地址

        获得一个 MCAPI 符号地址，等同于 CPP 中 `dlsym`

        Args:
            symbol: 需要查询的符号

        Returns:
            查询结果，若查询失败则返回空指针
        """
    @staticmethod
    def fromAddress(address: str | int) -> NativePointer:
        """
        获得地址实例

        获得一个指定地址的指针实例

        Args:
            address: 地址，以 16进制字符串 或 数字 表示

        Returns:
            对应地址的指针实例
        """
    @staticmethod
    def malloc(size: int) -> NativePointer:
        """
        内存申请

        此函数帮助申请一块指定大小内存

        Args:
            size: 欲申请的内存的大小

        Returns:
            指向新内存的指针
        """
    @staticmethod
    def free(block: NativePointer) -> None:
        """
        销毁内存

        销毁一个指定内存块

        Args:
            block: 需要销毁的内存块
        """
    def asRawAddress(self) -> int:
        """
        获得指针地址

        Returns:
            以数字形式表示的指针所指地址
        """
    def asHexAddress(self) -> str:
        """
        获得指针地址描述

        获取原始指针地址（16 进制字符串）

        Returns:
            以十六进制形式表示的指针所指地址
        """
    def offset(self, offset: int) -> NativePointer:
        """
        指针偏移

        获取相对某个指针偏移后的地址

        Args:
            offset: 偏移

        Returns:
            偏移后指针
        """
    def asRef(self) -> NativePointer: ...
    def deRef(self) -> NativePointer: ...
    def isNull(self) -> bool: ...
    def asStdString(self) -> NativeStdString: ...
    def asEntity(self) -> LLSE_Entity: ...
    def asItem(self) -> LLSE_Item: ...
    def asPlayer(self) -> LLSE_Player: ...
    def asContainer(self) -> LLSE_Container: ...
