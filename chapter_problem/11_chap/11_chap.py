# # 11.3.1 setdefault()とdefaultdict()
# periodic_table = {'Hydrogen': 1, 'Helium': 2}
# print(periodic_table)
# carbon = periodic_table.setdefault('Carbon', 12)
# print(carbon)
# print(periodic_table)
# helium = periodic_table.setdefault('Helium', 947)
# print(helium)
# print(periodic_table)
# periodic_table['Helium'] = 947
# print(periodic_table)

# from collections import defaultdict
# periodic_table = defaultdict(int)
# periodic_table['Hydrogen'] = 1
# print(periodic_table['Lead'])
# print(periodic_table)

# def no_idea():
#     return 'Huh?'

# bestiary = defaultdict(no_idea)
# bestiary['A'] = 'Abominable Snowman'
# bestiary['B'] = 'Basilisk'
# print(bestiary['A'])
# print(bestiary['B'])
# print(bestiary['C'])

# bestiary = defaultdict(lambda: 'Huh?')
# print(bestiary['E'])

# from collections import defaultdict
# food_counter = defaultdict(int)
# for food in ['spam', 'spam', 'eggs', 'spam']:
#     food_counter[food] += 1
# for food, count in food_counter.items():
#     print(food, count)

# # 11.3.2 Counter()
# from collections import Counter
# breakfast = ['spam', 'spam', 'eggs', 'spam']
# breakfast_counter = Counter(breakfast)
# print(breakfast_counter)

# print(breakfast_counter.most_common())
# print(breakfast_counter.most_common(1))

# lunch = ['eggs', 'eggs', 'bacon']
# lunch_counter = Counter(lunch)
# print(lunch_counter)

# print(breakfast_counter + lunch_counter)
# print(breakfast_counter - lunch_counter)
# print(lunch_counter - breakfast_counter)
# print(breakfast_counter & lunch_counter)
# print(breakfast_counter | lunch_counter)

# # 11.3.3 OrderedDict()
# from collections import OrderedDict
# quotes = OrderedDict([
#     ('Moe', 'A wise guy, huh?'),
#     ('Larry', 'Ow!'),
#     ('Curly', 'Nyuk nyuk!'),
# ])
# for stooge in quotes:
#     print(stooge)

# # 11.3.4 スタック＋キュー==デック
# from collections import deque
# def palindrome(word):
#     dq = deque(word)
#     while len(dq) > 1:
#         if dq.popleft() != dq.pop():
#             return False
#         return True
# print(palindrome('racecar'))
# print(palindrome('halibut'))

# # 11.3.5 itertoolsの反復処理
# import itertools
# for item in itertools.chain([1, 2], ['a', 'b']):
#     print(item)

# for item in itertools.accumulate([1, 2, 3, 4]):
#     print(item)

# def multiply(a, b):
#     return a * b
# for item in itertools.accumulate([1, 2, 3, 4], multiply):
#     print(item)

# # 11.3.6 pprint()
# from pprint import pprint
# quotes = OrderedDict([
#     ('Moe', 'A wise guy, huh?'),
#     ('Larry', 'Ow!'),
#     ('Curly', 'Nyuk nyuk!'),
# ])
# print(quotes)
# pprint(quotes)

# # 11.3.7 ランダムな値
# from random import choice
# print(choice([23, 9, 46, 'bacon', 0x123abc]))
# print(choice('alphabet'))

# from random import sample
# print(sample([23, 9, 46, 'bacon', 0x123abc], 3))

# from random import randint
# print(randint(38, 74))

# from random import randrange
# print(randrange(38, 74, 10))

# from random import random
# print(random())

# q11.1
import zoo
zoo.hours()

# q11.2
import zoo as menagerie
menagerie.hours()

# q11.3
from zoo import hours
hours()

# q11.4
from zoo import hours as info
info()

# q11.5
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

# q11.6
from collections import OrderedDict
fancy = OrderedDict(plain)
print(fancy)

# q11.7
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])