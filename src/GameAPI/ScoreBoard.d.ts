/// <reference path="../index.d.ts" />

declare class Objective {
  /** 计分项名称 */
  readonly name: string;

  /** 计分项显示名称 */
  readonly displayName: string;

  /**
   * 获取跟踪的某个目标的分数
   * @param target 待查询的跟踪目标，可传入玩家对象或者任意字符串
   * @returns number 该目标/玩家在此计分项中的分数
   */
  getScore(target: Player | string): number;

  /**
   * 修改某个目标的分数
   * @param target 计分项跟踪的目标，可传入玩家对象或者任意字符串
   * @param score 要设置的分数
   * @returns number|null 该目标在经过设置操作后的分数
   */
  setScore(target: Player | string, score: number): number | null;

  /**
   * 修改某个目标的分数
   * @param target 计分项跟踪的目标，可传入玩家对象或者任意字符串
   * @param score 要增加的分数
   * @returns number|null 该目标在经过增加操作后的分数
   */
  addScore(target: Player | string, score: number): number | null;

  /**
   * 修改某个目标的分数
   * @param target 计分项跟踪的目标，可传入玩家对象或者任意字符串
   * @param score 要减少的分数
   * @returns number|null 该目标在经过减少操作后的分数
   */
  reduceScore(target: Player | string, score: number): number | null;

  /**
   * 停止跟踪某个目标
   * @param target 计分项跟踪的目标，可传入玩家对象或者任意字符串
   * @returns boolean 是否停止成功
   */
  deleteScore(target: Player | string): boolean;

  /**
   * 设置计分项的显示状态
   * @param slot 显示槽位名称字符串，可以为`"sidebar"`/`"belowname"`/`"list"`
   * @param sortOrder （可选参数）排序方式，可以为`0`(升序)或`1`(降序)，默认值为`0`
   * @returns boolean 是否设置成功
   */
  setDisplay(
    slot: "sidebar" | "belowname" | "list",
    sortOrder?: number | sidebar
  ): boolean;
}

declare namespace mc {
  /**
   * 创建一个新的计分项
   * @param name 计分项名称
   * @param displayName 计分项显示名称
   * @returns Objective|null 新增创建的计分项对象
   */
  function newScoreObjective(
    name: string,
    displayName: string
  ): Objective | null;

  /**
   * 获取某个已存在的计分项
   * @param name 要获取的计分项名称
   * @returns Objective|null 对应的计分项对象
   */
  function getScoreObjective(name: string): Objective | null;

  /**
   * 获取所有计分项
   * @returns Array<Objective> 计分板系统记录的所有计分项对象
   */
  function getAllScoreObjectives(): Array<Objective>;

  /**
   * 获取某个处于显示状态的计分项
   * @param slot 待查询的显示槽位名称，可以为`"sidebar"`/`"belowname"`/`"list"`
   * @returns Objective|null 正在`slot`槽位显示的计分项
   */
  function getDisplayObjective(
    slot: "sidbar" | "belowname" | "list"
  ): Objective | null;

  /**
   * 移除一个已存在的计分项
   * @param name 计分项名称
   * @returns boolean 是否移除成功
   */
  function removeScoreObjective(name: string): boolean;

  /**
   * 使计分项停止显示
   * @param slot 显示槽位名称字符串，可以为`"sidebar"`/`"belowname"`/`"list"`
   * @returns boolean 是否清除成功
   */
  function clearDisplayObjective(
    slot: "sidebar" | "belowname" | "list"
  ): boolean;

  /**
   * 获取玩家计分项的分数
   * （可查询离线玩家计分板）
   * 
   * @param uuid 玩家的UUID
   * @param name 计分项名称
   * @returns 计分板上的数值
   */
  function getPlayerScore(uuid:string, name:string):number

  /**
   * 设置玩家计分项的分数
   * （可修改离线玩家计分板）
   * @param uuid 玩家的UUID 
   * @param name 计分项名称  
   * @param value 要设置的值
   * @returns 是否设置成功
   */
  function setPlayerScore(uuid:string, name:string, value:number):boolean

  /**
   * 增加玩家计分项的分数
   * （可修改离线玩家计分板）
   * @param uuid 玩家的UUID 
   * @param name 计分项名称  
   * @param value 要增加的值
   * @returns 是增加置成功
   */
  function addPlayerScore(uuid:string, name:string, value:number):boolean

  /**
   * 减少玩家计分项的分数
   * （可修改离线玩家计分板）
   * @param uuid 玩家的UUID 
   * @param name 计分项名称  
   * @param value 要减少的值
   * @returns 是否减少成功
   */
  function reducePlayerScore(uuid:string, name:string, value:number):boolean



}

declare class LLSE_Objective extends Objective{}