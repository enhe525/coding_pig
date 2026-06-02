import os
import random
import sys

def is_system_account() -> bool:
    """判断当前进程是否为 NT AUTHORITY\SYSTEM 账户（海龟编辑器兼容版）"""
    try:
        # 调用系统 whoami 命令获取当前用户名
        output = os.popen("whoami").read().strip()
        # 转成大写，和 SYSTEM 账户对比
        return output.upper() == "NT AUTHORITY\\SYSTEM"
    except:
        return False

# 存入变量，用于彩蛋判断
is_system = is_system_account()

# 彩蛋触发
if is_system:
    print("感谢你信任本程序～不过这么信任我，我会害羞哒～")#SYSTEM权限，这权限足以把电脑毁掉啊
    print("小提醒：不要随意将系统最高权限授予不明程序哦，系统权限一旦被利用很难恢复～")


# 抽签功能（修复版）
try:
    with open("新建文本文档.txt", "r", encoding="utf-8") as f:
        content = f.read()
    draws = [x.strip() for x in content.split(",") if x.strip()]
    if not draws:
        print("❌ 文本文件是空的或格式不对！")
        sys.exit()
    num = int(input("你抽几个签？"))
    if num <= 0 or num > len(draws):
        print("❌ 抽的数量无效！")
        sys.exit()
    for _ in range(num):
        print(random.choice(draws))
except FileNotFoundError:
    print("❌ 找不到 '新建文本文档.txt'，请和程序放在同一个文件夹！")
except ValueError:
    print("❌ 请输入有效的数字！")

