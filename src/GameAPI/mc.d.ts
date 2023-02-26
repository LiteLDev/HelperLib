/// <reference path="../index.d.ts" />
declare namespace mc {
    /**
     * 获取服务器游戏时间
     * @param TimeID 想要查询的时间 (0 代表daytime，1 代表gametime，2 代表day)
     * @returns 获取到的时间
     */
    function getTime(TimeID: 0 | 1 | 2): number

    /**
     * 设置服务器时间
     * @param tick 想要设置的时间
     * @returns 是否设置成功
     */
    function setTime(tick: number): boolean

    /**
     * 获取服务器天气
     * @returns 当前天气 (0 代表晴天，1 代表雨天，2 代表雷暴)
     */
    function getWeather(): 0 | 1 | 2

    /**
     * 设置服务器天气
     * @param WeatherID 想要设置的天气 (0 代表晴天，1 代表雨天，2 代表雷暴)
     * @returns 是否设置成功
     */
    function setWeather(WeatherID:0 |1 |2):boolean
}
