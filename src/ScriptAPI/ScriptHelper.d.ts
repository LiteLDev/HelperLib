/// <reference path="../index.d.ts" />

declare enum Version {
  Release,
  Beta,
  Dev,
}

declare namespace ll {
  /**
   * 注册插件
   * @param name 插件名字
   * @param introduction 对插件的简短介绍
   * @param version 插件的版本信息[2,0,1]
   * @param otherInformation 其他你愿意提供的的附加信息（如许可证、开源地址等）
   */
  function registerPlugin(
    name: string,
    introduction: string,
    version: readonly [number, number, number, Version?],
    otherInformation: Record<string, string>
  ): void;
}

/**
 * 输出信息到控制台
 * @param data 待输出的变量或者数据
 */
declare function log(...data: any[]): void;

/**
 * 输出带颜色文本
 * @param color 此行输出的颜色(代码示例和效果见文档)
 * @param data 待输出的变量或者数据
 */
declare function colorLog(color: string, ...data: any[]): void;

/**
 * 异步输出
 * @param data 待输出的变量或者数据
 */
declare function fastLog(...data: any[]): void;

/**
 * 推迟一段时间执行代码
 * @param func 待执行的函数或待执行的代码段
 * @param msec 推迟执行的时间（毫秒）
 * @returns Integer|null 此任务ID
 */
declare function setTimeout(
  func: () => void | string,
  msec: number
): number | null;

/**
 * 设置周期执行代码
 * @param func 待执行的函数或待执行的代码段
 * @param msec 执行间隔周期（毫秒）
 * @returns Integer|null 此任务ID
 */
declare function setInterval(
  func: () => void | string,
  msec: number
): number | null;

/**
 * 取消延时 / 周期执行项
 * @param taskid 由前几个函数返回的任务ID
 * @returns boolean 是否取消成功
 */
declare function clearInterval(taskid: number): boolean | null;
