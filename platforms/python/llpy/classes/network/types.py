from typing import Any, Callable, Literal, TypedDict

from .httprequest import HttpRequest
from .httpresponse import HttpResponse


class T_HttpGetResp(TypedDict):
    """`network.httpGetSync()` 返回的响应结果"""

    status: int
    """返回的 HTTP(s) 响应码，如200代表请求成功。如果请求执行失败，`status` 值将为 `-1`"""
    data: str
    """返回的具体数据"""


T_WSClientStatusOpen = Literal[0]
T_WSClientStatusClosing = Literal[1]
T_WSClientStatusClosed = Literal[2]
T_WSClientStatus = (
    T_WSClientStatusOpen | T_WSClientStatusClosing | T_WSClientStatusClosed
)

T_HTTPServerListener = Callable[[HttpRequest, HttpResponse], Any]
T_HTTPServerPreRoutingListener = Callable[[HttpRequest, HttpResponse], bool]
T_HTTPServerExceptionListener = Callable[[HttpRequest, HttpResponse, str], Any]
