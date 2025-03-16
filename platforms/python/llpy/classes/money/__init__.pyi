from typing import NoReturn, overload

from .types import T_MoneyHistory

class money:
    """经济系统 API"""

    def __init__(self) -> NoReturn: ...
    @staticmethod
    def set(xuid: str, value: int) -> bool:
        """
        设置玩家的存款金额

        Args:
            xuid: 要操作的玩家的 XUID 标识符
            value: 要设置的金额

        Returns:
            是否设置成功
        """
    @staticmethod
    def get(xuid: str) -> int:
        """
        获取玩家的存款金额

        Args:
            xuid: 要读取的玩家的 XUID 标识符

        Returns:
            玩家的资金数值
        """
    @staticmethod
    def add(xuid: str, value: int) -> bool:
        """
        增加玩家的存款

        Args:
            xuid: 要操作的玩家的 XUID 标识符
            value: 要增加的金额

        Returns:
            是否设置成功
        """
    @staticmethod
    def reduce(xuid: str, value: int) -> bool:
        """
        减少玩家的存款

        Args:
            xuid: 要操作的玩家的 XUID 标识符
            value: 要减小的金额

        Returns:
            是否设置成功
        """
    @overload
    @staticmethod
    def trans(xuid_pay: str, xuid_recv: str, value: int) -> None:
        """
        进行一笔转账

        Args:
            xuid_pay: 付款的玩家的 XUID 标识符
            xuid_recv: 收款的玩家的 XUID 标识符
            value: 要支付的金额
        """
    @overload
    @staticmethod
    def trans(xuid_pay: str, xuid_recv: str, value: int, note: str) -> bool:
        """
        进行一笔转账

        Args:
            xuid_pay: 付款的玩家的 XUID 标识符
            xuid_recv: 收款的玩家的 XUID 标识符
            value: 要支付的金额
            note: 给这笔转账附加一些文字说明

        Returns:
            是否转账成功
        """
    @staticmethod
    def getHistory(xuid: str, time: int) -> list[T_MoneyHistory]:
        """
        查询历史账单

        Args:
            xuid: 要操作的玩家的 XUID 标识符
            time: 查询从现在开始往前 `time` 秒的记录

        Returns:
            查询结果对象的数组
        """
    @staticmethod
    def clearHistory(time: int) -> bool:
        """
        删除账单历史记录

        Args:
            time: 删除从现在开始往前 `time` 秒的记录

        Returns:
            是否删除成功
        """
