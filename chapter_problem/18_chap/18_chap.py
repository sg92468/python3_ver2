# 18.1.5 標準ウェブライブラリ
import urllib.request
url = 'http://www.example.com/'
conn = urllib.request.urlopen(url)

print(conn.status)

data = conn.read()
print(data[:50])

str_data = data.decode('utf8')
print(str_data)
for key, value in conn.getheaders():
    print(key, value)

# 18.1.6 requests
import requests
resp = requests.get('http://example.com')
print(resp)
print(resp.status_code)
print(resp.text[:50])

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


