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
