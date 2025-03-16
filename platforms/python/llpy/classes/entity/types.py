from typing import Literal

T_DamageCauseOverride = Literal[0]
T_DamageCauseContact = Literal[1]
T_DamageCauseEntityAttack = Literal[2]
T_DamageCauseProjectile = Literal[3]
T_DamageCauseSuffocation = Literal[4]
T_DamageCauseFall = Literal[5]
T_DamageCauseFire = Literal[6]
T_DamageCauseFireTick = Literal[7]
T_DamageCauseLava = Literal[8]
T_DamageCauseDrowning = Literal[9]
T_DamageCauseBlockExplosion = Literal[10]
T_DamageCauseEntityExplosion = Literal[11]
T_DamageCauseVoid = Literal[12]
T_DamageCauseSuicide = Literal[13]
T_DamageCauseMagic = Literal[14]
T_DamageCauseWither = Literal[15]
T_DamageCauseStarve = Literal[16]
T_DamageCauseAnvil = Literal[17]
T_DamageCauseThorns = Literal[18]
T_DamageCauseFallingBlock = Literal[19]
T_DamageCausePiston = Literal[20]
T_DamageCauseFlyIntoWall = Literal[21]
T_DamageCauseMagma = Literal[22]
T_DamageCauseFireworks = Literal[23]
T_DamageCauseLightning = Literal[24]
T_DamageCauseCharging = Literal[25]
T_DamageCauseTemperature = Literal[26]
T_DamageCauseFreezing = Literal[27]
T_DamageCauseStalactite = Literal[28]
T_DamageCauseStalagmite = Literal[29]
T_DamageCause = (
    T_DamageCauseOverride
    | T_DamageCauseContact
    | T_DamageCauseEntityAttack
    | T_DamageCauseProjectile
    | T_DamageCauseSuffocation
    | T_DamageCauseFall
    | T_DamageCauseFire
    | T_DamageCauseFireTick
    | T_DamageCauseLava
    | T_DamageCauseDrowning
    | T_DamageCauseBlockExplosion
    | T_DamageCauseEntityExplosion
    | T_DamageCauseVoid
    | T_DamageCauseSuicide
    | T_DamageCauseMagic
    | T_DamageCauseWither
    | T_DamageCauseStarve
    | T_DamageCauseAnvil
    | T_DamageCauseThorns
    | T_DamageCauseFallingBlock
    | T_DamageCausePiston
    | T_DamageCauseFlyIntoWall
    | T_DamageCauseMagma
    | T_DamageCauseFireworks
    | T_DamageCauseLightning
    | T_DamageCauseCharging
    | T_DamageCauseTemperature
    | T_DamageCauseFreezing
    | T_DamageCauseStalactite
    | T_DamageCauseStalagmite
)
