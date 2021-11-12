# # 18.1.5 標準ウェブライブラリ
# from logging import debug
# import urllib.request
# url = 'http://www.example.com/'
# conn = urllib.request.urlopen(url)

# print(conn.status)

# data = conn.read()
# print(data[:50])

# str_data = data.decode('utf8')
# print(str_data)
# for key, value in conn.getheaders():
#     print(key, value)

# # 18.1.6 requests
# import requests
# resp = requests.get('http://example.com')
# print(resp)
# print(resp.status_code)
# print(resp.text[:50])

# # 18.5.1 webbrowser
# import antigravity
# import webbrowser
# url = 'http://www.python.org/'
# print(webbrowser.open(url))
# print(webbrowser.open_new(url))
# print(webbrowser.open_new_tab(url))

# # 18.5.2 webview
# import webview
# url = 'http://time.gov'
# webview.create_window(f"webview display of {url}", url)

# pip3 install pywebview[qt]でインストールできず。
# pip3 install pywebviewでインストールし上記コマンドをテストしたがwebviewは機能せず。

# # q18.2
# from flask import Flask

# app = Flask(__name__)

# app.run(port=5000, debug=True)

# # q18.3
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "It's alive"

# app.run(port=5000, debug=True)

# # q18.4
# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     thing = request.values.get('thing')
#     height = request.values.get('height')
#     color = request.values.get('color')
#     return render_template('home.html', thing=thing, height=height, color=color)
# # クエリを使用しない場合
# # @app.route('/<thing>/<height>/<color>/')
# # def home(thing, height, color):
# #     return render_template('home.html', thing=thing, height=height, color=color)

# app.run(port=5000, debug=True)

x = 551 % 31
print(x)