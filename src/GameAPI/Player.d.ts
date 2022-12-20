/// <reference path="../index.d.ts" />
declare enum sendTextType {
  raw = 0,
  chat = 1,
  popup = 4,
  tip = 5,
  json = 9,
}

/**玩家 */
declare class Player {
  /**玩家名 */
  readonly name: string;

  /**玩家所在坐标   */
  readonly pos: FloatPos;

  /**玩家所在的方块坐标 */
  readonly blockPos: IntPos;

  /**玩家上次死亡的坐标 */
  readonly lastDeathPos: IntPos;

  /**玩家的真实名字 */
  readonly realName: string;

  /**玩家Xuid字符串 */
  readonly xuid: string;

  /**玩家Uuid字符串 */
  readonly uuid: string;

  /**玩家的操作权限等级（0 - 4） */
  readonly permLevel: number;

  /**玩家的游戏模式（0 - 3） */
  readonly gameMode: number;

  /**玩家是否可以飞行 */
  readonly canFly: boolean;

  /**玩家是否可以睡觉 */
  readonly canSleep: boolean;

  /**玩家是否可以在地图上看到 */
  readonly canBeSeenOnMap: boolean;

  /**玩家是否可以冻结 */
  readonly canFreeze: boolean;

  /**玩家是否能看到日光 */
  readonly canSeeDaylight: boolean;

  /**玩家是否可以显示姓名标签 */
  readonly canShowNameTag: boolean;

  /**玩家是否可以开始在床上睡觉 */
  readonly canStartSleepInBed: boolean;

  /**玩家是否可以拾取物品 */
  readonly canPickupItems: boolean;

  /**玩家最大生命值 */
  readonly maxHealth: number;

  /**玩家当前生命值 */
  readonly health: number;

  /**玩家当前是否悬空 */
  readonly inAir: boolean;

  /**玩家当前是否在水中 */
  readonly inWater: boolean;

  /**玩家是否在熔岩中 */
  readonly inLava: boolean;

  /**玩家是否下雨 */
  readonly inRain: boolean;

  /**玩家是否在雪中 */
  readonly inSnow: boolean;

  /**玩家是否在墙上 */
  readonly inWall: boolean;

  /**玩家是否在水中或雨中 */
  readonly inWaterOrRain: boolean;

  /**玩家是否在世界 */
  readonly inWorld: boolean;

  /**玩家是否在云端 */
  readonly inClouds: boolean;

  /**玩家当前是否正在潜行 */
  readonly sneaking: boolean;

  /**玩家当前速度 */
  readonly speed: number;

  /**玩家当前朝向 */
  readonly direction: DirectionAngle;

  /**玩家（实体的）唯一标识符 */
  readonly uniqueId: string;

  /**玩家设置的语言的标识符(形如zh_CN)  */
  readonly langCode: string;

  /**玩家是否正在加载   */
  readonly isLoading: boolean;

  /**玩家是否隐身中 */
  readonly isInvisible: boolean;

  /**玩家在传送门中 */
  readonly isInsidePortal: boolean;

  /**玩家是否受伤 */
  readonly isHurt: boolean;

  /**未知 */
  readonly isTrusting: boolean;

  /**玩家是否在能造成伤害的方块上 */
  readonly isTouchingDamageBlock: boolean;

  /**玩家是否饿了 */
  readonly isHungry: boolean;

  /**玩家是否着火 */
  readonly isOnFire: boolean;

  /**玩家是否在地上 */
  readonly isOnGround: boolean;

  /**玩家是否在高温方块上（岩浆等） */
  readonly isOnHotBlock: boolean;

  /**玩家在交易 */
  readonly isTrading: boolean;

  /**玩家是否是冒险模式 */
  readonly isAdventure: boolean;

  /**玩家在滑行 */
  readonly isGliding: boolean;

  /**玩家是否是生存模式 */
  readonly isSurvival: boolean;

  /**玩家是否是观众模式 */
  readonly isSpectator: boolean;

  /**玩家是否在骑行 */
  readonly isRiding: boolean;

  /**玩家在跳舞？ */
  readonly isDancing: boolean;

  /**玩家是否是创造模式 */
  readonly isCreative: boolean;

