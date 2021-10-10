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

# 14.1.7 withによるファイルの自動クローズ
with open('relativity', 'w') as fout:
    fout.write(poem)

# 14.1.8 seek()による位置の変更
fin = open('bfile', 'rb')
fin.tell()
fin.seek(255)
bdata = fin.read()
print(len(bdata))
print(bdata[0])

import os
print(os.SEEK_SET)
print(os.SEEK_CUR)
print(os.SEEK_END)

fin = open('bfile', 'rb')
print(fin.seek(-1, 2))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])

fin = open('bfile', 'rb')
print(fin.seek(254, 0))
print(fin.tell())
print(fin.seek(1, 1))
print(fin.tell())
bdata = fin.read()
print(len(bdata))
print(bdata[0])
fin.close()

# 14.3.1 exists()のファイルチェック
import os
print(os.path.exists('oops.txt'))
print(os.path.exists('./oops.txt'))
print(os.path.exists('waffles'))
print(os.path.exists('.'))
print(os.path.exists('..'))

# 14.3.2 isfile()によるファイルタイプのチェック
name = 'oops.txt'
print(os.path.isfile(name))
print(os.path.isdir(name))
print(os.path.isdir('.'))
print(os.path.isabs('/big/fake/name'))
print(os.path.isabs('big/fake/name'))

# 14.3.3 copy()
import shutil
shutil.copy('oops.txt', 'ohno.txt')

# 14.3.4 rename()
import os
os.rename('ohno.txt', 'ohwell.txt')

# 14.3.5 link(),symlink()
# os.link('oops.txt', 'yikes.txt')
print(os.path.isfile('yikes.txt'))
print(os.path.islink('yikes.txt'))

# os.symlink('oops.txt', 'jeepers.txt')
print(os.path.islink('jeepers.txt'))

# 14.3.6 chmod()
# os.chmod('oops.txt', 0o400)
# import stat
# os.chmod('oops.txt', stat.S_IRUSR)

# 14.3.7 chown() オーナー変更
# uid = 5
# gid = 22
# os.chown('oops', uid, gid)

# 14.3.8 remove() ファイル削除
os.remove('oops.txt')
os.path.exists('oops.txt')

# 14.4.1 mkdir()
# os.mkdir('poems')
# os.path.exists('poems')

# 14.4.2 rmdir()
# os.rmdir('poems')
# os.path.exists('poems')

# 14.4.3 scandir()
# os.mkdir('poems')

with os.scandir("poems") as it:
    entries = [entry.name for entry in it]
print(entries)

# os.mkdir('poems/mcintyre')
with os.scandir("poems") as it:
    entries = [entry.name for entry in it]
print(entries)

# 14.4.4 chdir()
# import os
# os.chdir('poems')
# with os.scandir("poems") as it:
#     entries = [entry.name for entry in it]
# print(entries)

# 14.4.5 glob()
import glob
print(glob.glob('p*'))

# 14.5 パス名
# 14.5.1 abspath()
print(os.path.abspath('oops.txt'))

# 14.5.2 realpath()
print(os.path.realpath('jeepers.txt'))
print(os.path.abspath('jeepers.txt'))

# 14.5.3 os.path.loin()
import os
win_file = os.path.join("eek", "urk")
win_file = os.path.join(win_file, "snort.txt")
print(win_file)

# 14.5.4 pathlib
from pathlib import Path
file_path = Path('eek') / 'urk' / 'snort.txt'
print(file_path)

print(file_path.name)
print(file_path.suffix)
print(file_path.stem)

from pathlib import PureWindowsPath
print(PureWindowsPath(file_path))

# 14.6 BytesIO,StringIO

# q14.1
import glob
print(glob.glob('*'))

import os
with os.scandir('.') as it:
    entries = [entry.name for entry in it]
print(entries)

# q14.2
import glob
print(glob.glob('../*'))

with os.scandir('..') as it:
    entries = [entry.name for entry in it]
print(entries)

# q14.3
test1 = 'This is a test of the emergency text system'
with open('test.txt', 'w') as it:
    it.write(test1)

# q14.4
with open('test.txt', 'r') as it:
    test2 = it.read()
print(test2 == test1)
