/// <reference path="../../index.d.ts" />

declare namespace mc {
  /**
   * ### 生成一个整数坐标对象
   *
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimId
   * 维度ID
   *
   * 主世界 - `0`\
   * 下界 - `1`\
   * 末地 - `2`
   *
   * @returns 一个整数坐标对象
   */
  function newIntPos(x: number, y: number, z: number, dimId: 0 | 1 | 2): IntPos;

  /**
   * ### 生成一个浮点数坐标对象
   *
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimId
   * 维度ID
   *
   * 主世界 - `0`\
   * 下界 - `1`\
   * 末地 - `2`
   *
   * @returns 一个浮点数坐标对象
   */
  function newFloatPos(
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2
  ): FloatPos;

  /**
   * ### 获取结构NBT
   * 
   * @param pos1 第1点坐标对象
   * @param pos2 第2点坐标对象
   * @param ignoreBlocks 
   * @param ignoreEntities
   * @default ignoreBlocks - false
   * @default ignoreEntities - false
   * 
   * @returns 结构NBT
   */
  function getStructure(pos1: IntPos, pos2: IntPos, ignoreBlocks?: boolean, ignoreEntities?: boolean): NbtCompound

  /**
   * ### 放置结构NBT
   * 
   * @param nbt 结构nbt对象
   * @param pos 放置坐标对象
   * @param mirror 镜像 0:None 1:X 2:Z 3:XZ
   * @default mirror - 0
   * @param rotation 旋转 0:None 1:Rotate90 2:Rotate180 3:Rotate270
   * @default rotation - 0
   * 
   * @returns 是否放置成功
   */
  function setStructure(nbt: NbtCompound, pos: IntPos, mirror?: 0 | 1 | 2 | 3, rotation?: 0 | 1 | 2 | 3): boolean
}
