from typing import Literal, TypedDict


class T_PluginInfo(TypedDict):
    """`ll.getPluginInfo()` 或 `ll.getAllPluginInfo()` 返回的插件信息"""

    name: str
    """插件名称"""
    desc: str
    """插件描述"""
    version: list[int]
    """插件版本（数组形式）"""
    versionStr: str
    """插件版本"""
    filePath: str
    """插件路径"""
    others: dict[str, str]
    """其他信息"""


T_VersionStatusDev = Literal[0]
T_VersionStatusBeta = Literal[1]
T_VersionStatusRelease = Literal[2]
T_VersionStatus = T_VersionStatusDev | T_VersionStatusBeta | T_VersionStatusRelease
