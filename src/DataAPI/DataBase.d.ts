/** 创建 / 打开一个键值对数据库 */
declare class KVDatabase {
    constructor(dir: string);

    /** 数据库的储存目录路径，以BDS根目录为基准 */
    dir: string;

    /**
     * 写入数据项
     * @param name 数据项名字
     * @param data 要写入的数据
     * @returns boolean 是否写入成功
     */
    set(name: string, data: any): boolean;

    /**
     * 读取数据项
     * @param name 数据项名字
     * @returns any|null 数据库中储存的这个项的数据
     */
    get(name: string): any | null;

    /**
     * 删除数据项
     * @param name 数据库名字
     */
    delete(name: string): boolean;

    /**
     * 获取所有数据项名字
     * @returns Array 所有的数据项名字数组
     */
    listKey(): Array<string>;

    /**
     * 关闭数据库
     * @returns boolean 是否成功关闭
     */
    close(): boolean;
}

declare class DataBase_Params {
    /** 指定数据库所在路径 */
    path: string;

    /** 数据库不存在是否自动创建(默认true) */
    create?: boolean;

    /** 以只读模式打开(默认false) */
    readonly?: boolean;

    /** 以读写模式打开(默认true) */
    readwrite?: boolean;
}

/** 打开一个SQL数据库会话 */
declare class DBSession {
    /**
     * 打开一个SQL数据库会话
     * @param type 数据库的类型，目前仅支持
     * @param params DataBase_Params 连接参数
     */
    constructor(type: "sqlite3", params: DataBase_Params);

    /**
     * 打开一个SQL数据库会话
     * @param str 形如file:///mydb.db?k=v, mysql://root:password@localhost:3306/db的连接字符串
     */
    constructor(str: string);

    /**
     * 执行SQL并获取结果集
     * @param sql 要查询的SQL语句
     * @returns Array<Array> 查询的结果(结果集)
     * @tips 返回数组的第1行(`result[0]`)为结果集的表头(列名)，剩余行为结果数据
     */
    query(sql: string): Array<Array<any>>;

    /**
     * 执行SQL但不获取结果
     * @param sql 要执行的SQL语句
     * @returns DBSession 处理完毕的会话对象（便于连锁进行其他操作）
     */
    exec(sql: string): DBSession;

    /**
     * 执行SQL但不获取结果
     * @param sql 要执行的SQL语句
     * @returns DBSession 处理完毕的会话对象（便于连锁进行其他操作）
     */
    execute(sql: string): DBSession;

    /**
     * 获取当前会话是否为打开状态
     * @returns boolean 是否为打开状态
     */
    isOpen(): boolean;

    /**
     * 关闭数据库会话
     * @returns boolean 是否成功关闭
     */
    close(): boolean;

    /**
     * 准备一个预准备语句
     * @param sql 要准备的SQL语句
     * @returns DBStmt 预准备语句，失败抛出错误
     */
    prepare(sql: string): DBStmt;
}

/** SQL预准备语句 */
declare class DBStmt {
    /**
     * 绑定参数到一个SQL语句
     * @param val 要绑定的值
     * @tips 本重载将会将值绑定到第一个未绑定的参数上
     */
    bind(val: any): void;

    /**
     * 绑定参数到一个SQL语句
     * @param val 要绑定的值
     * @tips 要绑定的对象，等同于遍历此对象并执行
     * @tips 对于Object:bind(val, key) 对于Array:bind(val)
     */
    bind(val: any | Array<any>): void;

    /**
     * 绑定参数到一个SQL语句
     * @param val 要绑定的值
     * @param index 要绑定到的参数索引(从`0`开始)
     */
    bind(val: any, index: number): void;

    /**
     * 绑定参数到一个SQL语句
     * @param val 要绑定的值
     * @param name 要绑定到的参数的参数名
     */
    bind(val: any, name: string): void;

    /**
     * 执行SQL但不获取结果
     * @returns DBSession 处理完毕的会话对象（便于连锁进行其他操作）
     */
    execute(): DBStmt;

    /**
     * 步进到下一行结果
     * @returns boolean 执行成功与否
     */
    step(): boolean;

    /**
     * 步进到下一行结果
     * @returns boolean 执行成功与否
     */
    next(): boolean;

    /**
     * 获取当前结果行
     * @returns Object 当前结果行，形如`{col1: "value", col2: 2333}`
     */
    fetch(): { [key: string]: any };

    /**
     * 获取所有结果行
     * @returns Array<Array>
     * @tips 返回数组的第1行(`result[0]`)为结果集的表头(列名)，剩余行为结果数据
     */
    fetchAll(): Array<Array<any>>;

    /**
     * 重置当前语句状态至“待执行”
     * @returns DBStmt 处理完毕的语句对象（便于连锁进行其他操作）
     * @tips 本函数不会清除已绑定的参数
     */
    reset(): DBStmt;

    /**
     * 重新执行预准备语句
     * @returns DBStmt 处理完毕的语句对象（便于连锁进行其他操作）
     * @tips 本函数是一个便捷函数，等同于执行`stmt.reset()`和`stmt.execute()`
     */
    reexec(): DBStmt;

    /**
     * 清除所有已绑定的参数
     * @returns DBStmt 处理完毕的语句对象（便于连锁进行其他操作）
     */
    clear(): DBStmt;
}