  /**玩家是否在飞行 */
  readonly isFlying: boolean;

  /**玩家是否正在睡觉 */
  readonly isSleeping: boolean;

  /** 玩家是否移动 */
  readonly isMoving: boolean;

  /**玩家设备IP地址 */
  readonly ip: string;

  /**
   * 判断玩家是否为OP
   * @returns boolean 玩家是否为OP
   */
  isOP(): boolean;

  /**
   * 断开玩家连接
   * @param msg 被踢出玩家出显示的断开原因。
   * @returns boolean 是否成功断开连接
   */
  kick(msg?: string): boolean;

  /**
   * 发送一个文本消息给玩家
   * @param msg 待发送的文本
   * @param type （可选参数）发送的文本消息类型，默认为0
   * @returns boolean 是否成功发送
   */
  tell(msg: string, type?: sendTextType | number): boolean;

  /**
   * 发送一个文本消息给玩家
   * @param msg 待发送的文本
   * @param type （可选参数）发送的文本消息类型，默认为0
   * @returns boolean 是否成功发送
   */
  sendText(msg: string, type?: sendTextType | number): boolean;

  /**
   * 断开玩家连接
   * @param msg 被踢出玩家出显示的断开原因。
   * @returns boolean 是否成功断开连接
   */
  disconnect(msg?: string): boolean;

  /**
   * 在屏幕上方显示消息(类似于成就完成)
   * @param title 待发送的标题
   * @param message 待发送的文本
   * @returns boolean 是否成功发送
   */
  sendToast(title: string, message: string): boolean;

  /**
   * 以某个玩家身份执行一条命令
   * @param cmd 待执行的命令
   * @returns boolean 是否执行成功
   */
  runcmd(cmd: string): boolean;

  /**
   * 以某个玩家身份说话
   * @param text 模拟说话内容
   * @returns boolean 是否执行成功
   */
  talkAs(text: string): boolean;

  /**
   * 传送玩家至指定位置
   * @param pos 目标位置坐标 （或者使用x, y, z, dimid来确定玩家位置）
   * @returns boolean 是否成功传送
   */
  teleport(pos: IntPos | FloatPos): boolean;

  /**
   * 传送玩家至指定位置
   * @param pos 目标位置坐标 （或者使用x, y, z, dimid来确定玩家位置）
   * @returns boolean 是否成功传送
   */
  teleport(x: number, y: number, z: number, dimid: 0 | 1 | 2): boolean;

  /**
   * 杀死玩家
   * @returns 是否成功执行
   */
  kill(): boolean;

  /**
   * 对玩家造成伤害
   * @param damage 对玩家造成的伤害数值
   * @returns boolean 是否造成伤害
   */
  hurt(damage: number): boolean;

  /**
   * 治疗玩家
   * @param health 治疗的心数
   * @returns boolean 治疗是否成功
   */
  heal(health: number): boolean;

  /**
   * 设置玩家的生命值
   * @param health 生命值数
   * @returns boolean 是否成功
   */
  setHealth(health: number): boolean;

  /**
   * 设置玩家最大生命值
   * @param health 生命值数
   * @returns boolean 是否成功
   */
  setMaxHealth(health: number): boolean;

  /**
   * 设置玩家饥饿值
   * @param hunger 饥饿值数
   * @returns boolean 是否成功
   */
  setHungry(hunger: number): boolean;

  /**
   * 使指定玩家着火
   * @param time 着火时长，单位秒
   * @param isEffect 会不会有火的效果
   * @returns boolean 是否成功
   */
  setFire(time: number, isEffect: boolean): boolean;

  /**
   * 熄灭玩家
   * @returns boolean 是否已被熄灭
   */
  stopFire(): boolean;

  /**
   * 重命名玩家
   * @param newName 玩家新名字
   * @returns boolean 是否重命名成功
   */
  rename(newName: string): boolean;

  /**
   * 获取玩家当前站立所在的方块
   * @returns Block 当前站立在的方块对象
   */
  getBlockStandingOn(): Block

  /**
   * 获取玩家对应的设备信息对象
   * @returns Device 玩家对应的设备信息对象
   */
  getDevice(): Device;

