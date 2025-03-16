from typing import TypedDict

T_MoneyHistory = TypedDict(
    "T_MoneyHistory",
    {
        "from": str,  # 此项交易的发起者玩家 XUID
        "to": str,  # 此项交易的接收者玩家 XUID
        "money": int,  # 此项交易的金额
        "time": str,  # 此项交易发生时的时间字符串，格式为：YYYY-mm-dd hh:mm:ss
        "note": str,  # 此交易的附加说明信息
    },
)
"""`money.getHistory()` 返回的历史账单信息"""
