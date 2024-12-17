# 26002304049 矢野陽大
# A^n行列の計算

import ast
import numpy as np

def a_n(matrix, n):
    try:
        return np.linalg.matrix_power(matrix, n)
    except np.linalg.LinAlgError:
        print("エラー: 逆行列が存在しないため負の乗数は計算できません。")
        return None

# 入力処理
try:
    print("対象となる行列を入力 (例: [[1, 2], [3, 4]]):")
    matrix_A_input = input()
    matrix_A = np.array(ast.literal_eval(matrix_A_input))
    if matrix_A.ndim != 2 or matrix_A.shape[0] != matrix_A.shape[1]:
        raise ValueError("エラー: 行列は正方行列である必要があります。")
    
    n = int(input("乗数:"))
    result = a_n(matrix_A, n)
    
    if result is not None:
        print(f"Aの{n}乗:")
        print(result)
except (ValueError, SyntaxError):
    print("入力エラー: 正しい形式で行列と乗数を入力してください。")