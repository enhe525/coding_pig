DATA_FILE = "draws.txt"


def load_signs():
    """读取已有签文列表"""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


try:
    count = int(input("你要加几个签？"))
    existing = load_signs()

    with open(DATA_FILE, "a", encoding="utf-8") as f:
        for _ in range(count):
            sign = input("你这个签要加什么？").strip()
            if not sign:
                print("  签文不能为空，跳过。")
                continue
            if sign in existing:
                print(f"  「{sign}」已经存在，跳过。")
                continue
            f.write(sign + "\n")
            existing.append(sign)
            print(f"  已添加：{sign}")

except Exception as e:
    print(f"出错了：{e}")
