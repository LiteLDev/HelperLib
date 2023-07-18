/// <reference path="../../index.d.ts" />

/**
 * ### 🎈 实体对象
 *
 * 在脚本引擎中，使用「实体对象」来操作和获取某一个实体的相关信息。
 *
 * 该类**没有构造函数**，请使用下面的方法获取该类对象
 *
 * - 从监听事件中获取
 * - {@linkcode mc.getAllEntities()}
 * - {@linkcode mc.spawnMob()}
 * - {@linkcode mc.cloneMob()}
 * - 从其他API中获取
 *
 * **注意**：不要**长期保存**一个实体对象\
 * 当实体对象对应的实体被销毁时，对应的实体对象将同时释放。\
 * 因此，如果有长期操作某个实体的需要，请通过上述途径获取实时的实体对象
 *
 * @see [🎈 实体对象 API](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Entity)
 */
declare class Entity {
  /** 实体名称 */
  readonly name: string;

  /** 实体标准类型名 */
  readonly type: string;

  /** 实体的游戏内id */
  readonly id: number;

  /** 实体所在坐标 */
  readonly pos: FloatPos;

  /** 实体所在的方块坐标 */
  readonly blockPos: IntPos;

  /** 实体腿部所在坐标 */
  readonly feetPos: FloatPos;

  /** 实体最大生命值 */
  readonly maxHealth: number;

  /** 实体当前生命值 */
  readonly health: number;

  /** 实体是否能飞行 */
  readonly canFly: boolean;

  /** 实体是否能被冻结 */
  readonly canFreeze: boolean;

  /** 实体是否能看到天空 */
  readonly canSeeDaylight: boolean;

  /** 实体是否能拾取物品 */
  readonly canPickupItems: boolean;

  /** 实体是否悬空 */
  readonly inAir: boolean;

  /** 实体是否在水中 */
  readonly inWater: boolean;

  /** 实体是否在岩浆中 */
  readonly inLava: boolean;

  /** 实体是否在雨中 */
  readonly inRain: boolean;

  /** 实体是否在雪中 */
  readonly inSnow: boolean;

  /** 实体是否在墙上 */
  readonly inWall: boolean;

  /** 实体是否在水中或雨中 */
  readonly inWaterOrRain: boolean;

  /** 实体是否在世界中 */
  readonly inWorld: boolean;

  /** 实体当前速度 */
  readonly speed: number;

  /** 实体当前朝向 */
  readonly direction: DirectionAngle;

  /** 实体唯一标识符 */
  readonly uniqueId: string;

  /** 实体是否不可见 */
  readonly isInvisible: boolean;

  /** 实体是否在门户内 */
  readonly isInsidePortal: boolean;

  /** 实体是否信任 */
  readonly isTrusting: boolean;

  /** 实体是否接触到伤害方块 */
  readonly isTouchingDamageBlock: boolean;

  /** 实体是否着火 */
  readonly isOnFire: boolean;

  /** 实体是否在地面 */
  readonly isOnGround: boolean;

  /** 实体是否在热块上 */
  readonly isOnHotBlock: boolean;

  /** 实体是否在交易 */
  readonly isTrading: boolean;

  /** 实体是否正在骑行 */
  readonly isRiding: boolean;

  /** 实体是否在跳舞 */
  readonly isDancing: boolean;

  /** 实体是否在睡觉 */
  readonly isSleeping: boolean;

  /** 实体是否生气 */
  readonly isAngry: boolean;

  /** 实体是否为幼体 */
  readonly isBaby: boolean;

  /** 实体是否移动 */
  readonly isMoving: boolean;

  readonly posDelta: FloatPos;

  /**
   * ### 传送实体至指定位置
   *
   * @param pos 目标位置坐标
   * @param rot 传送后实体的朝向，若缺省则与传送前朝向相同
   *
   * @returns 是否成功传送
   */
  teleport(pos: IntPos | FloatPos, rot?: DirectionAngle): boolean;

  /**
   * ### 传送实体至指定位置
   *
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimId 维度Id
   * @param rot 传送后实体的朝向，若缺省则与传送前朝向相同
   *
   * @returns 是否成功传送
   */
  teleport(
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2 | 3,
    rot?: DirectionAngle
  ): boolean;

  /**
   * ### 杀死指定实体
   *
   * @returns 是否执行成功
   */
  kill(): boolean;

  /**
   * ### 对实体造成伤害
   *
   * 此处造成的伤害为真实伤害，无法被盔甲等保护装备减免
   *
   * @param damage 对实体造成的伤害数值
   * @param type 伤害类型（见{@linkcode ActorDamageCause}）
   *
   * @returns 是否造成伤害
   */
  hurt(damage: number, type?: number): boolean;

