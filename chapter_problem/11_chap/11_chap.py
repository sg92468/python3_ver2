# 11.3.1 setdefault()とdefaultdict()
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)
helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)
periodic_table['Helium'] = 947
print(periodic_table)

from collections import defaultdict
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
print(periodic_table['Lead'])
print(periodic_table)

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])

bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])

from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1
for food, count in food_counter.items():
    print(food, count)

# 11.3.2 Counter()
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

print(breakfast_counter + lunch_counter)
print(breakfast_counter - lunch_counter)
print(lunch_counter - breakfast_counter)
print(breakfast_counter & lunch_counter)
print(breakfast_counter | lunch_counter)

# 11.3.3 OrderedDict()
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])
for stooge in quotes:
    print(stooge)

# 11.3.4 スタック＋キュー==デック
