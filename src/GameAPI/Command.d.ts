/// <reference path="../index.d.ts" />

declare class commandResult {
  success: boolean;
  output: string;
}

declare enum PermType {
  Any,
  GameMasters,
  Console,
}

declare enum ParamType {
  
  Bool,     /**布尔值参数 */
  Int,      /**整数参数 */
  Float,    /**浮点数参数 */
  String,   /** 字符串参数*/
  Actor,    /** 实体目标选择器参数*/
  Player,   /** 玩家目标选择器参数*/
  BlockPos, /** 整数坐标参数*/
  Vec3,     /** 浮点数坐标参数*/
  RawText,  /** 原始字符串参数（可包含特殊字符，如逗号空格*/
  Message,  /** 消息类型参数（同 `/say,指令参数，会自动展开目标选择器等） */
  JsonValue,/** `Json`字符串参数*/
  Item,     /** 物品类型参数*/
  Block,    /** 方块类型参数*/
  Effect,   /** 效果类型参数*/
  Enum,     /** 枚举参数*/
  SoftEnum, /** 可变枚举参数*/
  ActorType,/** 实体类型参数*/
  Command,  /** 指令名称参数（仅供测试）*/
}

declare enum OriginType{
  
}

declare class CommandOrigin {
  //指令执行主体类型
  type: unknown;

  //指令执行主体的名称
  name: string;

  //指令执行主体的坐标
  pos: FloatPos;

  //指令执行主体的方块坐标
  blockPos: IntPos;

  //执行指令的实体（可空）
  entity: Entity | null;

  //执行指令的玩家（可空）
  player: Player | null;
}

declare class CommandOutput {
  /**
   * 输出一条成功信息
   * @param msg 要输出的信息
   * @returns boolean 是否成功输出
   */
  success(msg: string): boolean;

  /**
   * 输出一条错误信息
   * @param msg 要输出的信息
   * @returns boolean 是否成功输出
   */
  error(msg: string): boolean;

  /**
   * 输出一条普通信息
   * @param msg 要输出的信息
   * @returns boolean 是否成功输出
   */
  addMessage(msg: string): boolean;
}

declare class Command {
  /**
   * 设置指令别名
   * @param alias 指令别名
   * @returns boolean 是否成功设置
   */
  setAlias(alias: string): boolean;

  /**
   * 新增一个指令枚举选项
   * @param name 枚举名，用于设置参数时区分枚举
   * @param values 枚举的有效值
   * @returns boolean 是否成功设置
   */
  setEnum(name: string, values: Array<string>): boolean;

  /**
   * 新增一个必选参数
   * @param name 参数名，用于执行指令时识别参数
   * @param type 命令参数类型
   * @param enumName 枚举名（仅 `ParamType` 为 `Enum` 时有效，用于区分枚举选项）
   * @param identifier 参数标识，特殊情况下用于唯一识别参数，一般可用 `enumName` 或 `name` 代替
   * @param enumOptions 参数选项，设置为 `1` 可在指令提示中展开枚举选项
   * @returns boolean 是否成功设置
   */
  mandatory(
    name: string,
    type: ParamType,
    enumName?: string,
    identifier?: string,
    enumOptions?: number
  ): boolean;

  /**
   * 新增一个可选参数
   * @param name 参数名，用于执行指令时识别参数
   * @param type 命令参数类型
   * @param enumName 枚举名（仅 `ParamType` 为 `Enum` 时有效，用于区分枚举选项）
   * @param identifier 参数标识，特殊情况下用于唯一识别参数，一般可用 `enumName` 或 `name` 代替
   * @param enumOptions 参数选项，设置为 `1` 可在指令提示中展开枚举选项
   * @returns boolean 是否成功设置
   */
  optional(
    name: string,
    type: ParamType,
    enumName?: string,
    identifier?: string,
    enumOptions?: number
  ): boolean;

  /**
   * 新增一条指令重载
   * @param params 参数标识符，重载所用到的参数列表，可用 参数标识符、枚举名、参数名。
   * @returns boolean  是否成功设置
   */
  overload(params: Array<string>): boolean;

  /**
   * 设置指令回调
   * @param callback 注册的这个命令被执行时，接口自动调用的回调函数。
   * @returns boolean 是否成功设置
   */
  setCallback(
    callback: (
      cmd: string,
      origin: CommandOrigin,
      output: CommandOutput,
      result: Object
    ) => void
  ): boolean;

  /**
   * 安装指令
   * @returns boolean 是否成功安装
   */
  setup(): boolean;
}

declare namespace mc {
  /**
   * 执行一条后台命令
   * @param cmd 待执行的命令
   * @returns boolean 是否执行成功
   */
  function runcmd(cmd: string): boolean;

  /**
   * 执行一条后台命令（强化版）
   * @param cmd 待执行的命令
   * @returns commandResult 命令执行结果
   */
  function runcmdEx(cmd: string): commandResult;

  /**
   * 注册一条顶层命令
   * @param cmd 待注册的命令
   * @param description 命令描述文本
   * @param permission （可选参数）指令执行所需权限
   * @param flag （可选参数）默认值 `0x80`
   * @param alias （可选参数）命令的别名
   * @returns Command 指令对象
   */
  function newCommand(
    cmd: string,
    description: string,
    permission?: PermType,
    flag?: number | 0x80,
    alias?: string
  ): Command;

  /**
   * 注册一个新的玩家命令（假命令） 
   * @param cmd 待注册的命令
   * @param description 命令描述文本
   * @param callback 注册的这个命令被执行时，接口自动调用的回调函数。
   * @param level （可选参数）命令的注册等级，默认为 0 ，即所有人都可以执行  如果设置命令注册等级为1，则只有OP可以执行此命令
   * @returns boolean 是否注册成功
   */
  function regPlayerCmd(
    cmd: string,
    description: string,
    callback: (player: Player, args: Array<string>) => void,
    level?: number
  ): boolean;

  /**
   * 注册一个新的控制台命令（假命令）  
   * @param cmd 待注册的命令
   * @param description 命令描述文本
   * @param callback 注册的这个命令被执行时，接口自动调用的回调函数。
   * @returns boolean 是否注册成功
   */
   function regPlayerCmd(
    cmd: string,
    description: string,
    callback: (args: Array<string>) => void,
  ): boolean;
}
