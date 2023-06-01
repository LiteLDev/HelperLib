/// <reference path="../index.d.ts" />

declare namespace mc {
  /** 玩家开始连接服务器 */
  function listen(
    event: 'onPreJoin',
    listener: (player: Player) => boolean | void
  ): boolean;

  /** 玩家进入游戏（加载世界完成） */
  function listen(event: 'onJoin', listener: (player: Player) => void): boolean;

  /** 玩家离开游戏 */
  function listen(event: 'onLeft', listener: (player: Player) => void): boolean;

  /** 玩家重生 */
  function listen(
    event: 'onRespawn',
    listener: (player: Player) => void
  ): boolean;

  /** 玩家死亡 */
  function listen(
    event: 'onPlayerDie',
    listener: (player: Player, source: Entity | null) => void
  ): boolean;

  /** 玩家执行命令 */
  function listen(
    event: 'onPlayerCmd',
    listener: (player: Player, cmd: string) => boolean | void
  ): boolean;

  /** 玩家发送聊天信息 */
  function listen(
    event: 'onChat',
    listener: (player: Player, msg: string) => boolean | void
  ): boolean;

  /** 玩家切换维度 */
  function listen(
    event: 'onChangeDim',
    listener: (player: Player, dimId: 0 | 1 | 2) => void
  ): boolean;

  /** 玩家跳跃 */
  function listen(event: 'onJump', listener: (player: Player) => void): boolean;

  /** 玩家切换潜行状态 */
  function listen(
    event: 'onSneak',
    listener: (player: Player, isSneaking: boolean) => void
  ): boolean;

  /** 玩家攻击实体 */
  function listen(
    event: 'onAttackEntity',
    listener: (player: Player, entity: Entity, damage: number) => boolean | void
  ): boolean;

  /** 玩家攻击方块 */
  function listen(
    event: 'onAttackBlock',
    listener: (player: Player, block: Block, item: Item) => boolean | void
  ): boolean;

  /** 玩家使用物品 */
  function listen(
    event: 'onUseItem',
    listener: (player: Player, item: Item) => boolean | void
  ): boolean;

  /** 玩家对方块使用物品（点击右键） */
  function listen(
    event: 'onUseItemOn',
    listener: (
      player: Player,
      item: Item,
      block: Block,
      side: number,
      pos: FloatPos
    ) => boolean | void
  ): boolean;

  /** 玩家捡起物品 */
  function listen(
    event: 'onTakeItem',
    listener: (player: Player, entity: Entity, item: Item) => boolean | void
  ): boolean;

  /** 玩家丢出物品 */
  function listen(
    event: 'onDropItem',
    listener: (player: Player, item: Item) => boolean | void
  ): boolean;

  /** 玩家正在吃食物 */
  function listen(
    event: 'onEat',
    listener: (player: Player) => boolean | void
  ): boolean;

  /** 玩家消耗图腾 */
  function listen(
    event: 'onConsumeTotem',
    listener: (player: Player) => boolean | void
  ): boolean;

  /** 玩家获得效果 */
  function listen(
    event: 'onEffectAdded',
    listener: (
      player: Player,
      effectName: string,
      amplifier: number,
      duration: number
    ) => boolean | void
  ): boolean;

  /** 玩家开始连接服务器 */
  function listen(
    event: 'onPreJoin',
    listener: (player: Player) => boolean | void
  ): boolean;

  /** 玩家移除效果 */
  function listen(
    event: 'onEffectRemoved',
    listener: (player: Player, effectName: string) => boolean | void
  ): boolean;

  /** 玩家刷新效果 */
  function listen(
    event: 'onEffectUpdated',
    listener: (
      player: Player,
      effectName: string,
      amplifier: number,
      duration: number
    ) => boolean | void
  ): boolean;

  /** 玩家开始破坏方块/点击左键 */
  function listen(
    event: 'onStartDestroyBlock',
    listener: (player: Player, block: Block) => void
  ): boolean;

  /** 玩家破坏方块完成 */
  function listen(
    event: 'onDestroyBlock',
    listener: (player: Player, block: Block) => boolean | void
  ): boolean;

  /** 玩家尝试放置方块 */
  function listen(
    event: 'onPlaceBlock',
    listener: (player: Player, block: Block) => boolean | void
  ): boolean;

  /** 玩家放置方块 */
  function listen(
    event: 'afterPlaceBlock',
    listener: (player: Player, block: Block) => void
  ): boolean;

  /** 玩家打开容器方块 */
  function listen(
    event: 'onOpenContainer',
    listener: (player: Player, block: Block) => boolean | void
  ): boolean;

  /** 玩家关闭容器方块 */
  function listen(
    event: 'onCloseContainer',
    listener: (player: Player, block: Block) => boolean | void
  ): boolean;

  /** 玩家物品栏变化 */
  function listen(
    event: 'onInventoryChange',
    listener: (
      player: Player,
      slotNum: number,
      oldItem: Item,
      newItem: Item
    ) => void
  ): boolean;

  /** 玩家改变疾跑状态 */
  function listen(
    event: 'onChangeSprinting',
    listener: (player: Player, sprinting: boolean) => void
  ): boolean;

  /** 玩家使用重生锚 */
  function listen(
    event: 'onUseRespawnAnchor',
    listener: (player: Player, pos: IntPos) => boolean | void
  ): boolean;

  /** 玩家改变盔甲栏 */
  function listen(
    event: 'onSetArmor',
    listener: (player: Player, slotNum: number, item: Item) => boolean | void
  ): boolean;

  /** 玩家打开容器类GUI */
  function listen(
    event: 'onOpenContainerScreen',
    listener: (player: Player) => boolean | void
  ): boolean;

  /** 玩家获得经验 */
  function listen(
    event: 'onExperienceAdd',
    listener: (player: Player, exp: number) => boolean | void
  ): boolean;

  /** 玩家上床 */
  function listen(
    event: 'onBedEnter',
    listener: (player: Player, pos: IntPos) => boolean | void
  ): boolean;

  /** 玩家使用桶装东西 */
  function listen(
    event: 'onUseBucketPlace',
    listener: (
      player: Player,
      item: Item,
      block: Block | Item,
      side: 1 | 2 | 3 | 4 | 5 | 6,
      pos: FloatPos
    ) => boolean | void
  ): boolean;

  /** 玩家吃下食物 */
  function listen(
    event: 'onAte',
    listener: (player: Player, item: Item) => void
  ): boolean;
}
