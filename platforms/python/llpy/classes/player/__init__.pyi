from typing import Any, Literal, NoReturn, overload

from typing_extensions import deprecated

from llpy import (
    DirectionAngle,
    FloatPos,
    IntPos,
    LLSE_Block,
    LLSE_Container,
    LLSE_CustomForm,
    LLSE_Device,
    LLSE_Entity,
    LLSE_Item,
    LLSE_Packet,
    LLSE_SimpleForm,
    NativePointer,
    NbtCompound,
)
from llpy.types import T_DimID, T_EffectID, T_MoneyHistory, T_Number, T_PosType

from .types import (
    T_BossEventColor,
    T_CustomFormCallback,
    T_GameMode,
    T_ModalFormCallback,
    T_NavigatePath,
    T_PermLevel,
    T_PlayerInventory,
    T_SimpleFormCallback,
    T_TextPacketType,
    T_TitlePacketType,
)

class LLSE_Player:
    """玩家对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def name(self) -> str:
        """玩家名"""
    @property
    def pos(self) -> FloatPos:
        """玩家视角高度坐标"""
    @property
    def feetPos(self) -> FloatPos:
        """玩家腿部所在坐标（游戏内显示的方块坐标）"""
    @property
    def blockPos(self) -> IntPos:
        """玩家所在的方块坐标"""
    @property
    def lastDeathPos(self) -> IntPos:
        """玩家上次死亡的坐标"""
    @property
    def realName(self) -> str:
        """玩家的真实名字"""
    @property
    def xuid(self) -> str:
        """玩家 XUID 字符串"""
    @property
    def uuid(self) -> str:
        """玩家 UUID 字符串"""
    @property
    def permLevel(self) -> T_PermLevel:
        """玩家的操作权限等级"""
    @property
    def gameMode(self) -> T_GameMode:
        """玩家的游戏模式"""
    @property
    def canSleep(self) -> bool:
        """玩家是否可以睡觉"""
    @property
    def canFly(self) -> bool:
        """玩家是否可以飞行"""
    @property
    def canBeSeenOnMap(self) -> bool:
        """玩家是否可以在地图上看到"""
    @property
    def canFreeze(self) -> bool:
        """玩家是否可以冻结"""
    @property
    def canSeeDaylight(self) -> bool:
        """玩家是否能看到日光"""
    @property
    def canShowNameTag(self) -> bool:
        """玩家是否可以显示姓名标签"""
    @property
    def canStartSleepInBed(self) -> bool:
        """玩家是否可以开始在床上睡觉"""
    @property
    def canPickupItems(self) -> bool:
        """玩家是否可以拾取物品"""
    @property
    def maxHealth(self) -> int:
        """玩家最大生命值"""
    @property
    def health(self) -> int:
        """玩家当前生命值"""
    @property
    def inAir(self) -> bool:
        """玩家当前是否悬空"""
    @property
    def inWater(self) -> bool:
        """玩家当前是否在水中"""
    @property
    def inLava(self) -> bool:
        """玩家是否在熔岩中"""
    @property
    def inRain(self) -> bool:
        """玩家是否在淋雨"""
    @property
    def inSnow(self) -> bool:
        """玩家是否在雪中"""
    @property
    def inWall(self) -> bool:
        """玩家是否在墙上"""
    @property
    def inWaterOrRain(self) -> bool:
        """玩家是否在水中或雨中"""
    @property
    def inWorld(self) -> bool:
        """玩家是否在世界内"""
    @property
    def inClouds(self) -> bool:
        """玩家是否在云层上"""
    @property
    def speed(self) -> float:
        """玩家当前速度"""
    @property
    def direction(self) -> DirectionAngle:
        """玩家当前朝向"""
    @property
    def uniqueId(self) -> str:
        """玩家（实体的）唯一标识符"""
    @property
    def langCode(self) -> str:
        """玩家设置的语言的标识符(形如 `zh_CN`)"""
    @property
    def isLoading(self) -> bool:
        """玩家是否正在加载"""
    @property
    def isInvisible(self) -> bool:
        """玩家是否隐身中"""
    @property
    def isInsidePortal(self) -> bool:
        """玩家是否在传送门中"""
    @property
    def isHurt(self) -> bool:
        """玩家是否受伤"""
    @property
    def isTrusting(self) -> bool:
        """玩家是否受信任"""
    @property
    def isTouchingDamageBlock(self) -> bool:
        """玩家是否在能造成伤害的方块上"""
    @property
    def isHungry(self) -> bool:
        """玩家是否饿了"""
    @property
    def isOnFire(self) -> bool:
        """玩家是否着火"""
    @property
    def isOnGround(self) -> bool:
        """玩家是否在地上"""
    @property
    def isOnHotBlock(self) -> bool:
        """玩家是否在高温方块上（岩浆等）"""
    @property
    def isTrading(self) -> bool:
        """玩家是否在交易"""
    @property
    def isAdventure(self) -> bool:
        """玩家是否是冒险模式"""
    @property
    def isGliding(self) -> bool:
        """玩家是否在滑行"""
    @property
    def isSurvival(self) -> bool:
        """玩家是否是生存模式"""
    @property
    def isSpectator(self) -> bool:
        """玩家是否是旁观模式"""
    @property
    def isRiding(self) -> bool:
        """玩家是否在骑行"""
    @property
    def isDancing(self) -> bool:
        """玩家是否在跳舞"""
    @property
    def isCreative(self) -> bool:
        """玩家是否是创造模式"""
    @property
    def isFlying(self) -> bool:
        """玩家是否在飞行"""
    @property
    def isSleeping(self) -> bool:
        """玩家是否正在睡觉"""
    @property
    def isMoving(self) -> bool:
        """玩家是否正在移动"""
    @property
    def isSneaking(self) -> bool:
        """玩家是否正在潜行"""
    def isOP(self) -> bool:
        """
        判断玩家是否为 OP

        Returns:
            玩家是否为 OP
        """
    def setPermLevel(self, level: T_PermLevel) -> bool:
        """
        修改玩家操作权限

        Args:
            level: 目标操作权限等级

        Returns:
            是否成功修改
        """
    def setGameMode(self, mode: T_GameMode) -> bool:
        """
        修改玩家游戏模式

        Args:
            mode: 目标游戏模式

        Returns:
            是否成功修改
        """
    def runcmd(self, cmd: str) -> bool:
        """
        以某个玩家身份执行一条命令

        Args:
            cmd: 待执行的命令

        Returns:
            是否执行成功
        """
    @overload
    def teleport(self, pos: T_PosType) -> bool:
        """
        传送玩家至指定位置

        保持传送前朝向

        Args:
            pos: 目标位置坐标

        Returns:
            是否成功传送
        """
    @overload
    def teleport(self, pos: T_PosType, rot: DirectionAngle) -> bool:
        """
        传送玩家至指定位置

        Args:
            pos: 目标位置坐标
            rot: 传送后玩家的朝向

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
        传送玩家至指定位置

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
        传送玩家至指定位置

        Args:
            x: 目标位置 X 坐标
            y: 目标位置 Y 坐标
            z: 目标位置 Z 坐标
            dim_id: 目标维度 ID
            rot: 传送后玩家的朝向

        Returns:
            是否成功传送
        """
    def kill(self) -> bool:
        """
        杀死玩家

        Returns:
            是否成功执行
        """
    @overload
    def kick(self) -> bool:
        """
        断开玩家连接

        Returns:
            是否成功断开连接
        """
    @overload
    def kick(self, msg: str) -> bool:
        """
        断开玩家连接

        Args:
            msg: 被踢出玩家出显示的断开原因

        Returns:
            是否成功断开连接
        """
    @overload
    def disconnect(self) -> bool:
        """
        断开玩家连接

        Returns:
            是否成功断开连接
        """
    @overload
    def disconnect(self, msg: str) -> bool:
        """
        断开玩家连接

        Args:
            msg: 被踢出玩家出显示的断开原因

        Returns:
            是否成功断开连接
        """
    def tell(self, msg: str, msg_type: T_TextPacketType = 0) -> bool:
        """
        发送一个文本消息给玩家

        Args:
            msg: 待发送的文本
            msg_type: 发送的文本消息类型

        Returns:
            是否成功发送
        """
    def sendText(self, msg: str, msg_type: T_TextPacketType = 0) -> bool:
        """
        发送一个文本消息给玩家

        Args:
            msg: 待发送的文本
            msg_type: 发送的文本消息类型

        Returns:
            是否成功发送
        """
    @overload
    def talkAs(self, text: str) -> bool:
        """
        以某个玩家身份说话

        Args:
            text: 模拟说话内容

        Returns:
            是否执行成功
        """
    @overload
    def talkAs(self, target: LLSE_Player, text: str) -> bool:
        """
        以某个玩家身份向某玩家说话

        Args:
            target: 模拟说话对象
            text: 模拟说话内容

        Returns:
            是否执行成功
        """
    @overload
    def setTitle(self, content: str, title_type: T_TitlePacketType = 2) -> bool:
        """
        设置玩家显示标题

        Args:
            content: 欲设置标题内容
            title_type: 设置的标题类型

        Returns:
            是否成功发送
        """
    @overload
    def setTitle(
        self,
        content: str,
        title_type: T_TitlePacketType,
        fade_in_time: int,
        stay_time_int: int,
        fade_out_time: int,
    ) -> bool:
        """
        设置玩家显示标题

        Args:
            content: 欲设置标题内容
            title_type: 设置的标题类型
            fade_in_time: 淡入时间，单位为 `Tick`
            stay_time_int: 停留时间，单位为 `Tick`
            fade_out_time: 淡出时间，单位为 `Tick`

        Returns:
            是否成功发送
        """
    def rename(self, new_name: str) -> bool:
        """
        重命名玩家

        Args:
            new_name: 玩家的新名字

        Returns:
            是否重命名成功
        """
    def setFire(self, time: int, is_effect: bool) -> bool:
        """
        使指定玩家着火

        Args:
            time: 着火时长，单位秒
            is_effect: 会不会有火的效果

        Returns:
            是否成功着火
        """
    def stopFire(self) -> bool:
        """
        熄灭玩家

        Returns:
            是否已被熄灭
        """
    def transServer(self, server: str, port: int) -> bool:
        """
        传送玩家至指定服务器

        Args:
            server: 目标服务器 IP / 域名
            port: 目标服务器端口

        Returns:
            是否成功传送
        """
    def crash(self) -> bool:
        """
        使玩家客户端崩溃

        Returns:
            是否成功执行
        """
    def hurt(self, damage: int) -> bool:
        """
        对玩家造成伤害

        此处造成的伤害为真实伤害，无法被盔甲等保护装备减免

        Args:
            damage: 对玩家造成的伤害数值

        Returns:
            是否造成伤害
        """
    def heal(self, health: int) -> bool:
        """
        治疗玩家

        Args:
            health: 治疗的心数

        Returns:
            治疗是否成功
        """
    def setHealth(self, health: int) -> bool:
        """
        设置玩家的生命值

        Args:
            health: 生命值数

        Returns:
            是否成功
        """
    def setMaxHealth(self, health: int) -> bool:
        """
        设置玩家最大生命值

        Args:
            health: 生命值数

        Returns:
            是否成功
        """
    def setAbsorption(self, value: int) -> bool:
        """
        为玩家设置伤害吸收属性

        Args:
            value: 新的值

        Returns:
            为玩家设置属性值是否成功
        """
    def setAttackDamage(self, value: int) -> bool:
        """
        为玩家设置攻击伤害属性

        Args:
            value: 新的值

        Returns:
            为玩家设置属性值是否成功
        """
    def setMaxAttackDamage(self, value: int) -> bool:
        """
        为玩家设置最大攻击伤害属性

        Args:
            value: 新的值

        Returns:
            为玩家设置属性值是否成功
        """
    def setFollowRange(self, value: int) -> bool:
        """
        为玩家设置跟随范围

        Args:
            value: 新的值

        Returns:
            为玩家设置属性值是否成功
        """
    def setKnockbackResistance(self, value: int) -> bool:
        """
        为玩家设置击退抵抗属性

        Args:
            value: 新的值

        Returns:
            为玩家设置属性值是否成功
        """
    def setLuck(self, value: int) -> bool:
        """
        为玩家设置幸运属性

        Args:
            value: 新的值

        Returns:
            为玩家设置属性值是否成功
        """
    def setMovementSpeed(self, value: int) -> bool:
        """
        为玩家设置移动速度属性

        Args:
            value: 新的值

        Returns:
            为玩家设置属性值是否成功
        """
    def setUnderwaterMovementSpeed(self, value: int) -> bool:
        """
        为玩家设置水下移动速度属性

        Args:
            value: 新的值

        Returns:
            为玩家设置属性值是否成功
        """
    def setLavaMovementSpeed(self, value: int) -> bool:
        """
        为玩家设置岩浆上移动速度属性

        Args:
            value: 新的值

        Returns:
            为玩家设置属性值是否成功
        """
    def setHungry(self, hunger: int) -> bool:
        """
        设置玩家饥饿值

        Args:
            hunger: 饥饿值数

        Returns:
            是否成功
        """
    def refreshChunks(self) -> bool:
        """
        刷新玩家加载的所有区块

        Returns:
            是否成功刷新
        """
    @overload
    def giveItem(self, item: LLSE_Item) -> bool:
        """
        给予玩家一个物品

        如果玩家物品栏已满，将抛出多余物品

        Args:
            item: 给予的物品对象

        Returns:
            是否成功给予
        """
    @overload
    def giveItem(self, item: LLSE_Item, amount: int) -> bool:
        """
        给予玩家一个物品

        如果玩家物品栏已满，将抛出多余物品

        Args:
            item: 给予的物品对象
            amount: 给予物品对象的数量，物品对象自身的 `Count` 属性将被忽略

        Returns:
            是否成功给予
        """
    def clearItem(self, item_type: str, count: int = 1) -> int:
        """
        清除玩家背包中指定类型的物品

        将玩家物品栏、主手、副手、盔甲栏中所有物品的 `type` 属性与此字符串进行比较，如果相等，则清除此物品

        Args:
            item_type: 要清除的物品对象类型名
            count: 要清除的数量

        Returns:
            清除的物品个数
        """
    def isSprinting(self) -> bool:
        """
        获取玩家疾跑状态

        Returns:
            玩家疾跑状态
        """
    def setSprinting(self, sprinting: bool) -> bool:
        """
        设置玩家疾跑状态

        Args:
            sprinting: 是否为疾跑状态

        Returns:
            是否设置成功
        """
    def sendToast(self, title: str, message: str) -> bool:
        """
        在屏幕上方显示消息

        类似于成就完成

        Args:
            title: 待发送的标题
            message: 待发送的文本

        Returns:
            是否成功发送
        """
    def distanceTo(self, pos: LLSE_Entity | LLSE_Player | T_PosType) -> T_Number:
        """
        获取玩家到坐标的距离

        若玩家的坐标与目标的坐标不在同一维度，将返回整数最大值

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
        获取玩家到坐标的距离

        若玩家的坐标与目标的坐标不在同一维度，将返回整数最大值。

        Args:
            pos: 目标位置

        Returns:
            到坐标的距离(方块)
        """
    def getBlockStandingOn(self) -> LLSE_Block:
        """
        获取玩家当前站立所在的方块

        Returns:
            当前站立在的方块对象
        """
    def getDevice(self) -> LLSE_Device:
        """
        获取玩家对应的设备信息对象

        Returns:
            玩家对应的设备信息对象
        """
    def getHand(self) -> LLSE_Item:
        """
        获取玩家主手中的物品对象

        此处获取的物品对象为引用。
        也就是说，修改此处返回的物品对象，或使用其API，就相当于直接操作玩家主手中对应的物品

        Returns:
            玩家主手中的物品对象
        """
    def getOffHand(self) -> LLSE_Item:
        """
        获取玩家副手中的物品对象

        此处获取的物品对象为引用。
        也就是说，修改此处返回的物品对象，或使用其API，就相当于直接操作玩家副手中对应的物品

        Returns:
            玩家副手中的物品对象
        """
    def getPlayerInventoryContainer(self) -> LLSE_Container:
        """
        获取玩家物品栏对应的容器对象

        Returns:
            玩家物品栏对应的容器对象
        """
    def getArmor(self) -> LLSE_Container:
        """
        获取玩家盔甲栏的容器对象

        Returns:
            玩家盔甲栏对应的容器对象
        """
    def getEnderChest(self) -> LLSE_Container:
        """
        获取玩家末影箱的容器对象

        Returns:
            玩家末影箱对应的容器对象
        """
    def getRespawnPosition(self) -> IntPos:
        """
        获取玩家的重生坐标

        Returns:
            重生点坐标
        """
    @overload
    def setRespawnPosition(self, pos: IntPos) -> bool:
        """
        修改玩家的重生坐标

        Args:
            pos: 重生坐标

        Returns:
            是否成功修改
        """
    @overload
    def setRespawnPosition(self, x: int, y: int, z: int, dim_id: T_DimID) -> bool:
        """
        修改玩家的重生坐标

        Args:
            x: 重生 X 坐标
            y: 重生 Y 坐标
            z: 重生 Z 坐标
            dim_id: 重生维度 ID

        Returns:
            是否成功修改
        """
    def refreshItems(self) -> bool:
        """
        刷新玩家物品栏、盔甲栏

        在修改玩家物品之后，为了促使客户端生效，需要刷新玩家所有的物品

        Returns:
            是否成功刷新
        """
    def getScore(self, name: str) -> int:
        """
        获取在线玩家计分项的分数

        使用前，必须保证对应的计分项已经存在

        Args:
            name: 计分项名称

        Returns:
            计分板上的数值
        """
    def setScore(self, name: str, value: int) -> bool:
        """
        设置在线玩家计分项的分数

        若计分项不存在，则会返回 `False` 并创建计分项

        Args:
            name: 计分项名称
            value: 要设置的数值

        Returns:
            计分板上的数值
        """
    def addScore(self, name: str, value: int) -> bool:
        """
        增加在线玩家计分项的分数

        若计分项不存在，则会返回 `False` 并创建计分项

        Args:
            name: 计分项名称
            value: 要增加的数值

        Returns:
            计分板上的数值
        """
    def reduceScore(self, name: str, value: int) -> bool:
        """
        减少在线玩家计分项的分数

        若计分项不存在，则会返回 `False` 并创建计分项

        Args:
            name: 计分项名称
            value: 要减少的数值

        Returns:
            计分板上的数值
        """
    def deleteScore(self, name: str) -> bool:
        """
        玩家停止跟踪计分项

        使用前，必须保证对应的计分项已经存在

        Args:
            name: 计分项名称

        Returns:
            是否移除成功
        """
    def setSidebar(
        self,
        title: str,
        data: dict[str, int],
        sort_order: Literal[0, 1] = 1,
    ) -> bool:
        """
        设置玩家自定义侧边栏

        Args:
            title: 侧边栏标题
            data: 侧边栏对象内容对象。对象中的每个键值对将被设置为侧边栏内容的一行
            sort_order: 侧边栏内容的排序顺序。`0` 为按分数升序，`1` 为按分数降序

        Returns:
            _description_
        """
    def removeSidebar(self) -> bool:
        """
        移除玩家自定义侧边栏

        Returns:
            是否成功移除
        """
    @overload
    def setBossBar(
        self,
        title: str,
        percent: int,
        color: T_BossEventColor = 2,
    ) -> bool:
        """
        设置玩家看到的自定义 Boss 血条

        Args:
            title: 自定义血条标题
            percent: 血条中的血量百分比，有效范围为 0 ~ 100
            color: 血条颜色

        Returns:
            是否成功设置
        """
    @overload
    def setBossBar(
        self,
        uid: int,
        title: str,
        percent: int,
        color: T_BossEventColor = 2,
    ) -> bool:
        """
        设置玩家看到的自定义 Boss 血条

        Args:
            uid: 唯一标识符，不可冲突重复！一个 uid 对于一行 BossBar
            title: 自定义血条标题
            percent: 血条中的血量百分比，有效范围为 0 ~ 100
            color: 血条颜色

        Returns:
            是否成功设置
        """
    @overload
    def removeBossBar(self) -> bool:
        """
        移除玩家的自定义的指定 Boss 血条

        Returns:
            是否成功移除
        """
    @overload
    def removeBossBar(self, uid: int) -> bool:
        """
        移除玩家的自定义的指定 Boss 血条

        Args:
            uid: 标识符，与 `setBossBar` 对应

        Returns:
            是否成功移除
        """
    def addLevel(self, count: int) -> bool:
        """
        提高玩家经验等级

        Args:
            count: 要提高的经验等级

        Returns:
            是否设置成功
        """
    def reduceLevel(self, count: int) -> bool:
        """
        降低玩家经验等级

        Args:
            count: 要降低的经验等级

        Returns:
            是否设置成功
        """
    def getLevel(self) -> int:
        """
        获取玩家经验等级

        Returns:
            玩家的经验等级
        """
    def setLevel(self, count: int) -> bool:
        """
        设置玩家经验等级

        Args:
            count: 要设置的经验等级

        Returns:
            是否设置成功
        """
    def resetLevel(self) -> bool:
        """
        重置玩家经验

        Returns:
            是否设置成功
        """
    def addExperience(self, count: int) -> bool:
        """
        提高玩家经验值

        Args:
            count: 要提高的经验值

        Returns:
            是否设置成功
        """
    def reduceExperience(self, count: int) -> bool:
        """
        降低玩家经验值

        Args:
            count: 要降低的经验值

        Returns:
            是否设置成功
        """
    def getCurrentExperience(self) -> int:
        """
        获取玩家当前经验值

        Returns:
            玩家总经验值
        """
    def setCurrentExperience(self, count: int) -> bool:
        """
        设置玩家当前经验值

        Args:
            count: 要设置的经验值

        Returns:
            是否设置成功
        """
    def getTotalExperience(self) -> int:
        """
        获取玩家总经验值

        Returns:
            玩家总经验值
        """
    def setTotalExperience(self, count: int) -> bool:
        """
        设置玩家总经验值

        Args:
            count: 要设置的经验值

        Returns:
            是否设置成功
        """
    def getXpNeededForNextLevel(self) -> int:
        """
        获取玩家升级所需的经验值

        注意，此方法在计算时会忽略当前经验值

        Returns:
            玩家升级所需的经验值
        """
    def setScale(self, scale: int) -> bool:
        """
        缩放玩家

        Args:
            scale: 新的玩家体积

        Returns:
            玩家是否成功地被缩放
        """
    def setAbility(self, ability_id: int, value: bool) -> bool:
        """
        设置玩家 Ability 属性

        Args:
            ability_id: Ability 的 ID
            value: 是否开启

        Returns:
            无作用
        """
    def getBiomeId(self) -> int:
        """
        获取玩家所在群系 ID

        Returns:
            群系 ID
        """
    def getBiomeName(self) -> str:
        """
        获取玩家所在群系名称

        Returns:
            群系名称
        """
    def getAllEffects(self) -> list[T_EffectID] | None:
        """
        获取玩家身上的状态效果

        Returns:
            状态效果 ID 列表。如果玩家身上没有状态效果则返回 `None`
        """
    def addEffect(self, effect_id: T_EffectID, tick: int, level: int) -> bool:
        """
        给玩家添加状态效果

        Args:
            effect_id: 状态效果数字 ID
            tick: 持续的 `Ticks`
            level: 效果等级

        Returns:
            是否成功添加效果
        """
    def removeEffect(self, effect_id: T_EffectID) -> bool:
        """
        移除玩家的状态效果

        Args:
            effect_id: 状态效果数字 ID

        Returns:
            是否成功移除效果
        """
    def sendModalForm(
        self,
        title: str,
        content: str,
        confirm_button: str,
        cancel_button: str,
        callback: T_ModalFormCallback,
    ) -> int | None:
        """
        向玩家发送模式表单

        模式表单包含一个标题、一个文本显示框以及两个按钮

        Callback Args:
            player (LLSE_Player): 与表单互动的玩家对象
            result (bool | None): 玩家点击确定按钮为 `True`，取消按钮为 `False`。如果为 `None`，则代表玩家取消了表单

        Args:
            title: 表单标题
            content: 表单内容
            confirm_button: 按钮 1（确认）文本的字符串
            cancel_button: 按钮 2（取消）文本的字符串
            callback: 玩家点击按钮之后被调用的回调函数

        Returns:
            发送的表单 ID。如果返回值为 `None`，则代表发送失败
        """
    def sendSimpleForm(
        self,
        title: str,
        content: str,
        buttons: list[str],
        images: list[str],
        callback: T_SimpleFormCallback,
    ) -> int | None:
        """
        向玩家发送普通表单

        Callback Args:
            player (LLSE_Player): 与表单互动的玩家对象
            button_id (int | None): 玩家点击的表单按钮的序号，从 `0` 开始编号。如果为 `None`，则代表玩家取消了表单

        Args:
            title: 表单标题
            content: 表单内容
            buttons: 各个按钮文本的字符串数组
            images: 各个按钮对应的图片路径。不需要图片请设为空字符串
                元素格式为 `textures/items/apple`(材质包路径) 或 `https://1919810.work/apple.png`(完整URL)
            callback: 玩家点击按钮之后被调用的回调函数

        Returns:
            发送的表单 ID。如果返回值为 `None`，则代表发送失败
        """
    def sendCustomForm(self, json: str, callback: T_CustomFormCallback) -> int | None:
        """
        向玩家发送自定义表单（JSON 格式）

        Callback Args:
            player (LLSE_Player): 与表单互动的玩家对象
            data (list[bool | int | str | None] | None): 返回的表单内容数组。
                数组中，第一项一定为 `None`，从第二项开始，按表单上的控件顺序储存了每一个控件的内容
                如果 `data` 仅为 `None`，则代表玩家取消了表单

        Args:
            json: 自定义表单 json 字符串
            callback: 玩家提交表单之后被调用的回调函数

        Returns:
            发送的表单 ID。如果返回值为 `None`，则代表发送失败
        """
    @overload
    def sendForm(
        self,
        form: LLSE_SimpleForm,
        callback: T_SimpleFormCallback,
    ) -> int | None:
        """
        向玩家发送普通表单

        Callback Args:
            player (LLSE_Player): 与表单互动的玩家对象
            button_id (int | None): 玩家点击的表单按钮的序号，从 `0` 开始编号。如果为 `None`，则代表玩家取消了表单

        Args:
            form: 配置好的表单对象
            callback: 玩家与表单元素互动之后被调用的回调函数

        Returns:
            发送的表单 ID。如果返回值为 `None`，则代表发送失败
        """
    @overload
    def sendForm(
        self,
        form: LLSE_CustomForm,
        callback: T_CustomFormCallback,
    ) -> int | None:
        """
        向玩家发送自定义表单

        Callback Args:
            player (LLSE_Player): 与表单互动的玩家对象
            data (list[bool | int | str | None] | None): 返回的表单内容数组。
                数组中按表单上的控件顺序储存了每一个控件的内容。
                如果 `data` 仅为 `None`，则代表玩家取消了表单

        Args:
            form: 配置好的表单对象
            callback: 玩家与表单元素互动之后被调用的回调函数

        Returns:
            发送的表单 ID。如果返回值为 `None`，则代表发送失败
        """
    def sendPacket(self, packet: LLSE_Packet) -> bool:
        """
        向玩家发送数据包

        Args:
            packet: 数据包

        Returns:
            是否成功
        """
    def setExtraData(self, name: str, data: Any) -> bool:
        """
        储存玩家绑定数据

        Args:
            name: 要储存到绑定数据的名字
            data: 你要储存的绑定数据

        Returns:
            是否成功储存
        """
    def getExtraData(self, name: str) -> Any | None:
        """
        获取玩家绑定数据

        Args:
            name: 要读取的绑定数据的名字

        Returns:
            储存的绑定数据。如返回值为 `None` 则表示未获取到指定的绑定数据，或者数据为空
        """
    def delExtraData(self, name: str) -> bool:
        """
        删除玩家绑定数据

        Args:
            name: 要删除的绑定数据的名字

        Returns:
            是否删除成功
        """
    def setNbt(self, nbt: NbtCompound) -> bool:
        """
        写入在线玩家对应的 NBT 对象

        Args:
            nbt: NBT 对象

        Returns:
            是否成功写入
        """
    def getNbt(self) -> NbtCompound:
        """
        获取在线玩家对应的 NBT 对象

        Returns:
            玩家的 NBT 对象
        """
    def addTag(self, tag: str) -> bool:
        """
        为玩家增加一个 Tag

        Args:
            tag: 要增加的 tag 字符串

        Returns:
            是否设置成功
        """
    def removeTag(self, tag: str) -> bool:
        """
        为玩家移除一个 Tag

        Args:
            tag: 要移除的 tag 字符串

        Returns:
            是否移除成功
        """
    def hasTag(self, tag: str) -> bool:
        """
        检查玩家是否拥有某个 Tag

        Args:
            tag: 要检查的 tag 字符串

        Returns:
            是否拥有这个 Tag
        """
    def getAllTags(self) -> list[str]:
        """
        获取玩家拥有的所有 Tag 列表

        Returns:
            玩家所有的 tag 字符串列表
        """
    def getAbilities(self) -> dict[str, Any]:
        """
        获取玩家的 Abilities 能力列表（来自玩家 NBT）

        Returns:
            玩家所有能力信息的键 - 值对列表对象
        """
    def getAttributes(self) -> list[dict[str, Any]]:
        """
        获取玩家的 Attributes 属性列表（来自玩家 NBT）

        Returns:
            玩家所有属性对象的数组
        """
    def getEntityFromViewVector(self, max_distance: float = 5.25) -> LLSE_Entity | None:
        """
        获取视线方向实体

        Args:
            max_distance: 查找最大距离

        Returns:
            视线方向实体，如果获取失败，返回 `None`
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
    def quickEvalMolangScript(self, exp: str) -> float:
        """
        快速执行 Molang 表达式

        关于Molang的详细使用方法，请参考 [MOLANG 文档 bedrock.dev](https://bedrock.dev/zh/docs/stable/Molang)

        Args:
            exp: Molang 表达式

        Returns:
            表达式执行结果
        """
    def getMoney(self) -> int:
        """
        获取玩家的存款金额

        Returns:
            玩家的资金数值
        """
    def setMoney(self, value: int) -> bool:
        """
        设置玩家的存款金额

        Args:
            value: 要设置的金额

        Returns:
            是否设置成功
        """
    def addMoney(self, value: int) -> bool:
        """
        增加玩家的存款

        Args:
            value: 要增加的金额

        Returns:
            是否设置成功
        """
    def reduceMoney(self, value: int) -> bool:
        """
        减少玩家的存款

        Args:
            value: 要减小的金额

        Returns:
            是否设置成功
        """
    @overload
    def transMoney(self, target: LLSE_Player | str, money: int) -> bool: ...
    @overload
    def transMoney(self, target: LLSE_Player | str, money: int, note: str) -> bool:
        """
        进行一笔转账

        Args:
            target: 收款的玩家的 玩家对象 或 XUID 标识符
            money: 要支付的金额
            note: 给这笔转账附加一些文字说明

        Returns:
            是否转账成功
        """
    def getMoneyHistory(self, time: int) -> list[T_MoneyHistory]:
        """
        查询历史账单

        Args:
            time: 查询从现在开始往前 `time` 秒的记录

        Returns:
            查询结果对象的数组
        """
    def isSimulatedPlayer(self) -> bool:
        """
        判断是否为模拟玩家

        Returns:
            是否为模拟玩家
        """
    def simulateSneak(self) -> bool:
        """
        模拟潜行

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateAttack(self) -> bool:
        """
        模拟攻击

        默认攻击视线方向上的实体

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateAttack(self, target: LLSE_Entity) -> bool:
        """
        模拟攻击

        Args:
            target: 攻击目标

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateDestroy(self, pos: IntPos) -> bool:
        """
        模拟破坏

        默认破坏视线方向上的方块

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateDestroy(self, pos: IntPos, face: int = 0) -> bool:
        """
        模拟破坏

        Args:
            pos: 要破坏的方块的坐标
            face: 从哪面破坏

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateDestroy(self, block: LLSE_Block, face: int = 0) -> bool:
        """
        模拟破坏

        Args:
            block: 要破坏的方块
            face: 从哪面破坏

        Returns:
            是否成功模拟操作
        """
    def simulateDisconnect(self) -> bool:
        """
        模拟断开连接

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateInteract(self) -> bool:
        """
        模拟交互

        默认交互视线方向上的方块或实体

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateInteract(self, target: LLSE_Entity) -> bool:
        """
        模拟交互

        Args:
            block: 模拟交互目标

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateInteract(self, pos: IntPos, face: int = 0) -> bool:
        """
        模拟交互

        Args:
            block: 模拟交互目标坐标
            face: 模拟交互目标坐标的面

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateInteract(self, block: LLSE_Block, face: int = 0) -> bool:
        """
        模拟交互

        Args:
            block: 模拟交互目标方块
            face: 模拟交互目标方块的面

        Returns:
            是否成功模拟操作
        """
    def simulateRespawn(self) -> bool:
        """
        模拟重生

        Returns:
            是否成功模拟操作
        """
    def simulateJump(self) -> bool:
        """
        模拟跳跃

        Returns:
            是否成功模拟操作
        """
    def simulateLocalMove(self, pos: T_PosType, speed: T_Number = 1) -> bool:
        """
        相对玩家坐标系移动

        Args:
            pos: 移动方向
            speed: 移动速度

        Returns:
            是否请求移动成功
        """
    def simulateWorldMove(self, pos: T_PosType, speed: T_Number = 1) -> bool:
        """
        相对世界坐标系移动

        Args:
            pos: 移动方向
            speed: 移动速度

        Returns:
            是否请求移动成功
        """
    def simulateMoveTo(self, pos: T_PosType, speed: T_Number = 1) -> bool:
        """
        直线移动到坐标

        如需自动寻路，请考虑使用 `模拟导航移动` (`LLSE_Player.simulateNavigateTo()`)

        Args:
            pos: 移动方向
            speed: 移动速度

        Returns:
            是否请求移动成功
        """
    def simulateLookAt(self, target: T_PosType | LLSE_Entity | LLSE_Block) -> bool:
        """
        模拟看向某方块或实体

        Args:
            target: 要看向的 坐标 / 实体 / 方块

        Returns:
            是否成功模拟操作
        """
    def simulateSetBodyRotation(self, rot: T_Number) -> bool:
        """
        模拟设置身体角度

        Args:
            rot: 要设置的角度

        Returns:
            是否成功模拟操作
        """
    def simulateNavigateTo(
        self,
        target: T_PosType | LLSE_Entity,
        speed: T_Number = 1,
    ) -> T_NavigatePath:
        """
        模拟导航移动

        Args:
            target: 导航目标
            speed: 移动速度

        Returns:
            是否能到达指定位置以及导航路径
        """
    @overload
    def simulateUseItem(self) -> bool:
        """
        模拟使用物品

        使用的物品 默认为选中物品
        目标坐标 默认为朝向方块坐标
        目标方块面 默认为 `0`
        偏移坐标 默认为 `(0.5, 0.5, 0.5)`

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateUseItem(self, item: int | LLSE_Item) -> bool:
        """
        模拟使用物品

        目标坐标 默认为朝向方块坐标
        目标方块面 默认为 `0`
        偏移坐标 默认为 `(0.5, 0.5, 0.5)`

        Args:
            item: 要使用的物品 / 物品所在的槽位 ID

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateUseItem(self, item: int | LLSE_Item, pos: IntPos) -> bool:
        """
        模拟使用物品

        目标方块面 默认为 `0`
        偏移坐标 默认为 `(0.5, 0.5, 0.5)`

        Args:
            item: 要使用的物品 / 物品所在的槽位 ID
            pos: 目标坐标

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateUseItem(
        self,
        item: int | LLSE_Item,
        pos: IntPos,
        face: int,
    ) -> bool:
        """
        模拟使用物品

        偏移坐标 默认为 `(0.5, 0.5, 0.5)`

        Args:
            item: 要使用的物品 / 物品所在的槽位 ID
            pos: 目标坐标
            face: 目标方块的面

        Returns:
            是否成功模拟操作
        """
    @overload
    def simulateUseItem(
        self,
        item: int | LLSE_Item,
        pos: IntPos,
        face: int,
        relative: FloatPos,
    ) -> bool:
        """
        模拟使用物品

        Args:
            item: 要使用的物品 / 物品所在的槽位 ID
            pos: 目标坐标
            face: 目标方块的面
            relative: 相对方块偏移坐标

        Returns:
            是否成功模拟操作
        """
    def simulateStopDestroyingBlock(self) -> bool:
        """
        模拟停止破坏方块

        Returns:
            是否成功模拟操作
        """
    def simulateStopInteracting(self) -> bool:
        """
        模拟停止交互

        Returns:
            是否成功模拟操作
        """
    def simulateStopMoving(self) -> bool:
        """
        模拟停止移动

        Returns:
            是否成功模拟操作
        """
    def simulateStopUsingItem(self) -> bool:
        """
        模拟停止使用物品

        Returns:
            是否成功模拟操作
        """
    def simulateStopSneaking(self) -> bool:
        """
        模拟停止潜行

        Returns:
            是否成功模拟操作
        """
    def asPointer(self) -> NativePointer: ...
    @deprecated("请使用 `LLSE_Player.isSneaking`")
    @property
    def sneaking(self) -> bool: ...
    @deprecated("请使用 `LLSE_Player.getDevice()`")
    @property
    def ip(self) -> str: ...
    @deprecated("请使用 `LLSE_Player.setNbt()`")
    def setTag(self, nbt: NbtCompound) -> bool: ...
    @deprecated("请使用 `LLSE_Player.getNbt()`")
    def getTag(self) -> NbtCompound: ...
    @deprecated("请使用 `LLSE_Player.setFire()`")
    def setOnFire(self, time: int) -> bool: ...
    @deprecated("请使用 `LLSE_Player.getInventory()`")
    def removeItem(self, inventory_id: int, count: int) -> bool: ...
    @deprecated("请使用 `LLSE_Player.getInventory()`")
    def getAllItems(self) -> T_PlayerInventory: ...
    @deprecated("请使用 `LLSE_Player.deleteScore()`")
    def removeScore(self, name: str) -> bool: ...
    @deprecated("请使用 `LLSE_Player.distanceTo()`")
    def distanceToPos(self, pos: LLSE_Entity | LLSE_Player | T_PosType) -> T_Number: ...

Player = LLSE_Player
