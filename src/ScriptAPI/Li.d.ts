/// <reference path="../index.d.ts" />

declare class version{
    // 主版本号（如 **2**.1.0 里的 **2**）
    major:Integer;

    // 次版本号（如 2.**1**.0 里的 **1**）
    minor:Integer;

    // 修订版本号（如 2.1.**0** 里的 **0**）
    revision: Integer;

    // 当前版本是否为测试版
    isBeta:boolean;
}

declare namespace ll{
    /**
     * 获取LiteLoader加载器版本
     * @returns version 加载器版本对象
     */
    function version():version;

    /**
     * 获取LiteLoader加载器版本字符串
     * @returns string 加载器版本
     */
    function versionString():string;

    /**
     * 检查LiteLoader加载器版本
     * @returns boolean 检查结果
     */
    function requireVersion(major:Integer,minor?:Integer,revision?:Integer):boolean;

    /**
     * 列出所有已加载的插件
     * @returns Array<string> 列出所有已加载的插件
     */
    function listPlugins():Array<string>;

    /**
     * 导出函数(注意：由于TypeScript的保留字，请删除`_`使用ll._export=>ll.export)
     * @param func 要导出的函数
     * @param namespace 函数的命名空间名，只是方便用于区分不同插件导出的API
     * @param name 函数的导出名称。其他插件根据导出名称来调用这个函数
     * @returns boolean 是否成功导出
     */
    function _export(func:Function,namespace:string,name:string):boolean;

    /**
     * 导入函数(注意：由于TypeScript的保留字，请删除`_`使用ll._export=>ll.export)
     * @param namespace 要导入的函数使用的命名空间名称
     * @param name 要导入的函数使用的导出名称
     * @returns Function 导入的函数
     */
    function _import(namespace:string,name:string):Function;

    /**
     * 判断远程函数是否已导出
     * @param namespace 函数使用的命名空间名称
     * @param name 函数使用的导出名称
     * @returns boolean 函数是否已导出
     */
    function hasExported(namespace:string,name:string):boolean;

    /**
     * 设置插件依赖库
     * @param path 依赖库文件名（如`addplugin.js`)
     * @param remotePath （可选参数）查找并装载依赖库的路径，说明见文档
     * @returns boolean 是否加载依赖库成功
     */
    function require(path:string,remotePath?:string):boolean;

    /**
     * 将字符串作为脚本代码执行
     * @param str 要作为脚本代码执行的字符串
     * @returns any 执行结果
     */
    function eval(str:string):any;
}


