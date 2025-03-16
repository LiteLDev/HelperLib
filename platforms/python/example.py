# region import example / 导入示例

from typing import TYPE_CHECKING, Any

# I suggest not importing the package at runtime and providing type hints only in development
# this way, you don't have to install it as a plugin dependency
# 我推荐不在运行时导入该包，只让它在开发时提供类型提示，这样你就可以不用将它安装为插件依赖了
if TYPE_CHECKING:
    # you can input any ll's built-ins from `llpy`
    # 可以从 `llpy` 导入所有的 LLSE 内置类
    from llpy import *

    # you can input types provided by llpy from `llpy.types`
    # (add quotes when using these types because you didn't import it at runtime)
    # 可以从 `llpy.types` 导入本补全库提供的类型（使用时需要加引号，因为没在运行时内导入）
    from llpy.types import *

# endregion


# region register a listener example / 注册监听示例

# register manually / 使用传统方法注册一个监听器
mc.listen("onServerStarted", lambda: colorLog("green", "The Server Started!"))


# or you can use the decorator from BaseLib (no type hints) :(
# 也可以用 BaseLib 里的装饰器监听事件（没有类型提示）
@handle("onJoin")
def _(player: LLSE_Player):
    logger.info(f"Player {player.realName} joined the server!")


# endregion


# region register a command example / 注册指令示例

# register a command / 注册一个指令
cmd = mc.newCommand("testcmd", "A Test Command", PermType.Any)
cmd.optional("input", ParamType.RawText)
cmd.overload(["input"])


# set callback using decorator from BaseLib
# 使用 BaseLib 里的装饰器设置指令回调
@cmd.handle
def _(_, ori: LLSE_CommandOrigin, out: LLSE_CommandOutput, res: dict[str, Any]):
    arg: str | None = res.get("input")
    tip = f'§aYou inputed §r"§6§l{arg}§r"' if arg else "§cNothing inputted!"

    player = ori.player
    if player:
        # if player exec the cmd, send a form
        # 如果是玩家执行命令，发送表单
        form = mc.newSimpleForm().setTitle("Test Form").setContent(tip)
        player.sendForm(form, lambda _, __: None)

    else:
        # if not, send output to console
        # 不是玩家执行则输出到控制台
        out.success(tip) if arg else out.error(tip)

    return True


cmd.setup()  # set up it / 安装指令

# endregion


# and more... / 更多...


# set plugin metadata / 设置插件元信息
ll.registerPlugin(
    "example",
    "An example plugin",
    [0, 0, 1, Version.Dev],
    {"Author": "student_2333"},
)
