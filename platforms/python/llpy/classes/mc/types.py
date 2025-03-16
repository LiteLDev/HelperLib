from typing import Any, Callable, Literal, TypedDict

from llpy import LLSE_Player


class T_RunCmdExRet(TypedDict):
    """`mc.runCmdEx()` 的返回值"""

    success: bool
    """是否执行成功"""
    output: str
    """BDS 执行命令后的输出结果"""


T_BroadcastType_RAW = Literal[0]
"""普通消息"""
T_BroadcastType_CHAT = Literal[1]
"""聊天消息"""
T_BroadcastType_TRANSLATION = Literal[2]
T_BroadcastType_POPUP = Literal[3]
T_BroadcastType_JUKEBOX_POPUP = Literal[4]
T_BroadcastType_TIP = Literal[5]
"""物品栏上方的消息"""
T_BroadcastType_SYSTEM = Literal[6]
T_BroadcastType_WHISPER = Literal[7]
T_BroadcastType_ANNOUNCEMENT = Literal[8]
T_BroadcastType_JSON_WHISPER = Literal[9]
"""JSON 格式消息"""
T_BroadcastType_JSON = Literal[10]
T_BroadcastType = (
    T_BroadcastType_RAW
    | T_BroadcastType_CHAT
    | T_BroadcastType_TRANSLATION
    | T_BroadcastType_POPUP
    | T_BroadcastType_JUKEBOX_POPUP
    | T_BroadcastType_TIP
    | T_BroadcastType_SYSTEM
    | T_BroadcastType_WHISPER
    | T_BroadcastType_ANNOUNCEMENT
    | T_BroadcastType_JSON_WHISPER
    | T_BroadcastType_JSON
)
"""`mc.broadcast()` 的文本消息类型参数"""

T_StructureMirrorType = Literal[0, 1, 2, 3]
"""
`mc.setStructure()` 的镜像模式参数

- 0. 不镜像
- 1. X 轴
- 2. Y 轴
- 3. Z 轴
"""
T_StructRotationType = Literal[0, 1, 2, 3]
"""
`mc.setStructure()` 的旋转角度参数

- 0. 不旋转
- 1. 旋转 90°
- 2. 旋转 180°
- 3. 旋转 270°
"""

T_TimeID = Literal[0, 1, 2]
"""
`mc.getTime()` 的服务器游戏时间类型参数

- 0. 自当天日出后流逝的游戏刻数 (`daytime`)
- 1. 世界总共流逝的游戏刻数 (`gametime`)
- 2. 已流逝的游戏天数 (`day`)
"""

T_WeatherID = Literal[0, 1, 2]
"""
服务器天气类型

- 0. 晴天
- 1. 雨天
- 2. 雷暴
"""

T_PlayerCmdCallback = Callable[[LLSE_Player, list[str]], Any]
T_ConsoleCmdCallback = Callable[[list[str]], Any]