  /**
   * ### 治愈实体
   *
   * @param health 要回复的生命值
   *
   * @returns 是否成功回复
   */
  // 正式版未实装
  // heal(health: number): boolean;

  /**
   * ### 使指定实体着火
   *
   * @param time 着火时长，单位秒
   *
   * @returns 是否成功着火
   */
  setOnFire(time: number): boolean;

  /**
   * ### 设置实体体积
   *
   * @param scale 新的实体体积
   *
   * @returns 实体是否成功缩放
   */
  // 正式版未实装
  // setScale(scale: number): boolean;

  /**
   * ### 获取实体到指定坐标的距离
   *
   * @param pos 目标位置
   *
   * @returns 到坐标的距离（方块）
   */
  // 正式版未实装
  // distanceToPos(pos: IntPos | FloatPos): number;

  /**
   * ### 判断一个实体对象是不是玩家
   *
   * @returns 当前实体对象是不是玩家
   */
  isPlayer(): boolean;

  /**
   * ### 将实体对象转换玩家对象
   *
   * 如果当前实体对象指向的是一个玩家，可以使用此函数将实体对象转换为玩家对象，以使用更多的玩家相关 API\
   * 如果此实体对象指向的不是某个玩家，或者转换失败，则返回 `null`
   *
   * @returns 转换成的玩家对象，失败返回`null`
   */
  toPlayer(): Player | null;

  /**
   * ### 判断一个实体对象是不是掉落物实体
   *
   * @returns 当前实体对象是不是掉落物实体
   */
  isItemEntity(): boolean;

  /**
   * ### 获取掉落物实体中的物品对象
   *
   * 如果当前实体对象是一个掉落物实体，可以使用此函数获取掉落物实体中的物品对象，以使用更多的物品相关 API\
   * 如果此实体对象不是掉落物实体，或者获取失败，则返回 `null`
   *
   * @returns 获取到的物品对象，失败返回`null`
   */
  toItem(): Item | null;

  /**
   * ### 获取实体当前站立所在的方块
   *
   * @returns 当前站立在的方块对象
   */
  getBlockStandingOn(): Block;

  /**
   * ### 获取生物盔甲栏的容器对象
   *
   * @returns 此实体盔甲栏对应的容器对象
   */
  getArmor(): Container;

  /**
   * ### 判断生物是否拥有容器（盔甲栏除外）
   *
   * 如羊驼身上的箱子等，他们各自拥有一个属于自己的容器对象
   *
   * @returns 这个生物实体是否拥有容器
   */
  hasContainer(): boolean;

  /**
   * ### 获取生物所拥有的容器对象（盔甲栏除外）
   *
   * @returns 这个生物实体所拥有的容器对象
   */
  getContainer(): Container;

  /**
   * ### 刷新生物物品栏、盔甲栏
   *
   * 在修改生物物品之后，为了促使客户端生效，需要刷新生物所有的物品
   *
   * @returns 是否成功刷新
   */
  refreshItems(): boolean;

  /**
   * ### 为实体增加一个Tag
   *
   * @param tag 要增加的tag字符串
   *
   * @returns 是否添加成功
   */
  addTag(tag: string): boolean;

  /**
   * ### 为为实体移除一个Tag
   *
   * @param tag 要移除的tag字符串
   *
   * @returns 是否移除成功
   */
  removeTag(tag: string): boolean;

  /**
   * ### 检查实体是否拥有某个Tag
   *
   * @param tag 要检查的tag字符串
   *
   * @returns 是否拥有这个Tag
   */
  hasTag(tag: string): boolean;

  /**
   * ### 返回实体拥有的所有Tag列表
   *
   * @returns 实体所有的 tag 字符串列表
   */
  getAllTags(): Array<string>;

  /**
   * ### 获取实体对应的NBT对象
   *
   * @returns 实体的NBT对象
   */
  getNbt(): NbtCompound;

  /**
   * ### 写入实体对应的NBT对象
   *
   * @param nbt NBT对象
   *
   * @returns 是否成功写入
   */
  setNbt(nbt: NbtCompound): boolean;

  /**
   * @deprecated
   * @alias {@linkcode getNbt()}
   */
  getTag(): NbtCompound;

  /**
   * @deprecated
   * @alias {@linkcode setNbt()}
   */
  setTag(nbt: NbtCompound): boolean | null;

  /**
   * ### 获取视线方向实体
   *
   * @param maxDistance 查找最大距离
   *
   * @returns 视线方向实体，如果获取失败，返回 `null`
   */
  getEntityFromViewVector(maxDistance?: number): Entity | null;

