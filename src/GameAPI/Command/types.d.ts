/// <reference path="../../index.d.ts" />

/**
 * ### 指令执行所需权限枚举
 *
 * @see [注册一条顶层命令](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Command?id=%e6%b3%a8%e5%86%8c%e4%b8%80%e6%9d%a1%e9%a1%b6%e5%b1%82%e5%91%bd%e4%bb%a4)
 * @see {@linkcode mc.newCommand()}
 * @see https://github.com/LiteLDev/LiteLoaderBDS/blob/main/LiteLoader/Header/MC/Command.hpp#L17
 */
declare enum PermType {
  /** 任何人都可以执行这条指令 */
  Any = 0,

  /** 只有OP可以执行这条指令（默认值） */
  GameMasters = 1,

  Admin = 2,

  HostPlayer = 3,

  /** 只有控制台可以执行这条指令 */
  Console = 4,

  Internal = 5,
}

/**
 * ### 命令参数类型
 *
 * @see [有效的指令参数及其解释](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Command?id=%e6%9c%89%e6%95%88%e7%9a%84%e5%91%bd%e4%bb%a4%e5%8f%82%e6%95%b0%e7%b1%bb%e5%9e%8b%e5%8f%8a%e8%a7%a3%e9%87%8a)
 * @see [`Command.mandatory()`](Command.d.ts)
 * @see [`Command.optional()`](Command.d.ts)
 */
declare enum ParamType {
  /** `boolean` - 布尔值参数 */
  Bool,

  /** `number` - 整数参数 */
  Int,

  /** `number` - 浮点数参数 */
  Float,

  /** `string` - 字符串参数 */
  String,

  /** {@linkcode Entity} - 实体目标选择器参数 */
  Actor,

  /** {@linkcode Player} - 玩家目标选择器参数 */
  Player,

  /** {@linkcode IntPos} - 整数坐标参数 */
  BlockPos,

  /** {@linkcode FloatPos} - 浮点数坐标参数 */
  Vec3,

  /** `string` - 原始字符串参数（可包含特殊字符，如逗号空格） */
  RawText,

  /** `string` - 消息类型参数（同 `/say` 指令参数，会自动展开目标选择器等） */
  Message,

  /** `string`  - `Json`字符串参数 */
  JsonValue,

  /** [`Item`](../Item.d.ts) - 物品类型参数 */
  Item,

  /** [`Block`](../Block/Block.d.ts) - 方块类型参数 */
  Block,

  /** `string`  - 效果类型参数 */
  Effect,

  /** `string`  - 枚举参数 */
  Enum,

  /** `string`  - 可变枚举参数 */
  SoftEnum,

  /** `string`  - 实体类型参数 */
  ActorType,

  /** `string`  - 指令名称参数（仅供测试） */
  Command,

  /** `null` - WildcardCommandSelector\<Actor\> */
  WildcardSelector,
}

/**
 * ### 指令执行主体类型
 *
 * @see [参数 origin ：命令的执行者](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Command?id=%e5%8f%82%e6%95%b0-origin-%ef%bc%9a%e5%91%bd%e4%bb%a4%e7%9a%84%e6%89%a7%e8%a1%8c%e8%80%85)
 * @see {@linkcode CommandOrigin.type}
 * @see https://github.com/LiteLDev/LiteLoaderBDS/blob/main/LiteLoader/Header/MC/Command.hpp#L22
 */
declare enum OriginType {
  Player = 0,
  Block = 1,
  MinecartBlock = 2,
  DevConsole = 3,
  Test = 4,
  AutomationPlayer = 5,
  ClientAutomation = 6,
  Server = 7,
  Actor = 8,
  Virtual = 9,
  GameArgument = 10,
  ActorServer = 11,
  Precompiled = 12,
  GameDirectorEntity = 13,
  Script = 14,
  ExecuteContext = 15,

  DedicatedServer = 7, // Server
}

/**
 * @see https://github.com/LiteLDev/LiteLoaderBDS/blob/main/ScriptEngine/API/CommandAPI.cpp#L32
 * @see https://github.com/LiteLDev/LiteLoaderBDS/blob/main/LiteLoader/Header/MC/CommandParameterData.hpp#L29
 */
declare enum ParamOption {
  None = 0,

  EnumAutocompleteExpansion = 1,

  /** be used in block or item name enum */
  HasSemanticConstraint = 2,

  /** be used in NewExecuteCommand */
  EnumAsChainedCommand = 4,
}
