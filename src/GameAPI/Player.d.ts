/// <reference path="../index.d.ts" />
declare enum sendTextType {
  raw = 0,
  chat = 1,
  popup = 4,
  tip = 5,
  json = 9,
}

/** 玩家 */
declare class Player {
  /** 玩家名 */
  readonly name: string;

  /** 玩家所在坐标   */
  readonly pos: FloatPos;

  /** 玩家所在的方块坐标 */
  readonly blockPos: IntPos;

  /** 玩家腿部所在坐标 */
  readonly feetPos: FloatPos;

  /** 玩家上次死亡的坐标 */
  readonly lastDeathPos: IntPos;

  /** 玩家的真实名字 */
  readonly realName: string;

  /** 玩家Xuid字符串 */
  readonly xuid: string;

  /** 玩家Uuid字符串 */
  readonly uuid: string;

  /** 玩家的操作权限等级（0 - 4） */
  readonly permLevel: number;

  /** 玩家的游戏模式（0 - 3） */
  readonly gameMode: number;

  /** 玩家是否可以飞行 */
  readonly canFly: boolean;

  /** 玩家是否可以睡觉 */
  readonly canSleep: boolean;

  /** 玩家是否可以在地图上看到 */
  readonly canBeSeenOnMap: boolean;

  /** 玩家是否可以冻结 */
  readonly canFreeze: boolean;

  /** 玩家是否能看到日光 */
  readonly canSeeDaylight: boolean;

  /** 玩家是否可以显示姓名标签 */
  readonly canShowNameTag: boolean;

  /** 玩家是否可以开始在床上睡觉 */
  readonly canStartSleepInBed: boolean;

  /** 玩家是否可以拾取物品 */
  readonly canPickupItems: boolean;

  /** 玩家最大生命值 */
  readonly maxHealth: number;

  /** 玩家当前生命值 */
  readonly health: number;

  /** 玩家当前是否悬空 */
  readonly inAir: boolean;

  /** 玩家当前是否在水中 */
  readonly inWater: boolean;

  /** 玩家是否在熔岩中 */
  readonly inLava: boolean;

  /** 玩家是否下雨 */
  readonly inRain: boolean;

  /** 玩家是否在雪中 */
  readonly inSnow: boolean;

  /** 玩家是否在墙上 */
  readonly inWall: boolean;

  /** 玩家是否在水中或雨中 */
  readonly inWaterOrRain: boolean;

  /** 玩家是否在世界 */
  readonly inWorld: boolean;

  /** 玩家是否在云端 */
  readonly inClouds: boolean;

  /** 玩家当前是否正在潜行 */
  readonly isSneaking: boolean;

  /** @deprecated 玩家当前是否正在潜行 */
  readonly sneaking: boolean;

  /** 玩家当前速度 */
  readonly speed: number;

  /** 玩家当前朝向 */
  readonly direction: DirectionAngle;

  /** 玩家（实体的）唯一标识符 */
  readonly uniqueId: string;

  /** 玩家设置的语言的标识符(形如zh_CN)  */
  readonly langCode: string;

  /** 玩家是否正在加载   */
  readonly isLoading: boolean;

  /** 玩家是否隐身中 */
  readonly isInvisible: boolean;

  /** 玩家在传送门中 */
  readonly isInsidePortal: boolean;

  /** 玩家是否受伤 */
  readonly isHurt: boolean;

  /** 未知 */
  readonly isTrusting: boolean;

  /** 玩家是否在能造成伤害的方块上 */
  readonly isTouchingDamageBlock: boolean;

  /** 玩家是否饿了 */
  readonly isHungry: boolean;

  /** 玩家是否着火 */
  readonly isOnFire: boolean;

  /** 玩家是否在地上 */
  readonly isOnGround: boolean;

  /** 玩家是否在高温方块上（岩浆等） */
  readonly isOnHotBlock: boolean;

  /** 玩家在交易 */
  readonly isTrading: boolean;

  /** 玩家是否是冒险模式 */
  readonly isAdventure: boolean;

  /** 玩家在滑行 */
  readonly isGliding: boolean;

  /** 玩家是否是生存模式 */
  readonly isSurvival: boolean;

  /** 玩家是否是观众模式 */
  readonly isSpectator: boolean;

  /** 玩家是否在骑行 */
  readonly isRiding: boolean;

  /** 玩家在跳舞？ */
  readonly isDancing: boolean;

  /** 玩家是否是创造模式 */
  readonly isCreative: boolean;

  /** 玩家是否在飞行 */
  readonly isFlying: boolean;

  /** 玩家是否正在睡觉 */
  readonly isSleeping: boolean;

