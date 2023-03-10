/// <reference path="../index.d.ts" />

declare namespace network {
  /**
   * 发送一个异步HTTP(s) Get请求
   * @param url 请求的目标地址（包括 Get 请求附带的参数）
   * @param callback 当请求返回时执行的回调函数，用于回传HTTP(s)响应结果。
   * @returns boolean 是否成功发送请求
   */
  function httpGet(
    url: string,
    callback: (status: number, result: string) => void
  ): boolean;

  /**
   * 发送一个异步HTTP(s) Get请求
   * @param url 请求的目标地址（包括 Get 请求附带的参数）
   * @param header 请求头（包括 Get 请求Request header）
   * @param callback 当请求返回时执行的回调函数，用于回传HTTP(s)响应结果。
   * @returns boolean 是否成功发送请求
   */
  function httpGet(
    url: string,
    header: any,
    callback: (status: number, result: string) => void
  ): boolean;

  /**
   * 发送一个异步HTTP(s) Post请求
   * @param url 请求的目标地址
   * @param data 发送的数据
   * @param type 发送的 Post 数据类型，形如 `text/plain` `application/x-www-form-urlencoded` 等
   * @param callback 当请求返回时执行的回调函数，用于回传HTTP(s)响应结果。
   * @returns boolean 是否成功发送请求
   */
  function httpPost(
    url: string,
    data: string,
    type: string,
    callback: (status: number, result: string) => void
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
  function httpPost(
    url: string,
    header: any,
    data: string,
    type: string,
    callback: (status: number, result: string) => void
  ): boolean;
}

declare type WSClientType = number;
declare class WSClient {
  /** 处于正常连接中   */
  Open: WSClientType;

  /** 正在断开连接 */
  Closing: WSClientType;

  /** 未连接 */
  Closed: WSClientType;

  /** 当前的连接状态 */
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
  listen(event: "onLostConnection", callback: (code: number) => void): boolean;

  /**
   * 关闭连接
   * @returns boolean 是否成功关闭连接
   * @tips 在处于关闭状态时，请勿继续使用此客户端对象！
   */
  close(): boolean;

  /**
   * 强制断开连接
   * @returns boolean 是否成功断开连接
   */
  shutdown(): boolean;

  /**
   * 获取错误码
   * @returns Integer 上一次错误产生的错误码
   */
  errorCode(): number;
}

declare class HttpRequest {
  /** 请求方法 */
  readonly method: string;

  /** 请求路径 */
  readonly path: string;

  /** 请求查询参数 */
  readonly query: any;

  /** 请求查询参数(同上) */
  readonly params: any;

  /** 请求头 */
  readonly headers: any;

  /** 请求内容 */
  readonly body: string;

  /** 请求源地址 */
  readonly remoteAddr: string;

  /** 请求源端口 */
  readonly remotePort: number;

  /** 请求版本 */
  readonly version: string;

  /** 请求路径正则匹配结果 */
  readonly matches: Array<any>;

  /**
   * 获取指定请求头的值
   * @param name 请求头名称
   * @returns Array<string> 请求头的值数组(如果没有该请求头，则返回`[]`空数组)
   */
  getHeader(name: string): Array<string>;
}

declare class HttpResponse {
  /** 响应状态码 */
  status: number;

  /** 响应头 */
  header: any;

  /** 响应内容 */
  body: string;

  /** 响应版本 */
  version: string;

  /** 错误原因 */
  reason: string;

  /**
   * 获取指定请求头的值
   * @param name 请求头名称
   * @returns Array<string> 请求头的值数组(如果没有该请求头，则返回`[]`空数组)
   */
  getHeader(name: string): Array<string>;

  /**
   * 设置指定响应头的值
   * @param name 响应头名称
   * @param value 响应头值
   * @returns HttpResponse 处理完毕的响应对象
   */
  setHeader(name: string, value: any): HttpResponse;

