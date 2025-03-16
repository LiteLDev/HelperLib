from typing import overload

from llpy import NbtCompound

from ..types import T_NbtClass, T_NbtType, T_NbtTypeList, T_ToNbtBase, T_ToNbtList

class NbtList:
    """NBT 列表对象"""

    @overload
    def __init__(self) -> None:
        """
        创建新的 NBT 列表对象

        如果创建失败，将抛出异常
        """
    @overload
    def __init__(self, default: list[T_NbtClass]) -> None:
        """
        创建新的 NBT 列表对象

        如果创建失败，将抛出异常

        Args:
            default: 对象的初始值
        """
    def getSize(self) -> int:
        """
        获取列表长度

        Returns:
            此列表的长度
        """
    def getTypeOf(self, index: int) -> T_NbtType | None:
        """
        获取某个下标位置储存的数据类型

        Args:
            index: 要查询的目标下标

        Returns:
            此下标处储存的 NBT 的数据类型。如果要读取的 NBT 不存在，将返回 `None`
        """
    def setEnd(self, index: int) -> "NbtList":
        """
        设置某个下标位置的具体数据

        Args:
            index: 要操作的目标下标

        Returns:
            写入完毕的 NBT 列表（便于连锁进行其他操作）
        """
    def setByte(self, index: int, data: int) -> "NbtList":
        """
        设置某个下标位置的具体数据

        Args:
            index: 要操作的目标下标
            data: 要写入的具体数据。写入的数据类型必须和下标位置储存的数据类型一致，且下标不能超出有效下标的最大值

        Returns:
            写入完毕的 NBT 列表（便于连锁进行其他操作）
        """
    def setInt(self, index: int, data: int) -> "NbtList":
        """
        设置某个下标位置的具体数据

        Args:
            index: 要操作的目标下标
            data: 要写入的具体数据。写入的数据类型必须和下标位置储存的数据类型一致，且下标不能超出有效下标的最大值

        Returns:
            写入完毕的 NBT 列表（便于连锁进行其他操作）
        """
    def setShort(self, index: int, data: int) -> "NbtList":
        """
        设置某个下标位置的具体数据

        Args:
            index: 要操作的目标下标
            data: 要写入的具体数据。写入的数据类型必须和下标位置储存的数据类型一致，且下标不能超出有效下标的最大值

        Returns:
            写入完毕的 NBT 列表（便于连锁进行其他操作）
        """
    def setLong(self, index: int, data: int) -> "NbtList":
        """
        设置某个下标位置的具体数据

        Args:
            index: 要操作的目标下标
            data: 要写入的具体数据。写入的数据类型必须和下标位置储存的数据类型一致，且下标不能超出有效下标的最大值

        Returns:
            写入完毕的 NBT 列表（便于连锁进行其他操作）
        """
    def setFloat(self, index: int, data: float) -> "NbtList":
        """
        设置某个下标位置的具体数据

        Args:
            index: 要操作的目标下标
            data: 要写入的具体数据。写入的数据类型必须和下标位置储存的数据类型一致，且下标不能超出有效下标的最大值

        Returns:
            写入完毕的 NBT 列表（便于连锁进行其他操作）
        """
    def setDouble(self, index: int, data: float) -> "NbtList":
        """
        设置某个下标位置的具体数据

        Args:
            index: 要操作的目标下标
            data: 要写入的具体数据。写入的数据类型必须和下标位置储存的数据类型一致，且下标不能超出有效下标的最大值

        Returns:
            写入完毕的 NB 列表（便于连锁进行其他操作）
        """
    def setString(self, index: int, data: str) -> "NbtList":
        """
        设置某个下标位置的具体数据

        Args:
            index: 要操作的目标下标
            data: 要写入的具体数据。写入的数据类型必须和下标位置储存的数据类型一致，且下标不能超出有效下标的最大值

        Returns:
            写入完毕的 NBT 列表（便于连锁进行其他操作）
        """
    def setByteArray(self, index: int, data: bytearray) -> "NbtList":
        """
        设置某个下标位置的具体数据

        Args:
            index: 要操作的目标下标
            data: 要写入的具体数据。写入的数据类型必须和下标位置储存的数据类型一致，且下标不能超出有效下标的最大值

        Returns:
            写入完毕的 NBT 列表（便于连锁进行其他操作）
        """
    def setTag(self, index: int, tag: T_NbtClass) -> "NbtList":
        """
        设置某个下标位置的 NBT 对象

        Args:
            index: 要操作的目标下标
            tag: 要写入的 NBT 对象。写入对象的数据类型必须和下标位置储存的数据类型一致，且下标不能超出有效下标的最大值

        Returns:
            写入完毕的 NBT 列表（便于连锁进行其他操作）
        """
    def addTag(self, tag: T_NbtClass) -> "NbtList":
        """
        往列表末尾追加一个 NBT 对象

        Args:
            tag: 要追加的 NBT 对象

        Returns:
            追加完毕的 NBT 列表（便于连锁进行其他操作）
        """
    def removeTag(self, index: int) -> "NbtList":
        """
        删除某个下标位置的 NBT 对象

        Args:
            index: 要删除的目标下标。下标不能超出有效下标的最大值

        Returns:
            处理完毕的 NBT 列表（便于连锁进行其他操作）
        """
    def getData(self, index: int) -> T_ToNbtBase | NbtList | NbtCompound | None:
        """
        读取某个下标位置的具体数据

        Args:
            index: 要操作的目标下标

        Returns:
            指定位置储存的具体数据。如果要读取的 NBT 不存在，将返回 `None`
        """
    def getTag(self, index: int) -> T_NbtClass | None:
        """
        读取某个下标位置的 NBT 对象

        Args:
            index: 要操作的目标下标

        Returns:
            下标位置的NBT对象。如果要读取的 NBT 不存在，将返回 `None`
        """
    def toArray(self) -> T_ToNbtList:
        """
        将 List 类型转换为 Python List

        将 List 的内容转换为脚本引擎数组 / 列表，把数据项都转换为脚本引擎数据类型储存于数组 / 列表的对应下标中，方便读取和处理

        Returns:
            对应的数组 / 列表
        """
    def getType(self) -> T_NbtTypeList: ...
    def toString(self, indent: int = -1) -> str: ...
