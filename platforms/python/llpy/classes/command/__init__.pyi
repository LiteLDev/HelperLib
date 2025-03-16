import typing
from typing import Callable, NoReturn, TypeVar

from .types import T_CommandCallback, T_ParamOption, T_ParamType

_T_ArgCallback = TypeVar("_T_ArgCallback", bound=T_CommandCallback)

class LLSE_Command:
    """指令对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def name(self) -> str:
        """指令名称"""
    @property
    def registered(self) -> bool:
        """指令是否已注册"""
    def setEnum(self, name: str, values: list[str]) -> str:
        """
        新增一个指令枚举选项

        Args:
            name: 枚举名，用于设置参数时区分枚举
            values: 枚举的有效值

        Returns:
            是否成功设置
        """
    def setAlias(self, alias: str) -> bool:
        """
        设置指令别名

        Args:
            alias: 指令别名

        Returns:
            是否成功设置
        """
    @typing.overload
    def mandatory(self, name: str, param_type: T_ParamType) -> int:
        """
        新增一个必选参数

        Args:
            name: 参数名，用于执行指令时识别参数
            param_type: 命令参数类型

        Returns:
            是否成功设置
        """
    @typing.overload
    def mandatory(
        self,
        name: str,
        param_type: T_ParamType,
        options: T_ParamOption = 0,
    ) -> int:
        """
        新增一个必选参数

        Args:
            name: 参数名，用于执行指令时识别参数
            param_type: 命令参数类型
            options: 参数选项

        Returns:
            是否成功设置
        """
    @typing.overload
    def mandatory(
        self,
        name: str,
        param_type: T_ParamType,
        enum_name: str,
        options: T_ParamOption = 0,
    ) -> int:
        """
        新增一个必选参数

        Args:
            name: 参数名，用于执行指令时识别参数
            param_type: 命令参数类型
            enum_name: 枚举名（仅 `param_type` 为 `ParamType.Enum` 时有效，用于区分枚举选项）
            options: 参数选项

        Returns:
            是否成功设置
        """
    @typing.overload
    def mandatory(
        self,
        name: str,
        param_type: T_ParamType,
        enum_name: str,
        identifier: str,
        options: T_ParamOption = 0,
    ) -> int:
        """
        新增一个必选参数

        Args:
            name: 参数名，用于执行指令时识别参数
            param_type: 命令参数类型
            enum_name: 枚举名（仅 `param_type` 为 `ParamType.Enum` 时有效，用于区分枚举选项）
            identifier: 参数标识，特殊情况下用于唯一识别参数，一般可用 `enum_name` 或 `name` 代替
            options: 参数选项

        Returns:
            是否成功设置
        """
    @typing.overload
    def optional(self, name: str, param_type: T_ParamType) -> int:
        """
        新增一个可选参数

        Args:
            name: 参数名，用于执行指令时识别参数
            param_type: 命令参数类型

        Returns:
            是否成功设置
        """
    @typing.overload
    def optional(
        self,
        name: str,
        param_type: T_ParamType,
        options: T_ParamOption = 0,
    ) -> int:
        """
        新增一个可选参数

        Args:
            name: 参数名，用于执行指令时识别参数
            param_type: 命令参数类型
            options: 参数选项

        Returns:
            是否成功设置
        """
    @typing.overload
    def optional(
        self,
        name: str,
        param_type: T_ParamType,
        enum_name: str,
        options: T_ParamOption = 0,
    ) -> int:
        """
        新增一个可选参数

        Args:
            name: 参数名，用于执行指令时识别参数
            param_type: 命令参数类型
            enum_name: 枚举名（仅 `param_type` 为 `ParamType.Enum` 时有效，用于区分枚举选项）
            options: 参数选项

        Returns:
            是否成功设置
        """
    @typing.overload
    def optional(
        self,
        name: str,
        param_type: T_ParamType,
        enum_name: str,
        identifier: str,
        options: T_ParamOption = 0,
    ) -> int:
        """
        新增一个可选参数

        Args:
            name: 参数名，用于执行指令时识别参数
            param_type: 命令参数类型
            enum_name: 枚举名（仅 `param_type` 为 `ParamType.Enum` 时有效，用于区分枚举选项）
            identifier: 参数标识，特殊情况下用于唯一识别参数，一般可用 `enum_name` 或 `name` 代替
            options: 参数选项

        Returns:
            是否成功设置
        """
    @typing.overload
    def overload(self) -> bool:
        """
        新增一条指令重载

        Returns:
            是否成功设置
        """
    @typing.overload
    def overload(self, params: list[str | int] | str | int, *args: str | int) -> bool:
        """
        新增一条指令重载

        Args:
            params: 参数标识符，重载所用到的参数列表，可用 参数标识符、枚举名、参数名。
                注意不能使用无法区分具体参数的标识符，如两个参数都叫 `action` 但枚举选项不同，此时应该使用枚举名而不是参数名

        Returns:
            是否成功设置
        """
    def setCallback(self, callback: T_CommandCallback) -> bool:
        """
        设置指令回调

        Callback Args:
            cmd (LLSE_Command): 自身的指令对象
            origin (LLSE_CommandOrigin): 命令的执行者
            output (LLSE_CommandOutput): 命令执行结果输出对象
            result (T_CommandCallback): 命令各项参数获取的结果

        Args:
            callback: 注册的这个命令被执行时，接口自动调用的回调函数

        Returns:
            是否成功设置
        """
    def setup(self) -> bool:
        """
        安装指令

        在对命令的所有配置完成之后，使用此函数将命令注册到 BDS 的命令系统当中

        Returns:
            是否成功安装
        """
    def setSoftEnum(self, name: str, enums: str) -> str: ...
    def addSoftEnumValues(self, name: str, enums: str) -> bool: ...
    def removeSoftEnumValues(self, name: str, enums: str) -> bool: ...
    def getSoftEnumValues(self, name: str) -> list[str]: ...
    def getSoftEnumNames(self) -> list[str]: ...

    # BaseLib.py
    @typing.overload
    def handle(
        self,
        func: None = None,
    ) -> Callable[[_T_ArgCallback], _T_ArgCallback]: ...
    @typing.overload
    def handle(self, func: _T_ArgCallback) -> _T_ArgCallback:
        """
        指令回调装饰器

        来源：`BaseLib.py`

        用法：

        ```py
        @cmd.handle
        def _(_, ori: LLSE_CommandOrigin, out: LLSE_CommandOutput, result: dict[str, Any]):
            ...
        ```
        """

Command = LLSE_Command
