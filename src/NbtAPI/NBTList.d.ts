/// <reference path="../index.d.ts" />

declare class NbtList{
  constructor(data?: Array<NbtType>);

  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  getType():9

  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toString(space?: number): string;
    
  /**
   * 获取列表长度
   * @returns Integer 此列表的长度
   */
  getSize(): number;

  /**
   * 获取某个下标位置储存的数据类型
   * @param index 要查询的目标下标
   * @returns NBT.enum 此下标处储存的NBT的数据类型
   */
  getTypeOf(index: number): NBT;

  /**
   * 设置某个下标位置的NBT对象
   * @param index 要操作的目标下标
   * @param tag 要写入的 NBT 对象
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setTag(index: number, tag: NbtType): NbtList;

  /**
   * 读取某个下标位置的NBT对象
   * @param index 要操作的目标下标
   * @returns NbtType|null NBT对象
   */
  getTag(index: number): NbtType | null;

  /**
   * 往列表末尾追加一个NBT对象
   * @param tag 要追加的 NBT 对象
   * @returns NbtList 追加完毕的NBT列表（便于连锁进行其他操作）
   */
  addTag(tag: NbtType): NbtList;

  /**
   * 删除某个下标位置的NBT对象
   * @param index 要删除的目标下标
   * @returns NbtList 处理完毕的NBT列表（便于连锁进行其他操作）
   */
  removeTag(index: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setEnd(index: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setByte(index: number, data: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setShort(index: number, data: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setInt(index: number, data: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setLong(index: number, data: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setFloat(index: number, data: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setDouble(index: number, data: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setByteBuffer(index: number, data: ByteBuffer): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setString(index: number, data: string): NbtList;

  /**
   * 读取某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @returns Any|NbtList|NbtCompound|null 键对应的值的具体数据
   */
  getData(index: number): any | NbtList | NbtCompound | null;

  /**
   * 将List类型转换为Array
   * @returns Array<any> 对应的数组/列表
   */
  toArray(): Array<any>;
}
