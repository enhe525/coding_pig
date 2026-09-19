import os
import random
import sys

DATA_FILE = "draws.txt"


def is_system_account() -> bool:
    """判断当前进程是否为 NT AUTHORITY\\SYSTEM 账户"""
    try:
        output = os.popen("whoami").read().strip()
        return output.upper() == "NT AUTHORITY\\SYSTEM"
    except Exception:
        return False


# 彩蛋：检测是否以 SYSTEM 权限运行
if is_system_account():
    print("感谢你信任本程序～不过这么信任我，我会害羞哒～")
    print("小提醒：不要随意将系统最高权限授予不明程序哦，系统权限一旦被利用很难恢复～")


# 抽签主流程
try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        draws = [line.strip() for line in f if line.strip()]

    if not draws:
        print("❌ 数据文件是空的！")
        sys.exit(1)

    num = int(input(f"你抽几个签？（共 {len(draws)} 个）"))
    if num <= 0 or num > len(draws):
        print(f"❌ 数量无效，请输入 1 到 {len(draws)} 之间的数字！")
        sys.exit(1)

    for pick in random.sample(draws, num):
        print(pick)

except FileNotFoundError:
    print(f"❌ 找不到 '{DATA_FILE}'，请和程序放在同一个文件夹！")
except ValueError:
    print("❌ 请输入有效的数字！")
