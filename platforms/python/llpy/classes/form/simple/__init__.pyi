from typing import NoReturn, overload

class LLSE_SimpleForm:
    """普通表单构建器"""

    def __init__(self) -> NoReturn: ...
    def setTitle(self, title: str) -> LLSE_SimpleForm:
        """
        设置表单的标题

        Args:
            title: 表单的标题

        Returns:
            处理完毕的表单对象
        """
    def setContent(self, content: str) -> LLSE_SimpleForm:
        """
        设置表单的内容

        Args:
            content: 表单的文本内容

        Returns:
            处理完毕的表单对象
        """
    @overload
    def addButton(self, text: str) -> LLSE_SimpleForm:
        """
        向表单内增加一行按钮

        Args:
            text: 按钮文本的字符串

        Returns:
            处理完毕的表单对象
        """
    @overload
    def addButton(self, text: str, image: str) -> LLSE_SimpleForm:
        """
        向表单内增加一行按钮

        Args:
            text: 按钮文本的字符串
            image: 按钮图片所在路径。格式为 `textures/items/apple`(材质包路径) 或 `https://1919810.work/apple.png`(完整URL)

        Returns:
            处理完毕的表单对象
        """

SimpleForm = LLSE_SimpleForm
