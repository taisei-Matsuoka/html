import time,requests,re,tkinter
from tkinter import messagebox
from tkinter import *
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import cgi
import sys
import io
import cgitb

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://www.youtube.com/')
# time.sleep(0.5)
# # search = driver.find_element_by_css_selector('#search').sends_key(txt)


# root = tkinter.Tk()
# root.title('検索ワード')
# message = Label(root, text = '検索ワードを入力してください')
# root.geometry("400x150")
# message.pack()

# EditBox = tkinter.Entry(width=50)
# EditBox.place(x=150,y=50)
# EditBox.insert(tkinter.END,' ')
# EditBox.pack()

# text_content ='text' 
# def btn_click():
#     global text_content
#     text_content = EditBox.get()
#     print(text_content)

# def destroy():
#     root.destroy()

# btn = tkinter.Button(root, text='検索', command=btn_click)
# btn_click()
# print(text_content)

# btn2 = tkinter.Button(root, text='削除', command=destroy)

# btn.place(x=125, y=70)
# btn2.place(x=180, y=70)

# root.mainloop()


cgitb.enable() # デバッグに使うので、本番環境では記述しない

form = cgi.FieldStorage() # フォームデータを取得する

print("Content-Type: text/html; charset=UTF-8") # HTMLを記述するためのヘッダ
print("")

# フォームのデータが入力されていない場合
if "text" not in form:
    print("<h1>Error!</h1>")
    print("<br>")
    print("テキストを入力してください！")
    print("<a href='/'><button type='submit'>戻る</button></a>")
    sys.exit()

text = form.getvalue("text") # データの値を取得する

print(text)