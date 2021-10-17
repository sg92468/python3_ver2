import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld']
]
with open('villains', 'w') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

with open('villains', 'r') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]

print(villains)