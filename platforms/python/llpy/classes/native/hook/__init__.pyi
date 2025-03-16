from typing import Any, Callable, NoReturn

from ..pointer import NativePointer

class NativeHook:
    """函数钩子"""

    def __init__(self) -> NoReturn: ...
    @property
    def call(self) -> Callable[..., Any]:
        """
        Call 功能

        通过虚拟对象 call，调用对应函数

        Returns:
            对应函数

        Return Function Args:
            *params: 对应 NativeHook 所描述的函数参数

        Return Function Returns:
            对应 NativeHook 所描述的返回类型
        """
    @property
    def address(self) -> int:
        """函数指针的指针值"""
    @address.setter
    def address(self, val: NativePointer | int): ...