  /** 玩家是否移动 */
  readonly isMoving: boolean;

  /** @deprecated 玩家设备IP地址 */
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
   * 以某个玩家身份向某玩家说话
   * @param target 模拟说话对象
   * @param text 模拟说话内容
   * @returns boolean 是否执行成功
   */
  talkAs(target: Player, text: string): boolean;

  /**
   * ### 获取实体到坐标的距离
   * @param pos 目标位置
   * @returns 到坐标的距离(方块)
   */
  distanceToSqr(pos: Entity | Player | IntPos | FloatPos): number;

  /**
   * ### 获取实体到坐标的距离
   * @param pos 目标位置
   * @returns 到坐标的距离(方块)
   */
  distanceTo(pos: Entity | Player | IntPos | FloatPos): number;

  /**
   * 传送玩家至指定位置
   * @param pos 目标位置坐标 （或者使用x, y, z, dimid来确定玩家位置）
   * @param rot 送后玩家的朝向，若缺省则与传送前朝向相同
   *
   * @returns boolean 是否成功传送
   */
  teleport(pos: IntPos | FloatPos, rot?: DirectionAngle): boolean;

  /**
   * 传送玩家至指定位置
   * @param pos 目标位置坐标 （或者使用x, y, z, dimid来确定玩家位置）
   * @param rot 送后玩家的朝向，若缺省则与传送前朝向相同
   *
   * @returns boolean 是否成功传送
   */
  teleport(
    x: number,
    y: number,
    z: number,
    dimid: 0 | 1 | 2,
    rot?: DirectionAngle
  ): boolean;

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
  getBlockStandingOn(): Block;

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
   *
   * 如果玩家物品栏已满，将抛出多余物品
   *
   * @param item 给予的物品对象
   * @param amount 给予物品对象的数量，物品对象自身的 `Count` 属性将被忽略
   * @returns boolean 是否成功给予
   */
  giveItem(item: Item, amount?: number): boolean;

  /**
   * 清除玩家背包中所有指定类型的物品
   * @param type 要清除的物品对象类型名
   * @returns number 清除的物品个数
   */
  clearItem(type: string): number;

  /**
   * 清除玩家背包中所有指定类型的物品
   * @param type 要清除的物品对象类型名
   * @param amount 清除的物品个数
   * @returns number 清除的物品个数
   */
  clearItem(type: string, amount: number): number;

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
  setSidebar(
    title: string,
    data: Record<string, number>,
    sortOrder?: sidebar | 0 | 1
  ): boolean;

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
  getAllTags(): Array<string>;

  /**
   * 获取玩家的Abilities能力列表（来自玩家NBT）
   * @returns object<String,any>  玩家所有能力信息的键 - 值对列表对象
   */
  getAbilities(): any;

  /**
   * 获取玩家的Attributes属性列表（来自玩家NBT）
   * @returns Array<Object> 玩家所有属性对象的数组
   */
  getAttributes(): Array<any>;

  /**
   * 设置伤害吸收属性
   * @param value 新的值
   * @returns 是否成功
   */
  setAbsorption(value: number): boolean;

  /**
   * 设置攻击伤害属性
   * @param value 新的值
   * @returns 是否成功
   */
  setAttackDamage(value: number): boolean;

  /**
   * 最大攻击伤害属性
   * @param value 新的值
   * @returns 是否成功
   */
  setMaxAttackDamage(value: number): boolean;

  /**
   * 设置跟随范围
   * @param value 新的值
   * @returns 是否成功
   */
  setFollowRange(value: number): boolean;

  /**
   * 设置击退抵抗属性
   * @param value 新的值
   * @returns 是否成功
   */
  setKnockbackResistance(value: 0 | 1): boolean;

  /**
   * 设置幸运属性
   * @param value 新的值
   * @returns 是否成功
   */
  setLuck(value: number): boolean;

  /**
   * 设置移动速度属性
   * @param value 新的值
   * @returns 是否成功
   */
  setMovementSpeed(value: number): boolean;

  /**
   * 置水下移动速度属性
   * @param value 新的值
   * @returns 是否成功
   */
  setUnderwaterMovementSpeed(value: number): boolean;

