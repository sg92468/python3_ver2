# marx_set = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
# print(marx_set.get(' ', 'harp'))

# 8.1
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f)
# 8.2
print(e2f['walrus'])
# 8.3
f2e = {value: key for key, value in e2f.items()}
print(f2e)
# 8.4
print(f2e['chien'])
# 8.5
print({value for value in e2f.keys()})
# 8.6
life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}
print(life)
# 8.7
print(life.keys())
# 8.8
print(life['animals'].keys())
# 8.9
print(life['animals']['cats'])
# 8.10
squares = {number: number ** 2 for number in range(10)}
print(squares)
# 8.11
print({number for number in squares if number % 2 == 1})
# 8.12
key = ('optimist', 'pessimist', 'troll')
value = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
print(dict(zip(key, value)))
# 8.13
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
print(dict(zip(titles, plots)))
