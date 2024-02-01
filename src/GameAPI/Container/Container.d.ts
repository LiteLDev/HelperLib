/// <reference path="../../index.d.ts" />

/**
 * ### 👜 容器对象
 *
 * 在LLSE中，使用「容器对象」来操作拥有格子、可以储存和放置物品的容器的相关信息。
 *
 * 此处的 **容器** 是一种宽泛的概念，除了箱子、桶这些传统的容器之外，如玩家物品栏、羊驼携带的箱子等这些也统统可以作为「容器」处理，获取并使用容器对应的API
 *
 * **注意**：在修改完玩家物品栏对应的物品之后，不要忘记使用玩家对象的成员函数{@linkcode Player.refreshItems()}，刷新客户端显示的玩家物品栏
 *
 * **注意**：不要长期保存一个容器对象\
 * 当容器对象对应的实体 / 方块被销毁时，对应的容器对象将变得无效。\
 * 因此，如果有长期操作某个容器的需要，请通过上述途径获取实时的容器对象
 *
 * 该类**没有构造函数**，请通过事件或API获取
 *
 * @see [👜 容器对象 API](https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/GameAPI/Container)
 */
declare class Container {
  /** 容器拥有的格子总数 */
  readonly size: number;

  /** 容器的类型名 */
  readonly type: string;

  /**
   * ### 放入物品对象到容器中
   *
   * **注意**：在修改完玩家物品栏对应的物品之后，不要忘记使用玩家对象的成员函数{@linkcode Player.refreshItems()}，刷新客户端显示的玩家物品栏
   *
   * @param item 待增加的物品对象
   *
   * @returns 是否成功增加
   */
  addItem(item: Item): boolean;

  /**
   * ### 放入物品对象到容器的第一个空格子
   *
   * **注意**：此函数将不会堆叠至容器内现有的物品堆中
   *
   * **注意**：在修改完玩家物品栏对应的物品之后，不要忘记使用玩家对象的成员函数{@linkcode Player.refreshItems()}，刷新客户端显示的玩家物品栏
   *
   * @param item 待增加的物品对象
   *
   * @returns 是否成功增加
   */
  addItemToFirstEmptySlot(item: Item): boolean;

  /**
   * ### 检查容器中是否（有空间）可以放入此物品
   *
   * @param item 待放入的物品对象
   *
   * @returns 是否可以放入
   */
  hasRoomFor(item: Item): boolean;

  /**
   * ##d 减少容器中的某个物品对象
   *
   * @param index 减少的物品对象所在的格子序号
   * @param count 减少的数量。如果大于等于此格子物品堆叠的数量，则物品堆将被整个清除
   *
   * @returns 是否成功减少
   */
  removeItem(index: number, count: number): boolean;

  /**
   * ### 获取容器某个格子的物品对象
   *
   * 此处获取的物品对象为引用。也就是说，修改此处返回的物品对象，或使用其API，就相当于直接操作容器中对应的物品
   *
   * **注意**：在修改完玩家物品栏对应的物品之后，不要忘记使用玩家对象的成员函数{@linkcode Player.refreshItems()}，刷新客户端显示的玩家物品栏
   *
   * @param index 待获取的格子序号
   *
   * @returns 格子位置的物品对象
   */
  getItem(index: number): Item;

  /**
   * ### 设置容器某个格子的物品对象
   *
   * **注意**：在修改完玩家物品栏对应的物品之后，不要忘记使用玩家对象的成员函数{@linkcode Player.refreshItems()}，刷新客户端显示的玩家物品栏
   *
   * @param index 待设置的格子序号
   * @param item 待设置的物品对象
   *
   * @returns 是否设置成功
   */
  setItem(index: number, item: Item): boolean;

  /**
   * ### 获取容器所有格子的物品对象列表
   *
   * 此处获取的物品对象均为引用。也就是说，修改此处返回的物品对象，或使用其API，就相当于直接操作容器中对应的物品
   *
   * **注意**：在修改完玩家物品栏对应的物品之后，不要忘记使用玩家对象的成员函数{@linkcode Player.refreshItems()}，刷新客户端显示的玩家物品栏
   *
   * @returns 容器中所有的物品对象
   */
  getAllItems(): Array<Item>;

  /**
   * ### 清空容器
   *
   * **注意**：在修改完玩家物品栏对应的物品之后，不要忘记使用玩家对象的成员函数{@linkcode Player.refreshItems()}，刷新客户端显示的玩家物品栏
   *
   * @returns 是否成功清空
   */
  removeAllItems(): boolean;

  /**
   * ### 判断容器是否为空
   *
   * @returns 判断容器是否为空
   */
  isEmpty(): boolean;

  /**
   * @deprecated
   * @alias {@linkcode getItem()}
   */
  getSlot(index: number): Item;

  /**
   * @deprecated
   * @alias {@linkcode getAllItems()}
   */
  getAllSlots(): Array<Item>;

  asPointer(): NativePointer;
}

declare class LLSE_Container extends Container {}