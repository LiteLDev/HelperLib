declare namespace data {
  /**
   * 变量转换为Json字符串
   * @param _var 要转换为Json字符串的变量
   * @param space （可选参数）如果要格式化输出的字符串
   * @returns string|null 转换成的Json字符串
   */
  function toJson(_var: any, space: number): string | null;

  /**
   * Json字符串解析为变量
   * @param json 要转换为变量的Json字符串
   * @returns any|null 转换成的变量
   */
  function parseJson(json: string): any | null;

  /**
   * MD5计算
   * @param str 要计算MD5的字符串 / 字节数组
   * @returns 原数据的MD5摘要字符串
   */
  function toMD5(str: string | ArrayBuffer): string;

  /**
   * SHA1计算
   * @param str 要计算SHA1的字符串 / 字节数组
   * @returns string 原数据的SHA1摘要字符串
   */
  function toSHA1(str: string | ArrayBuffer): string;

  /**
   * 数据转Base64
   * @param str 要转化为Base64的字符串 / 字节数组
   * @returns string Base64结果
   */
  function toBase64(str: string | ArrayBuffer): string;

  /**
   * Base64解码为数据
   * @param base64 要解码的base64字符串
   * @param isBinary 返回数据类型是否为二进制数据，默认为 false
   * @returns string|ArrayBuffer 解码后的数据
   */
  function fromBase64(base64: string, isBinary: boolean): string | ArrayBuffer;
}


