/// <reference path="../index.d.ts" />

declare class Entity {
  /**实体名称 */
  readonly name: string;

  /**实体标准类型名 */
  readonly type: string;

  /**实体的游戏内id */
  readonly id: number;

  /**实体所在坐标 */
  readonly pos: FloatPos;

  /**实体所在的方块坐标 */
  readonly blockPos: IntPos;

  /**实体最大生命值 */
  readonly maxHealth: number;

  /**实体当前生命值 */
  readonly health: number;

  /**实体当前是否悬空 */
  readonly inAir: boolean;

  /**实体当前是否在水中 */
  readonly inWater: boolean;

  /**实体当前速度 */
  readonly speed: number;

  /**实体当前朝向 */
  readonly direction: DirectionAngle;

  /**实体唯一标识符 */
  readonly uniqueId: string;

  /**
   * 传送实体至指定位置
   * @param pos 目标位置坐标（或者使用x, y, z, dimid来确定实体位置）
   * @returns boolean 是否成功传送
   */
  teleport(pos: IntPos | FloatPos): boolean;

  /**
   * 传送实体至指定位置
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimid 维度Id
   * @returns boolean 是否成功传送
   */
  teleport(x: number, y: number, z: number, dimid: 0 | 1 | 2 | 3): boolean;

  /**
   * 杀死指定实体
   * @returns boolean 是否执行成功
   */
  kill(): boolean;

  /**
   * 对实体造成伤害
   * @param damage 对实体造成的伤害数值
   * @returns boolean 是否造成伤害
   * @tips 此处造成的伤害为真实伤害，无法被盔甲等保护装备减免
   */
  hurt(damage: number): boolean;

  /**
   * 使指定实体着火
   * @param time 着火时长，单位秒
   * @returns boolean 是否成功着火
   */
  setOnFire(time: number): boolean;

  /**
   * 判断一个实体对象是不是玩家
   * @returns boolean 当前实体对象是不是玩家
   */
  isPlayer(): boolean;

  /**
   * 将实体对象转换玩家对象
   * @returns Player|null 转换成的玩家对象
   */
  toPlayer(): Player | null;

  /**
   * 判断一个实体对象是不是掉落物实体
   * @returns boolean 当前实体对象是不是掉落物实体
   */
  isItemEntity(): boolean;

  /**
   * 获取掉落物实体中的物品对象
   * @returns Item|null 获取到的物品对象
   */
  toItem(): Item | null;

  /**
   * 获取实体当前站立所在的方块
   * @returns Block 当前站立在的方块对象
   */
  getBlockStandingOn(): Block;

  /**
   * 获取生物盔甲栏的容器对象
   * @returns Container 此实体盔甲栏对应的容器对象
   */
  getArmor(): Container;

  /**
   * 判断生物是否拥有容器（盔甲栏除外）
   * @returns boolean 这个生物实体是否拥有容器
   */
  hasContainer(): boolean;

  /**
   * 获取生物所拥有的容器对象（盔甲栏除外）（仅用于`Entity`）
   * @warn Player获取背包请使用 `getInventory()`
   * @returns Container 这个生物实体所拥有的容器对象
   */
  getContainer(): Container;

  /**
   * 刷新生物物品栏、盔甲栏
   * @returns boolean 是否成功刷新
   * @tips 在修改生物物品之后，为了促使客户端生效，需要刷新生物所有的物品
   */
  refreshItems(): boolean;
  

  /**
   * 为实体增加一个Tag
   * @param tag 要增加的tag字符串
   * @returns boolean 是否添加成功
   */
  addTag(tag: string): boolean;

  /**
   * 为为实体移除一个Tag
   * @param tag 要移除的tag字符串
   * @returns boolean 是否移除成功
   */
  removeTag(tag: string): boolean;

  /**
   * 检查实体是否拥有某个Tag
   * @param tag 要检查的tag字符串
   * @returns boolean 是否拥有这个Tag
   */
  hasTag(tag: string): boolean;

  /**
   * 返回实体拥有的所有Tag列表
   * @returns Array<string> 实体所有的 tag 字符串列表
   */
  getAllTags(): Array<string>;

