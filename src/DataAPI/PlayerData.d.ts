/**玩家绑定数据 */
declare namespace Player {
  /**
   * 获取玩家绑定数据
   * @param name 要读取的绑定数据的名字
   * @returns any|null 储存的绑定数据
   */
  function getExtraData(name: string): any | null;

  /**
   * 删除玩家绑定数据
   * @param name 要删除的绑定数据的名字
   * @returns boolean 是否删除成功
   */
  function delExtraData(name: string): boolean;
}

/**Xuid 数据库 */
declare namespace data {
  /**
   * 根据玩家名查询Xuid
   * @param name 要查询的玩家名
   * @returns string 玩家的Xuid
   */
  function name2xuid(name: string): string | null;

  /**
   * 根据Xuid查询玩家名
   * @param xuid 要查询的玩家Xuid
   * @returns string 玩家名
   */
  function xuid2name(xuid: string): string | null;
}
