/* eslint-disable @typescript-eslint/triple-slash-reference */
/// <reference path="../../index.d.ts" />

/**
 * ### 方向角对象
 *
 * 引擎采用 `DirectionAngle` 对象来标示一个欧拉角，称之为「方向角对象」\
 * 它的两个成员均为浮点数，多用来表示实体的朝向等方向数据
 *
 * 方向角对象的各个成员都是**可读写**的
 *
 * @see [方向角对象](https://docs.litebds.com/#/zh_CN/Development/GameAPI/Basic?id=%f0%9f%93%90-%e6%96%b9%e5%90%91%e8%a7%92%e5%af%b9%e8%b1%a1)
 */
declare class DirectionAngle {
  constructor(pitch: number, yaw: number);

  /** 俯仰角（-90° ~ 90°） */
  pitch: number;

  /** 偏航角（旋转角） */
  yaw: number;

  /**
   * ### 将偏航角转换为基本朝向
   *
   * 返回值为`0`-`3`，代表 北东南西 四个基本朝向\
   * 用于快速确定实体面向的大致方向
   *
   * @returns 当前方向角对象所指示的基本朝向
   */
  toFacing(): 0 | 1 | 2 | 3;

  toString(): string;
}