  /**
   * 获取实体对应的NBT对象
   * @returns NbtCompound 实体的NBT对象
   */
  getNbt(): NbtCompound;

  /**
   * 写入实体对应的NBT对象
   * @param nbt NBT对象
   * @returns boolean 是否成功写入
   */
  setNbt(nbt: NbtCompound): boolean;

  /**
   * 获取视线方向实体
   * @param maxDistance 查找最大距离
   * @returns Entity|null 视线方向实体
   */
  getEntityFromViewVector(maxDistance?: number): Entity | null;

  /**
   * 获取视线方向方块
   * @param includeLiquid 是否包含液态方块
   * @param solidOnly 是否仅允许 `Solid` 类型的方块
   * @param maxDistance 查找最大距离
   * @param fullOnly 是否仅允许完整方块
   * @returns Block|null 视线方向方块
   */
  getBlockFromViewVector(
    includeLiquid?: boolean,
    solidOnly?: boolean,
    maxDistance?: number,
    fullOnly?: boolean
  ): Block | null;

  /**
   * 快速执行Molang表达式
   * @param str Molang表达式
   * @returns number 表达式执行结果
   */
  quickEvalMolangScript(str:string):number;
}

declare namespace mc {
  /**
   * 获取当前所有已加载的实体
   * @returns Array<Entity> 实体对象列表
   */
  function getAllEntities(): Array<Entity>;

  /**
   * 生成新生物并获取
   * @param name 生物的命名空间名称，如 `minectaft:creeper`
   * @param pos 生成生物的位置的坐标对象（或者使用x, y, z, dimid来确定生成位置）
   * @returns Entity|null 生成的实体对象
   */
  function spawnMob(name: string, pos: IntPos | FloatPos): Entity | null;

  /**
   * 生成新生物并获取
   * @param name 生物的命名空间名称，如 `minectaft:creeper`
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimid 维度Id
   * @returns Entity|null 生成的实体对象
   */
  function spawnMob(
    name: string,
    x: number,
    y: number,
    z: number,
    dimid: 0 | 1 | 2
  ): Entity | null;

  /**
   * 复制生物并获取
   * @param entiy 需要复制的实体对象
   * @param pos 生成生物的位置的坐标对象（或者使用x, y, z, dimid来确定生成位置）
   * @returns Entity|null 复制的实体对象
   */
  function cloneMob(entiy: Entity, pos: IntPos | FloatPos): Entity | null;

  /**
   * 复制生物并获取
   * @param entiy 需要复制的实体对象
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimid 维度Id
   * @returns Entity|null 复制的实体对象
   */
  function cloneMob(
    entiy: Entity,
    x: number,
    y: number,
    z: number,
    dimid: 0 | 1 | 2
  ): Entity | null;

  /**
   * 在指定位置制造一次爆炸
   * @param pos 引发爆炸的位置坐标（或者使用x, y, z, dimid来确定实体位置）
   * @param source 设置爆炸来源的实体对象，可以为`Null`
   * @param power 爆炸的威力值，影响爆炸的伤害大小和破坏范围
   * @param range 爆炸的范围半径，影响爆炸的波及范围
   * @param isDestroy 爆炸是否破坏方块
   * @param isFire 爆炸结束后是否留下燃烧的火焰
   * @returns boolean 是否成功制造爆炸
   */
  function explode(
    pos: IntPos | FloatPos,
    source: Entity,
    power: number,
    range: number,
    isDestroy: boolean,
    isFire: boolean
  ): boolean;

  /**
   * 在指定位置制造一次爆炸
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimid 维度Id
   * @param source 设置爆炸来源的实体对象，可以为`Null`
   * @param power 爆炸的威力值，影响爆炸的伤害大小和破坏范围
   * @param range 爆炸的范围半径，影响爆炸的波及范围
   * @param isDestroy 爆炸是否破坏方块
   * @param isFire 爆炸结束后是否留下燃烧的火焰
   * @returns boolean 是否成功制造爆炸
   */
   function explode(
    x: number,
    y: number,
    z: number,
    dimid: 0 | 1 | 2,
    source: Entity,
    power: number,
    range: number,
    isDestroy: boolean,
    isFire: boolean
  ): boolean;
}
