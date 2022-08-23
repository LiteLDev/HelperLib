/// <reference path="../index.d.ts" />


declare class BlockEntity{
    /**方块实体对应方块所在的坐标*/
    readonly pos:IntPos

    /**方块实体对象的类型ID */
    readonly type:number

    /**
     * 获取方块实体对应的NBT对象
     * @returns NbtCompound 方块实体的NBT对象
     */
    getNbt(): NbtCompound;

    /**
     * 写入方块实体对应的NBT对象
     * @param nbt NBT对象
     * @returns boolean 是否成功写入
     */
    setNbt(nbt:NbtCompound):boolean;

    /**
     * 获取方块实体对应的方块对象
     * @returns block 方块实体对应的方块对象
     */
    getBlock():block
}