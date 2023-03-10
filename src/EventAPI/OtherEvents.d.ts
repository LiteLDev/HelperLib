/// <reference path="../index.d.ts" />

declare namespace mc {
	/** 玩家计分板数值改变 */
  function listen(
    event: "onScoreChanged",
    listener: (player:Player,num:number,name:string,disName:string) => void
  ): boolean;

	/** 每个游戏刻触发 */
  function listen(
    event: "onTick",
    listener: () => boolean | void
  ): boolean;


	/** 服务器启动完毕 */
  function listen(
    event: "onServerStarted",
    listener: () => void
  ): boolean;

	/** 服务端执行后台命令 */
  function listen(
    event: "onConsoleCmd",
    listener: (cmd:string) => boolean | void
  ): boolean;

	/** 控制台产生命令输出 */
  function listen(
    event: "onConsoleOutput",
    listener: (output:string) => boolean | void
  ): boolean;
}
