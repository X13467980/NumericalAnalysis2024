import numpy as np

def newton_method(f_str, df_str, x0, accuracy=0.001, max_iterations=100):
    """
    ニュートン法を用いて f(x) = 0 の解を求める関数。
    
    Args:
        f_str (str): 解く関数の式 (例: "x**2 - 10*np.sin(x) - 2")
        df_str (str): 関数の微分の式 (例: "2*x - 10*np.cos(x)")
        x0 (float): 初期値
        accuracy (float): 許容される誤差（収束条件）
        max_iterations (int): 最大反復回数
    
    Returns:
        float: 解の近似値
    """
    def f(x):
        return eval(f_str)

    def df(x):
        return eval(df_str)

    x = x0
    n = 1

    print("=== ニュートン法による方程式の解法 ===")
    print(f"初期値: x0 = {x0}, 許容誤差: {accuracy}, 最大反復回数: {max_iterations}\n")
    
    while n <= max_iterations:
        try:
            # 微分値が0に近い場合の処理
            if abs(df(x)) < 1e-10:
                raise ZeroDivisionError("f'(x) が0に近いため、計算が不安定です。初期値を変更してください。")

            # ニュートン法の反復計算
            x_new = x - f(x) / df(x)
            print(f"{n}回目: x = {x_new:.6f}, f(x) = {f(x_new):.6f}")

            # 収束判定
            if abs(f(x_new)) < accuracy:
                print("\n収束しました！")
                return x_new

            # 更新
            x = x_new
            n += 1

        except ZeroDivisionError as e:
            print(f"エラー: {e}")
            return None
        except Exception as e:
            print(f"予期しないエラー: {e}")
            return None

    print("\n⚠️ 最大反復回数に達しました。解が収束しませんでした。")
    return None

def main():
    try:
        # ユーザーから解く関数とその微分を入力
        print("方程式 f(x) = 0 を解きます。")
        f_str = input("解く関数 f(x) を入力してください（例: x**2 - 10*np.sin(x) - 2）: ")
        df_str = input("f(x) の微分 df(x) を入力してください（例: 2*x - 10*np.cos(x)）: ")
        
        # 初期値、精度、最大反復回数を入力
        x0 = float(input("初期値 x0 を入力してください: "))
        accuracy = float(input("許容誤差（例: 0.001）を入力してください: ") or 0.001)
        max_iterations = int(input("最大反復回数（例: 100）を入力してください: ") or 100)
        
        # ニュートン法の実行
        result = newton_method(f_str, df_str, x0, accuracy, max_iterations)
        if result is not None:
            print(f"\n解の近似値: x = {result:.6f}")
        else:
            print("解を求めることができませんでした。")
    except ValueError:
        print("入力が無効です。数値を入力してください。")
    except Exception as e:
        print(f"予期しないエラー: {e}")

if __name__ == "__main__":
    main()