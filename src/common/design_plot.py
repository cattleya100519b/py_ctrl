"""ch4以降で使用するプロット関連の関数をまとめたモジュール
"""
from typing import List, Tuple
from matplotlib.axes import Axes


def linestyle_generator():
    """ラインスタイルを無限に生成するジェネレータ関数
    """
    linestyle = ['-', '--', '-.', ':']
    lineID = 0
    while True:
        yield linestyle[lineID]
        lineID = (lineID + 1) % len(linestyle)


def plot_set(fig_ax: Axes, *args: Tuple[str]):
    """プロットの設定をまとめて行う関数

    Parameters
    ----------
    fig_ax : matplotlib.axes.Axes
        グラフのAxes
    args : tuple
        プロットの設定をまとめたタプル
        args[0] : str
            x軸ラベル
        args[1] : str
            y軸ラベル
        args[2] : str, optional
            凡例の位置
    """
    if l:=len(args) == 2 or l == 3:
        pass
    else:
        raise Exception('args length must be 2 or 3')
    
    if type(fig_ax) == Axes:
        pass
    else:
        raise Exception('fig_ax must be Axes')

    fig_ax.set_xlabel(args[0]) # x軸ラベルを第2引数で設定
    fig_ax.set_ylabel(args[1]) # y軸ラベルを第3引数で設定
    fig_ax.grid(ls=':')
    if len(args) > 2:
        fig_ax.legend(loc=args[2]) # 凡例の位置を第4引数で設定


def bodeplot_set(fig_ax: List[Axes], *args: Tuple[str]):
    """ボード線図の設定をまとめて行う関数

    Parameters
    ----------
    fig_ax : matplotlib.axes.Axes
        ゲイン線図と位相線図のAxes
    args : tuple
        プロットの設定をまとめたタプル
        args[0] : str, optional
            ゲイン線図の凡例位置
        args[1] : str, optional
            位相線図の凡例位置
    """
    if 0 <= len(args) <= 2:
        pass
    else:
        raise Exception('args length must be 0 or 1 or 2')
    
    if len(fig_ax) == 2:
        pass
    else:
        raise Exception('fig_ax length must be 2')
    
    # ゲイン線図の設定
    fig_ax[0].grid(which='both', ls=':')
    fig_ax[0].set_ylabel('Gain [dB]')
    # 位相線図の設定
    fig_ax[1].grid(which='both', ls=':')
    fig_ax[1].set_xlabel('$\\omega$ [rad/s]')
    fig_ax[1].set_ylabel('Phase [deg]')
    # 凡例の設定
    if len(args) > 0:
        fig_ax[0].legend(loc=args[0]) # ゲイン線図の凡例位置を第2引数で設定
    if len(args) > 1:
        fig_ax[1].legend(loc=args[1]) # 位相線図の凡例位置を第3引数で設定