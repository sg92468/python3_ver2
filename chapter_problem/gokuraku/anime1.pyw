# 背景画像を表示

import sys
import tkinter as tk
from PIL import Image, ImageTk

# GUI設定
root = tk.Tk()
root.title("アニメーション")

# キャンバスを作成
cvs = tk.Canvas(root, width=640, height=480)
cvs.pack()

# 画像を作成
sky = ImageTk.PhotoImage(Image.open("sky.bmp"))

# 画像をキャンバスに配置
cvs.create_image(0, 0, image=sky, anchor=tk.NW)

root.update()    # 画像を更新（チラつき防止）

root.mainloop()