  /**
   * 获取玩家主手中的物品对象
   * @returns Item 玩家主手中的物品对象
   * @tips 此处获取的物品对象为引用。也就是说，修改此处返回的物品对象，或使用其API，就相当于直接操作玩家主手中对应的物品
   */
  getHand(): Item;

  /**
   * 获取玩家副手中的物品对象
   * @returns Item 玩家副手中的物品对象
   * @tips 此处获取的物品对象为引用。也就是说，修改此处返回的物品对象，或使用其API，就相当于直接操作玩家副手中对应的物品
   */
  getOffHand(): Item;

  /**
   * 获取玩家物品栏的容器对象
   * @returns Container 玩家物品栏对应的容器对象
   */
  getInventory(): Container;

  /**
   * 获取玩家盔甲栏的容器对象
   * @returns Container 玩家盔甲栏对应的容器对象
   */
  getArmor(): Container;

  /**
   * 获取玩家末影箱的容器对象
   * @returns Container 玩家末影箱对应的容器对象
   */
  getEnderChest(): Container;

  /**
   * 获取玩家的重生坐标
   * @returns IntPos 重生点坐标
   */
  getRespawnPosition(): IntPos;

  /**
   * 给予玩家一个物品
   * @param item 给予的物品对象
   * @returns boolean 是否成功给予
   */
  giveItem(item: Item): boolean;

  /**
   * 清除玩家背包中所有指定类型的物品
   * @param type 要清除的物品对象类型名
   * @returns number 清除的物品个数
   */
  clearItem(type: string): number;

  /**
   * 刷新玩家物品栏、盔甲栏
   * @returns boolean 是否成功刷新
   */
  refreshItems(): boolean;

  /**
   * 刷新玩家加载的所有区块
   * @returns boolean 是否成功刷新
   */
  refreshChunks(): boolean;

  /**
   * 修改玩家操作权限
   * @param level 目标操作权限等级
   * @returns boolean 是否成功修改
   */
  setPermLevel(level: 0 | 1 | 4): boolean;

  /**
   * 修改玩家游戏模式
   * @param mode 目标游戏模式，0为生存模式，1为创造模式，2为极限模式
   * @returns boolean 是否成功修改
   */
  setGameMode(mode: number): boolean;

  /**
   * 提高玩家经验等级
   * @param count 要提高的经验等级
   * @returns boolean 是否设置成功
   */
  addLevel(count: number): boolean;

  /**
   * 降低玩家经验等级
   * @param count 要降低的经验等级
   * @returns boolean 是否设置成功
   */
  reduceLevel(count: number): boolean;

  /**
   * 获取玩家经验等级
   * @returns number 玩家的经验等级
   */
  getLevel(): number;

  /**
   * 设置玩家经验等级
   * @param count 要设置的经验等级
   * @returns boolean 是否设置成功
   */
  setLevel(count: number): boolean;

  /**
   * 重置玩家经验
   * @returns boolean 是否设置成功
   */
  resetLevel(): boolean;

  /**
   * 获取玩家当前经验值
   * @returns number 玩家当前经验值
   */
  getCurrentExperience(): number;

  /**
   * 设置玩家当前经验值
   * @param count 要设置的经验值
   * @returns boolean 是否设置成功
   */
  setCurrentExperience(count: number): boolean;

  /**
   * 获取玩家总经验值
   * @returns number 玩家总经验
   */
  getTotalExperience(): number;

  /**
   * 设置玩家总经验值
   * @param count 要设置的经验值
   * @returns boolean 是否设置成功
   */
  setTotalExperience(count: number): boolean;

  /**
   * 提高玩家经验值
   * @param count 要提高的经验值
   * @returns boolean 是否设置成功
   */
  addExperience(count: number): boolean;

  /**
   * 降低玩家经验值
   * @param count 要降低的经验值
   * @returns boolean 是否设置成功
   */
  reduceExperience(count: number): boolean;

  /**
   * 获取玩家升级所需的经验值
   * @returns number 玩家升级所需的经验值
   */
  getXpNeededForNextLevel(): number;

  /**
   * 传送玩家至指定服务器
   * @param server 目标服务器IP / 域名
   * @param port 目标服务器端口
   * @returns boolean 是否成功传送
   */
  transServer(server: string, port: number): boolean;

