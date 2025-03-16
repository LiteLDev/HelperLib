from typing import Any, Callable, NoReturn, overload

from typing_extensions import deprecated

from llpy.types import T_HttpGetResp

from .wsclient import WSClient

class network:
    """网络接口 API"""

    def __init__(self) -> NoReturn: ...
    @overload
    @staticmethod
    def httpGet(url: str, callback: Callable[[int, str], Any]) -> bool:
        """
        发送一个异步 HTTP(s) Get 请求

        Callback Args:
            status (int): 返回的 HTTP(s) 响应码，如200代表请求成功。如果请求执行失败，`status` 值将为 `-1`
            result (str): 返回的具体数据

        Args:
            url: 请求的目标地址（包括 Get 请求附带的参数）
            callback: 当请求返回时执行的回调函数，用于回传 HTTP(s) 响应结果

        Returns:
            是否成功发送请求
        """
    @overload
    @staticmethod
    def httpGet(
        url: str,
        header: dict[str, str],
        callback: Callable[[int, str], Any],
    ) -> bool:
        """
        发送一个异步 HTTP(s) Get 请求

        Callback Args:
            status (int): 返回的 HTTP(s) 响应码，如200代表请求成功。如果请求执行失败，`status` 值将为 `-1`
            result (str): 返回的具体数据

        Args:
            url: 请求的目标地址（包括 Get 请求附带的参数）
            header: 请求头（包括 Get 请求 Request header）
            callback: 当请求返回时执行的回调函数，用于回传 HTTP(s) 响应结果

        Returns:
            是否成功发送请求
        """
    @overload
    @staticmethod
    def httpPost(
        url: str,
        data: str,
        post_type: str,
        callback: Callable[[int, str], Any],
    ) -> bool:
        """
        发送一个异步 HTTP(s) Post 请求

        Callback Args:
            status (int): 返回的 HTTP(s) 响应码，如200代表请求成功。如果请求执行失败，`status` 值将为 `-1`
            result (str): 返回的具体数据

        Args:
            url: 请求的目标地址
            data: 发送的数据
            post_type: 发送的 Post 数据类型，形如 `text/plain` `application/x-www-form-urlencoded` 等
            callback: 当请求返回时执行的回调函数，用于回传 HTTP(s) 响应结果

        Returns:
            是否成功发送请求
        """
    @overload
    @staticmethod
    def httpPost(
        url: str,
        header: dict[str, str],
        data: str,
        post_type: str,
        callback: Callable[[int, str], Any],
    ) -> bool:
        """
        发送一个异步 HTTP(s) Post 请求

        Callback Args:
            status (int): 返回的 HTTP(s) 响应码，如200代表请求成功。如果请求执行失败，`status` 值将为 `-1`
            result (str): 返回的具体数据

        Args:
            url: 请求的目标地址
            header: 请求头（包括 Post 请求 Request header）
            data: 发送的数据
            post_type: 发送的 Post 数据类型，形如 `text/plain` `application/x-www-form-urlencoded` 等
            callback: 当请求返回时执行的回调函数，用于回传 HTTP(s) 响应结果

        Returns:
            是否成功发送请求
        """
    @staticmethod
    def httpGetSync(url: str) -> T_HttpGetResp: ...
    @deprecated("请使用 `WSClient()`")
    @staticmethod
    def newWebSocket() -> WSClient: ...
