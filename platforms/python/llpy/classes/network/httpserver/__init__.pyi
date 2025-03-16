from ..types import (
    T_HTTPServerExceptionListener,
    T_HTTPServerListener,
    T_HTTPServerPreRoutingListener,
)

class HttpServer:
    """HTTP 服务端对象"""

    def __init__(self) -> None:
        """创建一个新的服务器对象"""
    def onGet(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        监听 GET 请求

        Callback Args:
            request (HttpRequest): HTTP 请求对象
            response (HttpResponse): HTTP 响应对象

        Args:
            path: 请求路径，以 `/` 开头，可以包含正则表达式。如: `/test/(.+)`。如果有多个路径同时满足正则表达式，则选择先定义的路径。
            callback: 回调函数

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def onPut(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        监听 PUT 请求

        Callback Args:
            request (HttpRequest): HTTP 请求对象
            response (HttpResponse): HTTP 响应对象

        Args:
            path: 请求路径，以 `/` 开头，可以包含正则表达式。如: `/test/(.+)`。如果有多个路径同时满足正则表达式，则选择先定义的路径。
            callback: 回调函数

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def onPost(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        监听 POST 请求

        Callback Args:
            request (HttpRequest): HTTP 请求对象
            response (HttpResponse): HTTP 响应对象

        Args:
            path: 请求路径，以 `/` 开头，可以包含正则表达式。如: `/test/(.+)`。如果有多个路径同时满足正则表达式，则选择先定义的路径。
            callback: 回调函数

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def onPatch(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        监听 PATCH 请求

        Callback Args:
            request (HttpRequest): HTTP 请求对象
            response (HttpResponse): HTTP 响应对象

        Args:
            path: 请求路径，以 `/` 开头，可以包含正则表达式。如: `/test/(.+)`。如果有多个路径同时满足正则表达式，则选择先定义的路径。
            callback: 回调函数

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def onDelete(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        监听 DELETE 请求

        Callback Args:
            request (HttpRequest): HTTP 请求对象
            response (HttpResponse): HTTP 响应对象

        Args:
            path: 请求路径，以 `/` 开头，可以包含正则表达式。如: `/test/(.+)`。如果有多个路径同时满足正则表达式，则选择先定义的路径。
            callback: 回调函数

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def onOptions(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        监听 OPTIONS 请求

        Callback Args:
            request (HttpRequest): HTTP 请求对象
            response (HttpResponse): HTTP 响应对象

        Args:
            path: 请求路径，以 `/` 开头，可以包含正则表达式。如: `/test/(.+)`。如果有多个路径同时满足正则表达式，则选择先定义的路径。
            callback: 回调函数

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def onPreRouting(self, callback: T_HTTPServerPreRoutingListener) -> HttpServer:
        """
        监听 PreRouting 预路由事件

        Callback Args:
            request (HttpRequest): HTTP 请求对象
            response (HttpResponse): HTTP 响应对象。在回调函数中可以修改响应

        Callback Returns:
            如果返回 `False`，则不会继续路由至对应路径的回调函数 (但仍然会触发 `PostRouting` 事件)。

        Args:
            path: 请求路径，以 `/` 开头，可以包含正则表达式。如: `/test/(.+)`。如果有多个路径同时满足正则表达式，则选择先定义的路径。
            callback: 回调函数，在收到请求时调用。

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def onPostRouting(self, callback: T_HTTPServerListener) -> HttpServer:
        """
        监听 PostRouting 后路由事件

        Callback Args:
            request (HttpRequest): HTTP 请求对象
            response (HttpResponse): HTTP 响应对象。在回调函数中可以修改响应

        Args:
            path: 请求路径，以 `/` 开头，可以包含正则表达式。如: `/test/(.+)`。如果有多个路径同时满足正则表达式，则选择先定义的路径。
            callback: 回调函数，在对应目录的回调函数 (或 `PreRouting` 事件) 执行完毕后调用

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def onError(self, callback: T_HTTPServerListener) -> HttpServer:
        """
        监听 Error 错误事件

        Callback Args:
            request (HttpRequest): HTTP 请求对象
            response (HttpResponse): HTTP 响应对象

        Args:
            path: 请求路径，以 `/` 开头，可以包含正则表达式。如: `/test/(.+)`。如果有多个路径同时满足正则表达式，则选择先定义的路径。
            callback: 回调函数，在在错误 (状态码 >= `400`) 时调用

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def onException(self, callback: T_HTTPServerExceptionListener) -> HttpServer:
        """
        监听 Error 错误事件

        Callback Args:
            request (HttpRequest): HTTP 请求对象
            response (HttpResponse): HTTP 响应对象。在回调函数中可以修改响应
            exception (str): 异常信息

        Args:
            path: 请求路径，以 `/` 开头，可以包含正则表达式。如: `/test/(.+)`。如果有多个路径同时满足正则表达式，则选择先定义的路径。
            callback: 回调函数，在 `handler` 中有抛出异常时调用

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def listen(self, addr: str, port: int) -> HttpServer:
        """
        监听端口并开启服务器

        Args:
            addr: 监听地址，可以是 IP 地址或域名
            port: 监听端口

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def startAt(self, addr: str, port: int) -> HttpServer:
        """
        监听端口并开启服务器

        Args:
            addr: 监听地址，可以是 IP 地址或域名
            port: 监听端口

        Returns:
            处理完毕的服务器对象（便于连锁进行其他操作）
        """
    def stop(self) -> None:
        """停止服务器"""
    def close(self) -> None:
        """停止服务器"""
    def isRunning(self) -> bool:
        """
        获取服务器是否正在运行

        Returns:
            服务器正在运行与否
        """
