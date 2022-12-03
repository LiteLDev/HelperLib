/// <reference path="../../index.d.ts" />
declare namespace mc{
    /**
     * ### 生成一个粒子生成器对象
     * 
     * @param displayRadius 默认值 `4294967295`
     * @param highDetial 默认值 `true`
     * @param doubleSide 默认值 `true`
     */
    function newParticleSpawner(displayRadius?:number , highDetial?:boolean , doubleSide?:boolean ):ParticleSpawner
}