from typing import TypeVar, overload

from ..types import T_ToIniType

_T_DefaultVal = TypeVar("_T_DefaultVal", bound=T_ToIniType)

class IniConfigFile:
    """Ini 格式配置文件"""

    @overload
    def __init__(self, path: str) -> None:
        """
        创建 / 打开一个 Ini 配置文件

        如果创建 / 打开失败，将抛出异常。

        我们建议你在 `BDS根目录/plugins/插件名字/` 目录下建立名为 `config.ini` 的配置文件，以保持各插件的配置统一

        Args:
            path: 配置文件所在路径，以 BDS 根目录为基准。如果配置文件路径中有目录尚不存在，脚本引擎会自动创建
        """
    @overload
    def __init__(self, path: str, default: str) -> None:
        """
        创建 / 打开一个 Ini 配置文件

        如果创建 / 打开失败，将抛出异常。

        我们建议你在 `BDS根目录/plugins/插件名字/` 目录下建立名为 `config.ini` 的配置文件，以保持各插件的配置统一

        Args:
            path: 配置文件所在路径，以 BDS 根目录为基准。如果配置文件路径中有目录尚不存在，脚本引擎会自动创建
            default: 配置文件的默认内容。如果初始化时目标文件不存在，引擎将新建一个配置文件并将此处的默认内容写入文件中。如果不传入此参数，新建时的配置文件将为空
        """
    def init(
        self,
        section: str,
        name: str,
        default: _T_DefaultVal,
    ) -> T_ToIniType | _T_DefaultVal:
        """
        初始化配置项（方便函数）

        这里提供了一种简便的方法来初始化配置文件，避免了需要手写默认配置文件内容的麻烦

        如果 `init` 访问的配置项不存在，那么引擎将在配置文件中自动创建此项，并写入给出的默认值；
        如果 `init` 访问的配置项已经存在，引擎将读取并返回配置文件中已有的值

        Args:
            section: 配置项键名
            name: 配置项名字
            default: 配置项初始化时写入的值

        Returns:
            指定配置项的数据
        """
    def set(self, section: str, name: str, data: T_ToIniType) -> bool:
        """
        写入配置项

        如果配置项不存在，接口会自动创建

        Args:
            section: 配置项键名
            name: 配置项名字
            data: 要写入的配置数据

        Returns:
            是否写入成功
        """
    def getStr(
        self,
        section: str,
        name: str,
        default: _T_DefaultVal = 0,
    ) -> str | _T_DefaultVal:
        """
        读取字符串

        Args:
            section: 配置项键名
            name: 配置项名字
            default: 当读取失败时返回的默认值

        Returns:
            指定配置项的数据
        """
    def getInt(
        self,
        section: str,
        name: str,
        default: _T_DefaultVal = 0,
    ) -> int | _T_DefaultVal:
        """
        读取整数项

        Args:
            section: 配置项键名
            name: 配置项名字
            default: 当读取失败时返回的默认值

        Returns:
            指定配置项的数据
        """
    def getFloat(
        self,
        section: str,
        name: str,
        default: _T_DefaultVal = 0,
    ) -> float | _T_DefaultVal:
        """
        读取浮点数

        Args:
            section: 配置项键名
            name: 配置项名字
            default: 当读取失败时返回的默认值

        Returns:
            指定配置项的数据
        """
    def getBool(
        self,
        section: str,
        name: str,
        default: _T_DefaultVal = 0,
    ) -> bool | _T_DefaultVal:
        """
        读取布尔值

        Args:
            section: 配置项键名
            name: 配置项名字
            default: 当读取失败时返回的默认值

        Returns:
            指定配置项的数据
        """
    def delete(self, section: str, name: str) -> bool:
        """
        删除配置项

        如果这个配置项你不需要了，为了避免在他人修改配置文件时引起迷惑，你可以选择将它删除

        Args:
            section: 配置项键名
            name: 配置项名字

        Returns:
            是否删除成功
        """
    def reload(self) -> bool:
        """
        重新加载文件中的配置项

        为了性能考虑，配置文件接口对读操作进行缓存，每次读取操作都从直接内存中读取，而写入才会直接写入磁盘文件。
        考虑到配置文件可能被用户修改，当你确认用户已经修改配置文件之后，需要使用此函数刷新配置文件的内存缓存数据。

        Returns:
            是否成功加载
        """
    def close(self) -> bool:
        """
        关闭配置文件

        配置文件关闭之后，请勿继续使用！

        Returns:
            是否成功关闭
        """
    def getPath(self) -> str:
        """
        获取配置文件路径

        Returns:
            当前配置文件的文件路径
        """
    def read(self) -> str:
        """
        读取整个配置文件的内容

        Returns:
            当前配置文件的所有内容
        """
    def write(self, content: str) -> bool:
        """
        写入整个配置文件的内容

        Args:
            content: 写入的内容

        Returns:
            是否写入成功
        """
