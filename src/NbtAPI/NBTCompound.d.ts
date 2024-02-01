/// <reference path="../index.d.ts" />

declare class NbtCompound{
  constructor(data?: object);

  /**
   * 获取NBT对象储存的数据类型
   * @returns NBT.enum 此NBT对象储存的数据类型
   */
  getType():10

  /**
   * 将NBT对象转换为Json字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toString(space?: number): string;

  /**
   * 获取所有的键
   * @returns Array<string> Compound 中所有的键
   */
  getKeys(): Array<string>;

  /**
   * 获取键对应的值的数据类型
   * @param key 要查询的键名
   * @returns NBT.enum 对应的值的数据类型
   */
  getTypeOf(key: string): NBT;

  /**
   * 设置键对应的 NBT 对象
   * @param key 要操作的键名
   * @param tag 要写入的 NBT 对象（它承载着具体的NBT数据）
   * @returns boolean 是否写入成功
   */
  setTag(key: string, tag: NbtType): boolean;

  /**
   * 读取键对应的 NBT 对象
   * @param key 要操作的键名
   * @returns NbtObject|Null 键对应的NBT对象
   */
  getTag(key: string): NbtType | null;

  /**
   * 删除键对应的 NBT 对象
   * @param key 要操作的键名。键名必须已经存在
   * @returns NbtCompound 处理完毕的NBT对象（便于连锁进行其他操作）
   */
  removeTag(key: string): NbtCompound;

  /**
   * 设置键对应的值的具体数据
   * @param key 要操作的键名
   * @returns NbtCompound 处理完毕的NBT对象（便于连锁进行其他操作）
   */
  setEnd(key: string): NbtCompound;

  /**
   * 设置键对应的值的具体数据
   * @param key 要操作的键名
   * @param data 要写入的具体数据
   * @returns NbtCompound 处理完毕的NBT对象（便于连锁进行其他操作）
   */
  setByte(key: string, data: number): NbtCompound;

  /**
   * 设置键对应的值的具体数据
   * @param key 要操作的键名
   * @param data 要写入的具体数据
   * @returns NbtCompound 处理完毕的NBT对象（便于连锁进行其他操作）
   */
  setShort(key: string, data: number): NbtCompound;

  /**
   * 设置键对应的值的具体数据
   * @param key 要操作的键名
   * @param data 要写入的具体数据
   * @returns NbtCompound 处理完毕的NBT对象（便于连锁进行其他操作）
   */
  setInt(key: string, data: number): NbtCompound;

  /**
   * 设置键对应的值的具体数据
   * @param key 要操作的键名
   * @param data 要写入的具体数据
   * @returns NbtCompound 处理完毕的NBT对象（便于连锁进行其他操作）
   */
  setLong(key: string, data: number): NbtCompound;

  /**
   * 设置键对应的值的具体数据
   * @param key 要操作的键名
   * @param data 要写入的具体数据
   * @returns NbtCompound 处理完毕的NBT对象（便于连锁进行其他操作）
   */
  setFloat(key: string, data: number): NbtCompound;

  /**
   * 设置键对应的值的具体数据
   * @param key 要操作的键名
   * @param data 要写入的具体数据
   * @returns NbtCompound 处理完毕的NBT对象（便于连锁进行其他操作）
   */
  setDouble(key: string, data: number): NbtCompound;

  /**
   * 设置键对应的值的具体数据
   * @param key 要操作的键名
   * @param data 要写入的具体数据
   * @returns NbtCompound 处理完毕的NBT对象（便于连锁进行其他操作）
   */
  setByteArray(key: string, data: ByteBuffer): NbtCompound;

  /**
   * 设置键对应的值的具体数据
   * @param key 要操作的键名
   * @param data 要写入的具体数据
   * @returns NbtCompound 处理完毕的NBT对象（便于连锁进行其他操作）
   */
  setString(key: string, data: string): NbtCompound;

  /**
   * 读取键对应的值的具体数据
   * @param key 要操作的键名
   * @returns Any|NbtList|NbtCompound|null 键对应的值的具体数据
   */
  getData(key: string): any | NbtList | NbtCompound | null;

  /**
   * 将 NBT 标签对象 转换为Object
   * @returns Object 对应的对象/表
   */
  toObject(): any;

  /**
   * 将 NBT 标签对象 序列化为二进制NBT
   * @returns ByteBuffer 对应的二进制NBT数据
   */
  toBinaryNBT(): ByteBuffer;

  /**
   * 将NBT对象转换为SNBT字符串
   * @param space （可选参数）如果要格式化输出的字符串，则传入此参数  
   */
  toSNBT(space?:number):string

  /**
   * 销毁此 NBT 标签对象
   * @returns boolean 是否成功清理
   */
  destroy(): boolean;
}
