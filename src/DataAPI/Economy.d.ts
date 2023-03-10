/* eslint-disable @typescript-eslint/triple-slash-reference */

declare class record {
  /** 此项交易的发起者玩家Xuid */
  from: string;

  /** 此项交易的接收者玩家Xuid */
  to: string;

  /** 此项交易的金额 */
  money: number;

  /** 此项交易发生时的时间字符串 */
  time: string;

  /** 此交易的附加说明信息 */
  note: string;
}

/** 经济系统 API */
declare namespace money {
  /**
   * 设置玩家的存款金额
   * @param xuid 要操作的玩家的Xuid标识符
   * @param money 要设置的金额
   * @returns boolean 是否设置成功
   */
  function set(xuid: string, money: number): boolean;

  /**
   * 获取玩家的存款金额
   * @param xuid 要读取的玩家的Xuid标识符
   * @returns number 玩家的资金数值
   */
  function get(xuid: string): number;

  /**
   * 增加玩家的存款
   * @param xuid 要操作的玩家的Xuid标识符
   * @param money 要增加的金额
   */
  function add(xuid: string, money: number): boolean;

  /**
   * 减少玩家的存款
   * @param xuid 要操作的玩家的Xuid标识符
   * @param money 要减少的金额
   */
  function reduce(xuid: string, money: number): boolean;

  /**
   * 进行一笔转账
   * @param xuid_1 付款的玩家的Xuid标识符
   * @param xuid_2 收款的玩家的Xuid标识符
   * @param money 要支付的金额
   * @param note （可选参数）给这笔转账附加一些文字说明
   * @returns boolean 是否转账成功
   */
  function trans(
    xuid_1: string,
    xuid_2: string,
    money: number,
    note?: string
  ): boolean;

  /**
   * 查询历史账单
   * @param xuid 要操作的玩家的Xuid标识符
   * @param time 查询从现在开始往前time秒的记录
   * @returns Array<Object> 查询结果对象的数组
   */
  function getHistory(xuid: string, time: number): Array<record>;

  /**
   * 删除账单历史记录
   * @param time 删除从现在开始往前time秒的记录
   * @returns boolean
   */
  function clearHistory(time: number): boolean;
}
