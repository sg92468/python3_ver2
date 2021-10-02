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

# 12.1.2 UTF-8
