from typing import NoReturn

from ..types import T_VersionStatusBeta, T_VersionStatusDev, T_VersionStatusRelease

class Version:
    """插件版本状态枚举"""

    def __init__(self) -> NoReturn: ...

    Dev: T_VersionStatusDev
    """插件版本状态枚举 | 开发版本"""
    Beta: T_VersionStatusBeta
    """插件版本状态枚举 | 测试版本"""
    Release: T_VersionStatusRelease
    """插件版本状态枚举 | 正式发布版本（默认值）"""
