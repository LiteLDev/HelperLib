from typing import NoReturn, overload

from .role import Role
from .types import T_PermInfo

class Permission:
    """权限系统 API"""

    def __init__(self) -> NoReturn: ...
    @overload
    @staticmethod
    def createRole(name: str) -> Role:
        """
        创建身份组

        显示名称默认为 `name`

        Args:
            name: 身份组名称，必须是唯一的。不能含有 `@` `#` `[` `]` `{` `}` `<` `>` `(` `)` `/` `|` `$` `%` `^` `&` `*` `!` `~` `"` `'` `+` `=` `?` `\\n` `\\t` `\\r` `\\f` `\\v`
            display_name: 身份组显示名称

        Raises:
            无效的参数 / 无效的名称 / 该身份组已存在

        Returns:
            身份组实例
        """
    @overload
    @staticmethod
    def createRole(name: str, display_name: str) -> Role:
        """
        创建身份组

        Args:
            name: 身份组名称，必须是唯一的。不能含有 `@` `#` `[` `]` `{` `}` `<` `>` `(` `)` `/` `|` `$` `%` `^` `&` `*` `!` `~` `"` `'` `+` `=` `?` `\\n` `\\t` `\\r` `\\f` `\\v`
            display_name: 身份组显示名称

        Raises:
            无效的参数 / 无效的名称 / 该身份组已存在

        Returns:
            身份组实例
        """
    @staticmethod
    def roleExists(name: str) -> bool:
        """
        检查身份组是否存在

        Args:
            name: 身份组名称

        Raises:
            无效的参数

        Returns:
            身份组是否存在
        """
    @staticmethod
    def getRole(name: str) -> Role:
        """
        获取已有身份组

        Args:
            name: 身份组名称

        Raises:
            无效的参数 / 找不到该身份组

        Returns:
            身份组实例
        """
    @staticmethod
    def getOrCreateRole(name: str) -> Role:
        """
        创建或获取身份组实例

        Args:
            name: 身份组名称，必须是唯一的。不能含有 `@` `#` `[` `]` `{` `}` `<` `>` `(` `)` `/` `|` `$` `%` `^` `&` `*` `!` `~` `"` `'` `+` `=` `?` `\\n` `\\t` `\\r` `\\f` `\\v`

        Raises:
            无效的参数 / 无效的名称

        Returns:
            身份组实例
        """
    @staticmethod
    def deleteRole(name: str) -> None:
        """
        删除身份组

        Args:
            name: 身份组名称

        Raises:
            无效的参数 / 身份组不存在
        """
    @staticmethod
    def registerPermission(name: str, desc: str) -> None:
        """
        注册权限

        Args:
            name: 权限名，唯一且不包含 `空格` `\\n` `\\t` `\\r` `\\f` `\\v`
            desc: 权限描述

        Raises:
            无效的参数 / 无效的权限名 / 权限已经存在
        """
    @staticmethod
    def deletePermission(name: str) -> None:
        """
        删除权限

        Args:
            name: 身份组名称

        Raises:
            无效的参数 / 身份组不存在
        """
    @staticmethod
    def permissionExists(name: str) -> bool:
        """
        检查权限是否存在

        Args:
            name: 权限名称

        Raises:
            无效的参数

        Returns:
            权限是否存在
        """
    @staticmethod
    def checkPermission(xuid: str, perm_name: str) -> bool:
        """
        检查玩家是否有指定权限

        注意：权限的额外数据将被忽略，此方法会返回 `true` 如果 `enabled` 字段为 `true`

        Args:
            xuid: 玩家 XUID
            perm_name: 权限名称

        Raises:
            无效的参数 / 找不到玩家 / 找不到权限

        Returns:
            玩家是否有指定权限
        """
    @staticmethod
    def isMemberOf(xuid: str, role_name: str) -> bool:
        """
        检查玩家是否是指定身份组的成员

        注意：如果找不到指定权限组，此方法将返回 `False`。

        Args:
            xuid: 玩家 XUID
            role_name: 身份组名称

        Raises:
            无效的参数 / 找不到玩家

        Returns:
            玩家是否是指定身份组的成员
        """
    @staticmethod
    def getPlayerRoles(xuid: str) -> list[Role]:
        """
        获取玩家的身份组列表

        Args:
            xuid: 玩家 XUID

        Returns:
            此玩家的身份组列表
        """
    @staticmethod
    def getPlayerPermissions(xuid: str) -> list[T_PermInfo]:
        """
        获取玩家的权限列表

        Args:
            xuid: 玩家 XUID

        Returns:
            此玩家的权限列表
        """
    @staticmethod
    def saveData() -> None:
        """
        保存数据

        数据将每 100 游戏刻自动保存一次
        """
