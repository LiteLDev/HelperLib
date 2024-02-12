interface PlayerInfo {
  /** 玩家名 */
  name: string,
  /** 玩家XUID */
  xuid: string,
  /** 玩家UUID */
  uuid: string
}
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

  /**
   * 根据玩家名查询uuid
   * @param name 要查询的玩家名
   * @returns string 玩家的uuid
   */
  function name2uuid(name: string): string | null;

  /**
   * 根据Xuid查询玩家的uuid
   * @param xuid 要查询的玩家Xuid
   * @returns string 玩家的uuid
   */
  function xuid2uuid(xuid: string): string | null;

  function getAllPlayerInfo(): PlayerInfo[]

}
