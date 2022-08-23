/* eslint-disable @typescript-eslint/triple-slash-reference */
/// <reference path="../../index.d.ts" />
/// <reference path="../../baseTypes.d.ts" />

/**
 * ### 浮点数 坐标对象
 *
 * 成员均为**浮点数**，多用来表示实体坐标等用无法用整数表示的位置
 *
 * 坐标对象的各个成员都是**可读写**的
 */
declare class FloatPos {
  constructor(x: Float, y: Float, z: Float, dimId: Integer);

  /** x坐标（浮点数） */
  x: Float;

  /** y坐标（浮点数） */
  y: Float;

  /** z坐标（浮点数） */
  z: Float;

  /**
   * 维度文字名
   *
   * 主世界 - `Overworld`\
   * 下界 - `Nether`\
   * 末地 - `TheEnd`
   */
  dim: string;

  /**
   * 维度ID
   *
   * 主世界 - `0`\
   * 下界 - `1`\
   * 末地 - `2`
   *
   * 如果某种情况下维度无效，或者无法获取，你会发现`dimid`的值为`-1`
   */
  dimid: Integer;

  toString(): string;
}
