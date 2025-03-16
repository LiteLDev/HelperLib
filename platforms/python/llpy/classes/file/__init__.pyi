from typing import Any, Callable, Generic, Literal, TypeVar, overload

from typing_extensions import deprecated

from .types import (
    T_FileOpenMode,
    T_FileOpenModeAppend,
    T_FileOpenModeRead,
    T_FileOpenModeWrite,
)

_T_Mode = TypeVar("_T_Mode", str, bytearray)

class File(Generic[_T_Mode]):
    """文件对象"""

    # region static
    ReadMode: T_FileOpenModeRead
    WriteMode: T_FileOpenModeWrite
    AppendMode: T_FileOpenModeAppend

    @staticmethod
    def readFrom(path: str) -> str | None:
        """
        读入文件的所有内容

        Args:
            path: 目标文件的路径，相对路径以 BDS 根目录为基准

        Returns:
            文件的所有数据。如返回值为 `None` 则表示读取失败
        """
    @staticmethod
    def writeTo(path: str, text: str) -> bool:
        """
        向指定文件写入内容

        注意：若文件不存在会自动创建，若存在则会先将其 **清空** 再写入

        Args:
            path: 目标文件的路径，相对路径以 BDS 根目录为基准
            text: 要写入的内容

        Returns:
            是否写入成功
        """
    @overload
    @staticmethod
    def writeLine(path: str, text: str) -> bool:
        """
        向指定文件追加一行

        Args:
            path: 目标文件的路径，相对路径以 BDS 根目录为基准
            text: 要写入的内容

        Returns:
            是否写入成功
        """
    @staticmethod
    def createDir(dir_path: str) -> bool:
        """
        创建文件夹

        Args:
            dir_path: 目标文件夹的路径，可以直接创建多层，不需要逐层创建。相对路径以 BDS 根目录为基准

        Returns:
            是否成功创建
        """
    @staticmethod
    def mkdir(dir_path: str) -> bool:
        """
        创建文件夹

        Args:
            dir_path: 目标文件夹的路径，可以直接创建多层，不需要逐层创建。相对路径以 BDS 根目录为基准

        Returns:
            是否成功创建
        """
    @staticmethod
    def copy(from_path: str, to_path: str) -> bool:
        """
        复制文件 / 文件夹到指定位置

        Args:
            from_path: 源文件 / 文件夹的路径，相对路径以 BDS 根目录为基准
            to_path: 目标文件 / 文件夹的位置，相对路径以 BDS 根目录为基准

        Returns:
            是否复制成功
        """
    @staticmethod
    def move(from_path: str, to_path: str) -> bool:
        """
        移动文件 / 文件夹到指定位置

        Args:
            from_path: 源文件 / 文件夹的路径，相对路径以 BDS 根目录为基准
            to_path: 目标文件 / 文件夹的位置，相对路径以 BDS 根目录为基准

        Returns:
            是否移动成功
        """
    @staticmethod
    def rename(from_path: str, to_path: str) -> bool:
        """
        重命名指定文件 / 文件夹

        Args:
            from_path: 源文件 / 文件夹的路径，相对路径以 BDS 根目录为基准
            to_path: 目标文件 / 文件夹的位置，相对路径以 BDS 根目录为基准

        Returns:
            是否重命名成功
        """
    @staticmethod
    def delete(path: str) -> bool:
        """
        删除文件 / 文件夹

        Args:
            path: 目标文件 / 文件夹的路径，相对路径以 BDS 根目录为基准

        Returns:
            是否成功删除
        """
    @staticmethod
    def exists(path: str) -> bool:
        """
        判断文件 / 文件夹是否存在

        Args:
            path: 目标文件 / 文件夹的路径，相对路径以 BDS 根目录为基准

        Returns:
            目标是否存在
        """
    @staticmethod
    def checkIsDir(path: str) -> bool:
        """
        判断指定路径是否是文件夹

        如果目标路径不存在，同样将返回 `False`

        Args:
            path: 所判断的路径，相对路径以 BDS 根目录为基准

        Returns:
            目标路径是否是文件夹
        """
    @staticmethod
    def getFileSize(path: str) -> int:
        """
        获取指定文件的大小

        如果传入的路径位置是一个文件夹，则返回 `-1`

        Args:
            path: 所操作的文件路径，相对路径以 BDS 根目录为基准

        Returns:
            文件的大小（字节）
        """
    @staticmethod
    def getFilesList(dir_path: str) -> list[str]:
        """
        列出指定文件夹下的所有文件 / 文件夹

        Args:
            dir_path: 文件夹路径，相对路径以 BDS 根目录为基准

        Returns:
            文件名、文件夹名 数组
        """
    # endregion

    # region instance
    def __init__(
        self,
        path: str,
        mode: T_FileOpenMode,
        is_binary: bool = False,
    ) -> None:
        """
        创建一个新的文件对象

        类型注：当 `is_binary` 为 `False` 时，返回 `File[str]`；
        当 `is_binary` 为 `True` 时，返回 `File[bytearray]`

        Args:
            path: 想要打开的文件路径
            mode: 文件的打开模式
            is_binary: 是否以二进制模式打开文件
                普通模式下，文件读写过程中，换行符将会被按本地格式转换。
                如果你使用二进制模式打开文件，表明此文件并非普通的文本格式，这些自动转换将不会发生。
        """
    @property
    def path(self) -> str:
        """当前文件路径"""
    @property
    def absolutePath(self) -> str:
        """当前文件的绝对路径"""
    @property
    def size(self) -> int:
        """当前文件大小"""
    def readSync(self, cnt: int) -> _T_Mode | None:
        """
        从文件读取文本 / 二进制数据

        从当前文件指针处开始读取

        Args:
            cnt: 要读取的字符数 / 字节数

        Returns:
            读取的字符串内容 / 二进制数据。如返回值为 `None` 则表示读取失败
        """
    def readLineSync(self) -> str | None:
        """
        从文件读取一行文本

        注意，字符串尾部的换行符要自行处理

        Returns:
            读取的字符串内容。如返回值为 `None` 则表示读取失败
        """
    def readAllSync(self) -> _T_Mode | None:
        """
        从文件读取所有内容

        从当前文件指针处开始读取，一直读取到文件末尾为止。

        Returns:
            读取的字符串内容 / 二进制数据。如返回值为 `None` 则表示读取失败
        """
    def writeSync(self, data: _T_Mode) -> bool:
        """
        写入文本 / 二进制数据到文件

        Args:
            data: 要写入的内容

        Returns:
            是否成功写入
        """
    def writeLineSync(self, string: str) -> bool:
        """
        写入一行文本到文件

        此函数执行时，将在字符串尾自动添加换行符

        Args:
            string: 要写入的内容

        Returns:
            是否成功写入
        """
    def read(self, cnt: int, callback: Callable[[_T_Mode | None], Any]) -> bool:
        """
        从文件读取文本 / 二进制数据（异步）

        从当前文件指针处开始读取

        Callback Args:
            result (_T_Mode | None): 读取到的文本 / 二进制数据。如为 `None` 则表示读取失败

        Args:
            cnt: 要读取的字符数 / 字节数
            callback: 获取结果的回调函数

        Returns:
            是否成功发送请求
        """
    def readLine(self, callback: Callable[[str | None], Any]) -> bool:
        """
        从文件读取一行文本（异步）

        注意，字符串尾部的换行符要自行处理

        Callback Args:
            result (str | None): 读取到的文本。如为 `None` 则表示读取失败

        Args:
            callback: 获取结果的回调函数

        Returns:
            是否成功发送请求
        """
    def readAll(self, callback: Callable[[_T_Mode | None], Any]) -> bool:
        """
        从文件读取所有内容（异步）

        从当前文件指针处开始读取，一直读取到文件末尾为止

        Callback Args:
            result (_T_Mode | None): 读取到的文本 / 二进制数据。如为 `None` 则表示读取失败

        Args:
            callback: 获取结果的回调函数

        Returns:
            是否成功发送请求
        """
    @overload
    def write(self, data: _T_Mode) -> bool:
        """
        写入文本 / 二进制数据到文件（异步）

        Args:
            data: 要写入的内容

        Returns:
            是否成功发送请求
        """
    @overload
    def write(self, data: _T_Mode, callback: Callable[[bool], Any]) -> bool:
        """
        写入文本 / 二进制数据到文件（异步）

        Callback Args:
            result (bool): 是否写入成功

        Args:
            data: 要写入的内容
            callback: 获取结果的回调函数

        Returns:
            是否成功发送请求
        """
    @overload
    def writeLine(self, string: str) -> bool:
        """
        写入一行文本到文件（异步）

        此函数执行时，将在字符串尾自动添加换行符

        Args:
            string: 要写入的内容

        Returns:
            是否写入成功
        """
    @overload
    def writeLine(self, string: str, callback: Callable[[bool], Any]) -> bool:
        """
        写入一行文本到文件（异步）

        此函数执行时，将在字符串尾自动添加换行符

        Callback Args:
            result (bool): 是否写入成功

        Args:
            string: 要写入的内容
            callback: 获取结果的回调函数

        Returns:
            是否写入成功
        """
    def isEOF(self) -> bool:
        """
        文件指针是否位于文件尾

        Returns:
            文件指针是否处于文件尾
        """
    def seekTo(self, pos: int, is_relative: bool) -> bool:
        """
        移动文件指针

        Args:
            pos: 文件指针要移动到的位置
            is_relative: 是否是相对当前文件指针位置移动
                如果为 `True`，`pos` 表示相对当前位置移动，正数为向后移动，负数为向前移动
                如果为 `False`，`pos` 表示相对文件开头移动，为 `0` 或正数。如果为 `-1`，表示移动到文件末尾

        Returns:
            是否移动成功
        """
    def setSize(self, size: int) -> bool:
        """
        设定文件大小

        设定的新大小可以大于文件的当前大小。如果设定的新大小 小于文件的当前大小，原文件将被截断。

        Args:
            size: 要设定的目标大小

        Returns:
            是否设定成功
        """
    def close(self) -> bool:
        """
        关闭文件

        文件关闭后，严禁再次使用

        Returns:
            是否成功关闭
        """
    def flush(self) -> bool:
        """
        刷新文件缓冲区

        Returns:
            是否成功刷新
        """
    def errorCode(self) -> int:
        """
        获取错误码

        如果在上述接口使用中遇到了失败，可以从这里获取上一个错误码

        Returns:
            上一次 IO 操作产生的错误码
        """
    def clear(self) -> bool:
        """
        清除错误状态

        如果在上述接口使用中遇到了失败，在获取错误码完成之后，使用此函数清除错误状态，以继续正常使用文件对象

        Returns:
            是否成功清除
        """
    # endregion

    @deprecated("请使用 `File` 的构造函数")
    @overload
    @staticmethod
    def open(
        path: str,
        mode: T_FileOpenMode,
        is_binary: bool = False,
    ) -> File[str]: ...
    @deprecated("请使用 `File` 的构造函数")
    @overload
    @staticmethod
    def open(
        path: str,
        mode: T_FileOpenMode,
        is_binary: Literal[True],
    ) -> File[bytearray]: ...
