from typing import NoReturn

from llpy import IntPos, LLSE_Block, NativePointer, NbtCompound

class LLSE_BlockEntity:
    """方块实体对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def name(self) -> str:
        """方块实体名称（如 `container.chest`）"""
    @property
    def pos(self) -> IntPos:
        """方块实体对应方块所在的坐标"""
    @property
    def type(self) -> int:
        """方块实体对象的类型 ID"""
    def setNbt(self) -> bool:
        """
        写入方块实体对应的 NBT 对象

        Returns:
            是否成功写入
        """
    def getNbt(self) -> NbtCompound:
        """
        获取方块实体对应的 NBT 对象

        Returns:
            方块实体的 NBT 对象
        """
    def getBlock(self) -> LLSE_Block:
        """
        获取方块实体对应的方块对象

        Returns:
            方块实体对应的方块对象
        """
    def asPointer(self) -> NativePointer: ...

BlockEntity = LLSE_BlockEntity
