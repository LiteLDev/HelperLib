from typing import Literal, NoReturn

class Format:
    """格式化代码枚举"""

    def __init__(self) -> NoReturn: ...

    Black: Literal["§0"]
    """格式化代码枚举 | 黑色"""
    DarkBlue: Literal["§1"]
    """格式化代码枚举 | 深蓝色"""
    DarkGreen: Literal["§2"]
    """格式化代码枚举 | 深绿色"""
    DarkAqua: Literal["§3"]
    """格式化代码枚举 | 湖蓝色"""
    DarkRed: Literal["§4"]
    """格式化代码枚举 | 深红色"""
    DarkPurple: Literal["§5"]
    """格式化代码枚举 | 紫色"""
    Gold: Literal["§6"]
    """格式化代码枚举 | 金色"""
    Gray: Literal["§7"]
    """格式化代码枚举 | 灰色"""
    DarkGray: Literal["§8"]
    """格式化代码枚举 | 深灰色"""
    Blue: Literal["§9"]
    """格式化代码枚举 | 蓝色"""
    Green: Literal["§a"]
    """格式化代码枚举 | 浅绿色"""
    Aqua: Literal["§b"]
    """格式化代码枚举 | 天蓝色"""
    Red: Literal["§c"]
    """格式化代码枚举 | 浅红色"""
    LightPurple: Literal["§d"]
    """格式化代码枚举 | 浅紫色"""
    Yellow: Literal["§e"]
    """格式化代码枚举 | 浅黄色"""
    White: Literal["§f"]
    """格式化代码枚举 | 白色"""
    MinecoinGold: Literal["§g"]
    """格式化代码枚举 | 硬币金色"""

    Bold: Literal["§l"]
    """格式化代码枚举 | 加粗"""
    Italics: Literal["§o"]
    """格式化代码枚举 | 斜体"""
    Underline: Literal["§n"]
    """格式化代码枚举 | 下划线"""
    StrikeThrough: Literal["§m"]
    """格式化代码枚举 | 删除线"""
    Random: Literal["§k"]
    """格式化代码枚举 | 乱码"""
    Clear: Literal["§r"]
    """格式化代码枚举 | 清除格式"""
