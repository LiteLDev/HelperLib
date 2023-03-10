declare class NbtEnd {
  constructor();

  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  getType():0

  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toString(space?: number): string;

  /**
   * 设置对象的数据
   * @param data 写入对应类型的数据
   */
  set(data: any): true;

  /**
   * 读取对象的数据
   * @returns 对象中储存的数据
   */
  get(): null;
}

declare class NbtByte {
  constructor(data?: number);

  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  getType():1

  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toString(space?: number): string;

  /**
   * 设置对象的数据
   * @param data 写入对应类型的数据
   */
  set(data: number): boolean;

  /**
   * 读取对象的数据
   * @returns 对象中储存的数据
   */
  get(): number;
}
declare class NbtShort {
  constructor(data?: number);

  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  getType():2

  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toString(space?: number): string;

  /**
   * 设置对象的数据
   * @param data 写入对应类型的数据
   */
  set(data: number): boolean;

  /**
   * 读取对象的数据
   * @returns 对象中储存的数据
   */
  get(): number;
}
declare class NbtInt {
  constructor(data?: number);

  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  getType():3

  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toString(space?: number): string;

  /**
   * 设置对象的数据
   * @param data 写入对应类型的数据
   */
  set(data: number): boolean;

  /**
   * 读取对象的数据
   * @returns 对象中储存的数据
   */
  get(): number;
}
declare class NbtLong {
  constructor(data?: number);

  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  getType():4

  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toString(space?: number): string;

  /**
   * 设置对象的数据
   * @param data 写入对应类型的数据
   */
  set(data: number): boolean;

  /**
   * 读取对象的数据
   * @returns 对象中储存的数据
   */
  get(): number;
}
declare class NbtFloat {
  constructor(data?: number);

  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  getType():5

  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toString(space?: number): string;

  /**
   * 设置对象的数据
   * @param data 写入对应类型的数据
   */
  set(data: number): boolean;

  /**
   * 读取对象的数据
   * @returns 对象中储存的数据
   */
  get(): number;
}
declare class NbtDouble {
  constructor(data?: number);

  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  getType():6

  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toString(space?: number): string;

  /**
   * 设置对象的数据
   * @param data 写入对应类型的数据
   */
  set(data: number): boolean;

  /**
   * 读取对象的数据
   * @returns 对象中储存的数据
   */
  get(): number;
}
declare class NbtByteArray {
  constructor(data?: ArrayBuffer);

  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  getType():7

  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toString(space?: number): string;

  /**
   * 设置对象的数据
   * @param data 写入对应类型的数据
   */
  set(data: ArrayBuffer): boolean;

  /**
   * 读取对象的数据
   * @returns 对象中储存的数据
   */
  get(): ArrayBuffer;
}
declare class NbtString {
  constructor(data?: string);

  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  getType():8

  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toString(space?: number): string;

  /**
   * 设置对象的数据
   * @param data 写入对应类型的数据
   */
  set(data: string): boolean;

  /**
   * 读取对象的数据
   * @returns 对象中储存的数据
   */
  get(): string;
}