  /**
   * 使玩家客户端崩溃
   * @returns boolean 是否成功崩溃
   */
  crash(): boolean;

  /**
   * 设置玩家自定义侧边栏
   * @param title 侧边栏标题
   * @param data 侧边栏对象内容对象
   * @param sortOrder （可选参数）侧边栏内容的排序顺序。`0`为按分数升序，`1`为按分数降序。默认值为`1`
   * @returns boolean 是否成功设置
   */
  setSidebar(title: string, data: Object, sortOrder?: sidebar | 0 | 1): boolean;

  /**
   * 移除玩家自定义侧边栏
   * @returns boolean 是否成功移除
   */
  removeSidebar(): boolean;

  /**
   * 设置玩家看到的自定义Boss血条
   * @param uid 唯一标识符，不可冲突重复！一个uid对于一行bar
   * @param title 自定义血条标题
   * @param percent 血条中的血量百分比，有效范围为0~100。0为空血条，100为满
   * @param colour 血条颜色(默认值为2(RED))
   * @returns boolean 是否设置成功
   */
  setBossBar(
    uid: number,
    title: string,
    percent: number,
    colour: number
  ): boolean;

  /**
   * 移除玩家的自定义的指定Boss血条
   * @param uid 标识符，与setBossBar对应！
   * @returns boolean 是否成功移除
   */
  removeBossBar(uid: number): boolean;

  /**
   * 获取在线玩家对应的NBT对象
   * @returns NbtCompound 玩家的NBT对象
   */
  getNbt(): NbtCompound;

  /**
   * 写入在线玩家对应的NBT对象
   * @param nbt NBT对象
   * @returns boolean 是否成功写入
   */
  setNbt(nbt: NbtCompound): boolean;

  /**
   * 为玩家增加一个Tag
   * @param tag 要增加的tag字符串
   * @returns boolean 是否设置成功 
   */
  addTag(tag: string): boolean;

  /**
   * 为玩家移除一个Tag
   * @param tag 要移除的tag字符串
   * @returns boolean 是否移除成功
   */
  removeTag(tag: string): boolean;

  /**
   * 检查玩家是否拥有某个Tag
   * @param tag 要检查的tag字符串
   * @returns boolean 是否拥有这个Tag
   */
  hasTag(tag: string): boolean;

  /**
   * 玩家所有的 tag 字符串列表
   * @returns Array<String> 玩家所有的 tag 字符串列表
   */
  getAllTags(): Array<String>

  /**
   * 获取玩家的Abilities能力列表（来自玩家NBT）
   * @returns object<String,any>  玩家所有能力信息的键 - 值对列表对象
   */
  getAbilities(): Object;

  /**
   * 获取玩家的Attributes属性列表（来自玩家NBT）
   * @returns Array<Object> 玩家所有属性对象的数组
   */
  getAttributes(): Array<Object>;

  /**
   * 获取玩家疾跑状态
   * @returns boolean 玩家疾跑状态
   */
  isSprinting(): boolean;

  /**
   * 设置玩家疾跑状态
   * @param sprinting 是否为疾跑状态
   * @returns boolean 是否设置成功
   */
  setSprinting(sprinting: boolean): boolean;

  /**
   * 获取视线方向实体
   * @param maxDistance 查找最大距离
   * @returns Entity|null 视线方向实体，如果获取失败，返回 Null
   */
  getEntityFromViewVector(maxDistance?: number): Entity | null;

  /**
   * 获取视线方向方块
   * @param includeLiquid 是否包含液态方块
   * @param solidOnly 是否仅允许 Solid 类型的方块
   * @param maxDistance 查找最大距离
   * @param fullOnly 是否仅允许完整方块
   * @returns Block|null 视线方向方块，如果获取失败，返回 Null
   */
  getBlockFromViewVector(includeLiquid?: boolean, solidOnly?: boolean, maxDistance?: number, fullOnly?: boolean): Block | null;

  /**
   * 向玩家发送数据包
   * @param packet 数据包
   */
  sendPacket(packet: Packet): boolean | null;

  /**
   * 获取玩家所在群系ID
   * @returns number 群系ID
   */
  getBiomeId(): number;

