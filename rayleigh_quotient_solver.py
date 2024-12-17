import numpy as np

def rayleigh_quotient(A, x, tolerance=1e-6, max_iter=100):
    """
    レイリー商を用いて最大固有値を求める関数
    
    Args:
        A (np.ndarray): 対象の正方行列
        x (np.ndarray): 初期ベクトル
        tolerance (float): 許容誤差（収束条件）
        max_iter (int): 最大反復回数
    
    Returns:
        tuple: 最大固有値の近似値と対応する固有ベクトル
    """
    try:
        # 行列が正方行列であることを確認
        if A.shape[0] != A.shape[1]:
            raise ValueError("行列は正方行列である必要があります。")
        
        # 初期ベクトルの次元チェック
        if A.shape[0] != x.shape[0]:
            raise ValueError("初期ベクトルの次元が行列に一致していません。")
        
        print("\n=== レイリー商による最大固有値の計算 ===")
        x = x / np.linalg.norm(x)  # 初期ベクトルを正規化
        previous_r = 0  # 前回のレイリー商
        for i in range(1, max_iter + 1):
            # 行列とベクトルの積
            Ax = A @ x

            # レイリー商の計算
            r = (x.T @ Ax) / (x.T @ x)
            r = r.item()  # スカラー値に変換
            
            # ベクトルの正規化
            x_new = Ax / np.linalg.norm(Ax)

            print(f"反復 {i}: レイリー商 r ≈ {r:.6f}")
            print(f"正規化されたベクトル:\n{x_new}\n")

            # 収束条件のチェック
            if abs(r - previous_r) < tolerance:
                print("収束しました！")
                return r, x_new

            # 更新
            x = x_new
            previous_r = r
        
        print("最大反復回数に達しました。収束しませんでした。")
        return None, None
    except ValueError as e:
        print(f"入力エラー: {e}")
    except Exception as e:
        print(f"予期しないエラー: {e}")
    return None, None

def get_input():
    """行列と初期ベクトルを受け取る関数"""
    try:
        # 行列入力
        print("対象となる行列を入力してください（例: [[4, -1], [-1, 4]]）:")
        A_input = input()
        A = np.array(eval(A_input), dtype=float)

        # 初期ベクトル入力
        print("初期ベクトルを入力してください（例: [1, 0]）:")
        x_input = input()
        x = np.array(eval(x_input), dtype=float)

        # 行列とベクトルの次元チェック
        if len(x.shape) != 1:
            raise ValueError("初期ベクトルは1次元配列で入力してください。")
        x = x.reshape(-1, 1)  # 列ベクトルに変換
        
        return A, x
    except (SyntaxError, ValueError):
        print("入力が無効です。正しい形式で行列とベクトルを入力してください。")
    except Exception as e:
        print(f"予期しないエラー: {e}")
    return None, None

def main():
    print("=== レイリー商による最大固有値計算ツール ===")
    
    # 入力の取得
    A, x = get_input()
    if A is None or x is None:
        return

    # 収束条件と最大反復回数の設定
    try:
        tolerance = float(input("許容誤差（例: 1e-6）を入力してください（デフォルト: 1e-6）: ") or 1e-6)
        max_iter = int(input("最大反復回数（例: 100）を入力してください（デフォルト: 100）: ") or 100)
    except ValueError:
        print("無効な入力です。デフォルト値を使用します。")
        tolerance = 1e-6
        max_iter = 100

    # レイリー商の計算実行
    r, eigenvector = rayleigh_quotient(A, x, tolerance, max_iter)
    if r is not None and eigenvector is not None:
        print("\n最大固有値の近似値:")
        print(f"r ≈ {r:.6f}")
        print("\n対応する固有ベクトル:")
        print(eigenvector)
    else:
        print("計算に失敗しました。")


if __name__ == "__main__":
    main()