from typing import Any, Callable, Literal, overload

from ..types import (
    T_WSClientStatus,
    T_WSClientStatusClosed,
    T_WSClientStatusClosing,
    T_WSClientStatusOpen,
)

class WSClient:
    """WebSocket 客户端对象 API"""

    Open: T_WSClientStatusOpen
    """连接状态枚举 | 处于正常连接中"""
    Closing: T_WSClientStatusClosing
    """连接状态枚举 | 正在断开连接"""
    Closed: T_WSClientStatusClosed
    """连接状态枚举 | 未连接"""

    def __init__(self) -> None:
        """创建一个新的 WebSocket 客户端对象"""
    @property
    def status(self) -> T_WSClientStatus:
        """当前的连接状态（`WSClient.Open` / `WSClient.Closing` / `WSClient.Closed`）"""
    def connect(self, target: str) -> bool:
        """
        创建连接

        Args:
            target: 要连接的目标地址，形如 `ws://hostname[:port][/path/path][?query=value]`

        Returns:
            是否成功连接
        """
    def connectAsync(self, target: str, callback: Callable[[bool], Any]) -> bool:
        """
        异步创建连接

        Callback Args:
            success (bool): WebSocket 连接是否成功

        Args:
            target: 要连接的目标地址，形如 `ws://hostname[:port][/path/path][?query=value]`
            callback: 当连接成功或者失败时执行的回调函数

        Returns:
            是否成功开始尝试连接
        """
    def send(self, msg: str | bytearray) -> bool:
        """
        发送文本 / 二进制消息

        如果传入的参数类型是 `str`，会按照文本发送，如果是 `bytearray` 将按照二进制数据发送

        Args:
            msg: 要发送的文本 / 二进制数据

        Returns:
            是否成功发送
        """
    @overload
    def listen(
        self,
        event: Literal["onTextReceived"],
        callback: Callable[[str], Any],
    ) -> bool:
        """
        监听 WebSocket 事件

        收到文本消息 监听

        Callback Args:
            msg (str): 收到的文本消息

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    def listen(
        self,
        event: Literal["onBinaryReceived"],
        callback: Callable[[bytearray], Any],
    ) -> bool:
        """
        监听 WebSocket 事件

        收到二进制消息 监听

        Callback Args:
            data (bytearray): 收到的二进制消息

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    def listen(self, event: Literal["onError"], callback: Callable[[str], Any]) -> bool:
        """
        监听 WebSocket 事件

        发生错误 监听

        Callback Args:
            msg (str): 错误的提示信息

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    def listen(
        self,
        event: Literal["onLostConnection"],
        callback: Callable[[int], Any],
    ) -> bool:
        """
        监听 WebSocket 事件

        连接丢失 监听

        Callback Args:
            code (int): 错误码

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    def close(self) -> bool:
        """
        关闭连接

        在处于关闭状态时，请勿继续使用此客户端对象！

        Returns:
            是否成功关闭连接
        """
    def shutdown(self) -> bool:
        """
        强制断开连接

        在处于关闭状态时，请勿继续使用此客户端对象！

        Returns:
            是否成功断开连接
        """
    def errorCode(self) -> int:
        """
        获取错误码

        如果在上述接口使用中遇到了失败，可以从这里获取上一个错误码

        Returns:
            上一次错误产生的错误码
        """
