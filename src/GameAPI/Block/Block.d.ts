/// <reference path="../../index.d.ts" />

/**
 * ### 📦 方块对象
 *
 * 在LLSE中，使用「方块对象」来操作和获取某一类方块的相关信息
 *
 * 该类**没有构造函数**，请通过其他方式获得类对象
 *
 * **注意**：不要**长期保存**一个方块对象\
 * 当方块对象对应的方块被销毁时，对应的方块对象将变得无效。\
 * 因此，如果有长期操作某个方块的需要，请通过**事件提供的参数**或者**使用**{@linkcode mc.getBlock()}获取实时的方块对象
 *
 * @see [📦 方块对象](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Block)
 */
declare class Block {
  /** 游戏内显示的方块名称（例：`Stone`） */
  readonly name: string;

  /** 方块标准类型名（例：`minecraft:stone`） */
  readonly type: string;

  /** 方块的游戏内id */
  readonly id: number;

  /** 方块所在坐标 */
  readonly pos: IntPos;

  /** 方块数据值 */
  readonly tileData: number;

  /** The block variant */
  readonly variant: number;

  /** 方块透明度 */
  readonly translucency: number;

  /** 方块厚度 */
  readonly thickness: number;

  /** 方块是否为空气 */
  readonly isAir: boolean;

  /** 是否为可弹跳方块 */
  readonly isBounceBlock: boolean;

  /** 是否为按钮方块 */
  readonly isButtonBlock: boolean;

  /** 是否为农作物方块 */
  readonly isCropBlock: boolean;

  /** 是否为门方块 */
  readonly isDoorBlock: boolean;

  /** 是否为栅栏方块 */
  readonly isFenceBlock: boolean;

  /** 是否为栅栏门方块 */
  readonly isFenceGateBlock: boolean;

  /** 是否为细栅栏方块 */
  readonly isThinFenceBlock: boolean;

  /** 是否为重的方块 */
  readonly isHeavyBlock: boolean;

  /** 是否为干方块 */
  readonly isStemBlock: boolean;

  /** 是否为半砖方块 */
  readonly isSlabBlock: boolean;

  /** 方块是否为不可破坏 */
  readonly isUnbreakable: boolean;

  /** 方块是否可阻挡水 */
  readonly isWaterBlockingBlock: boolean;

  /**
   * ### 破坏方块
   *
   * @param drop 是否生成掉落物
   * @returns 是否成功破坏
   */
  destroy(drop: boolean): boolean;

  /**
   * ### 获取方块对应的NBT对象
   *
   * 关于NBT对象的更多使用，请参考 [NBT接口文档](https://docs.litebds.com/#/zh_CN/Development/NbtAPI/NBT)
   *
   * @returns 方块的NBT对象
   */
  getNbt(): NbtCompound;

  /**
   * @deprecated
   * @alias {@linkcode getNbt()}
   */
  getTag(): NbtCompound;

  /**
   * ### 写入方块对应的NBT对象
   *
   * 关于NBT对象的更多使用，请参考 [NBT接口文档](https://docs.litebds.com/#/zh_CN/Development/NbtAPI/NBT)
   *
   * 注意：慎重使用此api，请考虑使用 {@linkcode mc.setBlock()} 代替
   *
   * @param nbt NBT对象
   *
   * @returns 是否成功写入
   */
  setNbt(nbt: NbtCompound): boolean;

  /**
   * @deprecated
   * @alias {@linkcode setNbt()}
   */
  setTag(nbt: NbtCompound): boolean;

  /**
   * ### 获取方块的BlockState
   *
   * 方便函数，协助解析方块BlockState并转换为`Object`，方便读取与解析
   *
   * 等价于脚本执行`block.getNbt().getTag("states").toObject()`
   *
   * 关于NBT对象的更多使用，请参考 [NBT接口文档](https://docs.litebds.com/#/zh_CN/Development/NbtAPI/NBT)
   *
   * @returns 方块的BlockState
   */
  getBlockState(): object;

  /**
   * ### 判断方块是否拥有容器
   *
   * 如箱子、桶等容器，他们各自拥有一个属于自己的容器对象
   *
   * 关于容器对象的更多使用，请参考 [容器对象 API文档](https://docs.litebds.com/#/zh_CN/Development/GameAPI/Container)
   *
   * @returns 这个方块是否拥有容器
   */
  hasContainer(): boolean;

  /**
   * ### 获取方块所拥有的容器对象
   *
   * 如箱子、桶等容器，他们各自拥有一个属于自己的容器对象
   *
   * 关于容器对象的更多使用，请参考 [容器对象 API文档](https://docs.litebds.com/#/zh_CN/Development/GameAPI/Container)
   *
   * @returns 这个方块所拥有的容器对象
   */
  getContainer(): Container;

  /**
   * ### 判断方块是否拥有方块实体
   *
   * 关于方块实体对象的更多使用，请参考 [方块实体对象 API文档](https://docs.litebds.com/#/zh_CN/Development/GameAPI/BlockEntity)
   *
   * @returns 这个方块是否拥有方块实体
   */
  hasBlockEntity(): boolean;

  /**
   * ### 获取方块所拥有的方块实体
   *
   * 关于方块实体对象的更多使用，请参考 [方块实体对象 API文档](https://docs.litebds.com/#/zh_CN/Development/GameAPI/BlockEntity)
   *
   * @returns 这个方块所拥有的方块实体
   */
  getBlockEntity(): BlockEntity;

  /**
   * ### 删除方块所拥有的方块实体
   *
   * 关于方块实体对象的更多使用，请参考 [方块实体对象 API文档](https://docs.litebds.com/#/zh_CN/Development/GameAPI/BlockEntity)
   *
   * @returns 是否成功删除
   */
  removeBlockEntity(): boolean;

  asPointer(): NativePointer;
}


declare class LLSE_Block extends Block{}