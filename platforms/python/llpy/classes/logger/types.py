from typing import Literal

T_LogLevel = Literal[0, 1, 2, 3, 4, 5]
"""
日志输出等级

- 0. 不输出任何日志 (`Slient`)
- 1. 仅输出 严重错误信息 (`Fatal`)
- 2. 输出 严重错误、错误信息 (`Error`)
- 3. 输出 严重错误、错误、警告信息 (`Warn`)
- 4. 输出 严重错误、错误、警告、提示信息 (`Info`)
- 5. 输出 严重错误、错误、警告、提示 和 调试信息 (`Debug`)
"""
