/// <reference path="../../index.d.ts" />

declare namespace mc {
  /**
   * ### 通过方块坐标获取Block
   *
   * 通过此函数来手动生成对象
   *
   * **注意**：要获取的方块必须处于已被加载的范围中，否则会出现问题
   *
   * @param pos 方块所在坐标
   *
   * @returns 方块对象
   */
  function getBlock(pos: IntPos): Block | null;

  /**
   * ### 通过方块坐标获取Block
   *
   * 通过此函数来手动生成对象
   *
   * **注意**：要获取的方块必须处于已被加载的范围中，否则会出现问题
   *
   * @param x 方块x坐标
   * @param y 方块y坐标
   * @param z 方块z坐标
   * @param dimId 方块维度
   *
   * @returns 方块对象
   */
  function getBlock(
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2
  ): Block | null;

  /**
   * ### 设置指定位置的方块
   *
   * 通过此函数，将一个坐标对应的方块设置成另一个，类似于命令 `/setblock`
   *
   * @param pos 目标方块位置
   * @param block 要设置成的方块对象、方块标准类型名（如`minecraft:stone`）或方块NBT数据
   * @param tileData 方块状态值，同原版 `/setBlock` 指令的 `tiledata`，默认为`0`，仅通过方块类型名放置方块时有效
   *
   * @returns 是否成功设置
   */
  function setBlock(
    pos: IntPos,
    block: Block | string | NbtCompound,
    tileData: number
  ): boolean;

  /**
   * ### 设置指定位置的方块
   *
   * 通过此函数，将一个坐标对应的方块设置成另一个，类似于命令 `/setblock`
   *
   * @param x 方块x坐标
   * @param y 方块y坐标
   * @param z 方块z坐标
   * @param dimId 方块维度
   * @param block 要设置成的方块对象、方块标准类型名（如`minecraft:stone`）或方块NBT数据
   * @param tileData 方块状态值，同原版 `/setBlock` 指令的 `tiledata`，默认为`0`，仅通过方块类型名放置方块时有效
   *
   * @returns 是否成功设置
   */
  function setBlock(
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2,
    block: Block | string | NbtCompound,
    tileData: number
  ): boolean;

  /**
   * ### 在指定位置生成粒子效果
   *
   * 粒子效果名称可以查阅[Minecraft Wiki](https://minecraft.fandom.com/zh/wiki/%E7%B2%92%E5%AD%90?variant=zh#.E7.B1.BB.E5.9E.8B)得知
   *
   * 在传入参数的时候不要忘记命名空间前缀。类似于 `minecraft:heart_particle`
   *
   * @param pos 目标生成位置
   * @param type 要生成的粒子效果名称（可查阅wiki得知）
   *
   * @returns 是否生成成功
   */
  function spawnParticle(pos: IntPos | FloatPos, type: string): boolean;

  /**
   * ### 在指定位置生成粒子效果
   *
   * 粒子效果名称可以查阅[Minecraft Wiki](https://minecraft.fandom.com/zh/wiki/%E7%B2%92%E5%AD%90?variant=zh#.E7.B1.BB.E5.9E.8B)得知
   *
   * 在传入参数的时候不要忘记命名空间前缀。类似于 `minecraft:heart_particle`
   *
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimId 维度
   * @param type 要生成的粒子效果名称（可查阅wiki得知）
   *
   * @returns 是否生成成功
   */
  function spawnParticle(
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2,
    type: string
  ): boolean;
}