  /**
   * 设置岩浆上移动速度属性
   * @param value 新的值
   * @returns 是否成功
   */
  setLavaMovementSpeed(value: number): boolean;

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
  getBlockFromViewVector(
    includeLiquid?: boolean,
    solidOnly?: boolean,
    maxDistance?: number,
    fullOnly?: boolean
  ): Block | null;

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
   * 获取在线玩家计分项的分数（方便函数）
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
    callback: (player: Player, result: boolean | null) => void
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
    callback: (player: Player, id: number | null) => void
  ): number | null;

  /**
   * 向玩家发送自定义表单（Json格式）
   * @param json 自定义表单json字符串
   * @param callback 玩家提交表单之后被调用的回调函数。
   */
  sendCustomForm(
    json: string,
    callback: (player: Player, data: Array<any> | null) => void
  ): number | null;

  /**
   * 发送SimpleForm表单
   * @param fm 配置好的表单对象
   * @param callback 玩家与表单元素互动之后被调用的回调函数。
   */
  sendForm(
    fm: SimpleForm,
    callback: (player: Player, id: number | null) => void
  ): number | null;

  /**
   * 发送CustomForm表单
   * @param fm 配置好的表单对象
   * @param callback 玩家与表单元素互动之后被调用的回调函数。
   */
  sendForm(
    fm: CustomForm,
    callback: (player: Player, data: Array<any> | null) => void
  ): number | null;

  /**
   * 发送表单
   * @param fm 配置好的表单对象
   * @param callback 玩家与表单元素互动之后被调用的回调函数。
   */
  sendForm(
    fm: CustomForm | SimpleForm,
    callback: (player: Player, data: number | Array<any> | null) => void
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
  setTitle(
    content: string,
    type?: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8,
    fadeInTime?: number,
    stayTime?: number,
    fadeOutTime?: number
  ): boolean;

  /**
   * ### 获取玩家到坐标的距离
   *
   * @param pos 目标位置
   *
   * @returns 到坐标的距离(方块)
   *
   * @deprecated
   */
  distanceToPos(pos: IntPos | FloatPos): number;

  /**
   * 增加玩家的存款
   * @param value 要增加的金额
   * @returns 是否设置成功
   */
  addMoney(value: number): boolean;

  /**
   * 获取玩家全部药水效果
   * @returns 玩家所有的药水效果id
   */
  getAllEffects(): number[];
  
  /**
   * 为玩家添加一个药水效果
   * @param id 药水效果的id
   * @param tick 持续时间
   * @param level 等级
   * @param showParticles 是否显示粒子
   * @returns 是否成功
   */
  addEffect(id: number, tick: number, level: number, showParticles: boolean): boolean;

  /**
   * 为玩家移除一个药水效果
   * @param id 药水效果的id
   * @returns 是否成功
   */
  removeEffect(id: number): boolean;
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
  function setRespawnPosition(
    x: number,
    y: number,
    z: number,
    dimId: 0 | 1 | 2
  ): boolean;

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
   * @returns 玩家的NBT对象
   * **可获取离线玩家的nbt**
   */
  function getPlayerNbt(uuid: string): NbtCompound;

  /**
   * 写入玩家对应的NBT对象
   * @param uuid 玩家的UUID
   * @param nbt NBT对象
   * @returns 是否成功写入
   * **可操作离线玩家的nbt**
   */
  function setPlayerNbt(uuid: string, nbt: NbtCompound): boolean;

  /**
   * 覆盖玩家对应的NBT对象的特定NbtTag
   * @param uuid 玩家的UUID
   * @param nbt NBT对象
   * @param tags 需要覆盖的NbtTag (String)
   * @returns boolean 是否成功覆盖对应的Tag
   */
  function setPlayerNbtTags(
    uuid: string,
    nbt: NbtCompound,
    tags: Array<string>
  ): boolean;

  /**
   * 从存档中删除玩家对应的NBT对象的全部内容
   * @param uuid 玩家的UUID
   * @returns boolean 是否删除成功
   */
  function deletePlayerNbt(uuid: string): boolean;
}

declare enum sidebar {
  /** 降序 */
  Descending = 1,
  /** 升序 */
  Ascending = 0,
}

declare class LLSE_Player extends Player {}

/**
 * 模拟玩家
 * @see [🏃‍♂️ 玩家对象](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Player?id=%e6%a8%a1%e6%8b%9f%e7%8e%a9%e5%ae%b6%ef%bc%88%e7%94%b1%e4%ba%8e%e4%b8%8e%e7%8e%a9%e5%ae%b6api%e9%87%8d%e5%90%88%e8%bf%87%e5%a4%9a%ef%bc%8c%e6%9c%aa%e7%94%9f%e6%88%90%e6%96%b0%e7%9a%84%e6%a8%a1%e6%8b%9f%e7%8e%a9%e5%ae%b6%e7%b1%bb%ef%bc%89)
 * @see [mojang-gametest docs](https://docs.microsoft.com/zh-cn/minecraft/creator/scriptapi/mojang-gametest/simulatedplayer)
 */
