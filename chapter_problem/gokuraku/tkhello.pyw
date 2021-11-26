# 「Hello, World!」（tkinter版）

import sys
import tkinter as tk

# メイン関数


def main():
    root = tk.Tk()
    root.title("Hello, World!")

    helloLabel = tk.Label(text="こんにちは GUI!")
    nameBox = tk.Text()
    quitButton = tk.Button(text='終了', command=sys.exit)
    for widget in [helloLabel, nameBox, quitButton]:
        widget.pack()        # 各widgetを配置

    root.mainloop()


if __name__ == '__main__':
    main()
