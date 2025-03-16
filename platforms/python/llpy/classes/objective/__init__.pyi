from typing import NoReturn

from llpy import LLSE_Player

from .types import T_ScoreDisplaySlot, T_ScoreSortOrder

class LLSE_Objective:
    """计分项对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def name(self) -> str:
        """计分项名称"""
    @property
    def displayName(self) -> str:
        """计分项的显示名称"""
    def setDisplay(
        self,
        slot: T_ScoreDisplaySlot,
        sort_order: T_ScoreSortOrder = 0,
    ) -> bool:
        """
        设置计分项的显示状态

        Args:
            slot: 显示槽位名称字符串
            sort_order: 排序方式

        Returns:
            是否设置成功
        """
    def setScore(self, target: LLSE_Player | str, score: int) -> int | None:
        """
        设置某个目标的分数

        注意：若计分项不存在，则会尝试创建计分项，此时会返回 `0` (当 `target` 为 `str` 时) 或 `None` (当 `target` 为 `LLSE_Player` 时)

        原因参见：[#971](https://github.com/LiteLDev/LiteLoaderBDS/issues/971#issuecomment-1385047649)

        Args:
            target: 计分项跟踪的目标，可传入玩家对象或者任意字符串
            score: 要设置的分数

        Returns:
            如果返回 `None`，则代表操作失败
        """
    def addScore(self, target: LLSE_Player | str, score: int) -> int | None:
        """
        增加某个目标的分数

        注意：若计分项不存在，则会尝试创建计分项，此时会返回 `0` (当 `target` 为 `str` 时) 或 `None` (当 `target` 为 `LLSE_Player` 时)

        原因参见：[#971](https://github.com/LiteLDev/LiteLoaderBDS/issues/971#issuecomment-1385047649)

        Args:
            target: 计分项跟踪的目标，可传入玩家对象或者任意字符串
            score: 要增加的分数

        Returns:
            如果返回 `None`，则代表操作失败
        """
    def reduceScore(self, target: LLSE_Player | str, score: int) -> int | None:
        """
        减少某个目标的分数

        注意：若计分项不存在，则会尝试创建计分项，此时会返回 `0` (当 `target` 为 `str` 时) 或 `None` (当 `target` 为 `LLSE_Player` 时)

        原因参见：[#971](https://github.com/LiteLDev/LiteLoaderBDS/issues/971#issuecomment-1385047649)

        Args:
            target: 计分项跟踪的目标，可传入玩家对象或者任意字符串
            score: 要减少的分数

        Returns:
            如果返回 `None`，则代表操作失败
        """
    def deleteScore(self, target: LLSE_Player | str) -> bool:
        """
        停止跟踪某个目标

        停止跟踪将直接删除这个目标对应的计分项数值，下次如需要访问需要再次创建

        Args:
            target: 计分项跟踪的目标，可传入玩家对象或者任意字符串

        Returns:
            是否停止成功
        """
    def getScore(self, target: LLSE_Player | str) -> int:
        """
        获取跟踪的某个目标的分数

        使用前请保证计分项存在

        Args:
            target: 待查询的跟踪目标，可传入玩家对象或者任意字符串

        Returns:
            该目标 / 玩家在此计分项中的分数
        """

Objective = LLSE_Objective
