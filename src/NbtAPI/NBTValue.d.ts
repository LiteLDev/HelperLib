declare type NbtType =
  | NbtEnd
  | NbtByte
  | NbtShort
  | NbtInt
  | NbtLong
  | NbtFloat
  | NbtDouble
  | NbtByteArray
  | NbtString;

declare class NbtEnd {}
declare class NbtByte {
  constructor(data?: number);
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
