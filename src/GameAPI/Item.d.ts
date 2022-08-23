/// <reference path="../index.d.ts" />

declare class Item {
  /**游戏内显示的物品名称 */
  readonly name: string;

  /**物品标准类型名 */
  readonly type: string;

  /**物品的游戏内id */
  readonly id: number;

  /**这个物品对象堆叠的个数 */
  readonly count: number;
  /**物品附加值（如羊毛颜色） */
  readonly aux: number;

  /**
   * 从现有的物品对象克隆
   * @returns Item|null 生成的新物品对象
   */
  clone(): Item | null;

  /**
   * 判断物品对象是否为空
   * @returns boolean 这个物品对象是否为空
   */
  isNull(): boolean;

  /**
   * 将此物品对象置为空（删除物品）
   * @returns boolean 是否删除成功
   */
  setNull(): boolean;

  /**
   * 将此物品对象设置为另一个物品
   * @param item 要赋值的物品对象
   * @returns boolean 是否赋值成功
   */
  set(item: Item): boolean;

  /**
   * 设置物品的附加值
   * @param aux 物品附加值
   * @returns boolean 是否设置成功
   */
  setAux(aux: number): boolean;

  /**
   * 获取物品对应的NBT对象
   * @returns NbtCompound 物品的NBT对象
   */
  getNbt(): NbtCompound;

  /**
   * 写入物品对应的NBT对象
   * @param nbt NBT对象
   * @returns boolean 是否成功写入
   */
  setNbt(nbt: NbtCompound): boolean;

  /**
   * 设置自定义Lore
   * @param names 要设置的Lore字符串的数组
   * @returns boolean 是否设置成功
   */
  setLore(names: Array<string>): boolean;
}

declare namespace mc {
  /**
   * 根据物品对象生成掉落物实体
   * @param item 生成掉落物实体所使用的物品对象
   * @param pos 生成掉落物实体的位置的坐标对象（或者使用x, y, z, dimid来确定生成位置）
   * @returns Entity|null 生成的掉落物实体对象
   */
  function spawnItem(item: Item, pos: IntPos | FloatPos): Entity | null;

  /**
   * 根据物品对象生成掉落物实体
   * @param item 生成掉落物实体所使用的物品对象
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimid 维度Id
   * @returns Entity|null 生成的掉落物实体对象
   */
  function spawnItem(
    item: Item,
    x: number,
    y: number,
    z: number,
    dimid: 0 | 1 | 2
  ): Entity | null;

  /**
   * 通过NBT生成物品对象
   * @param nbt 生成物品对象所使用的物品NBT
   * @returns Item|null 生成的物品对象
   */
  function newItem(nbt: NbtCompound): Item | null;

  /**
   * 生成新的物品对象
   * @param name 物品的标准类型名，如`minecraft:bread`
   * @param count 物品堆叠数量
   */
  function newItem(name: string, count: number): Item | null;
}
