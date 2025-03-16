from typing import Any, Callable, NoReturn, overload

from .types import T_PluginInfo, T_VersionStatus

class ll:
    """加载器相关接口"""

    def __init__(self) -> NoReturn: ...

    language: str
    """LiteLoaderBDS使用的语言。(例如 `zh_Hans`、`en` 和 `ru_RU`)"""
    major: int
    """主版本号（如 2.1.0 里的 2）"""
    minor: int
    """次版本号（如 2.1.0 里的 1）"""
    revision: int
    """修订版本号（如 2.1.0 里的 0）"""
    status: T_VersionStatus
    """版本状态"""
    scriptEngineVersion: str
    """LiteLoaderBDS Script Engine版本"""
    isWine: bool
    """是否处于 Wine 环境下"""
    isDebugMode: bool
    """是否处于 debug 模式"""
    isBeta: bool
    """当前版本是否为测试版"""
    isDev: bool
    """当前版本是否为开发版"""
    isRelease: bool
    """当前版本是否为发布版本"""

    @staticmethod
    def versionString() -> str:
        """
        获取 LiteLoaderBDS 版本字符串

        Returns:
            加载器版本
        """
    @staticmethod
    def requireVersion(major: int, minor: int = 0, revision: int = 0) -> bool:
        """
        检查 LiteLoaderBDS 版本

        如果检测发现当前安装的脚本引擎版本低于传入的数值，将返回 `False`。
        你可以选择根据结果判断并报错，提醒用户升级自己的 LiteLoaderBDS 版本

        Args:
            major: 检查当前已安装 LiteLoaderBDS 的主版本号是否 >= 此值
            minor: 检查当前已安装 LiteLoaderBDS 的次版本号是否 >= 此值
            revision: 检查当前已安装 LiteLoaderBDS 的修订版本号是否 >= 此值

        Returns:
            检查结果
        """
    @staticmethod
    def getPluginInfo(name: str) -> T_PluginInfo | None:
        """
        获取有关插件的信息

        Args:
            name: 插件名称

        Returns:
            插件信息对象
        """
    @staticmethod
    def listPlugins() -> list[str]:
        """
        列出所有已加载的插件

        Returns:
            已加载的所有的插件名字列表
        """
    @staticmethod
    def getAllPluginInfo() -> list[T_PluginInfo]:
        """
        列出所有加载的插件信息

        Returns:
            包含所有已加载插件的插件对象的列表
        """
    @overload
    @staticmethod
    def exports(func: Callable[..., Any], namespace: str, name: str) -> bool:
        """
        导出函数

        注意：如果导出的函数的命名空间和名字与另一个已经导出的函数完全相同，将会导出失败。

        Args:
            func: 要导出的函数
            namespace: 函数的命名空间名，只是方便用于区分不同插件导出的API
            name: 函数的导出名称。其他插件根据导出名称来调用这个函数

        Returns:
            是否成功导出
        """
    @overload
    @staticmethod
    def exports(func: Callable[..., Any], name: str) -> bool:
        """
        导出函数

        注意：如果导出的函数的命名空间和名字与另一个已经导出的函数完全相同，将会导出失败。

        Args:
            func: 要导出的函数
            name: 函数的导出名称。其他插件根据导出名称来调用这个函数

        Returns:
            是否成功导出
        """
    @overload
    @staticmethod
    def imports(namespace: str, name: str) -> Callable[..., Any]:
        """
        导入函数

        `ll.import` 的返回值是一个函数。
        当你调用这个函数时，跨插件调用的流程将在后台自动完成。
        调用函数的参数将被包装并传递给远程函数，此函数的返回值即是远程函数执行完毕之后返回的返回值。

        注意：在调用函数的时候，需要保证你传入的参数和目标函数接受的参数数量和类型都是正确且一一对应的。
        否则，将会发生错误。

        Args:
            namespace: 要导入的函数使用的命名空间名称
            name: 要导入的函数使用的导出名称

        Returns:
            导入的函数
        """
    @overload
    @staticmethod
    def imports(name: str) -> Callable[..., Any]:
        """
        导入函数

        `ll.import` 的返回值是一个函数。
        当你调用这个函数时，跨插件调用的流程将在后台自动完成。
        调用函数的参数将被包装并传递给远程函数，此函数的返回值即是远程函数执行完毕之后返回的返回值。

        注意：在调用函数的时候，需要保证你传入的参数和目标函数接受的参数数量和类型都是正确且一一对应的。
        否则，将会发生错误。

        Args:
            name: 要导入的函数使用的导出名称

        Returns:
            导入的函数
        """
    @overload
    @staticmethod
    def hasExported(namespace: str, name: str) -> bool:
        """
        判断远程函数是否已导出

        Args:
            namespace: 函数使用的命名空间名称
            name: 函数使用的导出名称

        Returns:
            函数是否已导出
        """
    @overload
    @staticmethod
    def hasExported(name: str) -> bool:
        """
        判断远程函数是否已导出

        Args:
            name: 函数使用的导出名称

        Returns:
            函数是否已导出
        """
    @overload
    @staticmethod
    def require(path: str) -> bool:
        """
        设置插件依赖库

        有的时候，你需要确保某些插件在你自己的插件之前加载，以使用他们提供的前置服务，我们称这些前置插件为依赖库。

        Args:
            path: 依赖库文件名

        Returns:
            是否加载依赖库成功
        """
    @overload
    @staticmethod
    def require(path: str, remote_path: str) -> bool:
        """
        设置插件依赖库

        有的时候，你需要确保某些插件在你自己的插件之前加载，以使用他们提供的前置服务，我们称这些前置插件为依赖库。

        Args:
            path: 依赖库文件名
            remote_path: 查找并装载依赖库的路径。如果搜索依赖库完毕之后未发现对应的依赖库文件，则使用 HTTP(s) 协议请求 `remote_path` 参数对应的下载地址，并下载依赖库文件到 `plugins/lib` 目录。

        Returns:
            是否加载依赖库成功
        """
    @staticmethod
    def eval(code: str) -> Any:
        """
        将字符串作为脚本代码执行

        此处执行的脚本代码是在当前插件对应的引擎中直接执行的，类似于各语言的 `eval` 机制

        Args:
            code: 要作为脚本代码执行的字符串

        Returns:
            执行结果
        """
    @staticmethod
    def registerPlugin(
        name: str,
        introduction: str,
        version: list[int],
        other_information: dict[str, str],
    ):
        """
        注册插件

        Args:
            name: 插件名字
            introduction: 对插件的简短介绍
            version: 插件的版本信息 `[major (int), minor (int), revision (int), status (Version)]`
            other_information: 其他你愿意提供的的附加信息（如许可证、开源地址等）
        """
