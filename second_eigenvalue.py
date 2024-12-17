import ast
import numpy as np

def eigen(A):
    try:
        # 固有値と固有ベクトルを計算
        eigenvalues, eigenvectors = np.linalg.eig(A)
        
        # 固有値と固有ベクトルをソート（大きい順）
        sorted_pairs = sorted(zip(eigenvalues, eigenvectors.T), key=lambda x: x[0], reverse=True)
        max_eigenvalue, max_eigenvector = sorted_pairs[0]
        
        # 最大固有ベクトルの影響を取り除いた行列A'
        max_eigenvector_transposed = np.expand_dims(max_eigenvector, axis=1)  # 列ベクトルにする
        A_dash = A - max_eigenvalue * np.dot(max_eigenvector_transposed, max_eigenvector_transposed.T)
        
        return A_dash
    except Exception as e:
        print(f"エラー: 固有値と固有ベクトルの計算中に問題が発生しました。({e})")
        return None

def eigenValue(result):
    try:
        # A'の固有値を計算し、最大固有値を返す
        eigenvalues, _ = np.linalg.eig(result)
        return max(eigenvalues)
    except Exception as e:
        print(f"エラー: 2番目の固有値の計算中に問題が発生しました。({e})")
        return None

def get_matrix_input():
    while True:
        try:
            # ユーザーに行列の入力を求める
            print("対象となる行列を入力してください（例: [[4, -2], [1, 1]]）:")
            matrix_A_input = input()
            matrix_A = np.array(ast.literal_eval(matrix_A_input))

            # 入力が2次元正方行列か確認
            if matrix_A.ndim != 2 or matrix_A.shape[0] != matrix_A.shape[1]:
                raise ValueError("行列は正方の2次元配列である必要があります。")
            
            return matrix_A
        except (ValueError, SyntaxError):
            print("無効な入力です。正しい形式で正方行列を入力してください。")
        except Exception as e:
            print(f"予期しないエラー: {e}")

def main():
    print("=== 2番目の固有値計算ツール ===")
    
    # ユーザーから行列の入力を受け取る
    matrix_A = get_matrix_input()
    
    # 最大固有ベクトルの影響を除去した行列を計算
    result = eigen(matrix_A)
    if result is not None:
        print("\nAダッシュ (最大固有ベクトルの影響を除去した行列):")
        print(result)
        
        # 2番目の固有値を計算
        result2 = eigenValue(result)
        if result2 is not None:
            print("\n2番目の固有値:")
            print(result2)
        else:
            print("2番目の固有値の計算に失敗しました。")
    else:
        print("Aダッシュの計算に失敗しました。")

    print("\n計算が完了しました")

if __name__ == "__main__":
    main()