from typing import NoReturn, overload

class LLSE_CommandOutput:
    """命令执行结果输出对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def empty(self) -> bool: ...
    @property
    def successCount(self) -> int: ...
    @overload
    def success(self, msg: str) -> bool:
        """
        输出一条普通信息

        Args:
            msg: 要输出的信息

        Returns:
            是否成功输出
        """
    @overload
    def success(self, msg: str, args: list[str]) -> bool:
        """
        输出一条成功信息

        Args:
            msg: 要输出的信息
            args: 要替换的参数

        Returns:
            是否成功输出
        """
    @overload
    def error(self, msg: str) -> bool:
        """
        输出一条普通信息

        Args:
            msg: 要输出的信息

        Returns:
            是否成功输出
        """
    @overload
    def error(self, msg: str, args: list[str]) -> bool:
        """
        输出一条错误信息

        Args:
            msg: 要输出的信息
            args: 要替换的参数

        Returns:
            是否成功输出
        """
    @overload
    def addMessage(self, msg: str) -> bool:
        """
        输出一条普通信息

        Args:
            msg: 要输出的信息

        Returns:
            是否成功输出
        """
    @overload
    def addMessage(self, msg: str, args: list[str]) -> bool:
        """
        输出一条普通信息

        Args:
            msg: 要输出的信息
            args: 要替换的参数

        Returns:
            是否成功输出
        """
    def toString(self) -> str: ...

CommandOutput = LLSE_CommandOutput
