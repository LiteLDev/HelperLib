/** 创建或打开一个 Json 配置文件 */
declare class JsonConfigFile {
  constructor(path:string,_default?:string)

  /** 配置文件所在路径，以BDS根目录为基准  
    如果配置文件路径中有目录尚不存在，LLSE会自动创建 */
  path: string;

  /** （可选参数）配置文件的默认内容。  
    如果初始化时目标文件**不存在**，引擎将新建一个配置文件并将此处的默认内容写入文件中。  
    如果不传入此参数，新建时的配置文件将为空 */
  default?: string;

  /**
   * 初始化配置项（方便函数）
   * @param name 配置项名字
   * @param _default 配置项初始化时写入的值
   * @returns any 以具体储存的数据类型为准
   * 这里提供了一种简便的方法来初始化配置文件，避免了需要手写默认配置文件内容的麻烦
   */
  init(name: string, _default: any): any;

  /**
   * 写入配置项
   * @param name 配置项名字
   * @param data 指定类型
   * @returns boolean 是否写入成功
   */
  set(name: string, data: any): boolean;

  /**
   * 读取配置项
   * @param name 配置项名字
   * @param _default （可选参数）当读取失败时返回的默认值  默认为`null`
   * @returns any 指定配置项的数据
   */
  get(name: string, _default?: any | null): any;

  /**
   * 删除配置项
   * @param name 配置项名字
   * @returns boolean 是否删除成功
   */
  delete(name: string): boolean;

  /**
   * 重新加载文件中的配置项
   * @returns boolean 是否成功加载
   */
  reload(): boolean;

  /**
   * 关闭配置文件
   * @returns boolean 是否成功关闭
   */
  close(): boolean;

  /**
   * 获取配置文件路径
   * @returns string 当前配置文件的文件路径
   */
  getPath(): string;

  /**
   * 读取整个配置文件的内容
   * @returns string 当前配置文件的所有内容
   */
  read(): string;

  /**
   * 写入整个配置文件的内容
   * @param content 内容
   * @returns boolean 是否写入成功
   */
  write(content:string): boolean;
}

/** 创建或打开一个 Ini 配置文件 */
declare class IniConfigFile {
  constructor(path:string,_default?:string);

  /**
    配置文件所在路径，以BDS根目录为基准  
    如果配置文件路径中有目录尚不存在，LLSE会自动创建 */
  path: string;

  /** （可选参数）配置文件的默认内容。  
    如果初始化时目标文件**不存在**，引擎将新建一个配置文件并将此处的默认内容写入文件中 */
  _default?: string;

  /**
   * 初始化配置项
   * @param section 配置项键名
   * @param name 配置项名字
   * @param _default 配置项初始化时写入的值
   * @returns number|string|boolean 指定配置项的数据
   */
  init(section: string, name: string, _default: number | string | boolean): any;

  /**
   * 写入配置项
   * @param section 配置项键名
   * @param name 配置项名字
   * @param data 要写入的配置数据
   * @returns boolean 是否写入成功
   */
  set(section: string, name: string, data: number | string | boolean): boolean;

  /**
   *
   * @param section 配置项键名
   * @param name 配置项名字
   * @param _default （可选参数）当读取失败时返回的默认值  默认为`0`
   * @returns string 指定配置项的数据
   */
  getStr(
    section: string,
    name: string,
    _default?: string | number | boolean
  ): string;

  /**
   *
   * @param section 配置项键名
   * @param name 配置项名字
   * @param _default （可选参数）当读取失败时返回的默认值  默认为`0`
   * @returns number 指定配置项的数据
   */
  getInt(
    section: string,
    name: string,
    _default?: string | number | boolean
  ): number;

  /**
   *
   * @param section 配置项键名
   * @param name 配置项名字
   * @param _default （可选参数）当读取失败时返回的默认值  默认为`0`
   * @returns number 指定配置项的数据
   */
  getFloat(
    section: string,
    name: string,
    _default?: string | number | boolean
  ): number;

  /**
   *
   * @param section 配置项键名
   * @param name 配置项名字
   * @param _default （可选参数）当读取失败时返回的默认值  默认为`0`
   * @returns boolean 指定配置项的数据
   */
  getBool(
    section: string,
    name: string,
    _default?: string | number | boolean
  ): boolean;

  /**
   * @param section 配置项键名
   * @param name 配置项名字
   * @returns boolean 是否删除成功
   */
  delete(section: string, name: string): boolean;

  /**
   * 重新加载文件中的配置项
   * @returns boolean 是否成功加载
   */
  reload(): boolean;

  /**
   * 关闭配置文件
   * @returns boolean 是否成功关闭
   */
  close(): boolean;

  /**
   * 获取配置文件路径
   * @returns string 当前配置文件的文件路径
   */
  getPath(): string;

  /**
   * 读取整个配置文件的内容
   * @returns string 当前配置文件的所有内容
   */
  read(): string;

  /**
   * 写入整个配置文件的内容
   * @param content 内容
   * @returns boolean 是否写入成功
   */
  write(content:string): boolean;
}
