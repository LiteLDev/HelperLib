from typing import Any, Callable, Literal, NoReturn, overload

from typing_extensions import deprecated

from llpy import (
    FloatPos,
    IntPos,
    LLSE_Block,
    LLSE_Command,
    LLSE_CustomForm,
    LLSE_Entity,
    LLSE_Item,
    LLSE_Objective,
    LLSE_Player,
    LLSE_SimpleForm,
    NbtCompound,
    ParticleSpawner,
)
from llpy.classes.entity.types import T_DamageCause
from llpy.types import T_DimID, T_Number, T_PermType, T_PosType, T_ScoreDisplaySlot

from .types import (
    T_BroadcastType,
    T_ConsoleCmdCallback,
    T_PlayerCmdCallback,
    T_RunCmdExRet,
    T_StructRotationType,
    T_StructureMirrorType,
    T_TimeID,
    T_WeatherID,
)

class mc:
    """MC API"""

    def __init__(self) -> NoReturn: ...

    # region listener
    @overload
    @staticmethod
    def listen(
        event: Literal["onPreJoin"],
        callback: Callable[[LLSE_Player], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家开始连接服务器 监听

        拦截事件：函数返回 `False`

        注：在这个监听函数中只能获取一些玩家的基础信息，比如名字、IP、XUID等。因为此时玩家尚未完全进服

        Callback Args:
            player (LLSE_Player): 正在连接服务器的玩家对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onJoin"],
        callback: Callable[[LLSE_Player], Any],
    ) -> bool:
        """
        注册监听器

        玩家进入游戏（加载世界完成） 监听

        拦截事件：不可以拦截

        Callback Args:
            player (LLSE_Player): 进入游戏的玩家对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onLeft"],
        callback: Callable[[LLSE_Player], Any],
    ) -> bool:
        """
        注册监听器

        玩家离开游戏 监听

        拦截事件：不可以拦截

        Callback Args:
            player (LLSE_Player): 离开游戏的玩家对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onRespawn"],
        callback: Callable[[LLSE_Player], Any],
    ) -> bool:
        """
        注册监听器

        玩家重生 监听

        拦截事件：不可以拦截

        Callback Args:
            player (LLSE_Player): 重生的玩家对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onPlayerDie"],
        callback: Callable[[LLSE_Player, LLSE_Entity | None], Any],
    ) -> bool:
        """
        注册监听器

        玩家死亡 监听

        拦截事件：不可以拦截

        Callback Args:
            player (LLSE_Player): 死亡的玩家对象
            source (LLSE_Entity | None): 伤害来源的实体对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onPlayerCmd"],
        callback: Callable[[LLSE_Player, str], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家执行命令 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 执行命令的玩家对象
            cmd (str): 执行的命令

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onChat"],
        callback: Callable[[LLSE_Player, str], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家发送聊天信息 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 发送聊天信息的玩家对象
            msg (str): 发送的聊天消息

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onChangeDim"],
        callback: Callable[[LLSE_Player, T_DimID], Any],
    ) -> bool:
        """
        注册监听器

        玩家切换维度 监听

        拦截事件：不可以拦截

        提醒：当玩家从末地通过返回传送门返回主世界时，不会触发此事件。

        Callback Args:
            player (LLSE_Player): 切换维度的玩家对象
            dim_id (T_DimID): 前往维度的维度 ID

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onJump"],
        callback: Callable[[LLSE_Player], Any],
    ) -> bool:
        """
        注册监听器

        玩家跳跃 监听

        拦截事件：不可以拦截

        Callback Args:
            player (LLSE_Player): 跳跃的玩家对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onSneak"],
        callback: Callable[[LLSE_Player, bool], Any],
    ) -> bool:
        """
        注册监听器

        玩家切换潜行状态 监听

        拦截事件：不可以拦截

        Callback Args:
            player (LLSE_Player): 切换潜行状态的玩家对象
            is_sneaking (bool): `True` 表示玩家进入潜行状态，`False` 表示玩家退出潜行状态

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onAttackEntity"],
        callback: Callable[[LLSE_Player, LLSE_Entity, float], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家攻击实体 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 攻击实体的玩家对象
            entity (LLSE_Entity): 被攻击的实体对象
            damage (float): 攻击所造成的伤害

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onAttackBlock"],
        callback: Callable[[LLSE_Player, LLSE_Entity, LLSE_Item], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家攻击方块 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 攻击方块的玩家对象
            entity (LLSE_Entity): 被攻击的方块对象
            item (LLSE_Item): 手持的物品对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onUseItem"],
        callback: Callable[[LLSE_Player, LLSE_Item], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家使用物品 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 使用物品的玩家对象
            item (LLSE_Item): 被使用的物品对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onUseItemOn"],
        callback: Callable[
            [LLSE_Player, LLSE_Item, LLSE_Block, Literal[0, 1, 2, 3, 4, 5], FloatPos],
            Literal[False] | Any,
        ],
    ) -> bool:
        """
        注册监听器

        玩家对方块使用物品（点击右键） 监听

        拦截事件：函数返回 `False`

        注：Win10 客户端玩家右键会在服务端连续多次激发这个事件

        Callback Args:
            player (LLSE_Player): 使用物品的玩家对象
            item (LLSE_Item): 被使用的物品对象
            block (LLSE_Block): 被点击到的方块对象
            side (Literal[0, 1, 2, 3, 4, 5]): 方块被点击的面，依次为：`0`-下 `1`-上 `2`-北 `3`-南 `4`-西 `5`-东
            pos (FloatPos): 被点击的浮点位置

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onUseBucketPlace"],
        callback: Callable[
            [LLSE_Player, LLSE_Item, LLSE_Block, Literal[0, 1, 2, 3, 4, 5], FloatPos],
            Literal[False] | Any,
        ],
    ) -> bool:
        """
        注册监听器

        玩家使用桶倒出东西 监听

        拦截事件：函数返回 `False`

        注：无论是手机还是 Win10 玩家，可能会连续多次激发这个事件

        Callback Args:
            player (LLSE_Player): 使用物品的玩家对象
            item (LLSE_Item): 被使用的物品对象
            block (LLSE_Block): 被点击到的方块对象
            side (Literal[0, 1, 2, 3, 4, 5]): 方块被点击的面，依次为：`0`-下 `1`-上 `2`-北 `3`-南 `4`-西 `5`-东
            pos (FloatPos): 被点击的浮点位置

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onUseBucketTake"],
        callback: Callable[
            [
                LLSE_Player,
                LLSE_Item,
                LLSE_Block | LLSE_Entity,
                Literal[0, 1, 2, 3, 4, 5],
                FloatPos,
            ],
            Literal[False] | Any,
        ],
    ) -> bool:
        """
        注册监听器

        玩家使用桶装进东西 监听

        拦截事件：函数返回 `False`

        注：无论是手机还是 Win10 玩家，可能会连续多次激发这个事件

        Callback Args:
            player (LLSE_Player): 使用物品的玩家对象
            item (LLSE_Item): 被使用的物品对象
            target (LLSE_Block | LLSE_Entity): 被点击到的方块 / 实体对象
            side (Literal[0, 1, 2, 3, 4, 5]): 方块被点击的面，依次为：`0`-下 `1`-上 `2`-北 `3`-南 `4`-西 `5`-东
            pos (FloatPos): 被点击的浮点位置

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onTakeItem"],
        callback: Callable[[LLSE_Player, LLSE_Entity, LLSE_Item], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家捡起物品 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 捡起物品的玩家对象
            entity (LLSE_Entity): 即将被捡起的物品的掉落物实体
            item (LLSE_Item): 即将被捡起的物品对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onDropItem"],
        callback: Callable[[LLSE_Player, LLSE_Item], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家丢出物品 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 丢出物品的玩家对象
            item (LLSE_Item): 被丢出的物品对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onEat"],
        callback: Callable[[LLSE_Player, LLSE_Item], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家正在吃食物 监听

        拦截事件：函数返回 `False`

        此处的 食物 为宽泛物品的概念，包括常规食物、药水、牛奶、药品等多种可以被摄取的物品

        Callback Args:
            player (LLSE_Player): 正在吃的玩家对象
            item (LLSE_Item): 被吃的物品对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onAte"],
        callback: Callable[[LLSE_Player, LLSE_Item], Any],
    ) -> bool:
        """
        注册监听器

        玩家吃下食物 监听

        拦截事件：不可以拦截

        Callback Args:
            player (LLSE_Player): 正在吃的玩家对象
            item (LLSE_Item): 被吃的物品对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onConsumeTotem"],
        callback: Callable[[LLSE_Player], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家消耗图腾 监听

        拦截事件：函数返回 `False`

        此处拦截后，仍会触发图腾的复活效果，但不会消耗图腾

        Callback Args:
            player (LLSE_Player): 消耗图腾的玩家对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onEffectAdded"],
        callback: Callable[[LLSE_Player, str, int, int], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家获得效果 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 获得效果的玩家对象
            effect_name (str): 获得的效果名称（`minecraft:effect.效果`）
            amplifier (int): 获得的效果倍率（效果等级 -1）
            duration (int): 获得的效果时长（单位：tick）

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onEffectUpdated"],
        callback: Callable[[LLSE_Player, str, int, int], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家刷新效果 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 获得效果的玩家对象
            effect_name (str): 获得的效果名称（`minecraft:effect.效果`）
            amplifier (int): 获得的效果倍率（效果等级 -1）
            duration (int): 获得的效果时长（单位：tick）

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onEffectRemoved"],
        callback: Callable[[LLSE_Player, str], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家移除效果 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 被移除效果的玩家对象
            effect_name (str): 被移除的效果名称（`minecraft:effect.效果`）

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onStartDestroyBlock"],
        callback: Callable[[LLSE_Player, LLSE_Block], Any],
    ) -> bool:
        """
        注册监听器

        玩家开始破坏方块 / 点击左键 监听

        拦截事件：不可以拦截

        Callback Args:
            player (LLSE_Player): 正在破坏方块的玩家对象
            block (LLSE_Block): 正在被破坏的方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onDestroyBlock"],
        callback: Callable[[LLSE_Player, LLSE_Block], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家破坏方块完成 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 破坏方块的玩家对象
            block (LLSE_Block): 被破坏的方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onPlaceBlock"],
        callback: Callable[[LLSE_Player, LLSE_Block], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        onPlaceBlock 监听

        拦截事件：函数返回 `False`

        存在问题：
        1. 当玩家尝试放置方块时，该事件将持续被触发。
        2. 方块对象为准星对准的方块，并非将放置方块对象。

        Callback Args:
            player (LLSE_Player): 放置方块的玩家对象
            block (LLSE_Block): 将要放置的方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["afterPlaceBlock"],
        callback: Callable[[LLSE_Player, LLSE_Block], Any],
    ) -> bool:
        """
        注册监听器

        玩家放置方块 监听

        拦截事件：不可以拦截

        Callback Args:
            player (LLSE_Player): 放置方块的玩家对象
            block (LLSE_Block): 被放置的方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onOpenContainer"],
        callback: Callable[[LLSE_Player, LLSE_Block], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家打开容器方块 监听

        拦截事件：函数返回 `False`

        此处的 容器 为宽泛容器的概念，包括箱子、桶等多种可以储存物品的容器都可以触发此事件

        Callback Args:
            player (LLSE_Player): 打开容器方块的玩家对象
            block (LLSE_Block): 被打开的容器方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onCloseContainer"],
        callback: Callable[[LLSE_Player, LLSE_Block], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家关闭容器方块 监听

        拦截事件：函数返回 `False`

        由于监听函数下限制，目前支持监听关闭的容器有：箱子（`minecraft:chest`）、木桶（`minecraft:barrel`）

        Callback Args:
            player (LLSE_Player): 关闭容器方块的玩家对象
            block (LLSE_Block): 被关闭的容器方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onInventoryChange"],
        callback: Callable[[LLSE_Player, int, LLSE_Item, LLSE_Item], Any],
    ) -> bool:
        """
        注册监听器

        玩家物品栏变化 监听

        拦截事件：不可以拦截

        对回调参数的解释：
        旧物品对象与新物品对象有多种不同的组合情况，表示格子内不同的变化情况

        - 放入物品：旧物品对象为空，新物品对象不为空
        - 取出物品：旧物品对象不为空，新物品对象为空
        - 物品增加堆叠：旧物品对象的 `type` == 新物品对象的 `type`，且旧物品对象的 `count` < 新物品对象的 `count`
        - 物品减少堆叠：旧物品对象的 `type` == 新物品对象的 `type`，且旧物品对象的 `count` > 新物品对象的 `count`
        - 替换物品：旧物品对象的 `type` 不等于 新物品对象的 `type`，且两物品对象均不为空

        Callback Args:
            player (LLSE_Player): 操作物品栏的玩家对象
            slot_num (int): 操作物品栏的格子位置（第 `slot_num` 个格子）
            old_item (LLSE_Item): 格子中的原来旧物品对象
            new_item (LLSE_Item): 格子中新的物品对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onChangeSprinting"],
        callback: Callable[[LLSE_Player, bool], Any],
    ) -> bool:
        """
        注册监听器

        玩家改变疾跑状态 监听

        拦截事件：不可以拦截

        注：可在下一游戏刻执行 `player.setSprinting(False)` 达到拦截效果

        Callback Args:
            player (LLSE_Player): 要改变疾跑状态的玩家对象
            sprinting (bool): 要改变成的疾跑状态

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onSetArmor"],
        callback: Callable[
            [LLSE_Player, Literal[0, 1, 2, 3], LLSE_Item],
            Literal[False] | Any,
        ],
    ) -> bool:
        """
        注册监听器

        玩家改变盔甲栏 监听

        拦截事件：函数返回 `False`

        注：拦截后，进入游戏时会脱下原先的装备

        Callback Args:
            player (LLSE_Player): 改变盔甲栏的玩家对象
            slot_num (Literal[0, 1, 2, 3]): 盔甲栏序号，范围 `0-3`
            item (LLSE_Item): 盔甲栏中的物品对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onUseRespawnAnchor"],
        callback: Callable[[LLSE_Player, IntPos], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家使用重生锚 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 使用重生锚的玩家对象
            pos (IntPos): 被使用的重生锚的位置

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onOpenContainerScreen"],
        callback: Callable[[LLSE_Player], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家打开容器类 GUI 监听

        拦截事件：函数返回 `False`

        注：此事件非常强力，甚至可以拦截打开背包。

        Callback Args:
            player (LLSE_Player): 尝试打开 GUI 的玩家对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onExperienceAdd"],
        callback: Callable[[LLSE_Player, int], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家获得经验 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 获得经验的玩家对象
            exp (int): 获得的经验值

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onBedEnter"],
        callback: Callable[[LLSE_Player, IntPos], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家上床 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 上床的玩家对象
            pos (IntPos): 床的位置

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onPlayerPullFishingHook"],
        callback: Callable[
            [LLSE_Player, LLSE_Entity, LLSE_Item | None],
            Literal[False] | Any,
        ],
    ) -> bool:
        """
        注册监听器

        玩家使用钓鱼竿钓起实体 监听

        拦截事件：函数返回 `False`

        Callback Args:
            player (LLSE_Player): 使用钓鱼竿的玩家对象
            entity (LLSE_Entity): 钓起的实体（鱼钩拉起任意实体都会触发该事件，不一定是物品实体）
            item (LLSE_Item | None): 钓起的物品对象（如果钓到的不是物品则返回 `None`）

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onMobDie"],
        callback: Callable[
            [LLSE_Entity, LLSE_Entity | None, T_DamageCause],
            Literal[False] | Any,
        ],
    ) -> bool:
        """
        注册监听器

        生物死亡 监听

        拦截事件：不可以拦截

        注意，当玩家死亡时，除了触发 `onPlayerDie` 事件，这个事件同样也会被触发一次

        Callback Args:
            mob (LLSE_Entity): 死亡的实体对象
            source (LLSE_Entity | None): 伤害来源的实体对象
            cause (T_DamageCause): 死亡原因

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onMobHurt"],
        callback: Callable[
            [LLSE_Entity, LLSE_Entity | None, float, T_DamageCause],
            Literal[False] | Any,
        ],
    ) -> bool:
        """
        注册监听器

        生物受伤（包括玩家） 监听

        拦截事件：函数返回 `False`

        Callback Args:
            mob (LLSE_Entity): 受伤的实体对象
            source (LLSE_Entity | None): 伤害来源的实体对象
            damage (float): 受到的伤害数值
            cause (T_DamageCause): 受伤原因

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onEntityExplode"],
        callback: Callable[
            [LLSE_Entity, FloatPos, float, float, bool, bool],
            Literal[False] | Any,
        ],
    ) -> bool:
        """
        注册监听器

        发生由实体引起的爆炸 监听

        拦截事件：函数返回 `False`

        Callback Args:
            source (LLSE_Entity): 爆炸来源的实体对象
            pos (FloatPos): 爆炸发生的坐标
            radius (float): 爆炸波及的半径
            max_resistance (float): 爆炸可破坏的方块爆炸抗性上限
            is_destroy (bool): 爆炸是否破坏方块
            is_fire (bool): 爆炸是否产生火焰

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onProjectileHitEntity"],
        callback: Callable[[LLSE_Entity, LLSE_Entity], Any],
    ) -> bool:
        """
        注册监听器

        实体被弹射物击中 监听

        拦截事件：不可以拦截

        Callback Args:
            entity (LLSE_Entity): 被击中的实体对象
            source (LLSE_Source): 发射的弹射物实体（如箭）

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onWitherBossDestroy"],
        callback: Callable[[LLSE_Entity, IntPos, IntPos], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        凋灵破坏方块 监听

        拦截事件：函数返回 `False`

        注意，此事件不包括凋灵爆炸的破坏。

        Callback Args:
            wither (LLSE_Entity): 凋灵的实体对象
            pos_a (IntPos): 凋灵将破坏的区域（长方体），对角点 A 坐标
            pos_b (IntPos): 凋灵将破坏的区域（长方体），对角点 B 坐标

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onEnderDragonDestroy"],
        callback: Callable[[LLSE_Entity, LLSE_Block], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        末影龙破坏方块 监听

        拦截事件：函数返回 `False`

        Callback Args:
            dragon (LLSE_Entity): 末影龙的实体对象
            block (LLSE_Block): 末影龙破坏的方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onRide"],
        callback: Callable[[LLSE_Entity, LLSE_Entity], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        生物骑乘 监听

        拦截事件：函数返回 `False`

        注：骑乘包括坐矿车、坐船、骑马、骑猪等。

        Callback Args:
            entity (LLSE_Entity): 尝试骑乘的实体对象
            ridable (LLSE_Entity): 被骑乘的实体对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onStepOnPressurePlate"],
        callback: Callable[[LLSE_Entity, LLSE_Block], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        生物踩压力板 监听

        拦截事件：函数返回 `False`

        注：生物踩压力板时，将会反复多次触发此事件。

        Callback Args:
            entity (LLSE_Entity): 踩压力板的实体对象
            block (LLSE_Block): 被踩的压力板方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onSpawnProjectile"],
        callback: Callable[[LLSE_Entity, str], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        弹射物创建 监听

        拦截事件：函数返回 `False`

        注：已知可拦截的弹射物有鸡蛋、末影珍珠、雪球、三叉戟、箭、钓竿（鱼钩）。

        Callback Args:
            shooter (LLSE_Entity): 发射弹射物的的实体对象
            type (str): 弹射物标准类型名

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onProjectileCreated"],
        callback: Callable[[LLSE_Entity, LLSE_Entity], Any],
    ) -> bool:
        """
        注册监听器

        弹射物创建完毕 监听

        拦截事件：不可以拦截

        Callback Args:
            shooter (LLSE_Entity): 创建此弹射物的的实体对象
            entity (LLSE_Entity): 被创建的弹射物实体对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onNpcCmd"],
        callback: Callable[[LLSE_Entity, LLSE_Player, str], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        NPC 执行命令 监听

        拦截事件：函数返回 `False`

        Callback Args:
            npc (LLSE_Entity): 执行命令的 NPC 实体对象
            player (LLSE_Player): 触发 NPC 命令执行的玩家对象
            cmd (str): NPC 执行的命令

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onChangeArmorStand"],
        callback: Callable[[LLSE_Entity, LLSE_Player, int], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        操作盔甲架 监听

        拦截事件：函数返回 `False`

        Callback Args:
            armor_stand (LLSE_Entity): 被操作的盔甲架实体对象
            player (LLSE_Player): 操作盔甲架的玩家对象
            slot (int): 装备栏编号

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onEntityTransformation"],
        callback: Callable[[str, LLSE_Entity], Any],
    ) -> bool:
        """
        注册监听器

        实体转变 监听

        拦截事件：不可以拦截

        注：此事件为 Addons 中实体的 TransformationComponent 激活时触发，多用于引擎与Addon交互。
        由于转变前的实体指针很快被销毁，因此只提供 UniqueId。

        Callback Args:
            unique_id (str): 转变前的实体的唯一标识符
            entity (LLSE_Entity): 转换完成的实体

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onBlockInteracted"],
        callback: Callable[[LLSE_Player, LLSE_Block], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        方块接受玩家互动 监听

        拦截事件：函数返回 `False`

        只有可以被互动的方块才会触发此事件，如木桶、信标、制图台、磨石等。拦截事件对箱子、潜影盒、工作台无效

        Callback Args:
            player (LLSE_Player): 与方块互动的玩家对象
            block (LLSE_Block): 被互动的方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onBlockChanged"],
        callback: Callable[[LLSE_Block, LLSE_Block], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        方块改变 监听

        拦截事件：函数返回 `False`

        拦截此事件需要注意以下问题：

        1. 部分事件导致的方块变化无法拦截, 比如玩家挖掘，放置
        2. 对于方块与方块之间关系导致的变化，部分不可拦截，比如爆炸摧毁周围方块（实际上，客户端看起来那边还是存在方块的，但是已经是假方块了）
        3. 但是对于火把这种需要附着在其他方块上的方块，如果因为附着方块被摧毁，那么火把不会随之被破坏

        具体某些特性可以自行测试

        Callback Args:
            before (LLSE_Block): 改变前的方块对象
            after (LLSE_Block): 改变后的方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onBlockExplode"],
        callback: Callable[
            [LLSE_Block, IntPos, float, float, bool, bool],
            Literal[False] | Any,
        ],
    ) -> bool:
        """
        注册监听器

        发生由方块引起的爆炸 监听

        拦截事件：函数返回 `False`

        Callback Args:
            source (LLSE_Block): 爆炸来源的方块对象
            pos (IntPos): 爆炸发生的坐标
            radius (float): 爆炸波及的半径
            max_resistance (float): 爆炸可破坏的方块爆炸抗性上限
            is_destroy (bool): 爆炸是否破坏方块
            is_fire (bool): 爆炸是否产生火焰

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onRespawnAnchorExplode"],
        callback: Callable[[IntPos, LLSE_Player], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        发生由重生锚引起的爆炸 监听

        拦截事件：函数返回 `False`

        Callback Args:
            pos (IntPos): 爆炸发生的重生锚的坐标
            player (LLSE_Player): 试图使用重生锚的玩家

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onBlockExploded"],
        callback: Callable[[LLSE_Block, LLSE_Entity], Any],
    ) -> bool:
        """
        注册监听器

        方块被爆炸破坏 监听

        拦截事件：不可以拦截

        Callback Args:
            block (LLSE_Block): 被爆炸破坏的方块对象
            source (LLSE_Entity): 爆炸来源的实体对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onFireSpread"],
        callback: Callable[[IntPos], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        火焰蔓延 监听

        拦截事件：函数返回 `False`

        Callback Args:
            pos (IntPos): 火焰蔓延到的方块坐标

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onCmdBlockExecute"],
        callback: Callable[[str, IntPos, bool], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        命令方块执行命令 监听

        拦截事件：函数返回 `False`

        Callback Args:
            cmd (str): 执行的命令
            pos (IntPos): 执行命令的命令方块坐标
            is_minecart (bool): 命令是否由命令方块矿车执行

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onContainerChange"],
        callback: Callable[[LLSE_Player, LLSE_Block, int, LLSE_Item, LLSE_Item], Any],
    ) -> bool:
        """
        注册监听器

        容器内容改变 监听

        拦截事件：不可以拦截

        对回调参数的解释：
        旧物品对象与新物品对象有多种不同的组合情况，表示格子内不同的变化情况

        - 放入物品：旧物品对象为空，新物品对象不为空
        - 取出物品：旧物品对象不为空，新物品对象为空
        - 物品增加堆叠：旧物品对象的 `type` == 新物品对象的 `type`，且旧物品对象的 `count` < 新物品对象的 `count`
        - 物品减少堆叠：旧物品对象的 `type` == 新物品对象的 `type`，且旧物品对象的 `count` > 新物品对象的 `count`
        - 替换物品：旧物品对象的 `type` 不等于 新物品对象的 `type`，且两物品对象均不为空

        Callback Args:
            player (LLSE_Player): 操作容器的玩家对象
            container (LLSE_block): 被操作的容器的方块对象
            slot_num (int): 操作容器的格子位置（第 `slotNum` 个格子）
            old_item (LLSE_Item): 格子中的原来旧物品对象
            new_item (LLSE_Item): 格子中新的物品对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onProjectileHitBlock"],
        callback: Callable[[LLSE_Block, LLSE_Entity], Any],
    ) -> bool:
        """
        注册监听器

        方块被弹射物击中 监听

        拦截事件：不可以拦截

        Callback Args:
            block (LLSE_Block): 被击中的方块对象
            source (LLSE_Entity): 发射的弹射物实体（如箭）

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onRedStoneUpdate"],
        callback: Callable[[LLSE_Block, int, bool], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        发生红石更新 监听

        拦截事件：函数返回 `False`

        目前可以监测红石更新的方块种类有：红石线、红石火把、红石中继器、红石比较器

        Callback Args:
            block (LLSE_Block): 发生红石更新的方块对象
            level (int): 更新的红石能量等级（0-15）
            is_active (bool): 表示红石更新是激活还是熄灭。为 `True` 表示红石变为激活状态，为 `False` 表示红石变为熄灭状态

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onHopperSearchItem"],
        callback: Callable[[FloatPos, bool, LLSE_Item], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        漏斗（漏斗矿车）检测可否吸取物品 监听

        拦截事件：函数返回 `False`

        注：在放置漏斗之后，会在服务端反复不断触发这个事件，当你拦截事件之后，漏斗就会无法吸取这个物品

        Callback Args:
            pos (FloatPos): 漏斗（漏斗矿车）所在的位置
            is_minecart (bool): 是否为漏斗矿车
            item (LLSE_Item): 检测到的物品对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onHopperPushOut"],
        callback: Callable[[FloatPos, bool, LLSE_Item], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        漏斗输出物品 监听

        拦截事件：函数返回 `False`

        Callback Args:
            pos (FloatPos): 漏斗（漏斗矿车）所在的位置
            is_minecart (bool): 是否为漏斗矿车
            item (LLSE_Item): 准备输出的物品对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onPistonTryPush"],
        callback: Callable[[IntPos, LLSE_Block], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        活塞尝试推动 监听

        拦截事件：函数返回 `False`

        若活塞被方块阻挡无法推动，此事件将会不停地循环触发

        Callback Args:
            piston_pos (IntPos): 正在工作的活塞坐标
            block (LLSE_Block): 尝试被推动的方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onPistonPush"],
        callback: Callable[[IntPos, LLSE_Block], Any],
    ) -> bool:
        """
        注册监听器

        活塞推动 监听

        拦截事件：不可以拦截

        注：此事件与上事件不同，上一个 Try 事件在活塞推动前尝试时触发，此事件在推动完毕后触发

        Callback Args:
            piston_pos (IntPos): 正在工作的活塞坐标
            block (LLSE_Block): 被推动的方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onFarmLandDecay"],
        callback: Callable[[IntPos, LLSE_Entity], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        耕地退化 监听

        拦截事件：函数返回 `False`

        Callback Args:
            pos (IntPos): 退化的耕地的坐标
            entity (LLSE_Entity): 造成耕地退化的实体

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onUseFrameBlock"],
        callback: Callable[[LLSE_Player, LLSE_Block], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        操作物品展示框 监听

        拦截事件：函数返回 `False`

        注：操作包括放置物品、取下物品、旋转物品。

        Callback Args:
            player (LLSE_Player): 操作物品展示框的玩家对象
            block (LLSE_Block): 被操作的物品展示框方块对象

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onLiquidFlow"],
        callback: Callable[[LLSE_Block, IntPos], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        液体方块流动 监听

        拦截事件：函数返回 `False`

        Callback Args:
            from (LLSE_Block): 水源方块对象
            to (IntPos): 即将流经的方块位置

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onScoreChanged"],
        callback: Callable[[LLSE_Player, int, str, str], Any],
    ) -> bool:
        """
        注册监听器

        玩家计分板数值改变 监听

        拦截事件：不可以拦截

        Callback Args:
            player (LLSE_Player): 计分板数值改变的玩家
            num (int): 改变后的计分板数值
            name (str): 计分板计分项名称
            display_name (str): 计分板计分项的显示名称

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onTick"],
        callback: Callable[[], Any],
    ) -> bool:
        """
        注册监听器

        每个游戏刻触发 监听

        拦截事件：不可以拦截

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onServerStarted"],
        callback: Callable[[], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        服务器启动完毕 监听

        拦截事件：不可以拦截

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onConsoleCmd"],
        callback: Callable[[str], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        服务端执行后台命令 监听

        拦截事件：函数返回 `False`

        Callback Args:
            cmd (str): 执行的后台命令

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onConsoleOutput"],
        callback: Callable[[str], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        控制台产生命令输出 监听

        拦截事件：函数返回 `False`

        Callback Args:
            cmd (str): 输出的命令结果信息

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onMoneyAdd"],
        callback: Callable[[str, int], Any],
    ) -> bool:
        """
        注册监听器

        玩家金额增加事件 监听

        拦截事件：不可以拦截

        Callback Args:
            xuid (str): 金额变动的玩家的 XUID
            money (int): 增加的金额

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onMoneyReduce"],
        callback: Callable[[str, int], Any],
    ) -> bool:
        """
        注册监听器

        玩家金额增加事件 监听

        拦截事件：不可以拦截

        Callback Args:
            xuid (str): 金额变动的玩家的 XUID
            money (int): 增加的金额

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onMoneyTrans"],
        callback: Callable[[str, str, int], Any],
    ) -> bool:
        """
        注册监听器

        玩家转账事件 监听

        拦截事件：不可以拦截

        注意: 当 `onMoneyReduce` 或 `onMoneyAdd` 被触发时，该事件也会被触发

        Callback Args:
            from (str): 发起转账的玩家的 XUID
            to (str): 接受转账的玩家的 XUID
            money (int): 增加的金额

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onMoneySet"],
        callback: Callable[[str, int], Any],
    ) -> bool:
        """
        注册监听器

        直接设置玩家金额事件 监听

        拦截事件：不可以拦截

        Callback Args:
            xuid (str): 金额变动的玩家的 XUID
            money (int): 被设置的金额

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["beforeMoneyAdd"],
        callback: Callable[[str, int], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家金额增加前事件 监听

        拦截事件：函数返回 `False`

        Callback Args:
            xuid (str): 金额变动的玩家的 XUID
            money (int): 增加的金额

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["beforeMoneyReduce"],
        callback: Callable[[str, int], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家金额减少前事件 监听

        拦截事件：函数返回 `False`

        Callback Args:
            xuid (str): 金额变动的玩家的 XUID
            money (int): 减少的金额

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["beforeMoneyTrans"],
        callback: Callable[[str, str, int], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        玩家转账前事件 监听

        拦截事件：函数返回 `False`

        Callback Args:
            from (str): 发起转账的玩家的 XUID
            to (str): 接受转账的玩家的 XUID
            money (int): 增加的金额

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["beforeMoneySet"],
        callback: Callable[[str, int], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        设置玩家金额前事件 监听

        拦截事件：函数返回 `False`

        Callback Args:
            xuid (str): 金额变动的玩家的 XUID
            money (int): 被设置的金额

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onMobTrySpawn"],
        callback: Callable[[str, FloatPos], Literal[False] | Any],
    ) -> bool:
        """
        注册监听器

        实体尝试自然生成 监听

        拦截事件：函数返回 `False`

        Callback Args:
            type_name (str): 生成实体名称
            pos (FloatPos): 生成的坐标

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    @overload
    @staticmethod
    def listen(
        event: Literal["onMobSpawned"],
        callback: Callable[[str, FloatPos], Any],
    ) -> bool:
        """
        注册监听器

        实体自然生成完成 监听

        拦截事件：不可以拦截

        此事件为实体成功生成后触发，不可直接拦截，如需拦截请使用 `entity.despawn()` 或 `entity.remove()`

        Callback Args:
            type_name (str): 生成实体名称
            pos (FloatPos): 生成的坐标

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    # fallback
    @overload
    @staticmethod
    def listen(event: str, callback: Callable[..., Literal[False] | Any]) -> bool:
        """
        注册监听器

        拦截事件：函数返回 `False`（部分事件无法拦截）

        Args:
            event: 要监听的事件名
            callback: 注册的监听函数

        Returns:
            是否成功监听事件
        """
    # endregion

    @staticmethod
    def getBDSVersion() -> str:
        """
        获取服务器版本号

        Returns:
            服务端版本号字符串，格式形如 `v1.17.10`
        """
    @staticmethod
    def getServerProtocolVersion() -> int:
        """
        获取服务器协议版本

        Returns:
            服务端协议版本
        """
    @staticmethod
    def runcmd(cmd) -> bool:
        """
        执行一条后台命令

        Args:
            cmd: 待执行的命令

        Returns:
            是否执行成功
        """
    @staticmethod
    def runcmdEx(cmd) -> T_RunCmdExRet:
        """
        执行一条后台命令（强化版）

        `runcmdEx` 与普通 `runcmd` 实现区别非常大，在于 Ex 版本拥有隐藏输出的机制，执行结果不会输出至控制台。
        因此如果有需要，要手动用 `log` 函数将结果输出

        Args:
            cmd: 待执行的命令

        Returns:
            命令执行结果
        """
    @overload
    @staticmethod
    def newCommand(cmd: str, desc: str) -> LLSE_Command:
        """
        注册一条顶层命令

        默认指令权限 `PermType.GameMasters`

        Args:
            cmd: 待注册的命令
            desc: 命令描述文本

        Returns:
            指令对象
        """
    @overload
    @staticmethod
    def newCommand(cmd: str, desc: str, perm: T_PermType) -> LLSE_Command:
        """
        注册一条顶层命令

        Args:
            cmd: 待注册的命令
            desc: 命令描述文本
            perm: 指令执行所需权限（`PermType`）

        Returns:
            指令对象
        """
    @overload
    @staticmethod
    def newCommand(
        cmd: str,
        desc: str,
        perm: T_PermType,
        flag: int,
    ) -> LLSE_Command:
        """
        注册一条顶层命令

        Args:
            cmd: 待注册的命令
            desc: 命令描述文本
            perm: 指令执行所需权限（`PermType`）
            flag: 请输入 `0x80`

        Returns:
            指令对象
        """
    @overload
    @staticmethod
    def newCommand(
        cmd: str,
        desc: str,
        perm: T_PermType,
        flag: int,
        alias: str,
    ) -> LLSE_Command:
        """
        注册一条顶层命令

        Args:
            cmd: 待注册的命令
            desc: 命令描述文本
            perm: 指令执行所需权限（`PermType`）
            flag: 请输入 `0x80`
            alias: 命令的别名

        Returns:
            指令对象
        """
    @staticmethod
    def broadcast(msg: str, msg_type: T_BroadcastType = 0) -> bool:
        """
        广播一个文本消息给所有玩家

        Args:
            msg: 待发送的文本
            msg_type: 发送的文本消息类型

        Returns:
            是否成功发送
        """
    @staticmethod
    def getPlayer(info: str) -> LLSE_Player | None:
        """
        从现有玩家获取玩家对象

        Args:
            info: 玩家的 名字 或者 XUID 或者 uniqueId

        Returns:
            生成的玩家对象。如返回值为 `None` 则表示获取玩家失败
        """
    @staticmethod
    def getOnlinePlayers() -> list[LLSE_Player]:
        """
        获取所有在线玩家

        Returns:
            在线的玩家对象列表
        """
    @staticmethod
    def getAllEntities() -> list[LLSE_Entity]:
        """
        获取当前所有已加载的实体

        Returns:
            实体对象列表
        """
    @overload
    @staticmethod
    def getEntities(pos: T_PosType, distance: float = 2.0) -> list[LLSE_Entity]: ...
    @overload
    @staticmethod
    def getEntities(
        pos: T_PosType,
        pos2: T_PosType,
        distance: float = 2.0,
    ) -> list[LLSE_Entity]: ...
    @staticmethod
    def newItem(name: str, count: int) -> LLSE_Item | None:
        """
        生成新的物品对象

        Args:
            name: 物品的标准类型名，如 `minecraft:bread`
            count: 物品堆叠数量，最大值为 `64`

        Returns:
            生成的物品对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnMob(name: str, pos: T_PosType) -> LLSE_Entity | None:
        """
        生成新生物并获取

        通过此函数，在指定的位置生成一个新生物，并获取它对应的实体对象

        Args:
            name: 生物的命名空间名称，如 `minecraft:creeper`
            pos: 生成生物的位置的坐标对象

        Returns:
            生成的实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnMob(
        name: str,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
    ) -> LLSE_Entity | None:
        """
        生成新生物并获取

        通过此函数，在指定的位置生成一个新生物，并获取它对应的实体对象

        Args:
            name: 生物的命名空间名称，如 `minecraft:creeper`
            x: 生成生物的位置的 X 坐标
            y: 生成生物的位置的 Y 坐标
            z: 生成生物的位置的 Z 坐标
            dim_id: 生成生物的位置的 维度 ID

        Returns:
            生成的实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def cloneMob(entity: LLSE_Entity, pos: T_PosType) -> LLSE_Entity | None:
        """
        复制生物并获取

        通过此函数，在指定的位置复制另一个实体，并获取它对应的实体对象

        Args:
            entity: 需要复制的实体对象
            pos: 生成生物的位置的坐标对象

        Returns:
            生成的实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def cloneMob(
        entity: LLSE_Entity,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
    ) -> LLSE_Entity | None:
        """
        复制生物并获取

        通过此函数，在指定的位置复制另一个实体，并获取它对应的实体对象

        Args:
            entity: 需要复制的实体对象
            x: 生成生物的位置的 X 坐标
            y: 生成生物的位置的 Y 坐标
            z: 生成生物的位置的 Z 坐标
            dim_id: 生成生物的位置的 维度 ID

        Returns:
            生成的实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnItem(item: LLSE_Item, pos: T_PosType) -> LLSE_Entity | None:
        """
        根据物品对象生成掉落物实体

        通过此函数，根据物品对象，在指定的位置生成一个同样内容的掉落物实体

        Args:
            item: 生成掉落物实体所使用的物品对象
            pos: 生成掉落物实体的位置的坐标对象

        Returns:
            生成的掉落物实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnItem(
        item: LLSE_Item,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
    ) -> LLSE_Entity | None:
        """
        根据物品对象生成掉落物实体

        通过此函数，根据物品对象，在指定的位置生成一个同样内容的掉落物实体

        Args:
            item: 生成掉落物实体所使用的物品对象
            x: 生成掉落物实体的位置的 X 坐标
            y: 生成掉落物实体的位置的 Y 坐标
            z: 生成掉落物实体的位置的 Z 坐标
            dim_id: 生成掉落物实体的位置的 维度 ID

        Returns:
            生成的掉落物实体对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnSimulatedPlayer(name: str, pos: T_PosType) -> LLSE_Player | None:
        """
        创建一个模拟玩家

        Args:
            name: 模拟玩家名称
            pos: 生成模拟玩家的位置的坐标对象

        Returns:
            生成的模拟玩家对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def spawnSimulatedPlayer(
        name: str,
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
    ) -> LLSE_Player | None:
        """
        创建一个模拟玩家

        Args:
            name: 模拟玩家名称
            x: 生成模拟玩家的位置的 X 坐标
            y: 生成模拟玩家的位置的 Y 坐标
            z: 生成模拟玩家的位置的 Z 坐标
            dim_id: 生成模拟玩家的位置的 维度 ID

        Returns:
            生成的模拟玩家对象。如返回值为 `None` 则表示生成失败
        """
    @overload
    @staticmethod
    def explode(
        pos: T_PosType,
        source: LLSE_Entity | None,
        power: float,
        explode_range: float,
        is_destroy: bool,
        is_fire: bool,
    ) -> bool:
        """
        在指定位置制造一次爆炸

        Args:
            pos: 引发爆炸的位置坐标
            source: 设置爆炸来源的实体对象，可以为 `None`
            power: 爆炸的威力值，影响爆炸的伤害大小和破坏范围
            explode_range: 爆炸的范围半径，影响爆炸的波及范围
            is_destroy: 爆炸是否破坏方块
            is_fire: 爆炸结束后是否留下燃烧的火焰

        Returns:
            是否成功制造爆炸
        """
    @overload
    @staticmethod
    def explode(
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
        source: LLSE_Entity | None,
        power: float,
        explode_range: float,
        is_destroy: bool,
        is_fire: bool,
    ) -> bool:
        """
        在指定位置制造一次爆炸

        Args:
            x: 引发爆炸的位置的 X 坐标
            y: 引发爆炸的位置的 Y 坐标
            z: 引发爆炸的位置的 Z 坐标
            dim_id: 生成模拟玩家的位置的 维度 ID
            source: 设置爆炸来源的实体对象，可以为 `None`
            power: 爆炸的威力值，影响爆炸的伤害大小和破坏范围
            explode_range: 爆炸的范围半径，影响爆炸的波及范围
            is_destroy: 爆炸是否破坏方块
            is_fire: 爆炸结束后是否留下燃烧的火焰

        Returns:
            是否成功制造爆炸
        """
    @overload
    @staticmethod
    def getBlock(pos: IntPos) -> LLSE_Block | None:
        """
        通过方块坐标获取方块对象

        Args:
            pos: 方块所在坐标

        Returns:
            生成的方块对象。如返回值为 `None` 则表示获取方块失败
        """
    @overload
    @staticmethod
    def getBlock(x: int, y: int, z: int, dim_id: T_DimID) -> LLSE_Block | None:
        """
        通过方块坐标获取方块对象

        Args:
            x: 方块所在 X 坐标
            y: 方块所在 Y 坐标
            z: 方块所在 Z 坐标
            dim_id: 方块所在 维度 ID

        Returns:
            生成的方块对象。如返回值为 `None` 则表示获取方块失败
        """
    @overload
    @staticmethod
    def setBlock(
        pos: IntPos,
        block: LLSE_Block | str | NbtCompound,
        tiledata: int = 0,
    ) -> bool:
        """
        设置指定位置的方块

        Args:
            pos: 目标方块位置
            block: 要设置成的方块对象、方块标准类型名（如 `minecraft:stone`）或 方块NBT数据
            tiledata: 方块状态值，同原版 /setblock 指令的 `tiledata`，仅通过方块类型名放置方块时有效

        Returns:
            是否成功设置
        """
    @overload
    @staticmethod
    def setBlock(
        x: int,
        y: int,
        z: int,
        dim_id: T_DimID,
        pos: IntPos,
        block: LLSE_Block | str | NbtCompound,
        tiledata: int = 0,
    ) -> bool:
        """
        设置指定位置的方块

        Args:
            x: 方块所在 X 坐标
            y: 方块所在 Y 坐标
            z: 方块所在 Z 坐标
            dim_id: 方块所在 维度 ID
            block: 要设置成的方块对象、方块标准类型名（如 `minecraft:stone`）或 方块NBT数据
            tiledata: 方块状态值，同原版 /setblock 指令的 `tiledata`，仅通过方块类型名放置方块时有效

        Returns:
            是否成功设置
        """
    @overload
    @staticmethod
    def spawnParticle(pos: T_PosType, dim_id: T_DimID, particle_type: str) -> bool:
        """
        在指定位置生成粒子效果

        Args:
            pos: 目标生成位置
            dim_id: 目标生成位置 维度 ID
            particle_type: 要生成的粒子效果名称

        Returns:
            是否成功生成
        """
    @overload
    @staticmethod
    def spawnParticle(
        x: T_Number,
        y: T_Number,
        z: T_Number,
        dim_id: T_DimID,
        particle_type: str,
    ) -> bool:
        """
        在指定位置生成粒子效果

        Args:
            x: 目标生成位置 X 坐标
            y: 目标生成位置 Y 坐标
            z: 目标生成位置 Z 坐标
            dim_id: 目标生成位置 维度 ID
            particle_type: 要生成的粒子效果名称

        Returns:
            是否成功生成
        """
    @staticmethod
    def newSimpleForm() -> LLSE_SimpleForm:
        """
        创建普通表单构建器对象

        Returns:
            新创建的普通表单构建器对象
        """
    @staticmethod
    def newCustomForm() -> LLSE_CustomForm:
        """
        创建自定义表单构建器对象

        Returns:
            新创建的自定义表单构建器对象
        """
    @staticmethod
    def setMotd(motd: str) -> bool:
        """
        设置服务器MOTD字符串

        Args:
            motd: 目标 MOTD 字符串

        Returns:
            是否设置成功
        """
    @staticmethod
    def setMaxPlayers(num: int) -> bool:
        """
        设置服务器最大玩家数

        Args:
            num: 最大玩家数

        Returns:
            是否设置成功
        """
    @staticmethod
    def sendCmdOutput(output: str) -> bool:
        """
        模拟产生一个控制台命令输出

        Args:
            output: 模拟产生的命令输出

        Returns:
            是否成功执行
        """
    @staticmethod
    def newIntPos(x: int, y: int, z: int, dim_id: T_DimID) -> IntPos:
        """
        生成一个整数坐标对象

        Args:
            x: X 坐标
            y: Y 坐标
            z: Z 坐标
            dim_id: 维度 ID

        Returns:
            一个整数坐标对象
        """
    @staticmethod
    def newFloatPos(x: float, y: float, z: float, dim_id: T_DimID) -> FloatPos:
        """
        生成一个浮点数坐标对象

        Args:
            x: X 坐标
            y: Y 坐标
            z: Z 坐标
            dim_id: 维度 ID

        Returns:
            一个浮点数坐标对象
        """
    @staticmethod
    def getDisplayObjective(slot: T_ScoreDisplaySlot) -> LLSE_Objective | None:
        """
        获取某个处于显示状态的计分项

        Args:
            slot: 待查询的显示槽位名称

        Returns:
            正在 `slot` 槽位显示的计分项。如果返回 `None`，则代表对应槽位未显示计分项
        """
    @staticmethod
    def clearDisplayObjective(slot: T_ScoreDisplaySlot) -> bool:
        """
        使计分项停止显示

        Args:
            slot: 显示槽位名称字符串

        Returns:
            是否清除成功
        """
    @staticmethod
    def getScoreObjective(name: str) -> LLSE_Objective | None:
        """
        获取某个已存在的计分项

        Args:
            name: 要获取的计分项名称

        Returns:
            对应的计分项对象。如果返回 `None`，则代表计分项不存在
        """
    @staticmethod
    def newScoreObjective(name: str, display_name: str) -> LLSE_Objective | None:
        """
        创建一个新的计分项

        Args:
            name: 计分项名称
            display_name: 计分项显示名称

        Returns:
            新增创建的计分项对象。如果返回 `None`，则代表创建失败
        """
    @staticmethod
    def removeScoreObjective(name: str) -> bool:
        """
        移除一个已存在的计分项

        此接口的作用类似命令 `/scoreboard objectives remove <name>`

        Args:
            name: 计分项名称

        Returns:
            是否移除成功
        """
    @staticmethod
    def getAllScoreObjectives() -> list[LLSE_Objective]:
        """
        获取所有计分项

        此接口的作用类似命令 `/scoreboard objectives list`

        Returns:
            计分板系统记录的所有计分项对象
        """
    @staticmethod
    def setStructure(
        nbt: NbtCompound,
        pos: IntPos,
        mirror: T_StructureMirrorType,
        rotation: T_StructRotationType,
    ) -> bool:
        """
        放置结构 NBT

        Args:
            nbt: NBT
            pos: 放置坐标
            mirror: 镜像模式
            rotation: 旋转角度

        Returns:
            是否成功
        """
    @staticmethod
    def getStructure(
        pos1: IntPos,
        pos2: IntPos,
        ignore_blocks: bool = False,
        ignore_entities: bool = False,
    ) -> NbtCompound:
        """
        获取结构 NBT

        Args:
            pos1: 对角坐标 1（与 `fill` 命令的 `from` 参数类似）
            pos2: 对角坐标 2（与 `fill` 命令的 `to` 参数类似）
            ignore_blocks: 忽略方块
            ignore_entities: 忽略实体

        Returns:
            NBT
        """
    @staticmethod
    def newParticleSpawner(
        display_radius: int,
        high_detail: bool,
        double_side: bool,
    ) -> ParticleSpawner:
        """
        生成一个粒子生成器对象

        Args:
            display_radius: 粒子显示半径
            high_detail: 需要高细节线条
            double_side: 需要双面粒子

        Returns:
            一个粒子生成器对象
        """
    @staticmethod
    def getPlayerNbt(uuid: str) -> NbtCompound:
        """
        获取玩家对应的 NBT 对象

        此 API 的好处是可以获取到离线玩家 NBT，无需玩家在线，无需玩家对象。

        Args:
            uuid: 玩家的 UUID

        Returns:
            玩家的 NBT 对象
        """
    @staticmethod
    def setPlayerNbt(uuid: str, nbt: NbtCompound) -> bool:
        """
        写入玩家对应的 NBT 对象

        此 API 的好处是可以操作离线玩家 NBT，无需玩家在线，无需玩家对象。

        Args:
            uuid: 玩家的 UUID
            nbt: NBT 对象

        Returns:
            是否成功写入
        """
    @staticmethod
    def setPlayerNbtTags(uuid: str, nbt: NbtCompound, tags: list[str]) -> bool:
        """
        覆盖玩家对应的 NBT 对象的特定 NbtTag

        此 API 的好处是可以操作离线玩家 NBT，无需玩家在线，无需玩家对象。

        Args:
            uuid: 玩家的 UUID
            nbt: NBT 对象
            tags: 需要覆盖的 NbtTag 列表

        Returns:
            是否成功覆盖对应的 Tag
        """
    @staticmethod
    def deletePlayerNbt(uuid: str) -> bool:
        """
        从存档中删除玩家对应的 NBT 对象的全部内容

        此 API 的好处是可以操作离线玩家 NBT，无需玩家在线，无需玩家对象。

        Args:
            uuid: 玩家的 UUID

        Returns:
            是否删除成功
        """
    @staticmethod
    def getPlayerScore(uuid: str, name: str) -> int:
        """
        获取玩家计分项的分数

        可查询离线玩家计分板

        Args:
            uuid: 玩家的 UUID
            name: 计分项名称

        Returns:
            计分板上的数值
        """
    @staticmethod
    def setPlayerScore(uuid: str, name: str, value: int) -> bool:
        """
        设置玩家计分项的分数

        可修改离线玩家计分板

        Args:
            uuid: 玩家的 UUID
            name: 计分项名称
            value: 要设置的数值

        Returns:
            是否设置成功
        """
    @staticmethod
    def addPlayerScore(uuid: str, name: str, value: int) -> bool:
        """
        增加玩家计分项的分数

        可修改离线玩家计分板

        Args:
            uuid: 玩家的 UUID
            name: 计分项名称
            value: 要增加的数值

        Returns:
            是否设置成功
        """
    @staticmethod
    def reducePlayerScore(uuid: str, name: str, value: int) -> bool:
        """
        减少玩家计分项的分数

        可修改离线玩家计分板

        Args:
            uuid: 玩家的 UUID
            name: 计分项名称
            value: 要减少的数值

        Returns:
            是否设置成功
        """
    @staticmethod
    def deletePlayerScore(uuid: str, name: str) -> bool:
        """
        移除玩家计分项的分数

        可修改离线玩家计分板

        Args:
            uuid: 玩家的 UUID
            name: 计分项名称

        Returns:
            是否设置成功
        """
    @staticmethod
    def getTime(time_id: T_TimeID) -> int:
        """
        获取服务器游戏时间

        Args:
            time_id: 想要查询的时间

        Returns:
            获取到的时间
        """
    @staticmethod
    def setTime(tick: int) -> bool:
        """
        设置服务器游戏时间

        Args:
            tick: 想要设置的时间

        Returns:
            是否设置成功
        """
    @staticmethod
    def getWeather() -> T_WeatherID:
        """
        获取服务器天气

        Returns:
            当前天气
        """
    @staticmethod
    def setWeather(weather_id: T_WeatherID) -> bool:
        """
        设置服务器天气

        Args:
            weather_id: 想要设置的天气

        Returns:
            是否设置成功
        """
    @deprecated("请使用 `mc.newCommand()`")
    @staticmethod
    def regPlayerCmd(
        cmd: str,
        description: str,
        callback: T_PlayerCmdCallback,
        level: Literal[0, 1, 2, 3] = 0,
    ) -> bool:
        """
        注册一个新的玩家假命令

        Callback Args:
            player (LLSE_Player): 执行命令的玩家对象
            args (list[str]): 目标命令后面的参数，按空格为分界分割

        Args:
            cmd: 待注册的命令
            description: 命令描述文本
            callback: 注册的这个命令被执行时，接口自动调用的回调函数
            level: 命令的注册等级，类似于 `PermType`

        Returns:
            是否成功注册
        """
    @deprecated("请使用 `mc.newCommand()`")
    @staticmethod
    def regConsoleCmd(cmd: str, description: str, callback: T_ConsoleCmdCallback):
        """
        注册一个新的控制台假命令

        Callback Args:
            args (list[str]): 目标命令后面的参数，按空格为分界分割

        Args:
            cmd: 待注册的命令
            description: 命令描述文本
            callback: 注册的这个命令被执行时，接口自动调用的回调函数

        Returns:
            是否成功注册
        """
    @deprecated("请使用 `mc.getAllScoreObjectives()`")
    @staticmethod
    def getAllScoreObjective() -> list[LLSE_Objective]: ...
    @deprecated("请使用 `mc.getDisplayObjective()`")
    @staticmethod
    def getDisplayObjectives(slot: T_ScoreDisplaySlot) -> LLSE_Objective | None: ...
    @deprecated("已弃用，仅 DEBUG 模式下有效")
    @staticmethod
    def crash() -> bool:
        """让 BDS 崩溃"""
