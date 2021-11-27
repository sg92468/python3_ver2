# デジタル時計

import sys
import tkinter as tk
import datetime

# メイン関数


def main():
    root = tk.Tk()
    root.title("デジタル時計!")
    root.minsize(200, 100)

    dateLabel = tk.Label(font=('Helvetica', '24'), fg='blue', bg='red')
    timeLabel = tk.Label(font=('Helvetica', '80'), fg='white', bg='green')
    dateLabel.pack(fill=tk.X)
    timeLabel.pack(fill=tk.X)        # 各widgetを配置

    # 表示更新用ループ
    while True:
        dateLabel.configure(text=str(datetime.date.today()))
        timeLabel.configure(text=datetime.datetime.now().strftime("%H:%M:%S"))
        root.after(500)
        dateLabel.update()
        timeLabel.update()

    # イベントループ
    root.mainloop()


if __name__ == '__main__':
    main()
