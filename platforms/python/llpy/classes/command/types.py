from typing import Any, Callable, Literal

from llpy import FloatPos, IntPos, LLSE_Block, LLSE_Entity, LLSE_Item, LLSE_Player

from . import LLSE_Command
from .origin import LLSE_CommandOrigin
from .output import LLSE_CommandOutput

T_ParamTypeBool = Literal[0]
T_ParamTypeInt = Literal[1]
T_ParamTypeFloat = Literal[2]
T_ParamTypeString = Literal[3]
T_ParamTypeActor = Literal[4]
T_ParamTypePlayer = Literal[5]
T_ParamTypeBlockPos = Literal[6]
T_ParamTypeVec3 = Literal[7]
T_ParamTypeRawText = Literal[8]
T_ParamTypeMessage = Literal[9]
T_ParamTypeJsonValue = Literal[10]
T_ParamTypeItem = Literal[11]
T_ParamTypeBlock = Literal[12]
T_ParamTypeEffect = Literal[13]
T_ParamTypeEnum = Literal[14]
T_ParamTypeSoftEnum = Literal[15]
T_ParamTypeActorType = Literal[16]
T_ParamTypeCommand = Literal[17]
T_ParamTypeWildcardSelector = Literal[18]
T_ParamType = (
    T_ParamTypeBool
    | T_ParamTypeInt
    | T_ParamTypeFloat
    | T_ParamTypeString
    | T_ParamTypeActor
    | T_ParamTypePlayer
    | T_ParamTypeBlockPos
    | T_ParamTypeVec3
    | T_ParamTypeRawText
    | T_ParamTypeMessage
    | T_ParamTypeJsonValue
    | T_ParamTypeItem
    | T_ParamTypeBlock
    | T_ParamTypeEffect
    | T_ParamTypeEnum
    | T_ParamTypeSoftEnum
    | T_ParamTypeActorType
    | T_ParamTypeCommand
    | T_ParamTypeWildcardSelector
)

T_PermTypeAny = Literal[0]
T_PermTypeGameMasters = Literal[1]
T_PermTypeAdmin = Literal[2]
T_PermTypeHostPlayer = Literal[3]
T_PermTypeConsole = Literal[4]
T_PermTypeInternal = Literal[5]
T_PermType = (
    T_PermTypeAny
    | T_PermTypeGameMasters
    | T_PermTypeAdmin
    | T_PermTypeHostPlayer
    | T_PermTypeConsole
    | T_PermTypeInternal
)

T_ParamOptionNone = Literal[0]
T_ParamOptionEnumAutocompleteExpansion = Literal[1]
T_ParamOptionHasSemanticConstraint = Literal[2]
T_ParamOptionEnumAsChainedCommand = Literal[4]
T_ParamOption = (
    T_ParamOptionNone
    | T_ParamOptionEnumAutocompleteExpansion
    | T_ParamOptionHasSemanticConstraint
    | T_ParamOptionEnumAsChainedCommand
)

T_OriginTypePlayer = Literal[0]
T_OriginTypeBlock = Literal[1]
T_OriginTypeMinecartBlock = Literal[2]
T_OriginTypeDevConsole = Literal[3]
T_OriginTypeTest = Literal[4]
T_OriginTypeAutomationPlayer = Literal[5]
T_OriginTypeClientAutomation = Literal[6]
T_OriginTypeServer = Literal[7]
T_OriginTypeActor = Literal[8]
T_OriginTypeVirtual = Literal[9]
T_OriginTypeGameArgument = Literal[10]
T_OriginTypeActorServer = Literal[11]
T_OriginTypePrecompiled = Literal[12]
T_OriginTypeGameDirectorEntity = Literal[13]
T_OriginTypeScript = Literal[14]
T_OriginTypeExecuteContext = Literal[15]
T_OriginType = (
    T_OriginTypePlayer
    | T_OriginTypeBlock
    | T_OriginTypeMinecartBlock
    | T_OriginTypeDevConsole
    | T_OriginTypeTest
    | T_OriginTypeAutomationPlayer
    | T_OriginTypeClientAutomation
    | T_OriginTypeServer
    | T_OriginTypeActor
    | T_OriginTypeVirtual
    | T_OriginTypeGameArgument
    | T_OriginTypeActorServer
    | T_OriginTypePrecompiled
    | T_OriginTypeGameDirectorEntity
    | T_OriginTypeScript
    | T_OriginTypeExecuteContext
)

T_CommandCallbackResult = (
    bool
    | int
    | float
    | str
    | list[LLSE_Entity]
    | list[LLSE_Player]
    | IntPos
    | FloatPos
    | LLSE_Item
    | LLSE_Block
)
T_CommandCallback = Callable[
    [LLSE_Command, LLSE_CommandOrigin, LLSE_CommandOutput, dict[str, Any]],
    bool,
]
