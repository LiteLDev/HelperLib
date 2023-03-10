/// <reference path="../../index.d.ts" />
/**
 * ### ✨ 粒子生成器
 * 
 * 该类**没有构造函数**，  
 * 请通{@linkcode mc.newParticleSpawner()}过获得类对象
 * 
 * @see [✨ ParticleSpawner 对象](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Particle)
 */
declare class ParticleSpawner{
    /** 粒子显示半径 */
    displayRadius:number

    /** 需要高细节线条 */
    highDetial:boolean

    /** 需要双面粒子 */
    doubleSide:boolean


    /**
     * ### 生成指定名称粒子
     * 
     * @param pos 可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
     * @param name 
     */
    spawnParticle(pos: FloatPos | IntPos, name:string):boolean


    /**
     * ### 生成点粒子
     * 
     * @param pos 可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
     * @param pointSize 只有 1, 2, 4, 8, 16 大小可选 默认为 `4`
     * @param color 应当使用 ParticleColor 枚举填充 默认为 `ParticleColor.White`
     */
    drawPoint(pos: FloatPos | IntPos, pointSize?:1|2|4|8|16, color?:ParticleColor):boolean


    /**
     * ### 生成数字粒子
     * 
     * @param pos 可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
     * @param num 若为Number只可填 0\~16, 若为String可填 `0`\~`16` 或 `A`\~`F`
     * @param color 应当使用 ParticleColor 枚举填充 默认为 `ParticleColor.White`
     */
    drawNumber(pos: FloatPos | IntPos, num: number | string, color?:ParticleColor):boolean


    /**
     * ### 生成轴向线段
     * 
     * @param pos 线段起点, 可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
     * @param direction 应当使用 Direction 枚举填充
     * @param length 任意实数
     * @param color 应当使用 ParticleColor 枚举填充 默认为 `ParticleColor.White`
     */
    drawAxialLine(pos: FloatPos | IntPos, direction:Direction, length:number, color?:ParticleColor):boolean


    /**
     * ### 生成有向线段
     * 
     * @param start 线段起点, 可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
     * @param end 线段终点, 可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
     * @param lineWidth 只有 1, 2, 4, 8, 16 大小可选 默认值 `4`
     * @param minSpacing 任意实数, 此线段点最小间隔 默认值 `1`
     * @param maxParticlesNum 整数, 此线段最大粒子数，达到后会自动增加间隔 默认值 `64`
     * @param color 应当使用 ParticleColor 枚举填充 默认值 `ParticleColor.White`
     */
    drawOrientedLine(start: FloatPos | IntPos, end: FloatPos | IntPos, lineWidth?:1|2|4|8|16, minSpacing?:number, maxParticlesNum?:number, color?:ParticleColor):boolean


    /**
     * ### 生成圆
     * @param pos 圆心, 可以是浮点坐标或者整数坐标, 整数坐标会取方块中心点位置
     * @param facing 应当使用 Direction 枚举填充
     * @param radius 任意实数, 半径
     * @param lineWidth 只有 1, 2, 4, 8, 16 大小可选 默认值 `4`
     * @param minSpacing 任意实数, 此线段点最小间隔 默认值 `1`
     * @param maxParticlesNum 整数, 此线段最大粒子数，达到后会自动增加间隔 默认值 `64`
     * @param color 当使用 ParticleColor 枚举填充 默认值 `ParticleColor.White`
     */
    drawCircle(pos: FloatPos | IntPos, facing: Direction, radius:number, lineWidth?:1|2|4|8|16, minSpacing?:number, maxParticlesNum?:number, color?:ParticleColor):boolean





    /**
     * ### 生成立方体
     * @param pos 可以是浮点坐标或者整数坐标, 整数坐标会取方块角落底部位置, 若只有一个坐标，会画出 1×1×1 大小的立方体
     * @param pos2 可以是浮点坐标或者整数坐标, 整数坐标会取方块角落顶端位置, 会画出从最小角落 pos 到最大角落 pos2 的立方体
     * @param color 应当使用 ParticleColor 枚举填充 默认值 `ParticleColor.White`
     */
    drawCuboid(pos: FloatPos | IntPos ,pos2?: FloatPos | IntPos, color?:ParticleColor):boolean


}

/**
 * 粒子颜色枚举
 */
declare enum ParticleColor{
    Black,
    Indigo,
    Lavender,
    Teal,
    Cocoa,
    Dark,
    Oatmeal,
    White,
    Red,
    Apricot,
    Yellow,
    Green,
    Vatblue,
    Slate,
    Pink,
    Fawn
}

/**
 * 方向枚举
 */
declare enum Direction{
    NEG_Y,
    POS_Y,
    NEG_Z,
    POS_Z,
    NEG_X,
    POS_X
}
