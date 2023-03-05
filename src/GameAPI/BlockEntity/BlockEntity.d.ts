/// <reference path="../../index.d.ts" />

/**
 * ### 方块实体对象
 *
 * 在LLSE中，使用「方块实体对象」来操作和获取与特定方块关联的附加数据
 *
 * 该类**没有构造函数**，请通过其他方式获得类对象
 *
 * **注意**：**方块实体对象** 不是一种 **实体**！他们之间并没有特别的关系
 *
 * **注意**：不要长期保存一个方块实体对象\
 * 当方块对象对应的方块被销毁时，对应的方块实体对象将变得无效。\
 * 因此，如果有长期操作某个方块实体的需要，请通过{@linkcode Block.getBlockEntity()}获取实时的方块实体对象
 */
declare class BlockEntity {

  /** 方块实体的名称 */
  readonly name: string 

  /** 方块实体对应方块所在的坐标 */
  readonly pos: IntPos;

  /** 方块实体对象的类型ID */
  readonly type: number;

  /**
   * ### 获取方块实体对应的NBT对象
   *
   * 关于NBT对象的更多使用，请参考 [NBT接口文档](https://docs.litebds.com/#/zh_CN/Development/NbtAPI/NBT)
   *
   * @returns 方块实体的NBT对象
   */
  getNbt(): NbtCompound;

  /**
   * ### 写入方块实体对应的NBT对象
   *
   * 关于NBT对象的更多使用，请参考 [NBT接口文档](https://docs.litebds.com/#/zh_CN/Development/NbtAPI/NBT)
   *
   * @param nbt NBT对象
   *
   * @returns 是否成功写入
   */
  setNbt(nbt: NbtCompound): boolean;

  /**
   * ### 获取方块实体对应的方块对象
   *
   * @returns 方块实体对应的方块对象
   */
  getBlock(): Block;

  asPointer(): NativePointer;
}

declare class LLSE_BlockEntity extends BlockEntity{}
