# print(('yamada',) * 3)
# a = (7, 2)
# b = (8, 1, 9)
# print(a < b)

# import copy
# a = [1, 2, [8, 9]]
# b = copy.deepcopy(a)
# print(a)
# print(b)

# a[2][1] = 10
# print(a)
# print(b)

# rows = range(1, 4)
# cols = range(1, 3)
# cells = [(row, col) for row in rows for col in cols]
# for cell in cells:
#     print(cell)
# print(cells)

# 7.1
years_list = [year for year in range(1994, 2000) ]
print(years_list)
# 7.2
print(years_list[3])
# 7.3
print(years_list[5])
# 7.4
things = ["mozzarella", "cinderella", "salmonella"]
# 7.5
print(things[1].title())
print(things[1])
# 7.6
things[0] = things[0].upper()
print(things)
# 7.7
del things[2]
print(things)
# 7.8
surprise = ["Groucho", "Chico", "Harpo"]
# 7.9
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1] = surprise[-1].capitalize()
print(surprise[-1])
# 7.10
print([x for x in range(10) if x % 2 == 0])
# 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("frop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done")
]
start2 = "Someone"

for first, second in rhymes:
    print(f"{' '.join([word.capitalize() + '!' for word in start1])} {first.capitalize()}!")
    print(f"{start2} {second}.")