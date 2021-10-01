from choices import advice, fast

print("Let's go to", fast.pick())
print("Should we take out?", advice.give())

import sys
for place in sys.path:
    print(place)