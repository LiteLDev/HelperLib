/// <reference path="../index.d.ts" />

declare class NbtList {
  constructor(data?: Array<NbtType>);

  /**
   * 获取列表长度
   * @returns Integer 此列表的长度
   */
  getSize(): Integer;

  /**
   * 获取某个下标位置储存的数据类型
   * @param index 要查询的目标下标
   * @returns NBT.enum 此下标处储存的NBT的数据类型
   */
  getTypeOf(index: Integer): NBT;

  /**
   * 设置某个下标位置的NBT对象
   * @param index 要操作的目标下标
   * @param tag 要写入的 NBT 对象
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setTag(index: Integer, tag: NbtType): NbtList;

  /**
   * 读取某个下标位置的NBT对象
   * @param index 要操作的目标下标
   * @returns NbtType|null NBT对象
   */
  getTag(index: Integer): NbtType | null;

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
  removeTag(index: Integer): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setEnd(index: Integer): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setByte(index: Integer, data: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setShort(index: Integer, data: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setInt(index: Integer, data: Integer): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setLong(index: Integer, data: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setFloat(index: Integer, data: Number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setDouble(index: Integer, data: number): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setByteBuffer(index: Integer, data: ByteBuffer): NbtList;

  /**
   * 设置某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @param data 要写入的具体数据
   * @returns NbtList 写入完毕的NBT列表（便于连锁进行其他操作）
   */
  setString(index: Integer, data: string): NbtList;

  /**
   * 读取某个下标位置的具体数据
   * @param index 要操作的目标下标
   * @returns Any|NbtList|NbtCompound|null 键对应的值的具体数据
   */
  getData(index: Integer): any | NbtList | NbtCompound | null;

  /**
   * 将List类型转换为Array
   * @returns Array<any> 对应的数组/列表
   */
  toArray(): Array<any>;
}
