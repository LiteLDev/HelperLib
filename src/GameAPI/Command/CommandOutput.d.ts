/// <reference path="../../index.d.ts" />

/**
 * ### 🎯 命令输出对象
 *
 * 通过这个对象，可以向命令执行者输出命令的执行结果。
 *
 * 该类**没有构造函数**，请从指令回调函数中获取
 *
 * @see {@linkcode Command.setCallback()}
 * @see [参数 output ：向命令执行者输出命令的执行结果](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Command?id=%e5%8f%82%e6%95%b0-output-%ef%bc%9a%e5%90%91%e5%91%bd%e4%bb%a4%e6%89%a7%e8%a1%8c%e8%80%85%e8%be%93%e5%87%ba%e5%91%bd%e4%bb%a4%e7%9a%84%e6%89%a7%e8%a1%8c%e7%bb%93%e6%9e%9c)
 */
declare class CommandOutput {
  readonly empty: boolean;

  readonly successCount: number;

  /**
   * ### 输出一条成功信息
   * 
   * @param msg 要输出的信息
   * 
   * @param param 要替换的参数
   * 
   * @returns 是否成功输出
   */
  success(msg?: string, param?: any[]): boolean;

  /**
   * ### 输出一条错误信息
   * 
   * @param msg 要输出的信息
   * 
   * @param param 要替换的参数
   * 
   * @returns 是否成功输出
   */
  error(msg: string, param?: any[]): boolean;

  /**
   * ### 输出一条普通信息
   * 
   * @param msg 要输出的信息
   * 
   * @param param 要替换的参数
   * 
   * @param arg3 整数 作用未知
   * 
   * @returns 是否成功输出
   */
  addMessage(msg: string, param?: any[], arg3?:number): boolean;

  toString(): string;
}
