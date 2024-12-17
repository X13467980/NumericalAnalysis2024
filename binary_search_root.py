# 26002304049 矢野陽大
# 二分法

def f(x, target):
    """ 任意の数値 target の平方根を求めるための関数 """
    return x**2 - target

def binarySearch(f, a, b, target, limit=0.01, max_iter=50):
    """
    二分法で関数 f(x) = 0 の近似解を求める
    f: 解を求めたい関数
    a, b: 初期区間
    target: 目標値 (例: √target を求めたい数値)
    limit: 解の精度（区間幅がこれ以下になると終了）
    max_iter: 最大反復回数
    """
    num = 0
    if f(a, target) * f(b, target) > 0:  # 解が存在するかのチェック
        print("Error: 解がこの区間に存在しない可能性があります。")
        return None
    
    print(f"{num}回目: 初期区間 {a} <= x <= {b}")
    while (b - a) > limit and num < max_iter:
        c = (a + b) / 2.0  # 中点
        if f(c, target) == 0:  # 完全な解を発見
            return c
        elif f(a, target) * f(c, target) < 0:  # 解が左側にある場合
            b = c
        else:  # 解が右側にある場合
            a = c
        
        num += 1
        print(f"{num}回目: 区間を更新 a = {a}, b = {b}")
    
    c = (a + b) / 2.0
    print(f"終了: {num}回目で x ≈ {c}")
    return round(c, 2)  # 小数点2桁で丸める

# メイン実行部
if __name__ == '__main__':
    print("任意の数値の平方根を二分法で求めます。")
    try:
        target = float(input("目標値（例: 5 なら √5 を求めます）: "))
        a = float(input("初期区間の下端 a を入力: "))
        b = float(input("初期区間の上端 b を入力: "))
        limit = float(input("収束条件 (精度 limit) を入力 (例: 0.01): "))
        max_iter = int(input("最大反復回数を入力 (例: 50): "))
        
        print("\n--- 二分法の実行 ---\n")
        solution = binarySearch(f, a, b, target, limit, max_iter)
        if solution is not None:
            print(f"\n√{target} の近似解は x ≈ {solution}")
    except ValueError:
        print("エラー: 数値を正しく入力してください。")