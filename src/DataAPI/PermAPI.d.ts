/**
 * 身分组实例
 */
declare class Role{
    /**
     * 创建身分组
     * @param name 身份组名称，必须是唯一的并且不能含有@#[]{}<>()/|$%^&*!~`"'+=?\n\t\r\f\v
     * @param displayName 身份组显示名称(默认和name一样)
     */
    constructor(name:string,displayName?:string)

    /** 身份组名称 */
    name:string

    /** 身份组显示名称 */
    displayName:string

    /** 身份组优先级，越大越优先 */
    priority:number

    /** 身份组拥有的权限 */
    permissions:Array<{name:string,enabled:boolean,extra:object}>

    /** 身份组成员的Xuid */
    members:Array<string>

    /**
     * 检查身份组实例是否有效
     */
    isValid():boolean

    /**
     * 检查身份组是否有指定成员
     * @param xuid 成员(玩家)的Xuid
     */
    hasMember(xuid:string):boolean

    /**
     * 添加成员到身份组
     * @param xuid 成员(玩家)的Xuid
     */
    addMember(xuid:string):void

    /**
     * 从身份组中移除成员
     * @param xuid 成员(玩家)的Xuid
     */
    removeMember(xuid:string):void

    /**
     * 检查身份组是否有指定权限
     * @param name 权限名称
     * @returns 是否有该权限
     */
    hasPermission(name:string):boolean

    /**
     * 设置身份组权限
     * @param name 权限名称，必须已经注册在PermInfoList中
     * @param enabled 权限是否开启
     * @param extraData 权限的额外数据
     */
    setPermission(name:string, enabled:boolean, extraData?:object):void

    /**
     * 移除身份组中的权限
     * @param name 权限名称
     */
    removePermission(name:string):void

    /**
     * 检查权限是否存在于身份组中
     * @param name 权限是否已经存在于身份组中
     * 
     * 注意: 不同于hasPermission，这个方法会返回true只要权限已经存在于身份组，但权限不一定开启。
     */
    permissionExists(name:string):boolean

}

declare namespace Permission{
    /**
     * Get a role
     * @param name 身份组名称
     * @returns 身份组实例
     */
    function getRole(name:string):Role

    /**
     * Get or create a role
     * @param name 身份组名称，必须是唯一的并且不能含有@#[]{}<>()/|$%^&*!~`"'+=?\n\t\r\f\v
     * @returns 身份组实例
     */
    function getOrCreateRole(name:string):Role

    /**
     * 检查身份组是否存在
     * @param name 身份组名称
     */
    function roleExists(name:string):boolean

    /**
     * 删除身份组
     * @param name 身份组名称
     */
    function deleteRole(name:string):void

    /**
     * 注册权限
     * @param name 权限名，唯一且不包含空格或\t\n\r\f\v，形如namespace:name(至少有一个 `:`)
     * @param desc 权限描述
     */
    function registerPermission(name:string, desc:string):void

    /**
     * 检查权限是否存在
     * @param name 权限名称
     */
    function permissionExists(name:string):boolean

    /**
     * 检查玩家是否有指定权限
     * @param xuid 玩家Xuid
     * @param permName 权限名称
     */
    function checkPermission(xuid:string, permName:string):boolean

    /**
     * 检查玩家是否是指定身份组的成员
     * @param xuid 玩家Xuid
     * @param roleName 身份组名称
     */
    function isMemberOf(xuid:string, roleName:string):boolean

    /**
     * 获取玩家的身份组列表
     * @param xuid 玩家Xuid
     * @returns 此玩家的身份组列表
     */
    function getPlayerRoles(xuid:string):Array<Role>

    /**
     * 获取玩家的权限列表
     * @param xuid 玩家Xuid
     */
    function getPlayerPermissions(xuid:string):Array<object>

    /**
     * 保存数据
     */
    function saveData():void
}
