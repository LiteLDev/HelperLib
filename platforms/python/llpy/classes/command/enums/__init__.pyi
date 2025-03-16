from llpy.classes.base.enumdefine import _T_EnumDefineClass

from ..types import (
    T_OriginTypeActor,
    T_OriginTypeActorServer,
    T_OriginTypeAutomationPlayer,
    T_OriginTypeBlock,
    T_OriginTypeClientAutomation,
    T_OriginTypeDevConsole,
    T_OriginTypeExecuteContext,
    T_OriginTypeGameArgument,
    T_OriginTypeGameDirectorEntity,
    T_OriginTypeMinecartBlock,
    T_OriginTypePlayer,
    T_OriginTypePrecompiled,
    T_OriginTypeScript,
    T_OriginTypeServer,
    T_OriginTypeTest,
    T_OriginTypeVirtual,
    T_ParamOptionEnumAsChainedCommand,
    T_ParamOptionEnumAutocompleteExpansion,
    T_ParamOptionHasSemanticConstraint,
    T_ParamOptionNone,
    T_ParamTypeActor,
    T_ParamTypeActorType,
    T_ParamTypeBlock,
    T_ParamTypeBlockPos,
    T_ParamTypeBool,
    T_ParamTypeCommand,
    T_ParamTypeEffect,
    T_ParamTypeEnum,
    T_ParamTypeFloat,
    T_ParamTypeInt,
    T_ParamTypeItem,
    T_ParamTypeJsonValue,
    T_ParamTypeMessage,
    T_ParamTypePlayer,
    T_ParamTypeRawText,
    T_ParamTypeSoftEnum,
    T_ParamTypeString,
    T_ParamTypeVec3,
    T_ParamTypeWildcardSelector,
    T_PermTypeAdmin,
    T_PermTypeAny,
    T_PermTypeConsole,
    T_PermTypeGameMasters,
    T_PermTypeHostPlayer,
    T_PermTypeInternal,
)

class PermType(_T_EnumDefineClass):
    """命令权限枚举"""

    Any: T_PermTypeAny
    """命令权限枚举 | 所有人"""
    GameMasters: T_PermTypeGameMasters
    """命令权限枚举 | OP"""
    Admin: T_PermTypeAdmin
    """命令权限枚举 | ？"""
    HostPlayer: T_PermTypeHostPlayer
    """命令权限枚举 | ？"""
    Console: T_PermTypeConsole
    """命令权限枚举 | 控制台"""
    Internal: T_PermTypeInternal
    """命令权限枚举 | ？"""

class ParamType(_T_EnumDefineClass):
    """命令参数类型枚举"""

    Bool: T_ParamTypeBool
    """命令参数类型枚举 | 布尔值 (`bool`)"""
    Int: T_ParamTypeInt
    """命令参数类型枚举 | 整数 (`int`)"""
    Float: T_ParamTypeFloat
    """命令参数类型枚举 | 浮点数 (`float`)"""
    String: T_ParamTypeString
    """命令参数类型枚举 | 字符串 (`str`)"""
    Actor: T_ParamTypeActor
    """命令参数类型枚举 | 实体目标选择器 (`list[LLSE_Entity]`)"""
    Player: T_ParamTypePlayer
    """命令参数类型枚举 | 玩家目标选择器 (`list[LLSE_Player]`)"""
    BlockPos: T_ParamTypeBlockPos
    """命令参数类型枚举 | 整数坐标对象 (`IntPos`)"""
    Vec3: T_ParamTypeVec3
    """命令参数类型枚举 | 浮点数坐标对象 (`FloatPos`)"""
    RawText: T_ParamTypeRawText
    """命令参数类型枚举 | 原始字符串（只能作为最后一个参数）(`str`)"""
    Message: T_ParamTypeMessage
    """命令参数类型枚举 | 消息类型字符串（会自动展开目标选择器）(`str`)"""
    JsonValue: T_ParamTypeJsonValue
    """命令参数类型枚举 | JSON 字符串 (`str`)"""
    Item: T_ParamTypeItem
    """命令参数类型枚举 | 物品 (`LLSE_Item`)"""
    Block: T_ParamTypeBlock
    """命令参数类型枚举 | 方块 (`LLSE_Block`)"""
    Effect: T_ParamTypeEffect
    """命令参数类型枚举 | 效果类型字符串 (`str`)"""
    Enum: T_ParamTypeEnum
    """命令参数类型枚举 | 枚举字符串 (`str`)"""
    SoftEnum: T_ParamTypeSoftEnum
    """命令参数类型枚举 | 可变枚举字符串 (`str`)"""
    ActorType: T_ParamTypeActorType
    """命令参数类型枚举 | 实体类型字符串 (`str`)"""
    Command: T_ParamTypeCommand
    """命令参数类型枚举 | 指令名称（仅供测试）(`str`)"""
    WildcardSelector: T_ParamTypeWildcardSelector
    """命令参数类型枚举 | ？(`None`)"""

class ParamOption(_T_EnumDefineClass):
    """命令参数选项枚举"""

    None_: T_ParamOptionNone
    """
    命令参数选项枚举 | 无

    （由于 Python 保留字，请使用 0 代替或不填）
    """
    EnumAutocompleteExpansion: T_ParamOptionEnumAutocompleteExpansion
    """命令参数选项枚举 | 展开枚举选项"""
    HasSemanticConstraint: T_ParamOptionHasSemanticConstraint
    """命令参数选项枚举 | ？"""
    EnumAsChainedCommand: T_ParamOptionEnumAsChainedCommand
    """命令参数选项枚举 | ？"""

class OriginType(_T_EnumDefineClass):
    """指令执行主体类型枚举"""

    Player: T_OriginTypePlayer
    Block: T_OriginTypeBlock
    MinecartBlock: T_OriginTypeMinecartBlock
    DevConsole: T_OriginTypeDevConsole
    Test: T_OriginTypeTest
    AutomationPlayer: T_OriginTypeAutomationPlayer
    ClientAutomation: T_OriginTypeClientAutomation
    Server: T_OriginTypeServer
    DedicatedServer: T_OriginTypeServer
    Actor: T_OriginTypeActor
    Virtual: T_OriginTypeVirtual
    GameArgument: T_OriginTypeGameArgument
    ActorServer: T_OriginTypeActorServer
    Precompiled: T_OriginTypePrecompiled
    GameDirectorEntity: T_OriginTypeGameDirectorEntity
    Script: T_OriginTypeScript
    ExecuteContext: T_OriginTypeExecuteContext
