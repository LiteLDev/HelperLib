/// <reference path="../index.d.ts" />

declare class NBT {
  // enum
  static readonly End = 0

  static readonly Byte = 1

  static readonly Short = 2

  static readonly Int = 3

  static readonly Long = 4

  static readonly Float = 5

  static readonly Double = 6

  static readonly ByteArray = 7

  static readonly String = 8

  static readonly List = 9

  static readonly Compound = 10

  /**
   * 从 SNBT  字符串生成 NBT 标签对象
   * @param snbt 你要解析的SNBT字符串
   * @returns NbtCompound 生成的NBT对象
   */
  static parseSNBT(snbt: string): NbtCompound | null;

  /**
   * 从二进制 NBT 数据生成 NBT 标签对象
   * @param nbt 你要解析的二进制 NBT 数据
   * @returns NbtCompound 生成的NBT对象
   */
  static parseBinaryNBT(nbt: ArrayBuffer): NbtCompound | null;

  /** @deprecated */
  static newTag(arg:NbtEnum):NbtType

  /** @deprecated */
  static createTag(arg:NbtEnum):NbtType
}


declare type NbtType =
  | NbtEnd
  | NbtByte
  | NbtShort
  | NbtInt
  | NbtLong
  | NbtFloat
  | NbtDouble
  | NbtByteArray
  | NbtString
  | NbtList
  | NbtCompound;
declare type NbtValue = 
  | NbtEnd
  | NbtByte
  | NbtShort
  | NbtInt
  | NbtLong
  | NbtFloat
  | NbtDouble
  | NbtByteArray
  | NbtString;

declare type NbtEnum = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10