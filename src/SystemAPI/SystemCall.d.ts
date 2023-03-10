/// <reference path="../index.d.ts" />

declare class time{
	/** 年份数值（4位） */
	Y:number;

	/** 月份数值 */
	M:number;

	/** 天数数值 */
	D:number;

	/** 小时数值（24小时制） */
	h:number;

	/** 分钟数值 */
	m:number;

	/** 秒数值 */
	s:number;

	/** 毫秒数值 */
	ms:number;
}

declare namespace system {
  /**
   * 调用shell执行指定系统命令
   * @param cmd 执行的系统命令
   * @param callback shell进程结束之后返回数据使用的回调函数
   * @param timeLimit （可选参数）命令运行的最长时限，单位为毫秒  默认为`-1`，即不限制运行时间
   * @returns boolean 是否成功启动命令
   */
  function cmd(
    cmd: string,
    callback: (exitcode: number, output: string) => void,
    timeLimit?: number
  ): boolean;

  /**
   * 运行指定位置程序
   * @param process 运行的程序路径（与命令行参数）
   * @param callback 程序进程结束之后返回数据使用的回调函数
   * @param timeLimit （可选参数）程序进程运行的最长时限，单位为毫秒  默认为`-1`，即不限制运行时间
   * @returns boolean 是否成功启动命令
   */
  function newProcess(
    process: string,
    callback: (exitcode: number, output: string) => void,
    timeLimit?: number
  ): boolean;

	/**
	 * 获取当前时间字符串  
	 * @returns string 当前的时间字符串，使用当地时区和24小时制。 
	 */
	function getTimeStr():string;

	/**
	 * 获取当前的时间对象
	 * @returns timeObject 当前的时间对象
	 */
	function getTimeObj():time;

	/**
	 * 随机生成一个 GUID  字符串
	 * @returns string 一个随机生成的唯一标识符GUID
	 */
	function randomGuid():string;
}
