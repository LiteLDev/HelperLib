from typing import NoReturn

class LLSE_CustomForm:
    """自定义表单构建器"""

    def __init__(self) -> NoReturn: ...
    def setTitle(self, title: str) -> LLSE_CustomForm:
        """
        设置表单的标题

        Args:
            title: 表单的标题

        Returns:
            处理完毕的表单对象（便于连锁进行其他操作）
        """
    def addLabel(self, text: str) -> LLSE_CustomForm:
        """
        向表单内增加一行文本

        Args:
            text: 文本内容

        Returns:
            处理完毕的表单对象（便于连锁进行其他操作）
        """
    def addInput(
        self,
        title: str,
        placeholder: str = "",
        default: str = "",
    ) -> LLSE_CustomForm:
        """
        向表单内增加一行输入框

        Args:
            title: 输入框描述文本
            placeholder: 输入框内的提示字符
            default: 输入框中默认存在的内容

        Returns:
            处理完毕的表单对象（便于连锁进行其他操作）
        """
    def addSwitch(self, title: str, default: bool = False) -> LLSE_CustomForm:
        """
        向表单内增加一行开关选项

        Args:
            title: 开关选项描述文本
            default: 开关的默认状态 开 / 关

        Returns:
            处理完毕的表单对象（便于连锁进行其他操作）
        """
    def addDropdown(
        self,
        title: str,
        items: list[str],
        default: int = 0,
    ) -> LLSE_CustomForm:
        """
        向表单内增加一行下拉菜单

        Args:
            title: 下拉菜单描述文本
            items: 下拉菜单中的选项文本列表
            default: 下拉菜单默认选中的列表项序号。从 `0` 开始编号

        Returns:
            处理完毕的表单对象（便于连锁进行其他操作）
        """
    def addSlider(
        self,
        title: str,
        min_val: int,
        max_val: int,
        step: int = 1,
        default: int = 0,
    ) -> LLSE_CustomForm:
        """
        向表单内增加一行游标滑块

        Args:
            title: 游标滑块描述文本
            min_val: 游标滑块最小值
            max_val: 游标滑块最大值
            step: 游标滑块调整的最小分度值
            default: 游标滑块默认初始格数，数值必须在最小和最大格数之间。

        Returns:
            处理完毕的表单对象（便于连锁进行其他操作）
        """
    def addStepSlider(
        self,
        title: str,
        items: list[str],
        default: int = 0,
    ) -> LLSE_CustomForm:
        """
        向表单内增加一行步进滑块

        Args:
            title: 步进滑块描述文本
            items: 步进滑块的选项文本列表
            default: 步进滑块默认初始选项。序号从 `0` 开始编号

        Returns:
            处理完毕的表单对象（便于连锁进行其他操作）
        """

CustomForm = LLSE_CustomForm
