# # 12.1.1 Python3のUnicode文字列
# from typing import OrderedDict
# import unicodedata
# def unicode_test(value):
#     name = unicodedata.name(value)
#     value2 = unicodedata.lookup(name)
#     print(f'value="{value}", name="{name}", value2="{value2}"')

# unicode_test('A')
# unicode_test('\u2603')
# print(unicodedata.name('\u00e9'))
# print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))
# print('caf\u00e9')
# print(len('\U0001f47b'))

# # 12.1.3 エンコーディング
# snowman = '\u2603'
# print(len(snowman))
# ds = snowman.encode('utf-8')
# print(len(ds))
# print(ds)
# print(snowman.encode('ascii', 'ignore'))
# print(snowman.encode('ascii', 'replace'))
# print(snowman.encode('ascii', 'backslashreplace'))
# print(snowman.encode('ascii', 'xmlcharrefreplace'))

# # 12.1.4 デコーディング
# place = 'caf\u00e9'
# print(place)
# print(type(place))
# place_bytes = place.encode('utf-8')
# print(place_bytes)
# print(type(place_bytes))
# place2 = place_bytes.decode('utf-8')
# print(place2)

# place3 = place_bytes.decode('latin-1')
# print(place3)

# place4 = place_bytes.decode('windows-1252')
# print(place4)

# # 12.1.5 HTMLエンティティ
# import html
# print(html.unescape("&egrave;"))
# print(html.unescape("&#233;"))
# print(html.unescape("&#xe9;"))

# from html.entities import html5
# print(html5["egrave"])
# print(html5["egrave;"])

# char = '\u00e9'
# dec_value = ord(char)
# print(html.entities.codepoint2name[dec_value])

# place = 'caf\u00e9'
# byte_value = place.encode('ascii', 'xmlcharrefreplace')
# print(byte_value)
# print(byte_value.decode())

# # 12.1.6 正規化
# eacute1 = 'é'
# eacute2 = '\u00e9'
# eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}'
# eacute4 = chr(233)
# eacute5 = chr(0xe9)
# print(eacute1, eacute2, eacute3, eacute4, eacute5)
# print(eacute1==eacute2==eacute3==eacute4==eacute5)

# eacute_combined1 = "e\u0301"
# eacute_combined2 = "e\N{COMBINING ACUTE ACCENT}"
# eacute_combined3 = "e" + "\u0301"
# print(eacute_combined1, eacute_combined2, eacute_combined3)
# print(eacute_combined1 == eacute_combined2 == eacute_combined3)
# print(len(eacute_combined1))

# print(eacute1 == eacute_combined1)

# import unicodedata
# eacute_normalized = unicodedata.normalize('NFC', eacute_combined1)
# print(eacute_normalized)
# print(eacute_normalized == eacute1)
# print(unicodedata.name(eacute_normalized))

# # 12.2 正規表現
# import re
# result = re.match(r'You', 'Young Frankenstein')
# print(result)
# youpattern = re.compile(r'You')
# result = youpattern.match('Young Frankenstein')
# print(result)

# # 12.2.1 match()
# import re
# source = 'Young Frankenstein'
# m = re.match(r'You', source)
# if m:
#     print(m.group())

# m = re.match(r'^You', source)
# if m:
#     print(m.group())

# import re
# source = 'Young Frankenstein'
# if m := re.match(r'Frank', source):
#     print(m.group())

# import re
# source = 'Young Frankenstein'
# if m := re.search(r'Frank', source):
#     print(m.group())

# import re
# source = 'Young Frankenstein'
# if m := re.match(r'.*Frank', source):
#     print(m.group())

# # 12.2.2 search()
# import re
# source = 'Young Frankenstein'
# m = re.search(r'Frank', source)
# if m:
#     print(m.group())

# # 12.2.3 findall()
# import re
# source = 'Young Frankenstein'
# m = re.findall(r'n', source)
# print(m)
# print('Found', len(m), 'matches')

# m = re.findall(r'n.', source)
# print(m)

# m = re.findall(r'n.?', source)
# print(m)

# # 12.2.4 split()
# import re
# source = 'Young Frankenstein'
# m = re.split(r'n', source)
# print(m)

# # 12.2.5 sub()
# import re
# source = 'Young Frankenstein'
# m = re.sub(r'n', '?', source)
# print(m)

# # 12.2.6 パターンの特殊文字
# import string
# printable = string.printable
# print(len(printable))
# print(printable[0:50])
# print(printable[50:])
# print(re.findall('\d', printable))
# print(re.findall('\w', printable))
# print(re.findall('\s', printable))

# # 12.2.7 パターン:メタ文字
# source = """I wish I may, I wish I might
# Have a dish of fish tonight."""
# print(re.findall(r'wish', source))
# print(re.findall(r'wish|fish', source))
# print(re.findall(r'^wish', source))
# print(re.findall(r'^I wish', source))
# print(re.findall(r'fish$', source))
# print(re.findall(r'fish tonight\.$', source))

# # 12.2.8 パターン：マッチした文字列の出力の指定
# m = re.search(r'(. dish\b).*(\bfish)', source)
# print(m.group())
# print(m.groups())

# m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
# print(m.group())
# print(m.groups())
# print(m.group('DISH'))
# print(m.group('FISH'))

# # 12.3.1 bytesとbytearray
# blist = [1, 2, 3, 255]
# the_bytes = bytes(blist) # イミュータブル
# print(the_bytes)
# the_byte_array = bytearray(blist) # ミュータブル
# print(the_byte_array)

# the_bytes = bytes(range(0, 256))
# print(the_bytes)

# # 12.3.2 structのバイナリデータの変換
# import struct
# valid_png_header = b'\x89PNG\r\n\x1a\n'
# data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
#     b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
# if data[:8] == valid_png_header:
#     width, height = struct.unpack('>LL', data[16:24])
#     print('Valid PNG, with', width, 'height', height)
# else:
#     print('Not a valid PNG')

# q12.1
import unicodedata
mystery = '\U0001f984'
print(mystery)
print(unicodedata.name(mystery))

# q12.2
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

# q12.3
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
print(pop_string == mystery)

# q12.4
mammoth = """We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees
Or as the leaves upon the trees
It did require to make thee please,
And stand unrivalled Queen of Cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.

Of the youth beware of these
For some of them might rudely squeeze
And bite your cheek then songs or glees
We could not sing o' Queen of Cheese.

We'rt thou suspended from baloon,
You'd cast a shade, even at noon
Folks would think it was the moon
About to fall and crush them soon."""

# q12.5
import re
print(re.findall(r'\bc\w*', mammoth))

# q12.6
print(re.findall(r'\bc\w{4}', mammoth))

# q12.7
print(re.findall(r'\b\w*r\b', mammoth))

# q12.8
print(re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b', mammoth))

# q12.9
import binascii
hex_str = '47494638396101000100800000000000ffffff21f9' + \
    '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(hex_str)
print(len(gif))
print(gif)

# q12.10
print(gif[:6] == b'GIF89a')

# q12.11
import struct
width, height = struct.unpack('<HH', gif[6:10])
print(width, height)