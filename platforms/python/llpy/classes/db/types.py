from typing import Any, Callable, Literal, TypedDict

from typing_extensions import NotRequired

T_DBType = Literal["sqlite3"]
"""DBSession 数据库类型"""


class T_DBConnectParam(TypedDict):
    path: str
    """指定数据库所在路径"""
    create: NotRequired[bool]
    """数据库不存在是否自动创建（默认 `True`）"""
    readonly: NotRequired[bool]
    """以只读模式打开（默认 `False`）"""
    readwrite: NotRequired[bool]
    """以读写模式打开（默认 `True`）"""


T_DBFetchAllCallback = Callable[[dict[str, Any]], bool]
