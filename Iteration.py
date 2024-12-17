# 26002304049 矢野陽大
# 反復法

import sympy as sp

def generate_iteration_function(fx_expr, x_symbol):

    #パラメータ
    #   fx_expr (sympy expression): 入力関数 f(x)
    #   x_symbol (sympy symbol): x のシンボル
    #   g (function): 反復法の反復式 g(x)
        
    # f'(x) の導関数を計算
    f_prime = sp.diff(fx_expr, x_symbol)
    
    # 反復法の反復式 g(x) = x - f(x) / f'(x)
    gx_expr = x_symbol - fx_expr / f_prime
    print(f"反復式 g(x): {gx_expr}")
    
    # 反復式をPython関数に変換
    g_func = sp.lambdify(x_symbol, gx_expr, 'math')
    return g_func

if __name__ == "__main__":
    # シンボルの定義
    x = sp.symbols('x')
    
    # ユーザー入力: f(x)
    fx_input = input("f(x)を入力してください（例: x**2 - 2）: ")
    fx = sp.sympify(fx_input)
    
    # 反復式 g(x) を生成
    g = generate_iteration_function(fx, x)
    
    x0 = float(input("初期値を入力してください: "))
    tol = 1e-6
    max_iter = 100

    print("\n反復法の実行:")
    for i in range(max_iter):
        x_next = g(x0)
        print(f"Iteration {i+1}: x = {x_next}")
        if abs(x_next - x0) < tol:  # 収束判定
            print("収束")
            break
        x0 = x_next
    else:
        print("収束しない")