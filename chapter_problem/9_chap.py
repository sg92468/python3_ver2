def menu(wine, sntree, dessert='pudding'):
    return {'wine': wine, 'entree': 'chicken', 'dessert': dessert}

print(menu('chardonnay', 'chicken'))

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy('a')
nonbuggy('b')
nonbuggy('a', ['b', 'c'])