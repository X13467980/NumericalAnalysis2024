# 固有値分解

import numpy as np
import sympy as sp
import ast

def main():
    # 行列入力
    print("行列を入力してください (形式: [1, 2], [3, 4]):")
    A_input = input()
    A = np.array(ast.literal_eval(f"[{A_input}]"))  # 入力をリストとして評価
    
    print("\n入力された行列:")
    print(A)

    # 固有値分解
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print("\n固有値:")
    print(eigenvalues)

    print("\n固有ベクトル:")
    print(eigenvectors)

    n = sp.symbols('n')  # nを定義
    D = sp.diag(*[eigenval**n for eigenval in eigenvalues])  # D^nのシンボリック表現

    # 固有ベクトル行列Pとその逆行列
    P = sp.Matrix(eigenvectors)
    P_inv = P.inv()

    # A^n = P * D^n * P^(-1)
    A_n = P * D * P_inv

    print("\nA^n:")
    sp.pprint(A_n)

if __name__ == "__main__":
    main()