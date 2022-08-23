import { IntPos } from "./Basic";
import { NbtCompound } from "../NbtAPI/NBTCompound"
import { Container } from "./Container"

export interface block{
    /**游戏内显示的方块名称 */
    readonly name: string;

    /**方块标准类型名 */
    readonly type:string;

    /**方块的游戏内id */
    readonly id:number

    /**方块所在坐标 */
    readonly pos:IntPos

    /**方块数据值 */
    readonly tileData:number

    /**
     * 破坏方块
     * @param drop 是否生成掉落物
     * @returns boolean 是否成功破坏
     */
    destory(drop:boolean):boolean;

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
    setNbt(nbt:NbtCompound): boolean;

    /**
     * 获取方块的BlockState
     * @returns Object 方块的BlockState
     * @tips 方便函数，协助解析方块BlockState并转换为`Object`，方便读取与解析 等价于脚本执行`block.getNbt().getTag("states").toObject()`
     */
    getBlockState():Object;

    /**
     * 判断方块是否拥有容器
     * @returns boolean 这个方块是否拥有容器
     */
    hasContainer():boolean;

    /**
     * 获取方块所拥有的容器对象
     * @returns Container 这个方块所拥有的容器对象
     */
    getContainer(): Container

    /**
     * 判断方块是否拥有方块实体
     * @returns boolean 这个方块是否拥有方块实体
     */
    hasBlockEntity(): boolean;
}

declare namespace mc{
    /**
     * 通过方块坐标获取Block
     * @param pos 方块所在坐标
     * @returns block|null 方块对象
     */
    function getBlock(pos:IntPos): block|null;

    /**
     * 
     * @param x 方块x坐标
     * @param y 方块y坐标
     * @param z 方块z坐标
     * @param dimid 方块维度
     * @returns block|null 方块对象
     */
    function getBlock(x:number,y:number,z:number,dimid:0|1|2): block|null;
    
}