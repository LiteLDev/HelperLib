/// <reference path="../index.d.ts" />

declare enum NativeTypes {
  Void,
  Bool,
  Char,
  UnsignedChar,
  Short,
  UnsignedShort,
  Int,
  UnsignedInt,
  Long,
  UnsignedLong,
  LongLong,
  UnsignedLongLong,
  Float,
  Double,
  Pointer,
}

declare class NativeHook {
  /**
   * call功能
   * @param params 对应NativeFunction所描述的函数参数
   * @returns any 对应NativeFunction所描述的返回类型
   */
  call(...params: any[]): any;

  /** 函数指针的指针值 */
  address: NativePointer | number;

}

declare class NativeFunction {
  /**
   * Symbol获得函数
   * @param symbol 需要解析的函数
   * @returns 原生函数实例
   */
  static fromSymbol(symbol: string): NativeFunction;

  /**
   * Describe获得函数
   * @param ReturnValue 返回值类型
   * @param Params 参数类型，从左到右直接传递
   * @returns 原生函数实例
   */
  static fromDescription(
    ReturnValue: NativeTypes,
    Params: Array<NativeTypes>
  ): NativeFunction;

  /**
   * Script获得函数
   * @param ReturnValue 返回值类型
   * @param Params 参数类型，从左到右直接传递
   * @param Callback 回调函数，当该原生包装函数被调用后，会调用此函数
   * @returns 回调函数，当该原生包装函数被调用后，会调用此函数
   */
  static fromScript(
    ReturnValue: NativeTypes,
    Params: Array<NativeTypes>,
    Callback: (...Params: NativeTypes[]) => any
  ): NativeFunction;

  /**
   * Hook函数钩子
   * @param func 回调函数，请注意保持参数类型与NativeFunction描述的一致
   * @returns 原函数
   */
  hook(func: (...params: any[]) => any): NativeHook;


}