from typing import Any, Callable, Literal, TypeVar, overload

from .types import T_LogColorName

def log(*args: Any) -> None:
    """
    输出信息到控制台

    Args:
        args: 待输出的变量或者数据。可以是任意类型，参数数量可以是任意个
    """

def colorLog(color: T_LogColorName, *args: Any) -> None:
    """
    输出带颜色文本

    Args:
        color: 此行输出的颜色
        args: 待输出的变量或者数据。可以是任意类型，参数数量可以是任意个
    """

def fastLog(*args: Any) -> None:
    """
    异步输出信息到控制台

    此函数将输出请求发出后即刻返回，避免同步读写造成的阻塞时间。底层有锁保护，不同的 `fastLog` 之间不会出现串字符现象

    Args:
        args: 待输出的变量或者数据。可以是任意类型，参数数量可以是任意个
    """

@overload
def setTimeout(func: Callable[[], Any], ms: int) -> int | None:
    """
    推迟一段时间执行函数

    Args:
        func: 待执行的函数
        ms: 推迟执行的时间（毫秒）

    Returns:
        此任务ID。如果返回 `None`，则代表创建任务失败
    """

@overload
def setTimeout(func: str, ms: int) -> int | None:
    """
    推迟一段时间执行代码段（eval）

    Args:
        func: 待执行的代码段
        ms: 推迟执行的时间（毫秒）

    Returns:
        此任务ID。如果返回 `None`，则代表创建任务失败
    """

@overload
def setInterval(func: Callable[[], Any] | str, ms: int) -> int:
    """
    设置周期执行函数

    Args:
        func: 待执行的函数
        ms: 执行间隔周期（毫秒）

    Returns:
        此任务ID
    """

@overload
def setInterval(func: str, ms: int) -> int | None:
    """
    设置周期执行代码段（eval）

    Args:
        func: 待执行的代码段
        ms: 执行间隔周期（毫秒）

    Returns:
        此任务ID。如果返回 `None`，则代表创建任务失败
    """

def clearInterval(task_id: int) -> bool | None:
    """
    取消延时 / 周期执行项

    Args:
        task_id: 由 `setTimeout` / `setInterval` 返回的任务ID

    Returns:
        是否取消成功。如果返回Null，则代表取消任务失败
    """

_T_Listener = TypeVar("_T_Listener", bound=Callable[..., Literal[False] | Any])

# BaseLib.py
def handle(event: str) -> Callable[[_T_Listener], _T_Listener]:
    """
    监听事件函数装饰器

    来源：`BaseLib.py`

    用法：

    ```py
    @handle("onJoin")
    def _(player: LLSE_Player):
        log(f"{player.realName} joined the game!")
    ```

    Args:
        event: 要监听的事件名称
    """
