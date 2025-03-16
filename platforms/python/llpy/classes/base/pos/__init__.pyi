from typing import Generic, TypeVar

from ..types import T_DimID

_T_PyType = TypeVar("_T_PyType")

class _T_BasePos(Generic[_T_PyType]):
    def __init__(
        self,
        x: _T_PyType,
        y: _T_PyType,
        z: _T_PyType,
        dim_id: T_DimID,
    ) -> None:
        """
        生成一个坐标对象

        Args:
            x: X 坐标
            y: Y 坐标
            z: Z 坐标
            dim_id: 维度 ID
        """
    @property
    def x(self) -> _T_PyType:
        """X 坐标"""
    @x.setter
    def x(self, val: _T_PyType): ...
    @property
    def y(self) -> _T_PyType:
        """Y 坐标"""
    @y.setter
    def y(self, val: _T_PyType): ...
    @property
    def z(self) -> _T_PyType:
        """Z 坐标"""
    @z.setter
    def z(self, val: _T_PyType): ...
    @property
    def dim(self) -> str:
        """维度名称"""
    @property
    def dimid(self) -> T_DimID:
        """维度 ID。当某种情况下维度无效，或者无法获取时返回 `-1`"""
    @dimid.setter
    def dimid(self, val: T_DimID): ...
    def toString(self) -> str: ...

class IntPos(_T_BasePos[int]):
    """整数坐标对象"""

class FloatPos(_T_BasePos[float]):
    """浮点数坐标对象"""
