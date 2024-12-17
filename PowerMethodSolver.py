# 26002304049 矢野陽大
# 冪乗計算

import numpy as np

def power_method(matrix, v, limit=0.001, max_iter=100):
    """
    冪乗法で最大固有値と対応する固有ベクトルを計算する関数
    
    Args:
        matrix (np.ndarray): 対象の行列
        v (np.ndarray): 初期ベクトル
        limit (float): 収束の許容誤差
        max_iter (int): 最大反復回数
        
    Returns:
        tuple: 最大固有値と固有ベクトル (r, v)
    """
    try:
        # 入力行列の正方行列チェック
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("行列は正方行列である必要があります。")
        
        # 初期ベクトルの次元チェック
        if matrix.shape[0] != v.shape[0] or v.shape[1] != 1:
            raise ValueError("初期ベクトルの次元が行列に一致していません。")

        n = 0
        print("\n=== 冪乗法による固有値計算 ===")
        print(f"許容誤差: {limit}, 最大反復回数: {max_iter}\n")

        # 正規化された初期ベクトル
        v = v / np.linalg.norm(v)

        while n < max_iter:
            # 行列とベクトルの掛け算
            x = np.dot(matrix, v)
            r = np.linalg.norm(x)  # 固有値の近似値（ベクトルのノルム）

            # ベクトルの正規化
            v_new = x / r

            print(f"反復 {n + 1}: 固有値 r ≈ {r:.6f}")
            print(f"固有ベクトルの近似:\n{v_new}\n")

            # 収束条件のチェック
            if np.linalg.norm(v_new - v) < limit:
                print("収束しました！")
                return r, v_new

            v = v_new  # ベクトルの更新
            n += 1

        print("最大反復回数に達しました。収束しませんでした。")
        return None, None

    except ValueError as e:
        print(f"入力エラー: {e}")
    except Exception as e:
        print(f"予期しないエラー: {e}")
    return None, None


def get_matrix_input():
    """行列と初期ベクトルの入力を受け付ける関数"""
    try:
        # 行列入力
        print("対象となる行列を入力してください（例: [[4, 1], [2, 3]]）:")
        matrix_input = input()
        matrix = np.array(eval(matrix_input))

        # 初期ベクトル入力
        print("初期ベクトルを入力してください（例: [[1], [1]]）:")
        vector_input = input()
        v = np.array(eval(vector_input))

        return matrix, v
    except (SyntaxError, ValueError):
        print("入力が無効です。正しい形式で行列とベクトルを入力してください。")
        return None, None
    except Exception as e:
        print(f"予期しないエラー: {e}")
        return None, None


def main():
    print("=== 最大固有値と固有ベクトルの計算ツール ===")
    
    # 行列と初期ベクトルの入力
    matrix, v = get_matrix_input()
    if matrix is None or v is None:
        return
    
    # パラメータ入力（任意）
    try:
        limit = float(input("許容誤差（例: 0.001）を入力してください（デフォルト: 0.001）: ") or 0.001)
        max_iter = int(input("最大反復回数（例: 100）を入力してください（デフォルト: 100）: ") or 100)
    except ValueError:
        print("無効な入力です。デフォルト値を使用します。")
        limit = 0.001
        max_iter = 100

    # 冪乗法の実行
    r, v = power_method(matrix, v, limit, max_iter)
    if r is not None and v is not None:
        print("\n最大固有値の近似値:")
        print(f"r ≈ {r:.6f}")
        print("\n対応する固有ベクトル:")
        print(v)
    else:
        print("計算に失敗しました。")


if __name__ == "__main__":
    main()