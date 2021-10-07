# 14.1.1 open()
fout = open('oops.txt', 'w')
fout.close()

# 14.1.2 print()での書き込み
fout = open('oops.txt', 'w')
print('Oops, I created a file', file=fout)
fout.close()

# 14.1.3 write()での書き込み
poem = """There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.
"""
print(len(poem))

fout = open('relativity', 'w')
fout.write(poem)
fout.close()

fout = open('relativity', 'w')
print(poem, file=fout, sep='', end='')
fout.close()

fout = open('relativity', 'w')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset : offset + chunk])
    offset += chunk
fout.close()

try:
    fout = open('relativity', 'x')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists! That was a close one.')

# 14.1.4 read(),readline(),readlines()
fin = open('relativity', 'r')
poem = fin.read()
fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'r')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'r')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'r')
for line in fin:
    poem += line
fin.close()
print(len(poem))

fin = open('relativity', 'r')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')

# 14.1.5 write()のバイナリファイルの書き込み
bdata = bytes(range(256))
print(len(bdata))

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset : offset + chunk])
    offset += chunk
fout.close()

# 14.1.6 read()のバイナリファイルの呼び出し
fin = open('bfile', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()

