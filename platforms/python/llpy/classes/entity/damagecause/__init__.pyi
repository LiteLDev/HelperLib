from typing import NoReturn

from llpy.classes.base.enumdefine import _T_EnumDefineClass

from ..types import (
    T_DamageCauseAnvil,
    T_DamageCauseBlockExplosion,
    T_DamageCauseCharging,
    T_DamageCauseContact,
    T_DamageCauseDrowning,
    T_DamageCauseEntityAttack,
    T_DamageCauseEntityExplosion,
    T_DamageCauseFall,
    T_DamageCauseFallingBlock,
    T_DamageCauseFire,
    T_DamageCauseFireTick,
    T_DamageCauseFireworks,
    T_DamageCauseFlyIntoWall,
    T_DamageCauseFreezing,
    T_DamageCauseLava,
    T_DamageCauseLightning,
    T_DamageCauseMagic,
    T_DamageCauseMagma,
    T_DamageCauseOverride,
    T_DamageCausePiston,
    T_DamageCauseProjectile,
    T_DamageCauseStalactite,
    T_DamageCauseStalagmite,
    T_DamageCauseStarve,
    T_DamageCauseSuffocation,
    T_DamageCauseSuicide,
    T_DamageCauseTemperature,
    T_DamageCauseThorns,
    T_DamageCauseVoid,
    T_DamageCauseWither,
)

class ActorDamageCause:
    """实体伤害类型枚举"""

    def __init__(self) -> NoReturn: ...

    Override: T_DamageCauseOverride
    """伤害类型枚举 | 非正常伤害"""
    Contact: T_DamageCauseContact
    """伤害类型枚举 | 接触伤害（仙人掌、浆果丛）"""
    EntityAttack: T_DamageCauseEntityAttack
    """伤害类型枚举 | 实体攻击伤害"""
    Projectile: T_DamageCauseProjectile
    """伤害类型枚举 | 弹射物伤害"""
    Suffocation: T_DamageCauseSuffocation
    """伤害类型枚举 | 窒息伤害"""
    Fall: T_DamageCauseFall
    """伤害类型枚举 | 摔落伤害"""
    Fire: T_DamageCauseFire
    """伤害类型枚举 | 燃烧伤害"""
    FireTick: T_DamageCauseFireTick
    """伤害类型枚举 | 点燃伤害"""
    Lava: T_DamageCauseLava
    """伤害类型枚举 | 岩浆伤害"""
    Drowning: T_DamageCauseDrowning
    """伤害类型枚举 | 溺水伤害"""
    BlockExplosion: T_DamageCauseBlockExplosion
    """伤害类型枚举 | 方块爆炸、末地水晶爆炸伤害"""
    EntityExplosion: T_DamageCauseEntityExplosion
    """伤害类型枚举 | 实体爆炸伤害（末地水晶不算）"""
    Void: T_DamageCauseVoid
    """伤害类型枚举 | 虚空伤害"""
    Suicide: T_DamageCauseSuicide
    """伤害类型枚举 | `kill` 指令伤害"""
    Magic: T_DamageCauseMagic
    """伤害类型枚举 | 魔法伤害"""
    Wither: T_DamageCauseWither
    """伤害类型枚举 | 凋零效果伤害"""
    Starve: T_DamageCauseStarve
    """伤害类型枚举 | 饥饿伤害"""
    Anvil: T_DamageCauseAnvil
    """伤害类型枚举 | 下落铁砧砸中伤害"""
    Thorns: T_DamageCauseThorns
    """伤害类型枚举 | 荆棘伤害"""
    FallingBlock: T_DamageCauseFallingBlock
    """伤害类型枚举 | 下落方块砸中伤害"""
    Piston: T_DamageCausePiston
    """伤害类型枚举 | 活塞伤害"""
    FlyIntoWall: T_DamageCauseFlyIntoWall
    """伤害类型枚举 | 鞘翅飞行撞墙伤害"""
    Magma: T_DamageCauseMagma
    """伤害类型枚举 | 岩浆块伤害"""
    Fireworks: T_DamageCauseFireworks
    """伤害类型枚举 | 烟花火箭伤害"""
    Lightning: T_DamageCauseLightning
    """伤害类型枚举 | 闪电击中伤害"""
    Charging: T_DamageCauseCharging
    """伤害类型枚举 | ？"""
    Temperature: T_DamageCauseTemperature
    """伤害类型枚举 | 雪傀儡融化伤害"""
    Freezing: T_DamageCauseFreezing
    """伤害类型枚举 | 严寒效果伤害"""
    Stalactite: T_DamageCauseStalactite
    """伤害类型枚举 | 钟乳石砸中伤害"""
    Stalagmite: T_DamageCauseStalagmite
    """伤害类型枚举 | 石笋扎脚伤害"""

class DamageCause(_T_EnumDefineClass, ActorDamageCause): ...
