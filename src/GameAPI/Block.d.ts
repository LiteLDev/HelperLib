import { FloatPos, IntPos } from "./Basic";
import { NbtCompound } from "../NbtAPI/NBTCompound";
import { Container } from "./Container";
import { BlockEntity } from "./BlockEntity";

export interface block {
  /**游戏内显示的方块名称 */
  readonly name: string;

  /**方块标准类型名 */
  readonly type: string;

  /**方块的游戏内id */
  readonly id: number;

  /**方块所在坐标 */
  readonly pos: IntPos;

  /**方块数据值 */
  readonly tileData: number;

  /**
   * 破坏方块
   * @param drop 是否生成掉落物
   * @returns boolean 是否成功破坏
   */
  destory(drop: boolean): boolean;

  /**
   * 获取方块对应的NBT对象
   * @returns NbtCompound 方块的NBT对象
   */
  getNbt(): NbtCompound;

  /**
   * 写入方块对应的NBT对象
   * @param nbt NBT对象
   * @returns boolean 是否成功写入
   */
  setNbt(nbt: NbtCompound): boolean;

  /**
   * 获取方块的BlockState
   * @returns Object 方块的BlockState
   * @tips 方便函数，协助解析方块BlockState并转换为`Object`，方便读取与解析 等价于脚本执行`block.getNbt().getTag("states").toObject()`
   */
  getBlockState(): Object;

  /**
   * 判断方块是否拥有容器
   * @returns boolean 这个方块是否拥有容器
   */
  hasContainer(): boolean;

  /**
   * 获取方块所拥有的容器对象
   * @returns Container 这个方块所拥有的容器对象
   */
  getContainer(): Container;

  /**
   * 判断方块是否拥有方块实体
   * @returns boolean 这个方块是否拥有方块实体
   */
  hasBlockEntity(): boolean;

  /**
   * 获取方块所拥有的方块实体
   * @returns BlockEntity 这个方块所拥有的方块实体
   */
  getBlockEntity(): BlockEntity;

  /**
   * 删除方块所拥有的方块实体
   * @returns boolean 是否成功删除
   */
  removeBlockEntity(): boolean;
}

declare namespace mc {
  /**
   * 通过方块坐标获取Block
   * @param pos 方块所在坐标
   * @returns block|null 方块对象
   */
  function getBlock(pos: IntPos): block | null;

  /**
   *
   * @param x 方块x坐标
   * @param y 方块y坐标
   * @param z 方块z坐标
   * @param dimid 方块维度
   * @returns block|null 方块对象
   */
  function getBlock(
    x: number,
    y: number,
    z: number,
    dimid: 0 | 1 | 2
  ): block | null;

  /**
   *
   * @param pos 目标方块位置
   * @param block 要设置成的方块对象、方块标准类型名（如`minecraft:stone`）或方块NBT数据
   * @param tiledata 方块状态值，同原版 /setBlock 指令的 tiledata，默认为0，仅通过方块类型名放置方块时有效
   * @returns boolean 是否成功设置
   */
  function setBlock(
    pos: IntPos,
    block: block | string | NbtCompound,
    tiledata: number
  ): boolean;

  /**
   *
   * @param x 方块x坐标
   * @param y 方块y坐标
   * @param z 方块z坐标
   * @param dimid 方块维度
   * @param block 要设置成的方块对象、方块标准类型名（如`minecraft:stone`）或方块NBT数据
   * @param tiledata 方块状态值，同原版 /setBlock 指令的 tiledata，默认为0，仅通过方块类型名放置方块时有效
   * @returns boolean 是否成功设置
   */
  function setBlock(
    x: number,
    y: number,
    z: number,
    dimid: 0 | 1 | 2,
    block: block | string | NbtCompound,
    tiledata: number
  ): boolean;

  /**
   *
   * @param pos 目标生成位置（或者使用x, y, z, dimid来确定方块位置）
   * @param type 要生成的粒子效果名称（可查阅wiki得知）
   * @returns boolean 是否生成成功
   */
  function spawnParticle(pos: IntPos | FloatPos, type: string): boolean;

  /**
   *
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimid 维度
   * @param type 要生成的粒子效果名称（可查阅wiki得知）
   * @returns boolean 是否生成成功
   */
  function spawnParticle(
    x: number,
    y: number,
    z: number,
    dimid: 0 | 1 | 2,
    type: string
  ): boolean;
}
