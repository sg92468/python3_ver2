# 12.1.1 Python3のUnicode文字列
import unicodedata
def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f'value="{value}", name="{name}", value2="{value2}"')

unicode_test('A')
unicode_test('\u2603')
print(unicodedata.name('\u00e9'))
print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))
print('caf\u00e9')
print(len('\U0001f47b'))

# 12.1.3 エンコーディング
snowman = '\u2603'
print(len(snowman))
ds = snowman.encode('utf-8')
print(len(ds))
print(ds)
print(snowman.encode('ascii', 'ignore'))
print(snowman.encode('ascii', 'replace'))
print(snowman.encode('ascii', 'backslashreplace'))
print(snowman.encode('ascii', 'xmlcharrefreplace'))

# 12.1.4 デコーディング
place = 'caf\u00e9'
print(place)
print(type(place))
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
place2 = place_bytes.decode('utf-8')
print(place2)

place3 = place_bytes.decode('latin-1')
print(place3)

place4 = place_bytes.decode('windows-1252')
print(place4)

# 12.1.5 HTMLエンティティ
import html
print(html.unescape("&egrave;"))
print(html.unescape("&#233;"))
print(html.unescape("&#xe9;"))

from html.entities import html5
print(html5["egrave"])
print(html5["egrave;"])

char = '\u00e9'
dec_value = ord(char)
print(html.entities.codepoint2name[dec_value])

place = 'caf\u00e9'
byte_value = place.encode('ascii', 'xmlcharrefreplace')
print(byte_value)
print(byte_value.decode())

# 12.1.6 正規化
eacute1 = 'é'
eacute2 = '\u00e9'
eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}'
eacute4 = chr(233)
eacute5 = chr(0xe9)
print(eacute1, eacute2, eacute3, eacute4, eacute5)
print(eacute1==eacute2==eacute3==eacute4==eacute5)

eacute_combined1 = "e\u0301"
eacute_combined2 = "e\N{COMBINING ACUTE ACCENT}"
eacute_combined3 = "e" + "\u0301"
print(eacute_combined1, eacute_combined2, eacute_combined3)
print(eacute_combined1 == eacute_combined2 == eacute_combined3)
print(len(eacute_combined1))

print(eacute1 == eacute_combined1)

import unicodedata
eacute_normalized = unicodedata.normalize('NFC', eacute_combined1)
print(eacute_normalized)
print(eacute_normalized == eacute1)
print(unicodedata.name(eacute_normalized))