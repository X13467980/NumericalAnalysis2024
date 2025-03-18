# 固有値と固有ベクトル計算

import ast
import numpy as np

def eigen(A):
    try:
        # 固有値と固有ベクトルを計算
        eigenvalues, eigenvectors = np.linalg.eig(A)
        diagonal_matrix = np.diag(eigenvalues)

        # 結果を表示
        print("\n 固有値:")
        print(eigenvalues)
        print("\n 固有値からなる対角行列:")
        print(diagonal_matrix)
        print("\n 固有ベクトル:")
        print(eigenvectors)
    except np.linalg.LinAlgError as e:
        print(f"エラー: 行列の計算中に問題が発生しました ({e})")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

def get_matrix_input():
    while True:
        try:
            # ユーザーに行列入力を求める
            print("対象となる行列を入力してください (例: [[4, -2], [1, 1]]):")
            matrix_A_input = input()
            matrix_A = np.array(ast.literal_eval(matrix_A_input))

            # 入力が2次元配列か確認
            if matrix_A.ndim != 2:
                raise ValueError("行列は2次元配列である必要があります。")
            
            return matrix_A
        except (ValueError, SyntaxError):
            print("無効な入力です。正しい形式で2次元の行列を入力してください。")
        except Exception as e:
            print(f"予期しないエラー: {e}")

def main():
    print("=== 固有値・固有ベクトル計算ツール ===")
    matrix_A = get_matrix_input()
    eigen(matrix_A)
    print("\n計算が完了しました")

if __name__ == "__main__":
    main()