from typing import NoReturn

class HttpRequest:
    """HTTP 请求对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def headers(self) -> dict[str, list[str]]:
        """请求头"""
    @property
    def method(self) -> str:
        """请求方法"""
    @property
    def body(self) -> str:
        """请求内容"""
    @property
    def path(self) -> str:
        """请求路径"""
    @property
    def params(self) -> dict[str, str | list[str]]:
        """请求查询参数"""
    @property
    def query(self) -> dict[str, str | list[str]]:
        """请求查询参数"""
    @property
    def remoteAddr(self) -> str:
        """请求源地址"""
    @property
    def remotePort(self) -> int:
        """请求源端口"""
    @property
    def version(self) -> str:
        """请求版本"""
    @property
    def matches(self) -> list[str]:
        """
        请求路径正则匹配结果

        第一个元素 (`[0]`) 为原始文本，其后面的元素才是匹配结果
        """
    def getHeader(self, name: str) -> list[str]:
        """
        获取指定请求头的值

        Args:
            name: 请求头名称

        Returns:
            请求头的值数组 (如果没有该请求头，则返回空数组)
        """