  /**
   * 写入响应内容
   * @param content 响应内容
   * @returns HttpResponse 处理完毕的响应对象
   */
  write(...content: any[]): HttpResponse;
}

declare class HttpServer {
  /**
   * 监听 Get 请求
   * @param path 请求目录，以`/`开头，可以包含正则表达式。如: `/test/(.+)`
   * @param callback 回调函数，在收到符合path的GET请求回调
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
   */
  onGet(
    path: string,
    callback: (req: HttpRequest, resp: HttpResponse) => void
  ): HttpServer;

  /**
   * 监听 Put 请求
   * @param path 请求目录，以`/`开头，可以包含正则表达式。如: `/test/(.+)`
   * @param callback 回调函数，在收到符合path的Put请求回调
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
   */
  onPut(
    path: string,
    callback: (req: HttpRequest, resp: HttpResponse) => void
  ): HttpServer;

  /**
   * 监听 Post 请求
   * @param path 请求目录，以`/`开头，可以包含正则表达式。如: `/test/(.+)`
   * @param callback 回调函数，在收到符合path的Post请求回调
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
   */
  onPost(
    path: string,
    callback: (req: HttpRequest, resp: HttpResponse) => void
  ): HttpServer;

  /**
   * 监听 Patch 请求
   * @param path 请求目录，以`/`开头，可以包含正则表达式。如: `/test/(.+)`
   * @param callback 回调函数，在收到符合path的Patch请求回调
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
   */
  onPatch(
    path: string,
    callback: (req: HttpRequest, resp: HttpResponse) => void
  ): HttpServer;

  /**
   * 监听 Delete 请求
   * @param path 请求目录，以`/`开头，可以包含正则表达式。如: `/test/(.+)`
   * @param callback 回调函数，在收到符合path的Delete请求回调
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
   */
  onDelete(
    path: string,
    callback: (req: HttpRequest, resp: HttpResponse) => void
  ): HttpServer;

  /**
   * 监听 Options 请求
   * @param path 请求目录，以`/`开头，可以包含正则表达式。如: `/test/(.+)`
   * @param callback 回调函数，在收到符合path的Options请求回调
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
   */
  onOptions(
    path: string,
    callback: (req: HttpRequest, resp: HttpResponse) => void
  ): HttpServer;

  /**
   * 监听 PreRouting 预路由事件
   * @param callback 回调函数，在收到请求时调用。在回调函数中可以修改响应，如果返回`false`，则不会继续路由至对应路径的回调函数(但仍然会触发PostRouting事件)。
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
   */
  onPreRouting(
    callback: (req: HttpRequest, resp: HttpResponse) => void
  ): HttpServer;

  /**
   * 监听 PostRouting 后路由事件
   * @param callback 回调函数，在对应目录的回调函数(或PreRouting事件)执行完毕后调用，在回调函数中可以修改响应
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
   */
  onPostRouting(
    callback: (req: HttpRequest, resp: HttpResponse) => void
  ): HttpServer;

  /**
   * 监听 Error 错误事件
   * @param callback 回调函数，在错误(状态码 >= 400)时调用
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
   */
  onError(callback: (req: HttpRequest, resp: HttpResponse) => void): HttpServer;

  /**
   * 监听 Exception 异常事件
   * @param callback 回调函数，在handler中有抛出异常时调用，参数3为异常信息
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
   */
  onException(
    callback: (req: HttpRequest, resp: HttpResponse,error:string) => void
  ): HttpServer;

	/**
	 * 监听端口并开启服务器
	 * @param addr 监听地址，可以是IP地址或域名
	 * @param port 监听端口
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
	 */
	listen(addr:string, port:number):HttpServer;

	/**
	 * 监听端口并开启服务器
	 * @param addr 监听地址，可以是IP地址或域名
	 * @param port 监听端口
   * @returns HttpServer 处理完毕的服务器对象（便于连锁进行其他操作）
	 */
	startAt(addr:string, port:number):HttpServer;

	/**
	 * 停止服务器
	 */
	stop():void;

	/**
	 * 获取服务器是否正在运行
	 * @returns boolean 服务器正在运行与否
	 */
	isRunning():boolean;
}
