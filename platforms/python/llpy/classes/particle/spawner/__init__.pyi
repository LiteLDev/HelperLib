from typing import Literal, overload

from llpy import ParticleColor
from llpy.types import T_Number, T_PosType

from ..types import T_ParticleColor, T_ParticleNumber, T_ParticleSize, T_PosDirection

class ParticleSpawner:
    """粒子生成器对象"""

    def __init__(
        self,
        display_radius: int,
        high_detail: bool,
        double_side: bool,
    ) -> None:
        """
        生成一个粒子生成器对象

        Args:
            display_radius: 粒子显示半径
            high_detail: 需要高细节线条
            double_side: 需要双面粒子
        """
    @property
    def displayRadius(self) -> int:
        """粒子显示半径"""
    @property
    def highDetial(self) -> bool:
        """需要高细节线条"""
    @property
    def doubleSide(self) -> bool:
        """需要双面粒子"""
    @displayRadius.setter
    def displayRadius(self, val: int): ...
    @highDetial.setter
    def highDetial(self, val: bool): ...
    @doubleSide.setter
    def doubleSide(self, val: bool): ...
    def spawnParticle(self, pos: T_PosType, name: str) -> Literal[True]:
        """
        生成指定名称粒子

        Args:
            pos: 可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
            name: 粒子名称

        Returns:
            `True`
        """
    def drawPoint(
        self,
        pos: T_PosType,
        point_size: T_ParticleSize = 4,
        color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        生成点粒子

        Args:
            pos: 可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
            point_size: 粒子大小
            color: 粒子颜色。应当使用 `ParticleColor` 枚举填充

        Returns:
            `True`
        """
    def drawNumber(
        self,
        pos: T_PosType,
        num: T_ParticleNumber,
        color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        生成数字粒子

        Args:
            pos: 可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
            num: 粒子内容
            color: 粒子颜色。应当使用 `ParticleColor` 枚举填充

        Returns:
            `True`
        """
    def drawAxialLine(
        self,
        pos: T_PosType,
        direction: T_PosDirection,
        length: T_Number,
        color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        生成轴向线段

        Args:
            pos: 线段起点。可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
            direction: 线段方向。应当使用 `Direction` 枚举填充
            length: 线段长度
            color: 粒子颜色。应当使用 `ParticleColor` 枚举填充

        Returns:
            `True`
        """
    def drawOrientedLine(
        self,
        start: T_PosType,
        end: T_PosType,
        line_width: T_ParticleSize = 4,
        min_spacing: T_Number = 1,
        max_particles_num: int = 64,
        color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        生成有向线段

        Args:
            start: 线段起点。可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
            end: 线段终点。可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
            line_width: 线段宽度
            min_spacing: 线段点最小间隔
            max_particles_num: 线段最大粒子数，达到后会自动增加间隔
            color: 粒子颜色。应当使用 `ParticleColor` 枚举填充

        Returns:
            `True`
        """
    @overload
    def drawCuboid(
        self,
        pos: T_PosType,
        color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        生成立方体

        画出 1×1×1 大小的立方体

        Args:
            pos: 可以是浮点坐标或者整数坐标, 整数坐标会取方块角落底部位置
            color: 粒子颜色。应当使用 `ParticleColor` 枚举填充

        Returns:
            `True`
        """
    @overload
    def drawCuboid(
        self,
        pos: T_PosType,
        pos2: T_PosType,
        color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        生成立方体

        画出从最小角落 `pos` 到最大角落 `pos2` 的立方体

        Args:
            pos: 可以是浮点坐标或者整数坐标, 整数坐标会取方块角落底部位置
            pos2: 可以是浮点坐标或者整数坐标, 整数坐标会取方块角落顶端位置
            color: 粒子颜色。应当使用 `ParticleColor` 枚举填充

        Returns:
            `True`
        """
    def drawCircle(
        self,
        pos: T_PosType,
        facing: T_PosDirection,
        radius: T_Number,
        line_width: T_ParticleSize = 4,
        min_spacing: T_Number = 1,
        max_particles_num: int = 64,
        color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        生成圆

        Args:
            pos: 圆心。可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
            facing: 朝向。应当使用 `Direction` 枚举填充
            radius: 半径
            line_width: 圆线段宽度
            min_spacing: 圆线段点最小间隔
            max_particles_num: 圆最大粒子数，达到后会自动增加间隔
            color: 粒子颜色。应当使用 `ParticleColor` 枚举填充

        Returns:
            `True`
        """
