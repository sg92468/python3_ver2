# word = 'thud'
# for letter in word:
#     if letter == 'x':
#         break
#     print(letter)
# else:
#     print("No 'x' in there.")

# for x in range(2, -1, -1):
#     print(x)

# 6.1
array = [3, 2, 1, 0]
for x in array:
    print(x)
# 6.2
guess_me = 7
number = 1

while number <= guess_me:
    if number == guess_me:
        print('found it!')
        number += 1
        break
    print('too low')
    number += 1
else:
    print('oops')
# 6.3
guess_me = 5

for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
