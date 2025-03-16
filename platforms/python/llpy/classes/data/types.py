from typing import TypedDict


class T_PlayerInfo(TypedDict):
    """
    `data.getAllPlayerInfo()` 获取到的玩家信息

    提示：XUID 数据库中储存的玩家名为玩家对象对应的 `realName` 字段
    """

    name: str
    """玩家名"""
    xuid: str
    """玩家XUID"""
    uuid: str
    """玩家UUID"""
