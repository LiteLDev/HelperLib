/// <reference path="../index.d.ts" />

declare class SimpleForm {
  /**
   * 设置表单的标题
   * @param title 表单的标题
   * @returns SimpleForm 处理完毕的表单对象（便于连锁进行其他操作）
   */
  setTitle(title: string): SimpleForm;

  /**
   * 设置表单的内容
   * @param content 表单的标题
   * @returns SimpleForm 处理完毕的表单对象（便于连锁进行其他操作）
   */
  setContent(content: string): SimpleForm;

  /**
   * 向表单内增加一行按钮
   * @param text 按钮文本的字符串
   * @param image （可选参数）按钮图片所在路径
   * @returns SimpleForm 处理完毕的表单对象（便于连锁进行其他操作）
   */
  addButton(text: string, image?: string): SimpleForm;
}

declare class CustomForm {
  /**
   * 设置表单的标题
   * @param title 表单的标题
   * @returns CustomForm 处理完毕的表单对象（便于连锁进行其他操作）
   */
  setTitle(title: string): CustomForm;

  /**
   * 向表单内增加一行文本
   * @param text 一行文本
   * @returns CustomForm 处理完毕的表单对象（便于连锁进行其他操作）
   */
  addLabel(text: string): CustomForm;

  /**
   * 向表单内增加一行输入框
   * @param title 输入框描述文本
   * @param placeholder （可选参数）输入框内的提示字符
   * @param _default （可选参数）输入框中默认存在的内容
   * @returns CustomForm 处理完毕的表单对象（便于连锁进行其他操作）
   */
  addInput(title: string, placeholder?: string, _default?: string): CustomForm;

  /**
   * 向表单内增加一行开关选项
   * @param title 开关选项描述文本
   * @param _default （可选参数）开关的默认状态 开 / 关
   * @returns CustomForm 处理完毕的表单对象（便于连锁进行其他操作）
   */
  addSwitch(title: string, _default?: boolean): CustomForm;

  /**
   * 向表单内增加一行下拉菜单
   * @param title 下拉菜单描述文本
   * @param items 下拉菜单中的选项文本列表
   * @param _default （可选参数）下拉菜单默认选中的列表项序号。
   * @returns CustomForm 处理完毕的表单对象（便于连锁进行其他操作）
   */
  addDropdown(
    title: string,
    items: Array<string>,
    _default?: number
  ): CustomForm;

  /**
   * 向表单内增加一行游标滑块
   * @param title 游标滑块描述文本
   * @param min 游标滑块最小值
   * @param max 游标滑块最大值
   * @param step （可选参数）游标滑块调整的最小分度值，默认为1
   * @param _default （可选参数）游标滑块默认初始格数，数值必须在最小和最大格数之间。
   * @returns CustomForm 处理完毕的表单对象（便于连锁进行其他操作）
   */
  addSlider(
    title: string,
    min: number,
    max: number,
    step?: number,
    _default?: number
  ): CustomForm;

  /**
   * 向表单内增加一行步进滑块
   * @param title 步进滑块描述文本
   * @param items 步进滑块的选项文本列表
   * @param _default （可选参数）步进滑块默认初始选项。序号从0开始编号
   */
  addStepSlider(
    title: string,
    items: Array<string>,
    _default?: number
  ): CustomForm;
}

declare namespace mc {
  /**
   * 创建表单对象
   * @returns SimpleForm 新创建的空白表单对象
   */
  function newSimpleForm(): SimpleForm;

  /**
   * 创建表单对象
   * @returns CustomeForm 新创建的空白表单对象
   */
  function newCustomForm(): CustomForm;
}
declare class LLSE_SimpleForm extends SimpleForm {}
declare class LLSE_CustomForm extends CustomForm {}
