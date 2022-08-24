/// <reference path="../index.d.ts" />

declare class network {
  /**
   * 发送一个异步HTTP(s) Get请求
   * @param url 请求的目标地址（包括 Get 请求附带的参数）
   * @param callback 当请求返回时执行的回调函数，用于回传HTTP(s)响应结果。
   * @returns boolean 是否成功发送请求
   */
  httpGet(
    url: string,
    callback: (status: Integer, result: string) => void
  ): boolean;

  /**
   * 发送一个异步HTTP(s) Get请求
   * @param url 请求的目标地址（包括 Get 请求附带的参数）
   * @param header 请求头（包括 Get 请求Request header）
   * @param callback 当请求返回时执行的回调函数，用于回传HTTP(s)响应结果。
   * @returns boolean 是否成功发送请求
   */
  httpGet(
    url: string,
    header: Object,
    callback: (status: Integer, result: string) => void
  ): boolean;

  /**
   * 发送一个异步HTTP(s) Post请求
   * @param url 请求的目标地址
   * @param data 发送的数据
   * @param type 发送的 Post 数据类型，形如 `text/plain` `application/x-www-form-urlencoded` 等
   * @param callback 当请求返回时执行的回调函数，用于回传HTTP(s)响应结果。
   * @returns boolean 是否成功发送请求
   */
  httpPost(
    url: string,
    data: string,
    type: string,
    callback: (status: Integer, result: string) => void
  ): boolean;

  /**
   * 发送一个异步HTTP(s) Post请求
   * @param url 请求的目标地址
   * @param header 请求头（包括 Post 请求Request header）
   * @param data 发送的数据
   * @param type 发送的 Post 数据类型，形如 `text/plain` `application/x-www-form-urlencoded` 等
   * @param callback 当请求返回时执行的回调函数，用于回传HTTP(s)响应结果。
   * @returns boolean 是否成功发送请求
   */
  httpPost(
    url: string,
    header: Object,
    data: string,
    type: string,
    callback: (status: Integer, result: string) => void
  ): boolean;
}

declare type WSClientType = Integer;
declare class WSClient {
  /**处于正常连接中   */
  Open: WSClientType;

  /**正在断开连接 */
  Closing: WSClientType;

  /**未连接 */
  Closed: WSClientType;

  /**当前的连接状态 */
  readonly status: WSClientType;

  /**
   * 创建连接
   * @param target 要连接的目标地址
   * @returns boolean 是否成功连接
   */
  connect(target: string): boolean;

  /**
   * 异步创建连接
   * @param target 要连接的目标地址
   * @param callback 当连接成功或者失败时执行的回调函数。
   * @returns boolean 是否成功开始尝试连接
   */
  connectAsync(target: string, callback: (success: boolean) => void): boolean;

  /**
   * 发送文本 / 二进制消息
   * @param msg 要发送的文本 / 二进制数据
   * @returns boolean 是否成功发送
   */
  send(msg: string | ByteBuffer): boolean;

  /**
   * 监听WebSocket事件
   * @param event 要监听的事件名
   * @param callback 注册的监听函数
   * @returns boolean 是否成功监听事件
   */
  listen(event: "onTextReceived", callback: (msg: string) => void): boolean;

  /**
   * 监听WebSocket事件
   * @param event 要监听的事件名
   * @param callback 注册的监听函数
   * @returns boolean 是否成功监听事件
   */
  listen(
    event: "onBinaryReceived",
    callback: (data: ByteBuffer) => void
  ): boolean;

  /**
   * 监听WebSocket事件
   * @param event 要监听的事件名
   * @param callback 注册的监听函数
   * @returns boolean 是否成功监听事件
   */
  listen(event: "onError", callback: (msg: string) => void): boolean;

  /**
   * 监听WebSocket事件
   * @param event 要监听的事件名
   * @param callback 注册的监听函数
   * @returns boolean 是否成功监听事件
   */
  listen(event: "onLostConnection", callback: (code: Integer) => void): boolean;

	/**
	 * 关闭连接
	 * @returns boolean 是否成功关闭连接
	 * @tips 在处于关闭状态时，请勿继续使用此客户端对象！
	 */
	close():boolean;

	/**
	 * 强制断开连接
	 * @returns boolean 是否成功断开连接
	 */
	shutdown():boolean;

	/**
	 * 获取错误码
	 * @returns Integer 上一次错误产生的错误码
	 */
	errorCode():Integer
}

declare class HttpRequest{
	/**请求方法 */
	readonly method:string;

	/**请求路径 */
	readonly path:string;

	/**请求查询参数 */
	readonly query:Object;

	/**请求查询参数(同上) */
	readonly params:Object;

	/**请求头 */
	readonly headers:Object;
	
	/**请求内容 */
	readonly body:string;

	/**请求源地址 */
	readonly remoteAddr:string;

	/**请求源端口 */
	readonly remotePort:number;

	/**请求版本 */
	readonly version:string;

	/**请求路径正则匹配结果 */
	readonly matches:Array<any>;

	
}

declare class HttpResponse{
	/**响应状态码 */
	status:number;

	/**响应头 */
	header:Object;

	/**响应内容 */
	body:string;

	/**响应版本 */
	version:string;

	/**错误原因 */
	reason:string;
}

declare class HttpServer{
	onGet
}
