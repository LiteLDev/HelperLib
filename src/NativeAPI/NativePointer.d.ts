/// <reference path="../index.d.ts" />

declare class NativePointer{
    /**
     * 内存申请
     * @param size 欲申请的内存的大小
     * @returns NativePointer 指向新内存的指针
     */
    static malloc(size:number):NativePointer;

    /**
     * 销毁内存
     * @param block NativePointer
     */
    static free(block:NativePointer):void;

    /**
     * 指针偏移
     * @param offset 偏移量
     * @returns NativePointer 偏移后指针
     */
    offset(offset:number):NativePointer;

    /**
     * 获得符号地址
     * @param symbol 需要查询的符号
     * @returns NativePointer 查询结果，若查询失败则返回空指针
     */
    fromSymbol(symbol:string):NativePointer;

    /**
     * 获得地址实例
     * @param address 地址，以16进制字符串或数字表示
     * @returns NativePointer 对应地址的指针实例
     */
    fromAddress(address:string|number):NativePointer;

    /** 指针地址 */
    asRawAddress:number;

    /** 指针地址描述 */
    asHexAddress:string;

    /** 指针内存Type */
    byte:any;

    int8:any;

    uint8:any;

    int16:any;

    uint16:any;

    int32:any;

    uint32:any;

    long:any;

    ulong:any;

    int64:any;

    uint64:any;

    float:any;

    double:any;

    string:string;

    bool:boolean;

    asEntity():LLSE_Entity

    asItem():LLSE_Item

    asPlayer():LLSE_Player

    asContainer():LLSE_Container
}



