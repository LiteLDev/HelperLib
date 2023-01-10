/// <reference path="../../index.d.ts" />

/**
 * ### 🎯 浮点数 坐标对象
 *
 * x y z坐标均为**浮点数**，多用来表示实体坐标等用无法用整数表示的位置
 *
 * @see [🎯 坐标对象](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Basic?id=%f0%9f%8e%af-%e5%9d%90%e6%a0%87%e5%af%b9%e8%b1%a1)
 */
declare class FloatPos {
  /**
   * @param x x坐标（浮点数）
   * @param y y坐标（浮点数）
   * @param z z坐标（浮点数）
   * @param dimId 维度ID
   */
  constructor(x: number, y: number, z: number, dimId: number);

  /** x坐标（浮点数） */
  x: number;

  /** y坐标（浮点数） */
  y: number;

  /** z坐标（浮点数） */
  z: number;

  /**
   * ### 维度文字名
   *
   * 主世界 - `Overworld`\
   * 下界 - `Nether`\
   * 末地 - `TheEnd`
   */
  readonly dim: "主世界"|"下界"|"末地";

  /**
   * ### 维度ID
   *
   * 主世界 - `0`\
   * 下界 - `1`\
   * 末地 - `2`
   *
   * 如果某种情况下维度无效，或者无法获取，你会发现`dimid`的值为`-1`
   */
  dimid: 0 | 1 | 2;

  toString(): string;
}
