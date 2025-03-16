from typing import NoReturn

from typing_extensions import deprecated

from llpy import IntPos, LLSE_Container, NativePointer, NbtCompound
from llpy.types import T_ToNbtDict

from .entity import LLSE_BlockEntity

class LLSE_Block:
    """方块对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def name(self) -> str:
        """游戏内显示的方块名称"""
    @property
    def type(self) -> str:
        """方块标准类型名"""
    @property
    def id(self) -> int:
        """方块的游戏内 id"""
    @property
    def pos(self) -> IntPos:
        """方块所在坐标"""
    @property
    def tileData(self) -> int:
        """方块数据值"""
    @property
    def variant(self) -> int:
        """方块变体"""
    @property
    def translucency(self) -> int:
        """方块透明度"""
    @property
    def thickness(self) -> int:
        """方块厚度"""
    @property
    def isAir(self) -> bool:
        """方块是否为空气"""
    @property
    def isBounceBlock(self) -> bool:
        """是否为可弹跳方块"""
    @property
    def isButtonBlock(self) -> bool:
        """是否为按钮方块"""
    @property
    def isCropBlock(self) -> bool:
        """是否为农作物方块"""
    @property
    def isDoorBlock(self) -> bool:
        """是否为门方块"""
    @property
    def isFenceBlock(self) -> bool:
        """是否为栅栏方块"""
    @property
    def isFenceGateBlock(self) -> bool:
        """是否为栅栏门方块"""
    @property
    def isThinFenceBlock(self) -> bool:
        """是否为细栅栏方块"""
    @property
    def isHeavyBlock(self) -> bool:
        """是否为重的方块"""
    @property
    def isStemBlock(self) -> bool:
        """是否为干方块"""
    @property
    def isSlabBlock(self) -> bool:
        """是否为半砖方块"""
    @property
    def isUnbreakable(self) -> bool:
        """方块是否为不可破坏"""
    @property
    def isWaterBlockingBlock(self) -> bool:
        """方块是否可阻挡水"""
    def setNbt(self, nbt: NbtCompound) -> bool:
        """
        写入方块对应的 NBT 对象

        注意：慎重使用此 API，请考虑使用 `mc.setBlock()` 代替

        Args:
            nbt: NBT 对象

        Returns:
            是否成功写入
        """
    def getNbt(self) -> NbtCompound:
        """
        获取方块对应的 NBT 对象

        Returns:
            方块的 NBT 对象
        """
    def getBlockState(self) -> dict[str, T_ToNbtDict]:
        """
        获取方块的 BlockState

        方便函数，协助解析方块 `BlockState` 并转换为 `Object`，方便读取与解析

        等价于脚本执行 `block.getNbt().getTag("states").toObject()`

        Returns:
            方块的 BlockState
        """
    def hasContainer(self) -> bool:
        """
        判断方块是否拥有容器

        如箱子、桶等容器，他们各自拥有一个属于自己的容器对象

        Returns:
            这个方块是否拥有容器
        """
    def getContainer(self) -> LLSE_Container:
        """
        获取方块所拥有的容器对象

        Returns:
            这个方块所拥有的容器对象
        """
    def hasBlockEntity(self) -> bool:
        """
        判断方块是否拥有方块实体

        Returns:
            这个方块是否拥有方块实体
        """
    def getBlockEntity(self) -> LLSE_BlockEntity:
        """
        获取方块所拥有的方块实体

        Returns:
            这个方块所拥有的方块实体
        """
    def removeBlockEntity(self) -> bool:
        """
        删除方块所拥有的方块实体

        Returns:
            是否成功删除
        """
    def destroy(self, drop: bool) -> bool:
        """
        破坏方块

        Args:
            drop: 是否生成掉落物

        Returns:
            是否成功破坏
        """
    def asPointer(self) -> NativePointer: ...
    @deprecated("请使用 `LLSE_Block.setNbt()`")
    def setTag(self, nbt: NbtCompound) -> bool: ...
    @deprecated("请使用 `LLSE_Block.getNbt()`")
    def getTag(self) -> NbtCompound: ...

Block = LLSE_Block
