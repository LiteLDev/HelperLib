from typing import Literal

from .pos import FloatPos, IntPos

T_DimIDOverWorld = Literal[0]
"""维度ID | 主世界"""
T_DimIDNether = Literal[1]
"""维度ID | 下界"""
T_DimIDTheEnd = Literal[2]
"""维度ID | 末地"""
T_DimID = T_DimIDOverWorld | T_DimIDNether | T_DimIDTheEnd

T_BasicFacing = Literal[0, 1, 2, 3]
"""基本朝向。`0-3` 分别代表 北东南西 四个基本朝向"""

T_PosType = IntPos | FloatPos
T_Number = int | float

T_EffectID = Literal[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
]
"""
药水效果的 数字 ID

| 数字 ID | 名称         | 效果            |
| ------- | ------------ | --------------- |
| 1       | 迅捷         | `speed`           |
| 2       | 缓慢         | `slowness`        |
| 3       | 急迫         | `haste`           |
| 4       | 挖掘疲劳     | `mining_fatigue`  |
| 5       | 力量         | `strength`        |
| 6       | 瞬间治疗     | `instant_health`  |
| 7       | 瞬间伤害     | `instant_damage`  |
| 8       | 跳跃提升     | `jump_boost`      |
| 9       | 反胃         | `nausea`          |
| 10      | 生命恢复     | `regeneration`    |
| 11      | 抗性提升     | `resistance`      |
| 12      | 抗火         | `fire_resistance` |
| 13      | 水下呼吸     | `water_breathing` |
| 14      | 隐身         | `invisibility`    |
| 15      | 失明         | `blindness`       |
| 16      | 夜视         | `night_vision`    |
| 17      | 饥饿         | `hunger`          |
| 18      | 虚弱         | `weakness`        |
| 19      | 中毒         | `poison`          |
| 20      | 凋零         | `wither`          |
| 21      | 生命提升     | `health_boost`    |
| 22      | 伤害吸收     | `absorption`      |
| 23      | 饱和         | `saturation`      |
| 24      | 飘浮         | `levitation`      |
| 25      | 中毒（致命） | `fatal_poison`    |
| 26      | 潮涌能量     | `conduit_power`   |
| 27      | 缓降         | `slow_falling`    |
| 28      | 不祥之兆     | `bad_omen`        |
| 29      | 村庄英雄     | `village_hero`    |
| 30      | 黑暗         | `darkness`        |
"""
