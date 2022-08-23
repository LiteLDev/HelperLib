/* eslint-disable @typescript-eslint/triple-slash-reference */
/// <reference path="../../index.d.ts" />
/// <reference path="../../baseTypes.d.ts" />

/**
 * ### 整数 坐标对象
 *
 * 成员均为**整数**，多用来表示方块坐标等用整数表示的位置
 *
 * 坐标对象的各个成员都是**可读写**的
 *
 * @see [坐标对象](https://docs.litebds.com/#/zh_CN/Development/GameAPI/Basic?id=%f0%9f%8e%af-%e5%9d%90%e6%a0%87%e5%af%b9%e8%b1%a1)
 */
declare class IntPos {
  constructor(x: Integer, y: Integer, z: Integer, dimId: Integer);

  /** x坐标（整数） */
  x: Integer;

  /** y坐标（整数） */
  y: Integer;

  /** z坐标（整数） */
  z: Integer;

  /**
   * ### 维度文字名
   *
   * 主世界 - `Overworld`\
   * 下界 - `Nether`\
   * 末地 - `TheEnd`
   */
  dim: string;

  /**
   * ### 维度ID
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
