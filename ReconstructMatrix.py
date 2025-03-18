# 行列の再構築


import numpy as np
def restration(A, V):
    return V @ A @ V.T

# 固有値の対角要素を出力
A = np.diag([5, 3])
print("固有値の対角要素\n{}".format(A))

# 固有ベクトル出力
V = np.array([[1/np.sqrt(2), -1/np.sqrt(2)],[1/np.sqrt(2), 1/np.sqrt(2)]])
print(V)
print("固有ベクトル\n{}".format(V))

#計算結果を出力
print("結果\n{}".format(restration(A,V)))
