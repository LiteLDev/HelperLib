/// <reference path="../index.d.ts" />

declare namespace mc {
  /** 玩家金额增加前事件 */
  function listen(
    event: "beforeMoneyAdd",
    listener: (xuid: string, money: number) => boolean | void
  ): boolean;

  /** 玩家金额增加事件 */
  function listen(
    event: "onMoneyAdd",
    listener: (xuid: string, money: number) => void
  ): boolean;

  /** 玩家金额减少前事件 */
  function listen(
    event: "beforeMoneyReduce",
    listener: (xuid: string, money: number) => boolean | void
  ): boolean;

  /** 玩家金额减少事件 */
  function listen(
    event: "onMoneyReduce",
    listener: (xuid: string, money: number) => boolean | void
  ): boolean;

  /** 玩家转账前事件 */
  function listen(
    event: "beforeMoneyTrans",
    listener: (xuid: string, money: number) => boolean | void
  ): boolean;

  /** 玩家转账事件 */
  function listen(
    event: "onMoneyTrans",
    listener: (xuid: string, money: number) => boolean | void
  ): boolean;

  /** 设置玩家金额前事件 */
  function listen(
    event: "beforeMoneySet",
    listener: (xuid: string, money: number) => boolean | void
  ): boolean;

  /** 设置玩家金额事件 */
  function listen(
    event: "onMoneySet",
    listener: (xuid: string, money: number) => boolean | void
  ): boolean;
}
