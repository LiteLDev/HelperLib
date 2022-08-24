/// <reference path="../index.d.ts" />

declare class logger{
    /**
     * 设置日志是否输出到控制台
     * @param isOpen 设置日志是否输出到控制台  
     * @param logLevel （可选参数）控制台的日志输出等级，默认为`4` 
     */
    static setConsole(isOpen:boolean,logLevel?:0|1|2|3|4|5):void;

    /**
     * 设置日志是否输出到文件
     * @param filePath 设置日志输出到的文件路径
     * @param logLevel （可选参数）文件的最小日志输出等级，默认为`4` 
     */
    static setFile(filePath:string,logLevel?:0|1|2|3|4|5):void;

    /**
     * 设置日志是否输出到某个玩家
     * @param player 设置日志输出到的目标玩家对象
     * @param logLevel （可选参数）玩家的最小日志输出等级，默认为`4`   
     */
    static setPlayer(player:Player,logLevel?:0|1|2|3|4|5):void;

    // 输出普通文本
    static log(...data:any[]):void;

    // 输出调试信息  
    static debug(...data:any[]):void;

    // 输出提示信息
    static info(...data:any[]):void;

    // 输出警告信息
    static warn(...data:any[]):void;

    // 输出错误信息
    static error(...data:any[]):void;

    // 输出严重错误信息
    static fatal(...data:any[]):void;

    /**
     * 设置自定义日志消息标头 
     * @param title 设置的自定义标头
     */
    static setTitle(title:string):void;

    /**
     * 统一修改日志输出等级
     * @param level 日志输出等级  0~5
     */
    static setLogLevel(level:0|1|2|3|4|5):void;
}

