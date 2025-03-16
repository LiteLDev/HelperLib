from typing import Any, Callable, NoReturn

from llpy.types import T_TimeObj

class system:
    """系统调用 API"""

    def __init__(self) -> NoReturn: ...
    @staticmethod
    def getTimeStr() -> str:
        """
        获取当前时间字符串

        Returns:
            当前的时间字符串，使用当地时区和24小时制。形如 `2021-04-03 19:15:01`
        """
    @staticmethod
    def getTimeObj() -> T_TimeObj:
        """
        获取当前的时间对象

        Returns:
            当前的时间对象
        """
    @staticmethod
    def randomGuid() -> str:
        """
        随机生成一个 GUID 字符串

        Returns:
            一个随机生成的唯一标识符GUID
        """
    @staticmethod
    def cmd(
        cmd: str,
        callback: Callable[[int, str], Any],
        time_limit: int = -1,
    ) -> bool:
        """
        调用 shell 执行指定系统命令

        注意！这里执行的不是 MC 命令系统的命令

        此函数异步工作，不会等待系统执行完命令后再返回，而是由引擎自动调用给出的回调函数来返回结果

        Callback Args:
            exitcode (int): shell 退出码
            output (str): 标准输出和标准错误输出的内容

        Args:
            cmd: 执行的系统命令
            callback: shell 进程结束之后返回数据使用的回调函数
            time_limit: 命令运行的最长时限，单位为毫秒。默认为 `-1`，即不限制运行时间

        Returns:
            是否成功启动命令
        """
    @staticmethod
    def newProcess(
        process: str,
        callback: Callable[[int, str], Any],
        time_limit: int = -1,
    ) -> bool:
        """
        运行指定位置程序

        此函数异步工作，不会等待系统执行完命令后再返回，而是由引擎自动调用给出的回调函数来返回结果

        Callback Args:
            exitcode (int): 程序进程退出码
            output (str): 程序标准输出和标准错误输出的内容

        Args:
            process: 运行的程序路径（与命令行参数）
            callback: 程序进程结束之后返回数据使用的回调函数
            time_limit: 程序进程运行的最长时限，单位为毫秒。默认为 `-1`，即不限制运行时间

        Returns:
            是否成功启动进程
        """
