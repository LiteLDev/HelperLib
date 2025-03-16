from typing import Any, NoReturn, overload

from ..types import T_DBFetchAllCallback

class DBStmt:
    """数据库预准备语句对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def affectedRows(self) -> int:
        """获取该预准备语句执行后影响的行数 (仅对 `INSERT` `UPDATE` `DELETE` `REPLACE` 等语句生效)"""
    @property
    def insertId(self) -> int:
        """获取该 `INSERT` / `UPDATE` / `REPLACE` 语句执行后最后一个更改行的行号"""
    @overload
    def bind(self, obj: dict[str, Any]) -> DBStmt:
        """
        绑定参数到一个 SQL 语句

        在绑定完成后，应调用 `DBStmt.execute()` 执行语句，否则语句将不会被执行

        Args:
            obj: 要绑定的对象，等同于遍历此对象并执行 `bind(val, key)`

        Returns:
            处理完毕的语句对象（便于连锁进行其他操作）
        """
    @overload
    def bind(self, arr: list[Any]) -> DBStmt:
        """
        绑定参数到一个 SQL 语句

        在绑定完成后，应调用 `DBStmt.execute()` 执行语句，否则语句将不会被执行

        Args:
            arr: 要绑定的数组，等同于遍历此数组并执行 `bind(val)`

        Returns:
            处理完毕的语句对象（便于连锁进行其他操作）
        """
    @overload
    def bind(self, val: Any) -> DBStmt:
        """
        绑定参数到一个 SQL 语句

        本重载将会将值绑定到第一个未绑定的参数上

        在绑定完成后，应调用 `DBStmt.execute()` 执行语句，否则语句将不会被执行

        Args:
            val: 要绑定的值

        Returns:
            处理完毕的语句对象（便于连锁进行其他操作）
        """
    @overload
    def bind(self, val: Any, index: int) -> DBStmt:
        """
        绑定参数到一个 SQL 语句

        在绑定完成后，应调用 `DBStmt.execute()` 执行语句，否则语句将不会被执行

        Args:
            val: 要绑定的值
            index: 要绑定到的参数索引 (从 0 开始)

        Returns:
            处理完毕的语句对象（便于连锁进行其他操作）
        """
    @overload
    def bind(self, val: Any, name: str) -> DBStmt:
        """
        绑定参数到一个 SQL 语句

        在绑定完成后，应调用 `DBStmt.execute()` 执行语句，否则语句将不会被执行

        Args:
            val: 要绑定的值
            name: 要绑定到的参数的参数名

        Returns:
            处理完毕的语句对象（便于连锁进行其他操作）
        """
    def execute(self) -> DBStmt:
        """
        执行当前语句

        Returns:
            处理完毕的语句对象（便于连锁进行其他操作）
        """
    def step(self) -> bool:
        """
        步进到下一行结果

        注意：所有参数绑定完成后会自动执行语句，执行完后此时的 `step` 就在第一行上，
        请注意循环遍历的方式，否则将导致第一行被跳过

        Returns:
            执行成功与否
        """
    def fetch(self) -> dict[str, Any]:
        """
        获取当前结果行

        Returns:
            当前结果行
        """
    @overload
    def fetchAll(self) -> list[list[Any]]:
        """
        获取所有结果行

        Returns:
            查询的结果 (结果集)
        """
    @overload
    def fetchAll(self, callback: T_DBFetchAllCallback) -> DBStmt:
        """
        获取所有结果行

        Callback Args:
            line (dict[str, Any]): 当前遍历的结果行

        Callback Returns:
            返回 `False` 终止遍历

        Args:
            callback: 回调函数，用于遍历结果行

        Returns:
            处理完毕的语句对象（便于连锁进行其他操作）
        """
    def reset(self) -> DBStmt:
        """
        重置当前语句状态至 “待执行”

        注意：本函数不会清除已绑定的参数

        Returns:
            处理完毕的语句对象（便于连锁进行其他操作）
        """
    def reexec(self) -> DBStmt:
        """
        重新执行预准备语句

        本函数是一个便捷函数，等同于执行 `DBStmt.reset()` 和 `DBStmt.execute()`

        Returns:
            处理完毕的语句对象（便于连锁进行其他操作）
        """
    def clear(self) -> DBStmt:
        """
        清除所有已绑定的参数

        Returns:
            处理完毕的语句对象（便于连锁进行其他操作）
        """
