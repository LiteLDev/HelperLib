/// <reference path="../index.d.ts" />

declare namespace mc {
  /** 方块接受玩家互动 */
  function listen(
    event: "onBlockInteracted",
    listener: (player: Player, block: Block) => boolean | void
  ): boolean;

  /** 方方块改变 */
  function listen(
    event: "onBlockChanged",
    listener: (beforeBlock: Block, afterBlock: Block) => boolean | void
  ): boolean;

  /** 发生由方块引起的爆炸 */
  function listen(
    event: "onBlockExplode",
    listener: (
      source: Block,
      pos: FloatPos,
      radius: number,
      maxResistance: number,
      isDestroy: boolean,
      isFire: boolean
    ) => boolean | void
  ): boolean;

  /** 方块被爆炸破坏 */
  function listen(
    event: "onBlockExploded",
    listener: (block: Block, source: Entity) => void
  ): boolean;

  /** 火焰蔓延 */
  function listen(
    event: "onFireSpread",
    listener: (pos: IntPos) => boolean | void
  ): boolean;

  /** 命令方块执行命令 */
  function listen(
    event: "onCmdBlockExecute",
    listener: (cmd: string, pos: IntPos, isMinecart: boolean) => boolean | void
  ): boolean;

  /** 容器内容改变 */
  function listen(
    event: "onContainerChange",
    listener: (
      player: Player,
      container: Block,
      slotNum: number,
      oldItem: Item,
      newItem: Item
    ) => void
  ): boolean;

  /** 方块被弹射物击中 */
  function listen(
    event: "onProjectileHitBlock",
    listener: (player: Player, block: Block) => void
  ): boolean;

  /** 发生红石更新 */
  function listen(
    event: "onRedStoneUpdate",
    listener: (block: Block, level: number, isActive: boolean) => boolean | void
  ): boolean;

  /** 漏斗（漏斗矿车）检测可否吸取物品 */
  function listen(
    event: "onHopperSearchItem",
    listener: (pos: FloatPos, isMinecart: boolean) => boolean | void
  ): boolean;

  /** 漏斗输出物品 */
  function listen(
    event: "onHopperPushOut",
    listener: (cmd: string, pos: IntPos, isMinecart: boolean) => boolean | void
  ): boolean;

  /** 活塞尝试推动 */
  function listen(
    event: "onPistonTryPush",
    listener: (pistonPos: IntPos, block: Block) => boolean | void
  ): boolean;

  /** 活塞推动 */
  function listen(
    event: "onPistonPush",
    listener: (pistonPos: IntPos, block: Block) => boolean | void
  ): boolean;

  /** 耕地退化 */
  function listen(
    event: "onFarmLandDecay",
    listener: (pos: IntPos, entity: Entity) => boolean | void
  ): boolean;

  /** 操作物品展示框 */
  function listen(
    event: "onUseFrameBlock",
    listener: (player: Player, block: Block) => boolean | void
  ): boolean;

  /** 液体方块流动 */
  function listen(
    event: "onLiquidFlow",
    listener: (from: Block, to: IntPos) => boolean | void
  ): boolean;
}
