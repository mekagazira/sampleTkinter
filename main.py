import tkinter as tk
import subprocess

# ウィンドウ作成
win = tk.Tk()
win.geometry("300x150")
win.title("検索くん")

# ラベル作成
label = tk.Label(win, text='検索ワード')
label.pack()

# テキストボックス作成
text = tk.Entry(win)
text.pack()
text.insert(tk.END, 'ほげげほ') # 初期値を指定

# OKボタンを押した時のアクション
def ok_click():
    # テキストボックスの内容を得る
    search_word = text.get()
    # ダイアログを表示
    subprocess.Popen([r'C:\Program Files\Internet Explorer\iexplore.exe', 'https://www.google.co.jp/search?q=' + search_word])

# ボタン作成
okButton = tk.Button(win, text='検索', command=ok_click)
okButton.pack()

# ウィンドウを動かす
win.mainloop()