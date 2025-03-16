from typing import Any, NoReturn

class HttpResponse:
    """HTTP 响应对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def headers(self) -> dict[str, list[str]]:
        """响应头"""
    @property
    def status(self) -> int:
        """响应状态码"""
    @property
    def body(self) -> str:
        """响应内容"""
    @property
    def version(self) -> str:
        """响应版本"""
    @property
    def reason(self) -> str:
        """错误原因"""
    def getHeader(self, name: str) -> list[str]:
        """
        获取指定响应头的值

        Args:
            name: 响应头名称

        Returns:
            响应头的值数组 (如果没有该响应头，则返回空数组)
        """
    def setHeader(self, name: str, value: Any) -> HttpResponse:
        """
        设置指定响应头的值

        Args:
            name: 响应头名称
            value: 响应头值

        Returns:
            处理完毕的响应对象
        """
    def write(self, *args: Any) -> HttpResponse:
        """
        写入响应内容

        注：本函数在目前相当于 `res.body += arg1 + arg2 + ...`

        Args:
            *args: 响应内容

        Returns:
            处理完毕的响应对象
        """
