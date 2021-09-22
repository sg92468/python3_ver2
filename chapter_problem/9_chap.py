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

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@square_it
@document_it
def add_ints(a, b):
    return a + b

print(add_ints)
print(add_ints(3,5))
