from typing import Any, Callable, Literal, TypedDict

from typing_extensions import deprecated

from llpy import LLSE_Item

from . import LLSE_Player


@deprecated("请使用 `LLSE_Player.getInventory()`")
class T_PlayerInventory(TypedDict):
    """`LLSE_Player.getAllItems()` 返回的物品栏信息"""

    hand: LLSE_Item
    offHand: LLSE_Item
    inventory: list[LLSE_Item]
    armor: list[LLSE_Item]
    endChest: list[LLSE_Item]


T_PermLevel = Literal[0, 1, 2, 3, 4]
"""
操作权限等级

- 0. 普通成员
- 1. OP
- 4. 控制台
"""
T_GameMode = Literal[0, 1, 2, 6]
"""
游戏模式

- 0. 生存
- 1. 创造
- 2. 冒险
- 6. 旁观
"""
T_TextPacketType = Literal[0, 1, 4, 5, 9]
"""
`LLSE_Player.tell()` 发送的文本消息类型

- 0. 普通消息 (`Raw`)
- 1. 聊天消息 (`Chat`)
- 4. 音乐盒消息 (`Popup`)
- 5. 物品栏上方的消息 (`Tip`)
- 9. JSON格式消息 (`JSON`)
"""
T_TitlePacketType = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
"""
`LLSE_Player.setTitle()` 发送的标题类型

- 0. 清空 (`Clear`)
- 1. 重设 (`Reset`)
- 2. 主标题 (`SetTitle`)
- 3. 副标题 (`SetSubTitle`)
- 4. ActionBar (`SetActionBar`)
- 5. 设置显示时间 (`SetDurations`)
- 6. Json型主标题 (`TitleTextObject`)
- 7. Json型副标题 (`SubtitleTextObject`)
- 8. Json型 ActionBar (`ActionbarTextObject`)
"""
T_BossEventColor = Literal[0, 1, 2, 3, 4, 5, 6]
"""
`LLSE_Player.setBossBar()` 设置的 Boss 条颜色

- 0. 灰色 (`Gray`)
- 1. 蓝色 (`Blue`)
- 2. 红色 (`Red`)
- 3. 绿色 (`Green`)
- 4. 黄色 (`Yellow`)
- 5. 紫色 (`Purple`)
- 6. 白色 (`White`)
"""
T_AbilityID = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
"""
`LLSE_Player.setAbility()` 设置的 Ability ID

（以下翻译部分由 GPT-3.5 提供）

- 0. 放置 (`Build`)
- 1. 挖掘 (`Mine`)
- 2. 门与开关 (`DoorsAndSwitches`)
- 3. 打开容器 (`OpenContainers`)
- 4. 攻击玩家 (`AttackPlayers`)
- 5. 攻击生物 (`AttackMobs`)
- 6. 操作员命令 (`OperatorCommands`)
- 7. 传送 (`Teleport`)
- 8. 无敌 (`Invulnerable`)
- 9. 正在飞行 (`Flying`)
- 10. 飞行 (`MayFly`)
- 11. 快速建造 (`Instabuild`)
- 12. 引雷 (`Lightning`)
- 13. 飞行速度 (`FlySpeed`)
- 14. 行走速度 (`WalkSpeed`)
- 15. 禁言 (`Muted`)
- 16. 世界生成 (`WorldBuilder`)
- 17. 穿墙 (`NoClip`)
"""
T_ModalFormCallback = Callable[[LLSE_Player, bool | None], Any]
T_SimpleFormCallback = Callable[[LLSE_Player, int | None], Any]
T_CustomFormCallback = Callable[
    [LLSE_Player, list[bool | int | str | None] | None],
    Any,
]


class T_NavigatePath(TypedDict):
    """`LLSE_Player.simulateNavigateTo()` 的返回值"""

    isFullPath: bool
    path: list[list[int]]
