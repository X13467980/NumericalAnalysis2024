# 26002304049 矢野陽大
# 固有値分解

import numpy as np

# 関数: 固有値行列Aと固有ベクトル行列Vを使って行列を復元する
def restration(A, V):
    
    """
    行列A (固有値の対角行列) と固有ベクトル行列Vを用いて元の行列を復元する。
    計算式: V * A * V.T
    """
    return V @ A @ V.T

# 固有値の対角要素を持つ対角行列 A
A = np.diag([1, 1])
print("固有値の対角要素は\n{}".format(A))

# 固有ベクトルを含む行列 V
V = np.array([
    [1/np.sqrt(2), 1/np.sqrt(2)],  # 第一固有ベクトル
    [-1/np.sqrt(2), 1/np.sqrt(2)]  # 第二固有ベクトル
])
print("固有ベクトル行列は\n{}".format(V))

# 関数を使って復元結果を求める
result = restration(A, V)
print("復元結果は\n{}".format(result))