/// <reference path="../index.d.ts" />

declare class file {
  /**
   *
   * @param path 想要打开的文件路径
   * @param mode 文件的打开模式
   * @param isBinary （可选参数）是否以二进制模式打开文件，默认为`false`
   */
  constructor(path: string, mode: number, isBinary?: boolean);

  /** 当前文件路径 */
  readonly path: string;

  /** 当前文件的绝对路径 */
  readonly absolutePath: string;

  /** 当前文件大小 */
  readonly size: number;

  /** 文件打开模式枚举 - 只读 */
  static readonly ReadMode: number;

  /** 文件打开模式枚举 - 写入 */
  static readonly WriteMode: number;

  /** 文件打开模式枚举 - 追加 */
  static readonly AppendMode: number;

  /**
   * 读入文件的所有内容
   * @param path 目标文件的路径，相对路径以BDS根目录为基准
   * @returns string 文件的所有数据
   */
  static readFrom(path: string): string | null;

  /**
   * 向指定文件写入内容
   * @param path 目标文件的路径，相对路径以BDS根目录为基准
   * @param text 要写入的内容
   * @returns boolean 是否写入成功
   */
  static writeTo(path: string, text: string): boolean;

  /**
   * 向指定文件追加一行
   * @param path 目标文件的路径，相对路径以BDS根目录为基准
   * @param text 要写入的内容
   * @returns boolean 是否写入成功
   */
  static writeLine(path: string, text: string): boolean;

  /**
   * 从文件读取文本 / 二进制数据
   * @param cnt 要读取的字符数 / 字节数
   * @returns string|ByteBuffer 读取的字符串内容 / 二进制数据
   */
  readSync(cnt: number): string | ByteBuffer | null;

  /**
   * 从文件读取一行文本
   * @returns string|null 读取的字符串内容
   */
  readLineSync(): string | null;

  /**
   * 从文件读取所有内容
   * @returns string|ByteBuffer 读取的字符串内容 / 二进制数据
   */
  readAllSync(): string | ByteBuffer | null;

  /**
   * 写入文本 / 二进制数据到文件
   * @param str 要写入的内容
   * @returns boolean 是否成功写入
   */
  writeSync(str: string | ByteBuffer): boolean;

  /**
   * 写入一行文本到文件
   * @param str 要写入的内容
   * @returns boolean 是否成功写入
   */
  writeLineSync(str: string): boolean;

  /**
   * 从文件读取文本 / 二进制数据（异步）
   * @param cnt 要读取的字符数 / 字节数
   * @param callback 获取结果的回调函数
   * @returns boolean 是否成功发送请求
   */
  read(
    cnt: number,
    callback: (result: string | ByteBuffer | null) => void
  ): boolean;

  /**
   * 从文件读取一行文本（异步）
   * @param callback 获取结果的回调函数
   * @returns boolean 是否成功发送请求
   */
  readLine(callback: (result: string) => void): boolean;

  /**
   * 从文件读取所有内容（异步）
   * @param callback 获取结果的回调函数
   * @returns boolean 是否成功发送请求
   */
  readAll(callback: (result: string | ByteBuffer | null) => void): boolean;

  /**
   * 写入文本 / 二进制数据到文件（异步）
   * @param str 要写入的内容
   * @param callback （可选参数）获取结果的回调函数
   * @returns boolean 是否成功发送请求
   */
  write(
    str: string | ByteBuffer,
    callback?: (result: boolean) => void
  ): boolean;

  /**
   * 写入一行文本到文件（异步）
   * @param str 要写入的内容
   * @param callback （可选参数）获取结果的回调函数
   * @returns boolean 是否成功发送请求
   */
  writeLine(
    str: string | ByteBuffer,
    callback?: (result: boolean) => void
  ): boolean;

  /**
   * 移动文件指针
   * @param pos 文件指针要移动到的位置
   * @param isRelative 是否是相对当前文件指针位置移动
   * @returns boolean 是否移动成功
   */
  seekTo(pos: number, isRelative: boolean): boolean;

  /**
   * 设定文件大小
   * @param size 要设定的目标大小
   * @returns boolean 是否设定成功
   * @tips 设定的新大小可以大于文件的当前大小。如果设定的新大小小于文件的当前大小，原文件将被截断。
   */
  setSize(size: number): boolean;

  /**
   * 关闭文件
   * @returns boolean 是否成功关闭
   * @tips 文件关闭后，严禁再次使用
   */
  close(): boolean;

  /**
   * 文件指针是否位于文件尾
   * @returns boolean 文件指针是否处于文件尾
   */
  isEOF(): boolean;

  /**
   * 刷新文件缓冲区
   * @returns boolean 是否成功刷新
   */
  flush(): boolean;

  /**
   * 获取错误码
   * @returns Integer 上一次IO操作产生的错误码
   */
  errorCode(): number;

  /**
   * 清除错误状态
   * @return boolean 是否成功清除
   */
  clear(): boolean;

  /**
   * 创建文件夹
   * @param dir 目标文件夹的路径
   * @returns boolean 是否成功创建
   */
  static createDir(dir: string): boolean;

  /**
   * 创建文件夹
   * @param dir 目标文件夹的路径
   * @returns boolean 是否成功创建
   */
  static mkdir(dir: string): boolean;

  /**
   * 删除文件 / 文件夹
   * @param path 目标文件 / 文件夹的路径
   * @returns boolean 是否成功删除
   */
  static delete(path: string): boolean;

  /**
   * 判断文件 / 文件夹是否存在
   * @param path 目标文件 / 文件夹的路径
   * @returns boolean 目标是否存在
   */
  static exists(path: string): boolean;

  /**
   * 复制文件 / 文件夹到指定位置
   * @param from 源文件 / 文件夹的路径
   * @param to 目标文件 / 文件夹的位置
   * @returns boolean 是否复制成功
   */
  static copy(from: string, to: string): boolean;

  /**
   * 移动文件 / 文件夹到指定位置
   * @param from 源文件 / 文件夹的路径
   * @param to 目标文件 / 文件夹的位置
   * @returns boolean 是否复制成功
   */
  static move(from: string, to: string): boolean;

  /**
   * 重命名指定文件 / 文件夹
   * @param from 文件 / 文件夹的旧名字
   * @param to 新名字
   * @returns boolean 是否复制成功
   */
  static rename(from: string, to: string): boolean;

  /**
   * 获取指定文件的大小
   * @param path 所操作的文件路径
   * @returns Integer 文件的大小（字节）
   * @tips 如果传入的路径位置是一个文件夹，则返回`-1`
   */
  static getFileSize(path: string): number;

  /**
   * 判断指定路径是否是文件夹
   * @param path 所判断的路径
   * @returns boolean 目标路径是否是文件夹
   */
  static checkIsDir(path: string): boolean;

  /**
   * 列出指定文件夹下的所有文件 / 文件夹
   * @param dir 文件夹路径
   * @returns Array<string> 文件夹名数组
   */
  static getFilesList(dir: string): Array<string>;
}

declare class File extends file {}
