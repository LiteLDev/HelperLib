from typing import overload

from llpy.types import T_ToJsonDict

from ..types import T_PermInfo

class Role:
    """身份组对象"""

    @overload
    def __init__(self, name: str) -> None:
        """
        创建身份组

        显示名称默认为 `name`

        Raises:
            无效的参数 / 无效的名称 / 该身份组已存在

        Args:
            name: 身份组名称，必须是唯一的。不能含有 `@` `#` `[` `]` `{` `}` `<` `>` `(` `)` `/` `|` `$` `%` `^` `&` `*` `!` `~` `"` `'` `+` `=` `?` `\\n` `\\t` `\\r` `\\f` `\\v`
        """
    @overload
    def __init__(self, name: str, display_name: str) -> None:
        """
        创建身份组

        Raises:
            无效的参数 / 无效的名称 / 该身份组已存在

        Args:
            name: 身份组名称，必须是唯一的。不能含有 `@` `#` `[` `]` `{` `}` `<` `>` `(` `)` `/` `|` `$` `%` `^` `&` `*` `!` `~` `"` `'` `+` `=` `?` `\\n` `\\t` `\\r` `\\f` `\\v`
            display_name: 身份组显示名称
        """
    @property
    def name(self) -> str:
        """身份组名称"""
    @name.setter
    def name(self, val: str): ...
    @property
    def displayName(self) -> str:
        """身份组显示名称"""
    @displayName.setter
    def displayName(self, val: str): ...
    @property
    def priority(self) -> int:
        """身份组优先级，越大越优先"""
    @priority.setter
    def priority(self, val: int): ...
    @property
    def members(self) -> list[str]:
        """身份组成员的 XUID"""
    @members.setter
    def members(self, val: list[str]): ...
    @property
    def permissions(self) -> list[T_PermInfo]:
        """身份组拥有的权限"""
    @permissions.setter
    def permissions(self, val: list[T_ToJsonDict]):
        """
        设置身份组拥有的权限

        列表中的字典必须要有 `name`(`str`) 和 `enabled`(`bool`) 项，
        其余项会被作为 `extra` 项
        """
    def hasMember(self, xuid: str) -> bool:
        """
        检查身份组是否有指定成员

        Args:
            xuid: 成员（玩家）的 XUID

        Raises:
            无效的参数 / 身份组实例已被销毁

        Returns:
            是否有该成员
        """
    def addMember(self, xuid: str) -> None:
        """
        添加成员到身份组

        Args:
            xuid: 成员（玩家）的 XUID

        Raises:
            无效的参数 / 身份组实例已被销毁 / 成员已存在
        """
    def removeMember(self, xuid: str) -> None:
        """
        从身份组中移除成员

        Args:
            xuid: 成员（玩家）的 XUID

        Raises:
            无效的参数 / 身份组实例已被销毁 / 成员已存在
        """
    def hasPermission(self, name: str) -> bool:
        """
        检查身份组是否有指定权限

        注意：权限的额外数据将被忽略，此方法会返回 `true` 如果 `enabled` 字段为 `true`

        Args:
            name: 权限名称

        Raises:
            无效的参数 / 身份组实例已被销毁

        Returns:
            是否有该权限
        """
    @overload
    def setPermission(self, name: str, enabled: bool) -> None:
        """
        设置身份组权限

        如果在身份组中未找到指定权限，将会添加该权限并设置为指定值

        Args:
            name: 权限名称，必须已经注册
            enabled: 权限是否开启

        Raises:
            无效的参数 / 无效的额外数据 / 无效的权限名 / 身份组实例已被销毁
        """
    @overload
    def setPermission(
        self,
        name: str,
        enabled: bool,
        extra_data: T_ToJsonDict,
    ) -> None:
        """
        设置身份组权限

        如果在身份组中未找到指定权限，将会添加该权限并设置为指定值

        Args:
            name: 权限名称，必须已经注册
            enabled: 权限是否开启
            extra_data: 权限的额外数据

        Raises:
            无效的参数 / 无效的额外数据 / 无效的权限名 / 身份组实例已被销毁
        """
    def removePermission(self, name: str) -> None:
        """
        移除身份组中的权限

        Args:
            name: 权限名称

        Raises:
            无效的参数 / 身份组实例已被销毁 / 找不到指定权限
        """
    def permissionExists(self, name: str) -> bool:
        """
        检查权限是否存在于身份组中

        不同于 `hasPermission`，这个方法只要权限已经存在于身份组就会返回 `True`，但权限不一定开启。

        Args:
            name: 权限名称

        Raises:
            无效的参数 / 身份组实例已被销毁

        Returns:
            权限是否已经存在于身份组中
        """
    def isValid(self) -> bool:
        """
        检查身份组实例是否有效

        Returns:
            身份组实例是否有效
        """
