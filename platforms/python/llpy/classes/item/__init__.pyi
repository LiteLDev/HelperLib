from typing import NoReturn

from typing_extensions import deprecated

from llpy import NativePointer, NbtCompound

class LLSE_Item:
    """物品对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def name(self) -> str:
        """游戏内显示的物品名称"""
    @property
    def type(self) -> str:
        """物品标准类型名"""
    @property
    def id(self) -> int:
        """物品的游戏内 id"""
    @property
    def count(self) -> int:
        """这个物品对象堆叠的个数"""
    @property
    def aux(self) -> int:
        """物品附加值（如羊毛颜色）"""
    @property
    def damage(self) -> int:
        """物品当前耐久"""
    @property
    def lore(self) -> list[str]:
        """物品 Lore"""
    @property
    def attackDamage(self) -> int:
        """物品攻击伤害"""
    @property
    def maxDamage(self) -> int:
        """物品最大耐久"""
    @property
    def maxStackSize(self) -> int:
        """物品最大堆叠数量"""
    @property
    def isArmorItem(self) -> bool:
        """物品是否为盔甲"""
    @property
    def isBlock(self) -> bool:
        """物品是否为方块"""
    @property
    def isDamageableItem(self) -> bool:
        """物品是否可被破坏"""
    @property
    def isDamaged(self) -> bool:
        """物品耐久是否被消耗OC"""
    @property
    def isEnchanted(self) -> bool:
        """物品是否已被附魔"""
    @property
    def isEnchantingBook(self) -> bool:
        """物品是否为附魔书"""
    @property
    def isFireResistant(self) -> bool:
        """物品是否防火"""
    @property
    def isFullStack(self) -> bool:
        """物品是否已堆叠到最大堆叠数"""
    @property
    def isGlint(self) -> bool:
        """物品是否闪烁"""
    @property
    def isHorseArmorItem(self) -> bool:
        """物品是否为马铠"""
    @property
    def isLiquidClipItem(self) -> bool:
        """Whether the item is liquid clip"""
    @property
    def isMusicDiscItem(self) -> bool:
        """物品是否为唱片"""
    @property
    def isOffhandItem(self) -> bool:
        """物品是否可设置到副手"""
    @property
    def isPotionItem(self) -> bool:
        """物品是否为药水"""
    @property
    def isStackable(self) -> bool:
        """物品是否可堆叠"""
    @property
    def isWearableItem(self) -> bool:
        """物品是否可穿戴"""
    def set(self, item: LLSE_Item) -> bool:
        """
        将此物品对象设置为另一个物品

        Args:
            item: 要赋值的物品对象

        Returns:
            是否赋值成功
        """
    def clone(self) -> LLSE_Item | None:
        """
        克隆物品对象

        根据现有的物品对象克隆一个新的物品对象

        新的物品对象与旧的对象并无关联关系

        Returns:
            生成的新物品对象。如返回值为 `None` 则表示生成失败
        """
    def isNull(self) -> bool:
        """
        判断物品对象是否为空

        比如说当某个格子没有任何物品的时候，你获取到的物品对象即是空

        Returns:
            这个物品对象是否为空
        """
    def setNull(self) -> bool:
        """
        将此物品对象置为空（删除物品）

        Returns:
            是否删除成功
        """
    def setAux(self, aux: int) -> bool:
        """
        设置物品的附加值

        Args:
            aux: 物品附加值

        Returns:
            是否设置成功
        """
    def setLore(self, names: list[int]) -> bool:
        """
        设置自定义 Lore

        Args:
            names: 要设置的 Lore 字符串的数组

        Returns:
            是否设置成功
        """
    def setDisplayName(self, name: str) -> str:
        """
        设置自定义物品名称

        Args:
            name: 新物品名称

        Returns:
            设置物品名称是否成功
        """
    def setDamage(self, damage: int) -> bool:
        """
        设置物品耐久度

        Args:
            damage: 耐久度

        Returns:
            是否设置成功
        """
    def setNbt(self, nbt: NbtCompound) -> bool:
        """
        写入物品对应的 NBT 对象

        Args:
            nbt: 写入物品对应的 NBT 对象

        Returns:
            是否成功写入
        """
    def getNbt(self) -> NbtCompound:
        """
        获取物品对应的 NBT 对象

        Returns:
            物品的NBT对象
        """
    def match(self, item: LLSE_Item) -> bool:
        """
        判断是否为同类物品

        Args:
            item: 被判断的物品

        Returns:
            是否为同类物品
        """
    def asPointer(self) -> NativePointer: ...
    @deprecated("请使用 `LLSE_Item.setNbt()`")
    def setTag(self, nbt: NbtCompound) -> bool: ...
    @deprecated("请使用 `LLSE_Item.getTag()`")
    def getTag(self) -> NbtCompound: ...

Item = LLSE_Item
