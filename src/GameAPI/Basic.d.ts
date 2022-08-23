/**整数 坐标对象 */
export interface IntPos {
  /**x 坐标 */
  x: number;

  /**y 坐标 */
  y: number;

  /**z 坐标 */
  z: number;

  /**维度文字名 */
  dim: "主世界" | "下界" | "末地";

  /**维度ID */
  dimid: 0 | 1 | 2 | -1;
}

/**浮点数 坐标对象 */
export interface FloatPos {
  /**x 坐标 */
  x: number;

  /**y 坐标 */
  y: number;

  /**z 坐标 */
  z: number;

  /**维度文字名 */
  dim: "主世界" | "下界" | "末地";

  /**维度ID */
  dimid: 0 | 1 | 2 | -1;
}

/**坐标对象辅助接口 */
declare namespace mc {
  /**
   * 生成一个整数坐标对象
   * @param x x 坐标
   * @param y y 坐标
   * @param z z 坐标
   * @param dimid 维度ID：`0` 代表主世界，`1` 代表下界，`2` 代表末地
   */
  function newIntPos(x: number, y: number, z: number, dimid: 0 | 1 | 2): IntPos;

  /**
   * 生成一个整数坐标对象
   * @param x x 坐标
   * @param y y 坐标
   * @param z z 坐标
   * @param dimid 维度ID：`0` 代表主世界，`1` 代表下界，`2` 代表末地
   */
  function newFloatPos(
    x: number,
    y: number,
    z: number,
    dimid: 0 | 1 | 2
  ): FloatPos;
}

/**
 * 方向角对象 
 * @tips 由于MC的实体系统不存在 自转 的概念，所以没有翻滚角相关数据
 */
export interface DirectionAngle{
    /**俯仰角（-90° ~ 90°） */
    pitch: number;

    /**偏航角（旋转角） */
    yaw:number;

    /**
     * 将偏航角转换为基本朝向
     * @returns 0代表北 1代表东 2代表南 3代表西
     */
    toFacing():0|1|2|3
}