  /**
   * 获取玩家所在群系名称
   * @returns string 群系名称
   */
  getBiomeName(): string;

  /**
   * 设置玩家Ability属性
   * @param AbilityID Ability的ID
   * @param value 是否开启
   * @returns boolean 无作用
   */
  setAbility(AbilityID: number, value: boolean): boolean;

  /**
   * 判断是否为模拟玩家
   * @returns boolean 是否是模拟玩家
   */
  isSimulatedPlayer(): boolean;

  /**
   * 储存玩家绑定数据
   * @param name 要储存到绑定数据的名字
   * @param data 你要储存的绑定数据，可以是`Null`
   * @returns boolean 是否成功储存
   */
  setExtraData(name: string, data: any): boolean;

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

  /**
   * 获取玩家计分项的分数（方便函数）
   * @param name 计分项名称
   * @returns number 计分板上的数值
   */
  getScore(name: string): number;

  /**
   * 修改玩家计分项的分数（方便函数）
   * @param name 计分项名称
   * @param value 要设置的数值
   * @returns boolean 是否设置成功
   */
  setScore(name: string, value: number): boolean;

  /**
   * 修改玩家计分项的分数（方便函数）
   * @param name 计分项名称
   * @param value 要增加的数值
   * @returns boolean 是否设置成功
   */
  addScore(name: string, value: number): boolean;

  /**
   * 修改玩家计分项的分数（方便函数）
   * @param name 计分项名称
   * @param value 要设减少的数值
   * @returns boolean 是否设置成功
   */
  reduceScore(name: string, value: number): boolean;

  /**
   * 玩家停止跟踪计分项（方便函数）
   * @param name 计分项名称
   * @returns boolean 是否移除成功
   */
  deleteScore(name: string): boolean;

  /**
   * 向玩家发送模式表单
   * @param title 表单标题
   * @param content 表单内容
   * @param confirmButton 按钮1文本的字符串
   * @param cancelButton 按钮2文本的字符串
   * @param callback 玩家点击按钮之后被调用的回调函数。
   * @returns number|null 发送的表单ID
   */
  sendModalForm(
    title: string,
    content: string,
    confirmButton: string,
    cancelButton: string,
    callback: (player: Player, result: boolean) => void
  ): number | null;

  /**
   * 向玩家发送普通表单
   * @param title 表单标题
   * @param content 表单内容
   * @param buttons 各个按钮文本的字符串数组
   * @param images 各个按钮对应的图片路径
   * @param callback 玩家点击按钮之后被调用的回调函数。
   */
  sendSimpleForm(
    title: string,
    content: string,
    buttons: Array<string>,
    images: Array<string>,
    callback: (player: Player, id: number) => void
  ): number | null;

  /**
   * 向玩家发送自定义表单（Json格式）
   * @param json 自定义表单json字符串
   * @param callback 玩家提交表单之后被调用的回调函数。
   */
  sendCustomForm(
    json: string,
    callback: (player: Player, data: Array<any>) => void
  ): number | null;

  /**
   * 发送SimpleForm表单
   * @param fm 配置好的表单对象
   * @param callback 玩家与表单元素互动之后被调用的回调函数。
   */
  sendForm(
    fm: SimpleForm,
    callback: (player: Player, id: number) => void
  ): number | null;

  /**
   * 发送CustomForm表单
   * @param fm 配置好的表单对象
   * @param callback 玩家与表单元素互动之后被调用的回调函数。
   */
  sendForm(
    fm: CustomForm,
    callback: (player: Player, data: Array<any>) => void
  ): number | null;

  /**
   * 函数已弃用
   * @deprecated 函数已弃用 请使用 getInventory()
   */
  getContainer(): Container;

  /**
   * 缩放玩家
   * @param scale 新的玩家体积 (整数)
   * @returns boolean 是否缩放成功
   */
  setScale(scale: number): boolean;

  /**
   * 设置玩家显示标题
   * @param content 欲设置标题内容
   * @param type 设置的标题类型 默认为2
   * @param fadeInTime 淡入时间，单位为 Tick ，默认为10
   * @param stayTime 停留时间，单位为 Tick ，默认为70
   * @param fadeOutTime 淡出时间，单位为 Tick，默认为20
   * @returns 是否成功发送
   */
  setTitle(content: string, type?: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8, fadeInTime?: number, stayTime?: number, fadeOutTime?: number): boolean;

