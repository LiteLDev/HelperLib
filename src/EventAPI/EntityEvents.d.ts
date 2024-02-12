/// <reference path="../index.d.ts" />

declare enum DamageCause {
  /** 其他 */
  None = -0x01,

  /** 非正常方式（如脚本直接设置血量为0），这种方式的伤害不会被盔甲与buff吸收 */
  Override = 0x00,

  /** 接触伤害（如仙人掌） */
  Contact = 0x01,

  /** 实体攻击 */
  EntityAttack = 0x02,

  /** 抛射物攻击 */
  Projectile = 0x03,

  /** 窒息（密封空间） */
  Suffocation = 0x04,

  /** 掉落 */
  Fall = 0x05,

  /** 着火 */
  Fire = 0x06,

  /** 着火 */
  FireTick = 0x07,

  /** 熔岩 */
  Lava = 0x08,

  /** 溺水 */
  Drowning = 0x09,

  /** 方块爆炸 */
  BlockExplosion = 0x0a,

  /** 实体爆炸 */
  EntityExplosion = 0x0b,

  /** 虚空 */
  Void = 0x0c,

  /** 自杀 */
  Suicide = 0x0d,

  /** 尖牙对生物造成的伤害、守卫者对生物造成的魔法伤害和药水伤害等 */
  Magic = 0x0e,

  /** 凋零效果 */
  Wither = 0x0f,

  /** 饥饿 */
  Starve = 0x10,

  /** 下落的铁砧 */
  Anvil = 0x11,

  /** 荆棘 */
  Thorns = 0x12,

  /** 下落的方块 */
  FallingBlock = 0x13,

  /** 活塞 */
  Piston = 0x14,

  /** 动态能量（滑翔撞墙） */
  FlyIntoWall = 0x15,

  /** 岩浆块 */
  Magma = 0x16,

  /** 烟花 */
  Fireworks = 0x17,

  /** 闪电 */
  Lightning = 0x18,

  /** ？？？ */
  Charging = 0x19,

  /** 温度 （雪人？） */
  Temperature = 0x1a,

  /** 冰冻 */
  Freezing = 0x1b,

  /** 被钟乳石砸到 */
  Stalactite = 0x1c,

  /** 掉落到石笋上 */
  Stalagmite = 0x1d,

  /** 所有 */
  All = 0x1f,
}

declare namespace mc {
  /** 生物死亡 */
  function listen(
    event: "onMobDie",
    listener: (mob: Entity, source: Entity, cause: number) => void
  ): boolean;

  /** 生物受伤（包括玩家） */
  function listen(
    event: "onMobHurt",
    listener: (
      mob: Entity,
      source: Entity | null,
      damage: number,
      cause: DamageCause | number
    ) => boolean | void
  ): boolean;

  /** 发生由实体引起的爆炸 */
  function listen(
    event: "onEntityExplode",
    listener: (
      source: Entity,
      pos: FloatPos,
      radius: number,
      maxResistance: number,
      isDestroy: boolean,
      isFire: boolean
    ) => boolean | void
  ): boolean;

  /** 发生于实体生成
   * @deprecated 请使用 onMobTrySpawn 和 onMobSpawned 事件作为替代
   */
  function listen(
    event: "onMobSpawn",
    listener: (typeName: string, pos: FloatPos) => boolean | void
  ): boolean;

  /**
   * 发生于实体尝试自然生成
   * 
   * 在回调函数中:
   * * `typeName`: 生成实体名称
   * * `pos`: 生成的坐标
   */
  function listen(
    event: "onMobTrySpawn",
    listener: (typeName: string, pos: FloatPos) => boolean | void
  ): boolean;

  /**
   * 发生于实体自然生成完成
   * 
   * 在回调函数中:
   * * `entity`: 生成的实体对象
   * * `pos`: 生成的坐标
   */
  function listen(
    event: "onMobSpawned",
    listener: (entity: Entity | null, pos: FloatPos) => void
  ): boolean;

  /** 实体被弹射物击中 */
  function listen(
    event: "onProjectileHitEntity",
    listener: (entity: Entity, source: Entity) => void
  ): boolean;

  /** 凋零破坏方块 */
  function listen(
    event: "onWitherBossDestroy",
    listener: (witherBoss: Entity, AAbb: IntPos, aaBB: IntPos) => boolean | void
  ): boolean;

  /**
   * 末影龙破坏方块
   * 
   * 在回调函数中:
   * * `EnderDragon`: 末影龙的实体对象
   * * `block`: 末影龙破坏的方块对象
   */
  function listen(
    event: "onEnderDragonDestroy",
    listener: (EnderDragon: Entity, block: Block) => boolean | void
  ): boolean;

  /** 生物骑乘 */
  function listen(
    event: "onRide",
    listener: (entity1: Entity, entity2: Entity) => boolean | void
  ): boolean;

  /** 生物踩压力板 */
  function listen(
    event: "onStepOnPressurePlate",
    listener: (entity: Entity, pressurePlate: Block) => boolean | void
  ): boolean;

  /** 弹射物创建 */
  function listen(
    event: "onSpawnProjectile",
    listener: (shooter: Entity, type: string) => boolean | void
  ): boolean;

  /** 弹射物创建完毕 */
  function listen(
    event: "onProjectileCreated",
    listener: (shooter: Entity, entity: Entity) => boolean | void
  ): boolean;

  /** NPC执行命令 */
  function listen(
    event: "onNpcCmd",
    listener: (npc: Entity, pl: Player, cmd: string) => boolean | void
  ): boolean;

  /** 操作盔甲架 */
  function listen(
    event: "onChangeArmorStand",
    listener: (as: Entity, pl: Player, slot: number) => boolean | void
  ): boolean;

  /** 实体转变 */
  function listen(
    event: "onEntityTransformation",
    listener: (uniqueId: string, entity: Entity) => void
  ): boolean;
}
