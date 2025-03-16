from typing import Any, overload

from ..dbstmt import DBStmt
from ..types import T_DBConnectParam, T_DBType

class DBSession:
    """SQL 数据库会话"""

    @overload
    def __init__(self, url: str) -> None:
        """
        打开一个 SQL 数据库会话

        Args:
            url: 连接字符串
                例如 `mysql://root:password@localhost:3306/db`
        """
    @overload
    def __init__(self, db_type: T_DBType, params: T_DBConnectParam) -> None:
        """
        打开一个 SQL 数据库会话

        Args:
            db_type: 数据库的类型
            params: 连接参数
        """
    def query(self, sql: str) -> list[list[Any]]:
        """
        执行 SQL 并获取结果集

        返回数组的 第一行 为结果集的表头，剩余行 为结果数据

        例：若查询结果为

        | homo | senpai |
        | :--- | :----- |
        | 114  | 514    |
        | 1919 | 810    |

        则返回值为

        ```py
        [
            ["homo", "senpai"],
            [114, 514],
            [1919, 810],
        ]
        ```

        Args:
            sql: 要查询的 SQL 语句

        Returns:
            查询的结果 (结果集)
        """
    def exec(self, sql: str) -> DBSession:
        """
        执行 SQL 但不获取结果

        Args:
            sql: 要执行的 SQL 语句

        Returns:
            处理完毕的会话对象（便于连锁进行其他操作）
        """
    def execute(self, sql: str) -> DBSession:
        """
        执行 SQL 但不获取结果

        Args:
            sql: 要执行的 SQL 语句

        Returns:
            处理完毕的会话对象（便于连锁进行其他操作）
        """
    def prepare(self, sql: str) -> DBStmt:
        """
        准备一个预准备语句

        Args:
            sql: 要准备的 SQL 语句

        Returns:
            预准备语句
        """
    def close(self) -> bool:
        """
        关闭数据库会话

        Returns:
            关闭成功与否
        """
    def isOpen(self) -> bool:
        """
        获取当前会话是否为打开状态

        Returns:
            是否为打开状态
        """
