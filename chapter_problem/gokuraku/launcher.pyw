# アプリランチャー
# 16行目のメモ帳は取り出すことができない

import sys
import os
from subprocess import call
import tkinter as tk

# メイン関数


def main():
    ButtonDef = (
        #    ラベル  関数
        ("電卓", docalc),
        ("メモ帳", lambda e: call(r'notepad.exe ../text/amenimo.txt')),    # ラムダ式で関数名省略
        ("ヘロンの公式", doheron),
        ("エクスプローラ", doexplorer),
        ("終わり", sys.exit))

    root = tk.Tk()
    root.title("ランチャー")
    root.minsize(200, 100)    # 最小ウィンドウサイズ、
    # ボタンはこの幅まで横に延ばされる
    # ボタンの個数が増えると自動的に縦に延びる
    # ボタンを配置
    root.option_add('*Button.font', 'ＭＳゴシック 20')
    for (label, func) in ButtonDef:
        Button = tk.Button(text=label)
        Button.bind("<Button-1>", func)
        Button.pack(fill=tk.X)

    root.mainloop()

# ボタン毎の動作を定義（イベントドライバ群）


def docalc(e):                # 電卓を起動
    call(r'calc')


def doheron(e):                # pythonプログラムを起動
    call(r'python ./heron.py 135 352 377')


def doexplorer(e):            # エクスプローラを起動
    call(r'explorer.exe ' + os.getcwd())


if __name__ == '__main__':
    main()
