/// <reference path="../index.d.ts" />

declare class Item {
  /** 游戏内显示的物品名称 */
  readonly name: string;

  /** 物品标准类型名 */
  readonly type: string;

  /** 物品的游戏内id */
  readonly id: number;

  /** 这个物品对象堆叠的个数 */
  readonly count: number;

  /** 物品附加值（如羊毛颜色） */
  readonly aux: number;

  /**	物品当前耐久 */
  readonly damage: number;

  /** 物品攻击伤害 */
  readonly attackDamage: number;

  /** 物品最大耐久 */
  readonly maxDamage: number;

  /** Item Lore */
  readonly lore: Array<string>

  /**	物品是否为箭 */
  readonly isArmorItem: boolean

  /** 物品是否为方块 */
  readonly isBlock: boolean

  /** 物品是否可被破坏 */
  readonly isDamageableItem: boolean

  /** 物品耐久是否被消耗 */
  readonly isDamaged: boolean

  /** 物品是否已被附魔 */
  readonly isEnchanted: boolean

  /** 物品是否为附魔书 */
  readonly isEnchantingBook: boolean
  
  /** 物品是否防火 */
  readonly isFireResistant: boolean
  
  /** 物品是否已堆叠到最大堆叠数 */
  readonly isFullStack: boolean
  
  /** 物品是否闪烁 */
  readonly isGlint: boolean
  
  /** 物品是否为马铠 */
  readonly isHorseArmorItem: boolean
  
  /** Whether the item is liquid clip */
  readonly isLiquidClipItem: boolean
  
  /** 物品是否为唱片 */
  readonly isMusicDiscItem: boolean
  
  /** 物品是否可设置到副手 */
  readonly isOffhandItem: boolean
  
  /** 物品是否为药水 */
  readonly isPotionItem: boolean
  
  /** 物品是否可堆叠 */
  readonly isStackable: boolean
  
  /** 物品是否可穿戴 */
  readonly isWearableItem	: boolean

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

  /**
   * 设置自定义物品名称
   * @param name 新物品名称
   * @returns 是否成功
   */
  setDisplayName(name: string): boolean

  /**
   * 判断是否为同类物品
   * @param item 被判断的物品
   * @returns 是否为同类物品
   */
  match(item: Item): boolean
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
   * @param dimId 维度Id
   * @returns Entity|null 生成的掉落物实体对象
   */
  function spawnItem(
    item: Item,
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2
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

declare class LLSE_Item extends Item{}