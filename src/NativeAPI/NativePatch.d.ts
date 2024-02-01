/// <reference path="../index.d.ts" />

declare class NativePatch {
  /**
   * PatternSearch搜索
   * @param pattern 描述匹配模式的字符串
   * @returns 结果地址
   */
  search(pattern: string): NativePointer;

  /**
   * Patch应用补丁
   * @param pointer 目标地址
   * @param expect 原始字节
   * @param target 目标字节
   * @returns 成功结果
   */
  patch(pointer: NativePatch, expect: string, target: string): boolean;

  /**
   * Dump展示内存
   * @param pointer 目标地址
   * @param size 长度
   * @returns 内存内容
   */
  patch(pointer: NativePatch, size: number): string;
}
