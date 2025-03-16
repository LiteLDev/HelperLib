from typing import NoReturn, overload

from typing_extensions import deprecated

from llpy import LLSE_Item, NativePointer

class LLSE_Container:
    """
    容器对象

    注意！在修改完玩家物品栏对应的物品之后，不要忘记使用玩家对象的成员函数 `LLSE_Player.refreshItems()`，刷新客户端显示的玩家物品栏
    """

    def __init__(self) -> NoReturn: ...
    @property
    def size(self) -> int:
        """容器拥有的格子总数"""
    @property
    def type(self) -> str:
        """容器的类型名"""
    @overload
    def addItem(self, item: LLSE_Item) -> bool:
        """
        放入物品对象到容器中

        Args:
            item: 待增加的物品对象

        Returns:
            是否成功增加
        """
    @overload
    def addItem(self, item: LLSE_Item, amount: int) -> bool:
        """
        放入物品对象到容器中

        Args:
            item: 待增加的物品对象
            amount: 欲添加物品数量，`item` 对象本身的 `count` 属性将被忽略。

        Returns:
            是否成功增加
        """
    def addItemToFirstEmptySlot(self, item: LLSE_Item) -> bool:
        """
        放入物品对象到容器的第一个空格子

        Args:
            item: 待增加的物品对象

        Returns:
            是否成功增加
        """
    def hasRoomFor(self, item: LLSE_Item) -> bool:
        """
        检查容器中是否（有空间）可以放入此物品

        Args:
            item: 待放入的物品对象

        Returns:
            是否可以放入
        """
    def removeItem(self, index: int, count: int) -> bool:
        """
        减少容器中的某个物品对象

        Args:
            index: 减少的物品对象所在的格子序号
            count: 减少的数量。如果大于等于此格子物品堆叠的数量，则物品堆将被整个清除

        Returns:
            是否成功减少
        """
    def getItem(self, index: int) -> LLSE_Item:
        """
        获取容器某个格子的物品对象

        此处获取的物品对象为引用。也就是说，修改此处返回的物品对象，或使用其 API，就相当于直接操作容器中对应的物品

        Args:
            index: 待获取的格子序号

        Returns:
            格子位置的物品对象
        """
    def setItem(self, index: int, item: LLSE_Item) -> bool:
        """
        设置容器某个格子的物品对象

        Args:
            index: 待设置的格子序号
            item: 待设置的物品对象

        Returns:
            是否设置成功
        """
    def getAllItems(self) -> list[LLSE_Item]:
        """
        获取容器所有格子的物品对象列表

        此处获取的物品对象为引用。也就是说，修改此处返回的物品对象，或使用其 API，就相当于直接操作容器中对应的物品

        Returns:
            容器中所有的物品对象
        """
    def removeAllItems(self) -> bool:
        """
        清空容器

        Returns:
            是否成功清空
        """
    def isEmpty(self) -> bool:
        """
        判断容器是否为空

        Returns:
            当前容器是否为空
        """
    def asPointer(self) -> NativePointer: ...
    @deprecated("请使用 `LLSE_Container.getItem()`")
    def getSlot(self, index: int) -> LLSE_Item: ...
    @deprecated("请使用 `LLSE_Container.getAllItems()`")
    def getAllSlots(self) -> list[LLSE_Item]: ...

Container = LLSE_Container
