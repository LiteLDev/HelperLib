/// <reference path="../../index.d.ts" />

/**
 * ### 命令执行者对象
 *
 * 此对象表示某次命令的执行者，通过这个对象，可以对执行者进行一些操作
 *
 * 该类**没有构造函数**，请从指令回调函数中获取
 *
 * @see {@linkcode Command.setCallback()}
 * @see [参数 origin ：命令的执行者](https://docs.litebds.com/#/zh_CN/Development/GameAPI/Command?id=%e5%8f%82%e6%95%b0-origin-%ef%bc%9a%e5%91%bd%e4%bb%a4%e7%9a%84%e6%89%a7%e8%a1%8c%e8%80%85)
 */
declare class CommandOrigin {
  /** 指令执行主体类型 */
  readonly type: number;

  readonly typeName: string;

  /** 指令执行主体的名称 */
  readonly name: string;

  /** 指令执行主体的坐标 */
  readonly pos: FloatPos;

  /** 指令执行主体的方块坐标 */
  readonly blockPos: IntPos;

  /** 执行指令的实体（可空） */
  readonly entity?: Entity;

  /** 执行指令的玩家（可空） */
  readonly player?: Player;

  getNbt(): NbtCompound;

  toString(): string;
}
