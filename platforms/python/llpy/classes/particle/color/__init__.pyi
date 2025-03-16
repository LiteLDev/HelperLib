from typing import NoReturn

from ..types import (
    T_ParticleColorApricot,
    T_ParticleColorBlack,
    T_ParticleColorCocoa,
    T_ParticleColorDark,
    T_ParticleColorFawn,
    T_ParticleColorGreen,
    T_ParticleColorIndigo,
    T_ParticleColorLavender,
    T_ParticleColorOatmeal,
    T_ParticleColorPink,
    T_ParticleColorRed,
    T_ParticleColorSlate,
    T_ParticleColorTeal,
    T_ParticleColorVatblue,
    T_ParticleColorWhite,
    T_ParticleColorYellow,
)

class ParticleColor:
    """粒子生成器颜色枚举"""

    def __init__(self) -> NoReturn: ...

    Black: T_ParticleColorBlack
    """粒子颜色枚举 | 黑色"""
    Indigo: T_ParticleColorIndigo
    """粒子颜色枚举 | 靛蓝"""
    Lavender: T_ParticleColorLavender
    """粒子颜色枚举 | 薰衣草紫"""
    Teal: T_ParticleColorTeal
    """粒子颜色枚举 | 青色"""
    Cocoa: T_ParticleColorCocoa
    """粒子颜色枚举 | 可可棕"""
    Dark: T_ParticleColorDark
    """粒子颜色枚举 | 黑色"""
    Oatmeal: T_ParticleColorOatmeal
    """粒子颜色枚举 | 燕麦色"""
    White: T_ParticleColorWhite
    """粒子颜色枚举 | 白色"""
    Red: T_ParticleColorRed
    """粒子颜色枚举 | 红色"""
    Apricot: T_ParticleColorApricot
    """粒子颜色枚举 | 杏色"""
    Yellow: T_ParticleColorYellow
    """粒子颜色枚举 | 黄色"""
    Green: T_ParticleColorGreen
    """粒子颜色枚举 | 绿色"""
    Vatblue: T_ParticleColorVatblue
    """粒子颜色枚举 | 深蓝"""
    Slate: T_ParticleColorSlate
    """粒子颜色枚举 | 石板灰"""
    Pink: T_ParticleColorPink
    """粒子颜色枚举 | 粉色"""
    Fawn: T_ParticleColorFawn
    """粒子颜色枚举 | 鹿褐色"""
