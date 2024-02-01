/// <reference path="../index.d.ts" />



declare class version {
  /** 主版本号（如 **2**.1.0 里的 **2**） */
  major: number;

  /** 次版本号（如 2.**1**.0 里的 **1**） */
  minor: number;

  /** 修订版本号（如 2.1.**0** 里的 **0**） */
  revision: number;

  /** 当前版本是否为测试版 */
  isBeta: boolean;
}

interface Plugin {
  /** 插件名称 */
  name: string
  /** 插件描述 */
  desc: string
  /** 插件版本（数组形式） */
  version: [number, number, number]
  /** 插件版本 */
  versionStr: string
  /** 插件路径 */
  filePath: string
  /** 其他信息 */
  others: object
}

declare namespace ll {
  /** LiteLoaderBDS 使用的语言。(例如 `zh_Hans`、`en` 和 `ru_RU`) */
  const language: string;

  /** 主版本号（如 **2**.1.0 里的 **2**） */
  const major: number;

  /** 次版本号（如 2.**1**.0 里的 **1**） */
  const minor: number;

  /** 修订版本号（如 2.1.**0** 里的 **0**） */
  const revision: number;

  /** 版本状态 (`0` 为 `Dev`, `1` 为 `Beta`, `2` 为 `Release`) */
  const status: number;

  /** LiteLoaderBDS Script Engine 版本 */
  const scriptEngineVersion: string;

  /** 是否处于 Wine 环境下 */
  const isWine: boolean;

  /** 是否处于 debug 模式 */
  const isDebugMode: boolean;

  /** 当前版本是否为测试版 */
  const isBeta: boolean;

  /** 当前版本是否为开发版 */
  const isDev: boolean;

  /** 当前版本是否为发布版本 */
  const isRelease: boolean;

  /**
   * 获取 LiteLoader 加载器版本
   * @returns 加载器版本对象
   */
  function version(): version;

  /**
   * 获取 LiteLoader 加载器版本字符串
   * @returns 加载器版本
   */
  function versionString(): string;

  /**
   * 检查 LiteLoader 加载器版本
   * @param major 检查当前已安装LiteLoaderBDS的主版本号是否 >= 此值
   * @param minor (可选参数) 检查当前已安装LiteLoaderBDS的次版本号是否 >= 此值
   * @param revision (可选参数) 检查当前已安装LiteLoaderBDS的修订版本号是否 >= 此值
   * @returns 检查结果
   */
  function requireVersion(
    major: number,
    minor?: number,
    revision?: number
  ): boolean;

  /**
   * 获取有关插件的信息
   * @param name 插件名称
   */
  function getPluginInfo(name: string): Plugin

  /**
   * 列出所有已加载的插件
   * @returns 列出所有已加载的插件
   */
  function listPlugins(): string[];

  /** 列出所有加载的插件信息 */
  function getAllPluginInfo(): Plugin[];

  /**
   * 导出函数
   * @param func 要导出的函数
   * @param namespace 函数的命名空间名，只是方便用于区分不同插件导出的API
   * @param name 函数的导出名称。其他插件根据导出名称来调用这个函数
   * @returns 是否成功导出
   */
  function exports(
    func: (...arg: any[]) => any,
    namespace: string,
    name: string
  ): boolean;

  /**
   * 导出函数
   * @param func 要导出的函数
   * @param name 函数的导出名称。其他插件根据导出名称来调用这个函数
   * @returns 是否成功导出
   */
  function exports(func: (...arg: any[]) => any, name: string): boolean;

  /**
   * 导入函数
   * @param namespace 要导入的函数使用的命名空间名称
   * @param name 要导入的函数使用的导出名称
   * @returns 导入的函数
   */
  function imports(namespace: string, name: string): (...arg: any[]) => any;

  /**
   * 导入函数
   * @param name 要导入的函数使用的导出名称
   * @returns 导入的函数
   */
  function imports(name: string): (...arg: any[]) => any;

  /**
   * 判断远程函数是否已导出
   * @param namespace 函数使用的命名空间名称
   * @param name 函数使用的导出名称
   * @returns 函数是否已导出
   */
  function hasExported(namespace: string, name: string): boolean;

  /**
   * 判断远程函数是否已导出
   * @param name 函数使用的导出名称
   * @returns 函数是否已导出
   */
  function hasExported(name: string): boolean;

  /**
   * 设置插件依赖库
   * @param path 依赖库文件名（如 `addplugin.js`)
   * @param remotePath （可选参数）查找并装载依赖库的路径，说明见文档
   * @returns 是否加载依赖库成功
   */
  function require(path: string, remotePath?: string): boolean;

  /**
   * 将字符串作为脚本代码执行
   * @param str 要作为脚本代码执行的字符串
   * @returns 执行结果
   */
  function eval(str: string): any;
}
