from typing import Literal, NoReturn, overload

from typing_extensions import deprecated

from llpy import (
    DirectionAngle,
    FloatPos,
    IntPos,
    LLSE_Block,
    LLSE_Container,
    LLSE_Item,
    LLSE_Player,
    NativePointer,
    NbtCompound,
)
from llpy.types import T_DamageCause, T_DimID, T_EffectID, T_Number, T_PosType

class LLSE_Entity:
    """实体对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def name(self) -> str:
        """实体名称"""
    @property
    def type(self) -> str:
        """实体标准类型名"""
    @property
    def id(self) -> int:
        """实体的游戏内id"""
    @property
    def pos(self) -> FloatPos:
        """实体视角高度坐标"""
    @property
    def posDelta(self) -> FloatPos:
        """实体位置增量"""
    @property
    def feetPos(self) -> FloatPos:
        """实体腿部所在坐标（游戏内显示的方块坐标）"""
    @property
    def blockPos(self) -> IntPos:
        """实体所在的方块坐标"""
    @property
    def maxHealth(self) -> int:
        """实体最大生命值"""
    @property
    def health(self) -> int:
        """实体当前生命值"""
    @property
    def canFly(self) -> bool:
        """实体是否能飞行"""
    @property
    def canFreeze(self) -> bool:
        """实体是否能被冻结"""
    @property
    def canSeeDaylight(self) -> bool:
        """实体是否能看到天空"""
    @property
    def canPickupItems(self) -> bool:
        """实体是否能拾取物品"""
    @property
    def inAir(self) -> bool:
        """实体是否悬空"""
    @property
    def inWater(self) -> bool:
        """实体是否在水中"""
    @property
    def inLava(self) -> bool:
        """实体是否在岩浆中"""
    @property
    def inRain(self) -> bool:
        """实体是否在雨中"""
    @property
    def inSnow(self) -> bool:
        """实体是否在雪中"""
    @property
    def inWall(self) -> bool:
        """实体是否在墙上"""
    @property
    def inWaterOrRain(self) -> bool:
        """实体是否在水中或雨中"""
    @property
    def inWorld(self) -> bool:
        """实体是否在世界中"""
    @property
    def speed(self) -> float:
        """实体当前速度"""
    @property
    def direction(self) -> DirectionAngle:
        """实体当前朝向"""
    @property
    def uniqueId(self) -> str:
        """实体唯一标识符"""
    @property
    def isInvisible(self) -> bool:
        """实体是否不可见"""
    @property
    def isInsidePortal(self) -> bool:
        """实体是否在传送门内"""
    @property
    def isTrusting(self) -> bool:
        """实体是否受信任"""
    @property
    def isTouchingDamageBlock(self) -> bool:
        """实体是否接触到伤害方块"""
    @property
    def isOnFire(self) -> bool:
        """实体是否着火"""
    @property
    def isOnGround(self) -> bool:
        """实体是否在地面"""
    @property
    def isOnHotBlock(self) -> bool:
        """实体是否在高温方块上（岩浆等）"""
    @property
    def isTrading(self) -> bool:
        """实体是否在交易"""
    @property
    def isRiding(self) -> bool:
        """实体是否正在骑行"""
    @property
    def isDancing(self) -> bool:
        """实体是否在跳舞"""
    @property
    def isSleeping(self) -> bool:
        """实体是否在睡觉"""
    @property
    def isAngry(self) -> bool:
        """实体是否生气"""
    @property
    def isBaby(self) -> bool:
        """实体是否为幼体"""
    @property
    def isMoving(self) -> bool:
        """实体是否移动"""
    @overload
    def teleport(self, pos: T_PosType) -> bool:
        """
        传送实体至指定位置

        保持传送前朝向

        Args:
            pos: 目标位置坐标

        Returns:
            是否成功传送
        """
    @overload
    def teleport(self, pos: T_PosType, rot: DirectionAngle) -> bool:
        """
        传送实体至指定位置

        Args:
            pos: 目标位置坐标
            rot: 传送后实体的朝向

        Returns:
            是否成功传送
        """
    @overload
    def teleport(
        self,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
    ) -> bool:
        """
        传送实体至指定位置

        保持传送前朝向

        Args:
            x: 目标位置 X 坐标
            y: 目标位置 Y 坐标
            z: 目标位置 Z 坐标
            dim_id: 目标维度 ID

        Returns:
            是否成功传送
        """
    @overload
    def teleport(
        self,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
        rot: DirectionAngle,
    ) -> bool:
        """
        传送实体至指定位置

        Args:
            x: 目标位置 X 坐标
            y: 目标位置 Y 坐标
            z: 目标位置 Z 坐标
            dim_id: 目标维度 ID
            rot: 传送后实体的朝向

        Returns:
            是否成功传送
        """
    def kill(self) -> bool:
        """
        杀死指定实体

        Returns:
            是否成功执行
        """
    def despawn(self) -> bool:
        """
        使指定实体刷新消失

        Returns:
            是否成功执行
        """
    def remove(self) -> bool:
        """
        移除指定实体

        Returns:
            是否成功执行
        """
    def hurt(self, damage: float, damage_type: T_DamageCause) -> bool:
        """
        对实体造成伤害

        注意，此处造成的伤害为真实伤害，无法被盔甲等保护装备减免

        Args:
            damage: 对实体造成的伤害数值
            damage_type: 伤害类型（`ActorDamageCause` 枚举）

        Returns:
            是否造成伤害
        """
    def heal(self, health: int) -> bool:
        """
        治疗实体

        Args:
            health: 治疗的心数

        Returns:
            是否治疗成功
        """
    @overload
    def setPosDelta(self, pos: FloatPos) -> bool:
        """
        设置实体坐标偏移量

        Args:
            pos: 偏移量坐标

        Returns:
            是否设置成功
        """
    @overload
    def setPosDelta(self, x: T_Number, y: T_Number, z: T_Number) -> bool:
        """
        设置实体坐标偏移量

        Args:
            x: 偏移量 X 坐标
            y: 偏移量 Y 坐标
            z: 偏移量 Z 坐标

        Returns:
            是否设置成功
        """
    def setHealth(self, health: int) -> bool:
        """
        设置实体的生命值

        Args:
            health: 生命值数

        Returns:
            是否成功
        """
    def setAbsorption(self, value: int) -> bool:
        """
        为实体设置伤害吸收属性

        Args:
            value: 新的值

        Returns:
            为实体设置属性值是否成功
        """
    def setAttackDamage(self, value: int) -> bool:
        """
        为实体设置攻击伤害属性

        Args:
            value: 新的值

        Returns:
            为实体设置属性值是否成功
        """
    def setMaxAttackDamage(self, value: int) -> bool:
        """
        为实体设置最大攻击伤害属性

        Args:
            value: 新的值

        Returns:
            为实体设置属性值是否成功
        """
    def setFollowRange(self, value: int) -> bool:
        """
        为实体设置跟随范围

        Args:
            value: 新的值

        Returns:
            为实体设置属性值是否成功
        """
    def setKnockbackResistance(self, value: Literal[0, 1]) -> bool:
        """
        为实体设置击退抵抗属性

        Args:
            value: 新的值

        Returns:
            为实体设置属性值是否成功
        """
    def setLuck(self, value: int) -> bool:
        """
        为实体设置幸运属性

        Args:
            value: 新的值

        Returns:
            为实体设置属性值是否成功
        """
    def setMovementSpeed(self, value: int) -> bool:
        """
        为实体设置移动速度属性

        Args:
            value: 新的值

        Returns:
            为实体设置属性值是否成功
        """
    def setUnderwaterMovementSpeed(self, value: int) -> bool:
        """
        为实体设置水下移动速度属性

        Args:
            value: 新的值

        Returns:
            为实体设置属性值是否成功
        """
    def setLavaMovementSpeed(self, value: int) -> bool:
        """
        为实体设置岩浆上移动速度属性

        Args:
            value: 新的值

        Returns:
            为实体设置属性值是否成功
        """
    def setMaxHealth(self, health: int) -> bool:
        """
        设置实体的最大生命值

        Args:
            value: 生命值数

        Returns:
            是否成功
        """
    def setFire(self, time: int, is_effect: bool) -> bool:
        """
        设置特定实体为燃烧状态

        Args:
            time: 燃烧的时间，秒为单位
            is_effect: 是否有火焰效果

        Returns:
            是否设置成功
        """
    def stopFire(self) -> bool:
        """
        熄灭实体

        Returns:
            是否熄灭成功
        """
    def isPlayer(self) -> bool:
        """
        判断一个实体对象是不是玩家

        Returns:
            当前实体对象是不是玩家
        """
    def toPlayer(self) -> LLSE_Player | None:
        """
        将实体对象转换玩家对象

        如果当前实体对象指向的是一个玩家，可以使用此函数将实体对象转换为玩家对象，以使用更多的玩家相关 API

        Returns:
            转换成的玩家对象。如果此实体对象指向的不是某个玩家，或者转换失败，则返回 `None`
        """
    def isItemEntity(self) -> bool:
        """
        判断一个实体对象是不是掉落物实体

        Returns:
            当前实体对象是不是掉落物实体
        """
    def toItem(self) -> LLSE_Item | None:
        """
        获取掉落物实体中的物品对象

        Returns:
            获取到的物品对象。如果此实体对象不是掉落物实体，或者获取失败，则返回 `None`
        """
    def getBlockStandingOn(self) -> LLSE_Block:
        """
        获取实体当前站立所在的方块

        Returns:
            当前站立在的方块对象
        """
    def getArmor(self) -> LLSE_Container:
        """
        获取生物盔甲栏的容器对象

        Returns:
            此实体盔甲栏对应的容器对象
        """
    def distanceTo(self, pos: LLSE_Entity | LLSE_Player | T_PosType) -> T_Number:
        """
        获取实体到坐标的距离

        若实体的坐标与目标的坐标不在同一维度，将返回整数最大值

        Args:
            pos: 目标位置

        Returns:
            到坐标的距离(方块)
        """
    def distanceToSqr(
        self,
        pos: LLSE_Entity | LLSE_Player | T_PosType,
    ) -> T_Number:
        """
        获取实体到坐标的距离

        若实体的坐标与目标的坐标不在同一维度，将返回整数最大值。

        Args:
            pos: 目标位置

        Returns:
            到坐标的距离(方块)
        """
    def hasContainer(self) -> bool:
        """
        判断生物是否拥有容器（盔甲栏除外）

        如羊驼身上的箱子等，他们各自拥有一个属于自己的容器对象

        Returns:
            这个生物实体是否拥有容器
        """
    def getContainer(self) -> LLSE_Container:
        """
        获取生物所拥有的容器对象（盔甲栏除外）

        Returns:
            这个生物实体所拥有的容器对象
        """
    def refreshItems(self) -> bool:
        """
        刷新生物物品栏、盔甲栏

        修改生物物品之后，为了促使客户端生效，需要刷新生物所有的物品

        Returns:
            是否成功刷新
        """
    def setScale(self, scale: int) -> bool:
        """
        缩放实体

        Args:
            scale: 新的实体体积

        Returns:
            实体是否成功地被缩放
        """
    def setNbt(self, nbt: NbtCompound) -> bool:
        """
        写入实体对应的 NBT 对象

        Args:
            nbt: NBT 对象

        Returns:
            是否成功写入
        """
    def getNbt(self) -> NbtCompound:
        """
        获取实体对应的 NBT 对象

        Returns:
            实体的 NBT 对象
        """
    def addTag(self, tag: str) -> bool:
        """
        为实体增加一个 Tag

        Args:
            tag: 要增加的 tag 字符串

        Returns:
            是否设置成功
        """
    def removeTag(self, tag: str) -> bool:
        """
        为实体移除一个 Tag

        Args:
            tag: 要移除的 tag 字符串

        Returns:
            是否移除成功
        """
    def hasTag(self, tag: str) -> bool:
        """
        检查实体是否拥有某个 Tag

        Args:
            tag: 要检查的 tag 字符串

        Returns:
            是否拥有这个 Tag
        """
    def getAllTags(self) -> list[str]:
        """
        返回实体拥有的所有 Tag 列表

        Returns:
            实体所有的 tag 字符串列表
        """
    def getEntityFromViewVector(
        self,
        max_distance: float = 5.25,
    ) -> LLSE_Entity | None:
        """
        获取视线方向实体

        Args:
            max_distance: 查找最大距离

        Returns:
            视线方向实体。如果获取失败，返回 `None`
        """
    def getBlockFromViewVector(
        self,
        include_liquid: bool = False,
        solid_only: bool = False,
        max_distance: float = 5.25,
        full_only: bool = False,
    ) -> LLSE_Block | None:
        """
        获取视线方向方块

        Args:
            include_liquid: 是否包含液态方块
            solid_only: 是否仅允许 `Solid` 类型的方块
            max_distance: 查找最大距离
            full_only: 是否仅允许完整方块

        Returns:
            视线方向方块。如果获取失败，返回 `None`
        """
    def getBiomeId(self) -> int:
        """
        获取实体所在群系 ID

        Returns:
            群系 ID
        """
    def getBiomeName(self) -> str:
        """
        获取实体所在群系名称

        Returns:
            群系名称
        """
    def getAllEffects(self) -> list[T_EffectID]:
        """
        获取实体全部药水效果

        Returns:
            实体所有的药水效果 ID
        """
    def addEffect(
        self,
        effect_id: T_EffectID,
        tick: int,
        level: int,
        show_particles: bool,
    ) -> bool:
        """
        为实体添加一个药水效果

        Args:
            id: 药水效果的 ID
            tick: 持续时间
            level: 等级
            show_particles: 是否显示粒子

        Returns:
            操作是否成功
        """
    def removeEffect(self, effect_id: int) -> bool:
        """
        为实体移除一个药水效果

        Args:
            effect_id: 药水效果的 ID

        Returns:
            操作是否成功
        """
    def quickEvalMolangScript(self, exp: str) -> float:
        """
        快速执行 Molang 表达式

        关于 Molang 的详细使用方法，请参考 [MOLANG 文档 bedrock.dev](https://bedrock.dev/zh/docs/stable/Molang)

        Args:
            exp: Molang 表达式

        Returns:
            表达式执行结果
        """
    def asPointer(self) -> NativePointer: ...
    @deprecated("请使用 `LLSE_Entity.setNbt()`")
    def setTag(self, nbt: NbtCompound) -> bool: ...
    @deprecated("请使用 `LLSE_Entity.setFire()`")
    def setOnFire(self, time: int) -> bool: ...
    @deprecated("请使用 `LLSE_Entity.getNbt()`")
    def getTag(self) -> NbtCompound: ...
    @deprecated("请使用 `LLSE_Entity.distanceTo()`")
    def distanceToPos(self, pos: LLSE_Entity | LLSE_Player | T_PosType) -> T_Number: ...

Entity = LLSE_Entity
