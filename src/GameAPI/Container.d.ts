/// <reference path="../index.d.ts" />

declare class Container {
  /**容器拥有的格子总数 */
  readonly size: Integer;

  /**容器的类型名 */
  readonly type: string;

  /**
   * 放入物品对象到容器中
   * @param item 待增加的物品对象
   * @returns boolean 是否成功增加
   */
  addItem(item: Item): boolean;

  /**
   *放入物品对象到容器的第一个空格子
   * @param item 待增加的物品对象
   * @returns boolean 是否成功增加
   */
  addItemToFirstEmptySlot(item: Item): boolean;

  /**
   * 检查容器中是否（有空间）可以放入此物品
   * @param item 待放入的物品对象
   * @returns boolean 是否可以放入
   */
  hasRoomFor(item: Item): boolean;

  /**
   * 减少容器中的某个物品对象
   * @param index 减少的物品对象所在的格子序号
   * @param count 减少的数量。如果大于等于此格子物品堆叠的数量，则物品堆将被整个清除
   * @returns boolean 是否成功减少
   */
  removeItem(index: Integer, count: Integer): boolean;

  /**
   * 获取容器某个格子的物品对象
   * @param index 待获取的格子序号
   * @returns Item 格子位置的物品对象
   */
  getItem(index: Integer): Item;

  /**
   * 设置容器某个格子的物品对象
   * @param index 待设置的格子序号
   * @param item 待设置的物品对象
   * @returns boolean 是否设置成功
   */
  setItem(index: Integer, item: Item): boolean;

  /**
   * 获取容器所有格子的物品对象列表
   * @returns Array<Item> 容器中所有的物品对象
   * @tips 此处获取的物品对象均为引用。也就是说，修改此处返回的物品对象，或使用其API，就相当于直接操作容器中对应的物品
   */
  getAllItems(): Array<Item>;

  /**
   * 清空容器
   * @returns boolean 是否成功清空
   */
  removeAllItems(): boolean;

  /**
   * 判断容器是否为空
   * @returns boolean 判断容器是否为空
   */
  isEmpty(): boolean;
}
