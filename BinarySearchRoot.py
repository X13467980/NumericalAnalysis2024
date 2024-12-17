# 26002304049 矢野陽大
# 二分法

def binary_search(f, a, b, limit=0.01, max_iter=50):
    
    # 二分法で f(x) = 0 の解を求める
    # パラメータ
    #   f: 目的関数 (lambda形式で受け取る)
    #   a: 初期区間の下端
    #   b: 初期区間の上端
    #   limit: 収束条件（区間幅がこれ以下になると終了）
    #   max_iter: 最大反復回数
    
    num = 0

    # 解の存在チェック
    if f(a) * f(b) > 0:
        print("Error: 初期区間 [a, b] に解が存在しません")
        return None

    while (b - a) > limit and num < max_iter:
        c = (a + b) / 2.0  # 中点の計算

        print(f"{num + 1}回目: 区間 a = {a}, b = {b}, 中点 c ≈ {c}")

        # 収束判定（f(c) ≈ 0）
        if abs(f(c)) < 1e-8:  # 関数値が十分小さい場合
            return round(c, 5)

        # 解の存在する区間を絞る
        if f(a) * f(c) < 0:
            b = c  # 左側に解が存在
        else:
            a = c  # 右側に解が存在

        num += 1

    c = (a + b) / 2.0
    print(f"\n終了: {num}回目で x ≈ {c} (精度: {limit})")
    return round(c, 5)


# 実行部
if __name__ == '__main__':
    try:
        print("\n例: x^2 - 5 の場合、lambda x: x**2 - 5 と入力")
        func_input = input("関数 f(x) をPython形式で入力: ")
        f = eval(func_input)
        
        # 初期条件
        a = float(input("初期区間の下端 a を入力: "))
        b = float(input("初期区間の上端 b を入力: "))
        limit = float(input("収束条件 (精度 limit) を入力 (例: 0.01): "))
        max_iter = int(input("最大反復回数を入力 (例: 50): "))

        print("\n--- 二分法の実行 ---\n")
        solution = binary_search(f, a, b, limit, max_iter)
        if solution is not None:
            print(f"\n関数 f(x) = {func_input} の近似解は x ≈ {solution}")
    except ValueError:
        print("Error: 数値を正しく入力してください。")
    except Exception as e:
        print(f"予期しないエラー: {e}")