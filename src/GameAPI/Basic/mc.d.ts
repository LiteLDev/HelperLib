/// <reference path="../../index.d.ts" />

declare namespace mc {
  /**
   * ### 生成一个整数坐标对象
   *
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimId
   * 维度ID
   *
   * 主世界 - `0`\
   * 下界 - `1`\
   * 末地 - `2`
   *
   * @returns 一个整数坐标对象
   */
  function newIntPos(x: number, y: number, z: number, dimId: 0 | 1 | 2): IntPos;

  /**
   * ### 生成一个浮点数坐标对象
   *
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimId
   * 维度ID
   *
   * 主世界 - `0`\
   * 下界 - `1`\
   * 末地 - `2`
   *
   * @returns 一个浮点数坐标对象
   */
  function newFloatPos(
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2
  ): FloatPos;
}
