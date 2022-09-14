/// <reference path="../../index.d.ts" />

declare namespace mc {
  /**
   * ### 获取当前所有已加载的实体
   * 
   * @returns 实体对象列表
   */
  function getAllEntities(): Array<Entity>;

  /**
   * ### 生成新生物并获取
   * 
   * 通过此函数，在指定的位置生成一个新生物，并获取它对应的实体对象
   * 
   * @param name 生物的命名空间名称，如 `minectaft:creeper`
   * @param pos 生成生物的位置的坐标对象
   * 
   * @returns 生成的实体对象（失败返回`null`）
   */
  function spawnMob(name: string, pos: IntPos | FloatPos): Entity | null;

  /**
   * ### 生成新生物并获取
   * 
   * 通过此函数，在指定的位置生成一个新生物，并获取它对应的实体对象
   * 
   * @param name 生物的命名空间名称，如 `minectaft:creeper`
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimId 维度Id
   * 
   * @returns 生成的实体对象（失败返回`null`）
   */
  function spawnMob(
    name: string,
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2
  ): Entity | null;

  /**
   * ### 复制生物并获取
   * 
   * @param entity 需要复制的实体对象
   * @param pos 生成生物的位置的坐标对象
   * 
   * @returns 复制的实体对象（失败返回`null`）
   */
  function cloneMob(entity: Entity, pos: IntPos | FloatPos): Entity | null;

  /**
   * ##d 复制生物并获取
   * 
   * @param entity 需要复制的实体对象
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimId 维度Id
   * 
   * @returns Entity|null 复制的实体对象（失败返回`null`）
   */
  function cloneMob(
    entity: Entity,
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2
  ): Entity | null;

  /**
   * ### 在指定位置制造一次爆炸
   * 
   * @param pos 引发爆炸的位置坐标
   * @param source 设置爆炸来源的实体对象，可以为`Null`
   * @param power 爆炸的威力值，影响爆炸的伤害大小和破坏范围
   * @param range 爆炸的范围半径，影响爆炸的波及范围
   * @param isDestroy 爆炸是否破坏方块
   * @param isFire 爆炸结束后是否留下燃烧的火焰
   * 
   * @returns 是否成功制造爆炸
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
   * ### 在指定位置制造一次爆炸
   * 
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimId 维度Id
   * @param source 设置爆炸来源的实体对象，可以为`Null`
   * @param power 爆炸的威力值，影响爆炸的伤害大小和破坏范围
   * @param range 爆炸的范围半径，影响爆炸的波及范围
   * @param isDestroy 爆炸是否破坏方块
   * @param isFire 爆炸结束后是否留下燃烧的火焰
   * 
   * @returns 是否成功制造爆炸
   */
  function explode(
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2,
    source: Entity,
    power: number,
    range: number,
    isDestroy: boolean,
    isFire: boolean
  ): boolean;
}
