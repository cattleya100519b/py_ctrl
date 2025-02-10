def disp_mat(name_mat: str, mat: any) -> None:
    """jupyter notebook 内で行列を LaTeX 表示で出力する関数
    
    Args:
        name_mat (str): LaTeX 文字列
        mat: 数値配列 (numpy.ndarray, list, etc.)
    """
    from IPython.display import display, Math
    from sympy import latex, Matrix
    import numpy as np

    # スカラーの場合はそのまま表示
    if np.isscalar(mat):
        display(Math(f'{name_mat}={latex(mat)}'))
        return

    # 数値配列 >> sympy.Matrix object >> LaTeX 文字列 >> display-object
    display(Math(f'{name_mat}={latex(Matrix(mat))}'))