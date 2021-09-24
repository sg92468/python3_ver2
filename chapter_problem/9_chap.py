# def menu(wine, sntree, dessert='pudding'):
#     return {'wine': wine, 'entree': 'chicken', 'dessert': dessert}

# print(menu('chardonnay', 'chicken'))

# def nonbuggy(arg, result=None):
#     if result is None:
#         result = []
#     result.append(arg)
#     print(result)

# nonbuggy('a')
# nonbuggy('b')
# nonbuggy('a', ['b', 'c'])

# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('Running function:', func.__name__)
#         print('Positional arguments:', args)
#         print('Keyword arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('Result:', result)
#         return result
#     return new_function

# def square_it(func):
#     def new_function(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * result
#     return new_function

# @square_it
# @document_it
# def add_ints(a, b):
#     return a + b

# print(add_ints)
# print(add_ints(3,5))

# def flatten(lol):
#     for item in lol:
#         if isinstance(item, list):
#             yield from flatten(item)
#             # for subitem in flatten(item):
#             #     yield subitem
#         else:
#             yield item
# lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
# print(flatten(lol))
# print(list(flatten(lol)))

# 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())
# 9.2
def get_oods():
    for x in range(1, 10, 2):
        yield x

count = 1
for x in get_oods():
    if count == 3:
        print("The third odd number is", x)
        break
    count += 1
# 9.3
def test(func):
    def new_function(*args, **kwargs):
        print('Start function', func.__name__)
        result = func(*args, **kwargs)
        print('Finish function', func.__name__)
        return result
    return new_function

@test
def greeding():
    print('Hello world!')

test(greeding())
# 9.4
class OopsException(Exception):
    pass

# raise OopsException()
# try:
#     raise OopsException
# except OopsException:
#     print('Caught an oops')
# 9.5
for thing in (f'Got {number}' for number in range(10)):
    print(thing)
