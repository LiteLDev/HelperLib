from typing import NoReturn

class LLSE_Device:
    """玩家设备信息对象"""

    def __init__(self) -> NoReturn: ...
    @property
    def ip(self) -> str:
        """玩家设备的 IP 地址与端口（格式：`114.51.45.191:9810`）"""
    @property
    def avgPing(self) -> int:
        """玩家的平均网络延迟时间（ms）"""
    @property
    def avgPacketLoss(self) -> float:
        """玩家的平均网络丢包率（%）"""
    @property
    def lastPing(self) -> int:
        """玩家的网络延迟时间（ms）"""
    @property
    def lastPacketLoss(self) -> float:
        """玩家的网络丢包率（%）"""
    @property
    def os(self) -> str:
        """
        玩家设备的操作系统类型

        可能返回的值如下

        - `Android` | 手机谷歌Android
        - `iOS` | 手机苹果iOS/平板iPadOS
        - `OSX` | 电脑苹果macOS
        - `Amazon` | 平板/电视亚马逊FireOS
        - `GearVR` | 头显三星GearVR
        - `Hololens` | 头显微软HoloLens
        - `Windows10` | 电脑微软Windows
        - `Win32` | 电脑微软Win32（教育版？）
        - `TVOS` | 机顶盒苹果tvOS
        - `PlayStation` | 主机索尼PlayStation
        - `Nintendo` | 掌机任天堂Switch
        - `Xbox` | 主机微软Xbox
        - `WindowsPhone` | 手机微软Windows Mobile
        - `Unknown` | 未知系统
        """
    @property
    def inputMode(self) -> int:
        """
        玩家的操作模式

        - 1. 鼠标 (`Mouse`)
        - 2. 触控 (`Touch`)
        - 3. 手柄 (`GamePad`)
        - 4. 动作控制器 (`MotionController`)
        """
    @property
    def playMode(self) -> int:
        """
        玩家的游玩模式

        （由 GPT-3.5 翻译）

        - 0. 普通模式 (`Normal`)
        - 1. 引导模式 (`Teaser`)
        - 2. 屏幕模式 (`Screen`)
        - 3. 查看模式 (`Viewer`)
        - 4. 虚拟现实模式 (`VR`)
        - 5. 布置模式 (`Placement`)
        - 6. 客厅模式 (`LivingRoom`)
        - 7. 退出关卡 (`ExitLevel`)
        - 8. 退出关卡客厅 (`ExitLevelLivingRoom`)
        """
    @property
    def serverAddress(self) -> str:
        """玩家连接的地址"""
    @property
    def clientId(self) -> str:
        """玩家客户端的识别码 ID"""

Device = LLSE_Device
