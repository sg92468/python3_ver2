from typing import Pattern


sum = 0
test = 0
for n in range(1, 65):
    sum += n ** 4

print(sum)

# 2
array = [1, 0, 5]
for n in range(1, 32):
    x = array[n - 1] + array[n] + array[n + 1]
    array.append(x)
y = 1
print(array[31])

# 3
count = 0
for n in range(1, 40001):
    n_text = list(str(n))
    if n % 3 == 0 or '3' in n_text:
        count += n

print(count)
# 4
pattern = []
for x_205 in range(31):
    for x_82 in range(41):
        for x_30 in range(11):
            sum = 0
            sum = 205 * x_205 + 82 * x_82 + 30 * x_30
            if not sum in pattern:
                pattern.append(sum)

print(len(pattern))

# 5

kg = list(range(1, 778))
n = 80
count = 0
while n != 0:
    sum = 0
    while sum <= 5000:
        sum += kg[n]
        n -= 1
    count += 1

print(kg[1])
