from typing import Literal, NoReturn, overload

from typing_extensions import deprecated

from llpy import IniConfigFile, JsonConfigFile, KVDatabase
from llpy.types import T_ToJsonType

from .types import T_PlayerInfo

class data:
    """数据处理 API"""

    def __init__(self) -> NoReturn: ...
    @staticmethod
    def xuid2name(xuid) -> str | None:
        """
        根据 XUID 查询玩家名

        Args:
            xuid: 要查询的玩家 XUID

        Returns:
            玩家名。如果返回值为 `None`，则代表查询失败
        """
    @staticmethod
    def name2xuid(name: str) -> str | None:
        """
        根据玩家名查询 XUID

        Args:
            name: 要查询的玩家名

        Returns:
            玩家的 XUID。如果返回值为 `None`，则代表查询失败
        """
    @staticmethod
    def xuid2uuid(xuid: str) -> str | None:
        """
        根据 XUID 查询玩家 UUID

        Args:
            xuid: 要查询的玩家 XUID

        Returns:
            玩家的 UUID。如果返回值为 `None`，则代表查询失败
        """
    @staticmethod
    def name2uuid(name: str) -> str | None:
        """
        根据玩家名查询 UUID

        Args:
            name: 要查询的玩家名

        Returns:
            玩家的 UUID。如果返回值为 `None`，则代表查询失败
        """
    @staticmethod
    def getAllPlayerInfo() -> list[T_PlayerInfo]:
        """
        获取所有的玩家信息

        Returns:
            所有的玩家信息
        """
    @staticmethod
    def parseJson(json: str) -> T_ToJsonType | None:
        """
        JSON 字符串解析为变量

        Args:
            json: 要转换为变量的 JSON 字符串

        Returns:
            转换成的变量。如果返回值为 `None`，则代表转换失败
        """
    @staticmethod
    def toJson(var: T_ToJsonType, space: int = 0) -> str | None:
        """
        变量转换为 JSON 字符串

        Args:
            var: 要转换为 JSON 字符串的变量
            space: 每个缩进的空格数量，如果要格式化输出的字符串，则传入此参数。此参数默认为 `0`，即不对输出字符串进行格式化

        Returns:
            转换成的 JSON 字符串。如果返回值为 `None`，则代表转换失败
        """
    @staticmethod
    def toMD5(data: str | bytearray) -> str:
        """
        MD5 计算

        Args:
            data: 要计算 MD5 的字符串 / 字节数组

        Returns:
            原数据的 MD5 摘要字符串
        """
    @staticmethod
    def toSHA1(data: str | bytearray) -> str:
        """
        SHA1 计算

        Args:
            data: 要计算 SHA1 的字符串 / 字节数组

        Returns:
            原数据的 SHA1 摘要字符串
        """
    @staticmethod
    def toBase64(data: str | bytearray) -> str:
        """
        数据转 Base64

        Args:
            data: 要转化为 Base64 的字符串 / 字节数组

        Returns:
            Base64 结果
        """
    @overload
    @staticmethod
    def fromBase64(base64: str, is_binary: Literal[False] = False) -> str:
        """
        Base64 解码为数据

        Args:
            base64: 要解码的 Base64 字符串
            is_binary: 返回数据类型是否为二进制数据，默认为 `False`

        Returns:
            解码后的文本
        """
    @overload
    @staticmethod
    def fromBase64(base64: str, is_binary: Literal[True]) -> bytearray:
        """
        Base64 解码为数据

        Args:
            base64: 要解码的 Base64 字符串
            is_binary: 返回数据类型是否为二进制数据，默认为 `False`

        Returns:
            解码后的数据
        """
    @deprecated("请使用 `KVDatabase()`")
    @staticmethod
    def openDB(db_dir: str) -> KVDatabase: ...
    @deprecated("请使用 `JsonConfigFile()`")
    @overload
    @staticmethod
    def openConfig(
        path: str,
        conf_type: Literal["json"],
        default: str,
    ) -> JsonConfigFile | None: ...
    @deprecated("请使用 `IniConfigFile()`")
    @overload
    @staticmethod
    def openConfig(
        path: str,
        conf_type: Literal["ini"],
        default: str,
    ) -> IniConfigFile | None: ...
