from typing import NoReturn

from ..pointer import NativePointer

class NativePatch:
    """补丁工具"""

    def __init__(self) -> NoReturn: ...
    @staticmethod
    def search(pattern: str) -> NativePointer:
        """
        PatternSearch 搜索

        在全局范围内搜索指定 Bytes 并获得第一个结果地址

        Args:
            pattern: 描述匹配模式的字符串

        Returns:
            结果地址
        """
    @staticmethod
    def patch(pointer: NativePointer, expect: str, target: str) -> bool:
        """
        Patch 应用补丁

        对指定位置进行 Patch 操作

        Args:
            pointer: 目标地址
            expect: 原始字节
            target: 目标字节

        Returns:
            成功结果
        """
    @staticmethod
    def dump(pointer: NativePointer, size: int) -> str:
        """
        Dump 展示内存

        以十六进制字符串展示目标地址的指定长度内存

        Args:
            pointer: 目标地址
            size: 长度

        Returns:
            内存内容
        """
