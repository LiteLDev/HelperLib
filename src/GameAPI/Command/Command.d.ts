/// <reference path="../../index.d.ts" />

/**
 * ### 指令对象
 *
 * 通过对接 BDS 内置的命令系统，你注册的命令可以由玩家、控制台、命令方块、NPC等各种游戏中可以执行命令的对象所使用，\
 * 在 addon 中，也可以使用这里所注册的命令。
 *
 * 通过指令对象，你可以为这个命令注册各式各样的形式、功能。
 *
 * 该类**没有构造函数**，请使用{@linkcode mc.newCommand()}创建
 *
 * @see [命令注册API](https://docs.litebds.com/#/zh_CN/Development/GameAPI/Command?id=%e5%91%bd%e4%bb%a4%e6%b3%a8%e5%86%8c-api)
 */
declare class Command {
  readonly name: string;

  readonly registered: boolean;

  /**
   * ### 设置指令别名
   *
   * @param alias 指令别名
   *
   * @returns 是否成功设置
   */
  setAlias(alias: string): boolean;

  /**
   * ### 新增一个指令枚举选项
   *
   * @param name 枚举名，用于设置参数时区分枚举
   * @param values 枚举的有效值
   *
   * @returns 是否成功设置
   */
  setEnum(name: string, values: Array<string>): boolean;

  /**
   * ### 新增一个必选参数
   *
   * @param name 参数名，用于执行指令时识别参数
   * @param type 命令参数类型
   * @param enumName 枚举名（仅 `ParamType` 为 `Enum` 时有效，用于区分枚举选项）
   * @param identifier 参数标识，特殊情况下用于唯一识别参数，一般可用 `enumName` 或 `name` 代替
   * @param enumOptions 参数选项，设置为 `1` 可在指令提示中展开枚举选项，如 `<action : TagChangeAction>` 会变成 `<add|remove>`
   *
   * @returns 是否成功设置
   */
  mandatory(
    name: string,
    type: ParamType,
    enumName?: string,
    identifier?: string,
    enumOptions?: number
  ): boolean;

  /**
   * ### 新增一个可选参数
   *
   * @param name 参数名，用于执行指令时识别参数
   * @param type 命令参数类型
   * @param enumName 枚举名（仅 `ParamType` 为 `Enum` 时有效，用于区分枚举选项）
   * @param identifier 参数标识，特殊情况下用于唯一识别参数，一般可用 `enumName` 或 `name` 代替
   * @param enumOptions 参数选项，设置为 `1` 可在指令提示中展开枚举选项，如 `<action : TagChangeAction>` 会变成 `<add|remove>`
   *
   * @returns 是否成功设置
   */
  optional(
    name: string,
    type: ParamType,
    enumName?: string,
    identifier?: string,
    enumOptions?: number
  ): boolean;

  setSoftEnum(arg1: string, arg2: Array<string>): string;

  addSoftEnumValues(arg1: string, arg2: Array<string>): boolean;

  removeSoftEnumValues(arg1: string, arg2: Array<string>): boolean;

  getSoftEnumValues(arg1: string): Array<string>;

  getSoftEnumNames(): Array<string>;

  /**
   * ### 新增一条指令重载
   *
   * **编者注**：必须在调用{@linkcode Command.setup()}前调用此函数，否则会报错
   *
   * 指令重载是 BDS 区分不同指令形式的方法，每一种不同的指令形式对应着一种指令重载。
   *
   * 如你所见，指令重载中提供的各项参数名组成了一种新的指令形式
   *
   * @param params 参数标识符，重载所用到的参数列表，可用 参数标识符、枚举名、参数名。
   *
   * 注意不能使用无法区分具体参数的标识符，如两个参数都叫 `action` 但枚举选项不同，此时应该使用枚举名而不是参数名
   *
   * @returns  是否成功设置
   */
  overload(params?: Array<string>): boolean;

  /**
   * ### 设置指令回调
   *
   * @param callback 注册的这个命令被执行时，接口自动调用的回调函数。
   *
   * @returns 是否成功设置
   */
  setCallback(
    callback: (
      cmd: Command,
      origin: CommandOrigin,
      output: CommandOutput,
      result: object
    ) => void
  ): boolean;

  /**
   * ### 安装指令
   *
   * **编者注**：请在调用此函数前调用{@linkcode Command.overload()}，否则会报错
   *
   * @returns 是否成功安装
   */
  setup(): boolean;
}
