from typing import overload

from llpy import NbtList

from ..types import (
    T_NbtClass,
    T_NbtType,
    T_NbtTypeCompound,
    T_ToNbtBase,
    T_ToNbtDict,
)

class NbtCompound:
    """NBT 标签对象"""

    @overload
    def __init__(self) -> None:
        """
        创建新的 NBT 标签对象

        如果创建失败，将抛出异常
        """
    @overload
    def __init__(self, default: dict[str, T_NbtClass]) -> None:
        """
        创建新的 NBT 标签对象

        如果创建失败，将抛出异常

        Args:
            default: 对象的初始值
        """
    def getKeys(self) -> list[str]:
        """
        获取所有的键

        Returns:
            Compound 中所有的键
        """
    def getTypeOf(self, key: str) -> T_NbtType | None:
        """
        获取键对应的值的数据类型

        Args:
            key: 要查询的键名

        Returns:
            对应的值的数据类型。如果要读取的 NBT 不存在，将返回 `None`
        """
    def setEnd(self, key: str) -> "NbtCompound":
        """
        设置键对应的值的具体数据

        Args:
            key: 要操作的键名。不存在会自动创建

        Returns:
            写入完毕的NBT对象 （便于连锁进行其他操作）
        """
    def setByte(self, key: str, data: int) -> "NbtCompound":
        """
        设置键对应的值的具体数据

        Args:
            key: 要操作的键名。不存在会自动创建
            data: 要写入的具体数据。数据类型必须和键对应的值储存的数据类型一致

        Returns:
            写入完毕的NBT对象 （便于连锁进行其他操作）
        """
    def setInt(self, key: str, data: int) -> "NbtCompound":
        """
        设置键对应的值的具体数据

        Args:
            key: 要操作的键名。不存在会自动创建
            data: 要写入的具体数据。数据类型必须和键对应的值储存的数据类型一致

        Returns:
            写入完毕的NBT对象 （便于连锁进行其他操作）
        """
    def setShort(self, key: str, data: int) -> "NbtCompound":
        """
        设置键对应的值的具体数据

        Args:
            key: 要操作的键名。不存在会自动创建
            data: 要写入的具体数据。数据类型必须和键对应的值储存的数据类型一致

        Returns:
            写入完毕的NBT对象 （便于连锁进行其他操作）
        """
    def setLong(self, key: str, data: int) -> "NbtCompound":
        """
        设置键对应的值的具体数据

        Args:
            key: 要操作的键名。不存在会自动创建
            data: 要写入的具体数据。数据类型必须和键对应的值储存的数据类型一致

        Returns:
            写入完毕的NBT对象 （便于连锁进行其他操作）
        """
    def setFloat(self, key: str, data: float) -> "NbtCompound":
        """
        设置键对应的值的具体数据

        Args:
            key: 要操作的键名。不存在会自动创建
            data: 要写入的具体数据。数据类型必须和键对应的值储存的数据类型一致

        Returns:
            写入完毕的NBT对象 （便于连锁进行其他操作）
        """
    def setDouble(self, key: str, data: float) -> "NbtCompound":
        """
        设置键对应的值的具体数据

        Args:
            key: 要操作的键名。不存在会自动创建
            data: 要写入的具体数据。数据类型必须和键对应的值储存的数据类型一致

        Returns:
            写入完毕的NBT对象 （便于连锁进行其他操作）
        """
    def setString(self, key: str, data: str) -> "NbtCompound":
        """
        设置键对应的值的具体数据

        Args:
            key: 要操作的键名。不存在会自动创建
            data: 要写入的具体数据。数据类型必须和键对应的值储存的数据类型一致

        Returns:
            写入完毕的NBT对象 （便于连锁进行其他操作）
        """
    def setByteArray(self, key: str, data: bytearray) -> "NbtCompound":
        """
        设置键对应的值的具体数据

        Args:
            key: 要操作的键名。不存在会自动创建
            data: 要写入的具体数据。数据类型必须和键对应的值储存的数据类型一致

        Returns:
            写入完毕的NBT对象 （便于连锁进行其他操作）
        """
    def setTag(self, key: str, tag: T_NbtClass) -> bool:
        """
        设置键对应的 NBT 对象

        Args:
            key: 要操作的键名。不存在会自动创建
            tag: 要写入的 NBT 对象。数据类型必须和键对应的值储存的数据类型一致

        Returns:
            是否成功写入
        """
    def removeTag(self, key: str) -> "NbtCompound":
        """
        删除键对应的 NBT 对象

        Args:
            key: 要操作的键名。键名必须已经存在

        Returns:
            处理完毕的NBT对象（便于连锁进行其他操作）
        """
    def getData(self, key: str) -> T_ToNbtBase | NbtList | NbtCompound | None:
        """
        读取键对应的值的具体数据

        Args:
            key: 要操作的键名

        Returns:
            键对应的值的具体数据。如果要读取的 NBT 不存在，将返回 `None`
        """
    def getTag(self, key: str) -> T_NbtType | None:
        """
        读取键对应的 NBT 对象

        Args:
            key: 要操作的键名

        Returns:
            键对应的 NBT 对象。如果要读取的 NBT 不存在，将返回 `None`
        """
    def toObject(self) -> T_ToNbtDict:
        """
        将 NBT 标签对象 转换为 Object

        将 `Compound` 的内容转换为脚本引擎对象，把数据项都转换为脚本引擎数据类型储存于对象的对应 key 中，方便读取和处理

        如果 `Compound` 某一项储存的是 `List` 或者 `Compound` 类型的 NBT，将在对应位置递归展开为 `Array` 或 `Object`

        Returns:
            对应的对象 / 表
        """
    def toSNBT(self, indent: int = -1) -> str:
        """
        将 NBT 标签对象 序列化为 SNBT

        Args:
            indent: 每个缩进的空格数量，如果要格式化输出的字符串，则传入此参数。此参数默认为 `-1`，即不对输出字符串进行格式化

        Returns:
            对应的SNBT字符串
        """
    def toBinaryNBT(self) -> bytearray:
        """
        将 NBT 标签对象 序列化为二进制 NBT

        只有完整的顶层 Compound 标签可以被转换为二进制NBT

        Returns:
            对应的二进制NBT数据
        """
    def destroy(self) -> bool:
        """
        销毁此 NBT 标签对象

        注意，只有根 Compound 标签可以被销毁，而且，请谨慎使用此函数，不当的使用将会造成服务器崩溃

        合适的销毁有助于解决内存占用问题。在销毁完后，请千万不要再使用此 NBT 对象和他的所有子对象

        Returns:
            是否成功清理
        """
    def getType(self) -> T_NbtTypeCompound: ...
    def toString(self, indent: int = -1) -> str: ...
