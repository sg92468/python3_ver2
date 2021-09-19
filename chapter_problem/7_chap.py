# print(('yamada',) * 3)
# a = (7, 2)
# b = (8, 1, 9)
# print(a < b)

import copy
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(a)
print(b)

a[2][1] = 10
print(a)
print(b)

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
print(cells)