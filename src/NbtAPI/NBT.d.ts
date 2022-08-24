/// <reference path="../index.d.ts" />

declare enum NBT {
  End,
  Byt,
  Short,
  Int,
  Long,
  Float,
  Double,
  ByteArray,
  String,
  List,
  Compound,
}

declare class nbt {
  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  static getType(): NBT;
  
  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  static toString(space?:Integer):string;

  /**
   * 从 SNBT  字符串生成 NBT 标签对象
   * @param snbt 你要解析的SNBT字符串
   * @returns NbtCompound 生成的NBT对象
   */
  static parseSNBT(snbt:string):NbtCompound|null;

  /**
   * 从二进制 NBT 数据生成 NBT 标签对象
   * @param nbt 你要解析的二进制 NBT 数据
   * @returns NbtCompound 生成的NBT对象
   */
  static parseBinaryNBT(nbt:ArrayBuffer):NbtCompound|null;

  /**
   * 将 NBT 标签对象 序列化为SNBT
   * @param space （可选参数）缩进空格
   */
  static toSNBT(space?:Integer):string;
}
