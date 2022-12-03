/// <reference path="../../index.d.ts" />

declare namespace mc {
  /**
   * ### 执行一条后台命令
   *
   * @param cmd 待执行的命令
   *
   * @returns 是否执行成功
   */
  function runcmd(cmd: string): boolean;

  /**
   * ### 执行一条后台命令（强化版）
   *
   * **提示**：`runcmdEx` 与普通 {@linkcode runcmd} 实现区别非常大，在于 Ex 版本拥有**隐藏执行**的机制，执行结果不会输出至控制台，\
   * 因此如果有需要，要手动用 {@linkcode log} 函数将结果输出
   *
   * @param cmd 待执行的命令
   *
   * @returns 命令执行结果
   */
  function runcmdEx(cmd: string): {
    /** 是否执行成功 */
    success: boolean;

    /** BDS执行命令后的输出结果 */
    output: string;
  };

  /**
   * ### 注册一条顶层命令
   *
   * 这里提供了注册自定义命令的接口。
   *
   * 通过对接 BDS 内置的命令系统，你注册的命令可以由玩家、控制台、命令方块、NPC等各种游戏中可以执行命令的对象所使用，\
   * 在 addon 中，也可以使用这里所注册的命令。
   *
   * @see {@linkcode Command}
   * @see [🎯 命令注册API](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Command)
   *
   * @param cmd 待注册的命令
   * @param description 命令描述文本
   * @param permission 指令执行所需权限，默认为{@linkcode PermType.GameMasters}
   * @param flag 默认值 `0x80`，目前直接按此输入即可，后续会进行相关修改
   * @param alias 命令的别名
   *
   * 可以为命令设置多个别名，执行的时候相当于触发同一条命令\
   * （这里只能填一个，建议使用{@linkcode Command.setAlias()}）
   *
   * @returns 指令对象
   */
  function newCommand(
    cmd: string,
    description: string,
    permission?: PermType,
    flag?: number,
    alias?: string
  ): Command;

  /**
   * @deprecated
   *
   * ### 注册一个新的玩家命令（假命令）
   *
   * **警告**：
   *
   * 这里的假命令API为 **向下兼容** 而留存，请尽量使用 真命令API
   *
   * 尽管看起来比较简单，但是假命令有一些很重要的缺点，包括只能由玩家或控制台执行，其他对象（如命令方块、NPC等）都无法执行、所有参数数据都需要自行解析等等。
   *
   * @see {@linkcode mc.newCommand()}
   *
   * @param cmd 待注册的命令
   * @param description 命令描述文本
   * @param callback 注册的这个命令被执行时，接口自动调用的回调函数。
   * @param level 命令的注册等级，默认为 `0` ，即所有人都可以执行  如果设置命令注册等级为`1`，则只有OP可以执行此命令
   *
   * @returns 是否注册成功
   */
  function regPlayerCmd(
    cmd: string,
    description: string,
    callback: (player: Player, args: Array<string>) => void,
    level?: number
  ): boolean;

  /**
   * @deprecated
   *
   * ### 注册一个新的控制台命令（假命令）
   *
   * **警告**：
   *
   * 这里的假命令API为 **向下兼容** 而留存，请尽量使用 真命令API
   *
   * 尽管看起来比较简单，但是假命令有一些很重要的缺点，包括只能由玩家或控制台执行，其他对象（如命令方块、NPC等）都无法执行、所有参数数据都需要自行解析等等。
   *
   * @see {@linkcode mc.newCommand()}
   *
   * @param cmd 待注册的命令
   * @param description 命令描述文本
   * @param callback 注册的这个命令被执行时，接口自动调用的回调函数。
   *
   * @returns 是否注册成功
   */
  function regPlayerCmd(
    cmd: string,
    description: string,
    callback: (args: Array<string>) => void
  ): boolean;
}
