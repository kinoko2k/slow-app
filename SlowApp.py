import tkinter
# from tkinter
# import messagebox
import webbrowser
url = "youtube.com"
url1 = "discord.coom"
# webbrowser.open(url)

# click時のイベント
def btn_click():
  webbrowser.open(url)
def btn_click1():
    webbrowser.open(url1)

# 画面作成
tki = tkinter.Tk()
tki.geometry('300x200') # 画面サイズの設定
tki.title('アプリが最短で開けないアプリ') # 画面タイトルの設定

# ボタンの作成
btn = tkinter.Button(tki, text='Youubeを開く', command = btn_click)
btn.place(x=150, y=80) #ボタンを配置する位置の設定
btn1 = tkinter.Button(tki, text='Discordを開く', command = btn_click1)
btn1.place(x=360, y=80) #ボタンを配置する位置の設定

# 画面をそのまま表示
tki.mainloop()