  /**
   * 熄灭玩家
   */
  stopFire(): boolean;

  /**
   * ### 获取玩家到坐标的距离
   * 
   * @param pos 目标位置
   * 
   * @returns 到坐标的距离(方块)
   */
  distanceToPos(pos: IntPos | FloatPos): number;
}

declare namespace mc {
  /**
   * 广播一个文本消息给所有玩家
   * @param msg 待发送的文本
   * @param type （可选参数）发送的文本消息类型，默认为0
   * @returns boolean 是否成功发送
   */
  function broadcast(msg: string, type?: sendTextType | number): boolean;

  /**
   * 修改玩家的重生坐标
   * @param pos 重生坐标（或者使用x, y, z, dimid来确定重生位置）
   * @returns boolean 是否成功修改
   */
  function setRespawnPosition(pos: IntPos): boolean;

  /**
   * 修改玩家的重生坐标
   * @param pos 重生坐标（或者使用x, y, z, dimid来确定重生位置）
   * @returns boolean 是否成功修改
   */
  function setRespawnPosition(x: number, y: number, z: number, dimId: 0 | 1 | 2): boolean;

  /**
   * 创建一个模拟玩家
   * @param name 模拟玩家名
   * @param pos 生成生物的位置的坐标对象（或者使用x, y, z, dimid来确定生成位置）
   * @returns SimulatedPlayer 模拟玩家对象
   */
  function spawnSimulatedPlayer(
    name: string,
    pos: IntPos
  ): SimulatedPlayer | null;

  /**
   *
   * @param name 模拟玩家名
   * @param x x坐标
   * @param y y坐标
   * @param z z坐标
   * @param dimId 维度Id
   */
  function spawnSimulatedPlayer(
    name: string,
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2
  ): SimulatedPlayer | null;

  /**
   * 从现有玩家获取
   * @param info 玩家的名字或者Xuid
   * @returns Player 生成的玩家对象
   */
  function getPlayer(info: string): Player;

  /**
   * 获取所有在线玩家
   * @returns Array<Player> 玩家对象的数组
   */
  function getOnlinePlayers(): Array<Player>;

  /**
   * 获取玩家对应的NBT对象
   * @param uuid 玩家的UUID
   * @returns 玩家的UUID
   * **可获取离线玩家的nbt**
   */
  function getPlayerNbt(uuid: string): NbtCompound

  /**
   * 写入玩家对应的NBT对象
   * @param uuid 玩家的UUID
   * @param nbt NBT对象
   * @returns 是否成功写入
   * **可操作离线玩家的nbt**
   */
  function setPlayerNbt(uuid: string, nbt: NbtCompound): boolean

  /**
   * 覆盖玩家对应的NBT对象的特定NbtTag
   * @param uuid 玩家的UUID
   * @param nbt NBT对象
   * @param tags 需要覆盖的NbtTag (String)
   * @returns boolean 是否成功覆盖对应的Tag
   */
  function setPlayerNbtTags(uuid: string, nbt: NbtCompound, tags: Array<string>): boolean;

  /**
   * 从存档中删除玩家对应的NBT对象的全部内容
   * @param uuid 玩家的UUID
   * @returns boolean 是否删除成功
   */
  function deletePlayerNbt(uuid: string): boolean;
}

declare enum sidebar {
  /**降序 */
  Descending = 1,
  /**升序 */
  Ascending = 0,
}

declare class SimulatedPlayer extends Player {
  /**
   * 模拟攻击
   * @param target （可选参数）攻击目标，默认为视线方向上的实体
   * @returns boolean 是否成功模拟操作
   */
  simulateAttack(target: Entity): boolean;

  /**
   * 模拟破坏
   * @param target （可选参数）要破坏的方块的坐标或方块，默认为视线方向上的方块
   * @param face （可选参数）从哪面破坏，
   * @returns boolean 是否成功模拟操作
   */
  simulateDestroy(target: IntPos | Block, face: number): boolean;
}