  /**
   * ### 获取视线方向方块
   *
   * @param includeLiquid 是否包含液态方块
   * @param solidOnly 是否仅允许 `Solid` 类型的方块
   * @param maxDistance 查找最大距离
   * @param fullOnly 是否仅允许完整方块
   *
   * @returns 视线方向方块，如果获取失败，返回 `null`
   */
  getBlockFromViewVector(
    includeLiquid?: boolean,
    solidOnly?: boolean,
    maxDistance?: number,
    fullOnly?: boolean
  ): Block | null;

  /**
   * ### 快速执行Molang表达式
   *
   * 关于Molang的详细使用方法，请参考 [MOLANG文档 bedrock.dev](https://bedrock.dev/zh/docs/stable/Molang)
   *
   * @param str Molang表达式
   *
   * @returns 表达式执行结果
   */
  quickEvalMolangScript(str: string): number;

  asPointer(): NativePointer | null;

  /**
   * ### 缩放实体
   *
   * @param scale 新的玩家实体 (整数)
   *
   * @returns 是否缩放成功
   */
  setScale(scale: number): boolean;

  /**
   * ### 熄灭实体
   *
   * @returns 是否熄灭成功
   */
  stopFire(): boolean;

  /**
   * @deprecated
   * ### 获取实体到坐标的距离
   *
   * @param pos 目标位置
   *
   * @returns 到坐标的距离(方块)
   *
   */
  distanceToPos(pos: Entity | Player | IntPos | FloatPos): number;

  /**
   *
   * ### 获取实体到坐标的距离
   *
   * @param pos 目标位置
   *
   * @returns 到坐标的距离(方块)
   *
   */
  distanceToSqr(pos: Entity | Player | IntPos | FloatPos): number;

  /**
   *
   * ### 获取实体到坐标的距离
   *
   * @param pos 目标位置
   *
   * @returns 到坐标的距离(方块)
   *
   */
  distanceTo(pos: Entity | Player | IntPos | FloatPos): number;

  /** 设置生命值 */
  setHealth(health: number): boolean;

  /** 设置生命值上限 */
  setMaxHealth(health: number): boolean;

  /**
   * 设置伤害吸收属性
   * @param value 新的值
   * @returns 是否成功
   */
  setAbsorption(value: number): boolean;

  /**
   * 设置攻击伤害属性
   * @param value 新的值
   * @returns 是否成功
   */
  setAttackDamage(value: number): boolean;

  /**
   * 最大攻击伤害属性
   * @param value 新的值
   * @returns 是否成功
   */
  setMaxAttackDamage(value: number): boolean;

  /**
   * 设置跟随范围
   * @param value 新的值
   * @returns 是否成功
   */
  setFollowRange(value: number): boolean;

  /**
   * 设置击退抵抗属性
   * @param value 新的值
   * @returns 是否成功
   */
  setKnockbackResistance(value: 0 | 1): boolean;

  /**
   * 设置幸运属性
   * @param value 新的值
   * @returns 是否成功
   */
  setLuck(value: number): boolean;

  /**
   * 设置移动速度属性
   * @param value 新的值
   * @returns 是否成功
   */
  setMovementSpeed(value: number): boolean;

  /**
   * 置水下移动速度属性
   * @param value 新的值
   * @returns 是否成功
   */
  setUnderwaterMovementSpeed(value: number): boolean;

  /**
   * 设置岩浆上移动速度属性
   * @param value 新的值
   * @returns 是否成功
   */
  setLavaMovementSpeed(value: number): boolean;

  /**
   * 使指定实体刷新消失
   * @returns 是否成功执行
   */
  despawn(): boolean;

  /**
   * 移除指定实体
   * @returns 是否成功执行
   */
  remove(): boolean;

  setPosDelta(arg1: FloatPos): boolean;

  setPosDelta(arg1: number, arg2: number, arg3: number): boolean;

  /**
   * 获取实体全部药水效果
   * @returns 实体所有的药水效果id
   */
  getAllEffects(): number[];

  /**
   * 为实体添加一个药水效果
   * @param id 药水效果的id
   * @param tick 持续时间
   * @param level 等级
   * @param showParticles 是否显示粒子
   * @returns 是否成功
   */
  addEffect(
    id: number,
    tick: number,
    level: number,
    showParticles: boolean
  ): boolean;

  /**
   * 为实体移除一个药水效果
   * @param id 药水效果的id
   * @returns 是否成功
   */
  removeEffect(id: number): boolean;
}

declare class LLSE_Entity extends Entity {}
