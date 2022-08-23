/**玩家绑定数据 */
export declare class Player {
  /**
   * 获取玩家绑定数据
   * @param name 要读取的绑定数据的名字
   * @returns any|null 储存的绑定数据
   */
  getExtraData(name: string): any | null;

  /**
   * 删除玩家绑定数据
   * @param name 要删除的绑定数据的名字
   * @returns boolean 是否删除成功
   */
  delExtraData(name: string): boolean;
}

/**Xuid 数据库 */
export declare class data {
  /**
   * 根据玩家名查询Xuid
   * @param name 要查询的玩家名
   * @returns string 玩家的Xuid
   */
  static name2xuid(name: string): string | null;

  /**
   * 根据Xuid查询玩家名
   * @param xuid 要查询的玩家Xuid
   * @returns string 玩家名
   */
  static xuid2name(xuid: string): string | null;
}
