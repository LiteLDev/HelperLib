from typing import Literal

T_FileOpenModeRead = Literal[0]
T_FileOpenModeWrite = Literal[1]
T_FileOpenModeAppend = Literal[2]
T_FileOpenMode = T_FileOpenModeRead | T_FileOpenModeWrite | T_FileOpenModeAppend
