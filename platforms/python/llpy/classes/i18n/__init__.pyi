from typing import Any, NoReturn, overload

from .types import T_I18NJson

class i18n:
    """国际化 API"""

    def __init__(self) -> NoReturn: ...
    @staticmethod
    def tr(key: str, *args: Any) -> str:
        """
        使用默认语言翻译文本并格式化

        注意：格式化应遵循 [语法](https://fmt.dev/latest/syntax.html)

        Args:
            key: 文本或 ID
            args: 格式化参数

        Raises:
            参数无效

        Returns:
            翻译并格式化后的文本
        """
    @staticmethod
    def trl(locale_name: str, key: str, *args: Any) -> str:
        """
        使用指定语言翻译文本并格式化

        注意：格式化应遵循 [语法](https://fmt.dev/latest/syntax.html)

        Args:
            locale_name: 目标语言
            key: 文本或 ID
            args: 格式化参数

        Raises:
            参数无效

        Returns:
            翻译并格式化后的文本
        """
    @overload
    @staticmethod
    def get(key: str) -> str:
        """
        获取文本的翻译

        目标语言默认为 `default_locale_name`

        Args:
            key: 文本或 ID

        Raises:
            参数无效

        Returns:
            翻译内容（若经过多次回落仍未找到翻译，则返回 `key`）
        """
    @overload
    @staticmethod
    def get(key: str, locale_name: str) -> str:
        """
        获取文本的指定语言翻译

        Args:
            key: 文本或 ID
            locale_name: 目标语言

        Raises:
            参数无效

        Returns:
            翻译内容（若经过多次回落仍未找到翻译，则返回 `key`）
        """
    @overload
    @staticmethod
    def load(path: str) -> bool:
        """
        加载翻译数据

        默认跟随系统语言

        Args:
            path: 翻译数据所在的 文件 / 目录（目录内应全部为 `{locale_name}.json` 文件）

        Raises:
            参数无效

        Returns:
            是否载入成功
        """
    @overload
    @staticmethod
    def load(path: str, default_locale_name: str) -> bool:
        """
        加载翻译数据

        Args:
            path: 翻译数据所在的 文件 / 目录（目录内应全部为 `{locale_name}.json` 文件）
            default_locale_name: 默认的语言名称，形如 `zh_CN` 或 `en`。若传入空字符串，则默认跟随系统语言。如果没有提供目标语言给 `i18n.tr` 或 `i18n.get` 的翻译，这个参数将被使用

        Raises:
            参数无效

        Returns:
            是否载入成功
        """
    @overload
    @staticmethod
    def load(
        path: str,
        default_locale_name: str,
        default_lang_data: T_I18NJson,
    ) -> bool:
        """
        加载翻译数据

        Args:
            path: 翻译数据所在的 文件 / 目录（目录内应全部为 `{locale_name}.json` 文件）
            default_locale_name: 默认的语言名称，形如 `zh_CN` 或 `en`。若传入空字符串，则默认跟随系统语言。如果没有提供目标语言给 `i18n.tr` 或 `i18n.get` 的翻译，这个参数将被使用
            default_lang_data: 该参数将用于补全或创建翻译文件

        Raises:
            参数无效

        Returns:
            是否载入成功
        """
