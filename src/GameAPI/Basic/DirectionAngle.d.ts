/* eslint-disable @typescript-eslint/triple-slash-reference */
/// <reference path="../../index.d.ts" />
/// <reference path="../../baseTypes.d.ts" />

/**
 * ### 方向角对象
 *
 * 引擎采用 `DirectionAngle` 对象来标示一个欧拉角，称之为「方向角对象」\
 * 它的两个成员均为浮点数，多用来表示实体的朝向等方向数据
 *
 * 方向角对象的各个成员都是**可读写**的
 */
declare class DirectionAngle {
  constructor(pitch: Float, yaw: Float);

  /** 俯仰角（-90° ~ 90°） */
  pitch: Float;

  /** 偏航角（旋转角） */
  yaw: Float;

  /**
   * 将偏航角转换为基本朝向
   *
   * 返回值为0-3，代表 北东南西 四个基本朝向\
   * 用于快速确定实体面向的大致方向
   *
   * @returns 当前方向角对象所指示的基本朝向
   */
  toFacing(): Integer;

  toString(): string;
}
