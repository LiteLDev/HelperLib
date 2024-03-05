/**
 * 国际化API
 */
declare namespace i18n{
    /**
     * 加载翻译数据
     * @param path 翻译数据所在的文件/目录
     * @param defaultLocaleName 默认的语言名称，形如zh_CN或en，若传入空字符串，则默认跟随系统语言
     * @param defaultLangData 该参数将用于补全或创建翻译文件
     */
    function load(path:string, defaultLocaleName:string, defaultLangData?:object):void

    /**
     * 获取文本的指定语言翻译
     * @param key 文本或ID
     * @param localeName 目标语言，默认为i18n.load时传入的defaultLocaleName
     * @returns 翻译内容（若经过多次回落仍未找到翻译，则返回key）
     */
    function get(key:string,localeName?:string):string

    /**
     * 使用指定语言翻译文本并格式化
     * @param localeName 目标语言
     * @param key 文本或ID
     * @param info 格式化参数
     * @returns 翻译并格式化后的文本
     */ 
    function trl(localeName:string, key:string, ...info:any[]):string

    /**
     * 使用默认语言翻译文本并格式化
     * @param key 文本或ID
     * @param info 格式化参数
     * @returns 翻译并格式化后的文本
     */ 
    function tr(key:string, ...info:any[]):string
}
