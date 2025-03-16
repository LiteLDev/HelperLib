from llpy.types import T_ToJsonType

class KVDatabase:
    """
    键 - 值对 NoSQL 数据库

    底层使用 `LevelDB` 实现
    """

    def __init__(self, db_dir: str) -> None:
        """
        创建 / 打开一个键值对数据库

        一个 `LevelDB` 数据库是由多个文件组成的，所以你需要传入一个文件夹的路径，数据库文件会被储存于这个文件夹当中。
        如果这个目录已含有一个数据库，将打开它，否则会新建一个。

        Args:
            db_dir: 数据库的储存目录路径，以 BDS 根目录为基准。当给出的目录不存在时，将尝试自动逐层创建对应的目录路径
        """
    def set(self, name: str, data: T_ToJsonType) -> bool:
        """
        写入数据项

        Args:
            name: 数据项名字
            data: 要写入的数据

        Returns:
            是否写入成功
        """
    def get(self, name: str) -> T_ToJsonType | None:
        """
        读取数据项

        Args:
            name: 数据项名字

        Returns:
            _description_
        """
    def delete(self, name: str) -> bool:
        """
        删除数据项

        Args:
            name: 数据项名字

        Returns:
            是否成功删除
        """
    def listKey(self) -> list[str]:
        """
        获取所有数据项名字

        Returns:
            所有的数据项名字数组
        """
    def close(self) -> bool:
        """
        关闭数据库

        数据库关闭之后，请勿继续使用！

        Returns:
            是否成功关闭
        """
