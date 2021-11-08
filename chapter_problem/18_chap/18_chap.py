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

