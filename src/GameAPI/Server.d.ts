declare namespace mc{
    /**
     * 获取BDS服务端版本号
     * @returns string 服务端版本号字符串，格式形如`v1.17.10`
     */
    function getBDSVersion():string;

    /**
     * 获取BDS服务端协议版本
     * @returns number 服务端协议版本
     */
     function getServerProtocolVersion():number;

    /**
     * 设置服务器Motd字符串  
     * @param motd 目标Motd字符串  
     * @returns boolean 是否设置成功
     */
    function setMotd(motd:string):boolean;

    /**
     * 设置服务器最大玩家数
     * @param num 最大玩家数
     * @returns boolean 是否设置成功
     */
    function setMaxPlayers(num:number):boolean;
}