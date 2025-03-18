# 行列の再構築

import numpy as np
import math

def reconstruct_matrix(eigenvalues, eigenvectors):

    # 固有値を対角行列Dに変換
    D = np.diag(eigenvalues)
    
    # 固有ベクトルをP行列に変換
    P = np.array(eigenvectors)
    
    # Pの逆行列を計算
    P_inv = np.linalg.inv(P)
    
    # 行列Aを再構築 (A = P * D * P_inv)
    A = np.dot(np.dot(P, D), P_inv)
    
    return A

# --- 入力 ---

# 固有値
eigenvalues = [2, 0]  # 2つの固有値
# 固有ベクトル (各列が固有ベクトルを表す)
eigenvectors = [
    [1/math.sqrt(2), 1/math.sqrt(2)],  # 第1固有ベクトル
    [1/math.sqrt(2), -1/math.sqrt(2)]   # 第2固有ベクトル
]

# 元の行列を再構築
A = reconstruct_matrix(eigenvalues, eigenvectors)

# 結果を表示
print("再構築された行列 A:")
print(A)