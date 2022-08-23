/* eslint-disable @typescript-eslint/triple-slash-reference */
/// <reference path="../../index.d.ts" />
/// <reference path="../../baseTypes.d.ts" />

declare namespace mc {
  /**
   * 生成一个整数坐标对象
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
  function newIntPos(
    x: Integer,
    y: Integer,
    z: Integer,
    dimId: Integer
  ): IntPos;

  /**
   * 生成一个浮点数坐标对象
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
  function newFloatPos(x: Float, y: Float, z: Float, dimId: Integer): FloatPos;
}
