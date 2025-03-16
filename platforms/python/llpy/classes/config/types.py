T_ToIniType = int | float | str | bool
T_ToJsonBase = int | float | str | bool | None
T_ToJsonList = list["T_ToJsonType"]
T_ToJsonDict = dict[str, "T_ToJsonType"]
T_ToJsonType = T_ToJsonBase | T_ToJsonList | T_ToJsonDict