declare class SimulatedPlayer extends Player {
  /**
   * 模拟攻击
   * @param target （可选参数）攻击目标，默认为视线方向上的实体
   * @returns boolean 是否成功模拟操作
   */
  simulateAttack(target?: Entity): boolean;

  /**
   * 模拟破坏
   * @param target （可选参数）要破坏的方块的坐标或方块，默认为视线方向上的方块
   * @param face （可选参数）从哪面破坏，
   * @returns boolean 是否成功模拟操作
   */
  simulateDestroy(target?: IntPos | Block, face?: number): boolean;

  /**
   * 模拟重生
   * @returns boolean 是否成功模拟操作
   */
  simulateRespawn(): boolean;

  /**
   * 模拟断开连接
   * @returns boolean 是否成功模拟操作
   */
  simulateDisconnect(): boolean;

  /**
   * 模拟交互
   * @param target （可选参数）模拟交互目标，默认为视线方向上的方块或实体
   * @returns boolean 是否成功模拟操作
   */
  simulateInteract(target?: Entity): boolean;

  /**
   * 模拟交互
   * @param target （可选参数）模拟交互目标，默认为视线方向上的方块或实体
   * @param face （可选参数）模拟交互目标方块的面
   * @returns boolean 是否成功模拟操作
   */
  simulateInteract(target?: IntPos | Block, face?: number): boolean;

  /**
   * 模拟跳跃
   * @returns boolean 是否成功模拟操作
   */
  simulateJump(): boolean;

  /**
   * 模拟看向某方块或实体
   * @param target 要看向的目标(实体|坐标|方块)
   * @returns boolean 是否成功模拟操作
   */
  simulateLookAt(target: Entity | IntPos | FloatPos | Block): boolean;

  /**
   * 模拟设置身体角度
   * @param rot 要设置的角度
   * @returns boolean 是否成功模拟操作
   */
  simulateSetBodyRotation(rot: number): boolean;

  /**
   * 相对玩家坐标系移动
   * @param pos 移动方向
   * @param speed （可选参数）移动速度，默认为1
   * @returns boolean 是否请求移动成功
   */
  simulateLocalMove(pos: IntPos | FloatPos, speed?: number): boolean;

  /**
   * 相对世界坐标系移动
   * @param pos 移动方向
   * @param speed （可选参数）移动速度，默认为1
   * @returns boolean 是否请求移动成功
   */
  simulateWorldMove(pos: IntPos | FloatPos, speed?: number): boolean;

  /**
   * 直线移动到坐标
   * @param pos 移动方向
   * @param speed （可选参数）移动速度，默认为1
   * @returns boolean 是否请求移动成功
   * **注：如需自动寻路，请考虑使用 模拟导航移动{@linkcode simulateNavigateTo}**
   */
  simulateMoveTo(pos: IntPos | FloatPos, speed?: number): boolean;

  /**
   * 模拟导航移动
   * @param target 导航目标
   * @param speed （可选参数）移动速度，默认为1
   * @returns Object 是否能到达指定位置以及导航路径
   */
  simulateNavigateTo(
    target: Entity | IntPos | FloatPos,
    speed?: number
  ): {
    isFullPath: boolean;
    path: Array<Array<number>>;
  };

  /**
   * 模拟导航移动（多目标）
   * @param target 导航目标
   * @param speed （可选参数）移动速度，默认为1
   * @returns boolean 是否成功模拟操作
   */
  simulateNavigateTo(
    target: Array<IntPos> | Array<FloatPos>,
    speed?: number
  ): boolean;

  /**
   * 模拟使用物品
   * @param target （可选参数）要使用的物品(或物品所在的槽)，默认为选中物品
   * @param pos （可选参数）目标坐标，默认为朝向方块坐标
   * @param face （可选参数）目标方块的面，默认为0
   * @param relative （可选参数）相对方块偏移坐标，默认为{0.5,0.5,0.5}
   */
  simulateUseItem(
    target?: Item | number,
    pos?: IntPos,
    face?: number,
    relative?: FloatPos
  ): boolean;

  /**
   * 模拟停止破坏方块
   * @returns boolean 是否成功模拟操作
   */
  simulateStopDestroyingBlock(): boolean;

  /**
   * 模拟停止交互
   * @returns boolean 是否成功模拟操作
   */
  simulateStopInteracting(): boolean;

  /**
   * 模拟停止移动
   * @returns boolean 是否成功模拟操作
   */
  simulateStopMoving(): boolean;

  /**
   * 模拟停止使用物品
   * @returns boolean 是否成功模拟操作
   */
  simulateStopUsingItem(): boolean;
}
