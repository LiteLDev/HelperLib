/// <reference path="../index.d.ts" />

declare class Packet{
    /**
     * 获取数据包名称
     * @returns string 数据包名称
     */
    getName(): string;

    /**
     * 获取数据包名称
     * @returns number 数据包ID
     */
    getId(): number;
}

declare class BinaryStream{
    /**
     * 重置二进制流
     * @returns 是否成功
     */
    reset():boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeBool(value:boolean):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeByte(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeDouble(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeFloat(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeSignedBigEndianInt(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeSignedInt(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeSignedInt64(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeSignedShort(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeString(value:string):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeUnsignedChar(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeUnsignedInt(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeUnsignedInt64(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeUnsignedShort(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeUnsignedVarInt(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeUnsignedVarInt64(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeVarInt(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeVarInt64(value:number):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeVec3(value:FloatPos):boolean;

    /**
     * 写入二进制流
     * @param value 参数
     * @returns boolean 是否成功
     */
    writeCompountTag(value:NbtCompound):boolean;

    /**
     * 通过二进制流构建数据包
     * @param pktid 数据包ID
     * @returns Pakcet 数据包对象
     */
    createPacket(pktid:number): Packet;
}