from typing import Any, Callable, NoReturn

from ..hook import NativeHook
from ..pointer import NativePointer
from ..types import T_NativeType

class NativeFunction:
    """原生函数 API"""

    def __init__(self) -> NoReturn: ...
    @staticmethod
    def fromSymbol(symbol: str) -> NativeFunction:
        """
        Symbol 获得函数

        自动解析 Symbol 并得到一个可调用的函数，如解析失败，抛出异常

        Args:
            symbol: 需要解析的函数

        Returns:
            原生函数实例
        """
    @staticmethod
    def fromDescription(
        return_value: T_NativeType,
        *params: T_NativeType,
    ) -> NativeFunction:
        """
        Describe 获得函数

        描述函数类型并得到一个不可调用的函数，如需调用，则还需手动设置 `address` 属性

        Args:
            return_value: 返回值类型
            *params: 参数类型

        Returns:
            原生函数实例
        """
    @staticmethod
    def fromScript(
        return_value: T_NativeType,
        *params: T_NativeType,
        callback: Callable[..., Any],
    ) -> NativeFunction:
        """
        Script 获得函数

        描述函数类型并得到一个来自脚本的函数，其被包装为可直接在本机代码中调用的函数

        Args:
            return_value: 返回值类型
            *params: 参数类型
            callback: 回调函数，当该原生包装函数被调用后，会调用此函数

        Returns:
            原生函数实例
        """
    def hook(self, function: Callable[..., Any]) -> NativeHook:
        """
        Hook 函数钩子

        改写指定地址函数的头部，设置回调函数，当原函数调用时则会调用回调函数

        如果需要保留原始功能，请记得在回调函数内调用原函数

        Args:
            function:  回调函数，请注意保持参数类型与 `NativeFunction` 描述的一致

        Returns:
            原函数
        """
    @property
    def call(self) -> Callable[..., Any]:
        """
        Call 功能

        通过虚拟对象 call，调用对应函数

        Returns:
            对应函数

        Return Function Args:
            *params: 对应 NativeFunction 所描述的函数参数

        Return Function Returns:
            对应 NativeFunction 所描述的返回类型
        """
    @property
    def address(self) -> int:
        """函数指针的指针值"""
    @address.setter
    def address(self, val: NativePointer | int): ...
