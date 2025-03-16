from typing import NoReturn, TypeVar, overload

_T_Str = TypeVar("_T_Str", bound=str)

class _T_EnumDefineClass:
    def __init__(self) -> NoReturn: ...

    keys: list[str]
    @overload
    @staticmethod
    def getName(value: _T_Str) -> _T_Str | None: ...
    @overload
    @staticmethod
    def getName(value: int) -> str | None: ...
