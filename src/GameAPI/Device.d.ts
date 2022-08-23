declare class device {
  /**玩家设备的IP地址 */
  ip: string;

  /**玩家的平均网络延迟时间（ms） */
  avgPing: number;

  /**玩家的平均网络丢包率（%） */
  avgPacketLoss: number;

  /** 玩家的网络延迟时间（ms）*/
  lastPing: number;

  /**玩家的网络丢包率（%） */
  lastPacketLoss: number;

  /**玩家设备的操作系统类型 */
  os:
    | `Android`
    | `iOS`
    | `OSX`
    | `Amazon`
    | `GearVR`
    | `Hololens`
    | `Windows10`
    | `Win32`
    | `TVOS`
    | `PlayStation`
    | `Nintendo`
    | `Xbox`
    | `WindowsPhone`
    | `Unknown`;

  /**玩家连接的地址 */
  serverAddress: string;

  /**玩家客户端的识别码ID */
  clientId: string;
}
