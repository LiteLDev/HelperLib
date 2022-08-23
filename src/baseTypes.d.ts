/* eslint-disable @typescript-eslint/triple-slash-reference */
/// <reference path="index.d.ts" />

/** 空，未定义，不存在等等 */
declare type Null = undefined | null;

/** 整数 */
declare type Integer = number;

/** 浮点数（小数，实数） */
declare type Float = number;

/** 字符串 */
// type String = string; // 重复

/** 布尔型 */
// type Boolean = boolean; // 重复

/** 函数（方法） */
// type Function 重复

/** 数组（列表） */
// type Array 重复

/** 对象（映射，字典，表） */
// type Object = object; // 重复

/** 字节数组 */
declare type ByteBuffer = ArrayBuffer;
