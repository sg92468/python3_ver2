# class Cat:
#     pass

# a_cat = Cat()
# another_cat = Cat()
# print(a_cat)
# print(another_cat)

# a_cat.age = 3
# print(a_cat.age)
# a_cat.nemesis = another_cat
# a_cat.nemesis.name = "Mr. Bigglesworth"
# print(another_cat.name)
# print(a_cat.nemesis.name)

# class Cat:
#     def __init__(self, name):
#         self.name = name

# furball = Cat('Grumpy')
# print(furball.name)

# class Car:
#     def exclaim(self):
#         print("I'm a Car!")
# class Yugo(Car):
#     def exclaim(self):
#         print("I'm a Yugo!")

# print(issubclass(Yugo, Car))

# give_me_a_car = Car()
# give_me_a_yugo = Yugo()
# give_me_a_car.exclaim()
# give_me_a_yugo.exclaim()

# class Person:
#     def __init__(self, name):
#         self.name = name
# class MDPerson(Person):
#     def __init__(self, name):
#         self.name = "Doctor " + name
# class JDPerson(Person):
#     def __init__(self, name):
#         self.name = name + ", Esquire"

# person = Person('Fudd')
# doctor = MDPerson('Fudd')
# lawyer = JDPerson('Fudd')
# print(person.name)
# print(doctor.name)
# print(lawyer.name)

# # mixin
# import pprint
# class PrettyMixin:
#     def dump(self):
#         pprint.pprint(vars(self))

# class Thing(PrettyMixin):
#     pass

# t = Thing()
# t.name = "Nyarlathotep"
# t.feature = "ichor"
# t.age = "eldritch"

# print(t.dump())

# # 属性へのアクセス
# class Duck:
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     @property
#     def name(self):
#         print('inside the getter')
#         return self.hidden_name
#     @name.setter
#     def name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name

# fowl = Duck('Howard')
# print(fowl.name)
# fowl.name = 'Donald'
# print(fowl.name)

# # 計算用プロパティ
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     @property
#     def diameter(self):
#         return 2 * self.radius

# c = Circle(5)
# print(c.diameter)
# c.radius = 7
# print(c.diameter)

# # クラスメソッド
# class A:
#     count = 0
#     def __init__(self):
#         A.count += 1
#     def exclaim(self):
#         print("I'm an A!")
#     @classmethod
#     def kids(cls):
#         print("A has", cls.count, "little objects.")

# easy_a = A()
# breezy_a = A()
# wheezy_a = A()
# A.kids()

# # 静的メソッド
# class CoyoteWeapon:
#     @staticmethod
#     def commercial():
#         print('This CoyoteWeapon has been brought to you by Acme')
# CoyoteWeapon.commercial()

# # ダックタイピング
# class Quote:
#     def __init__(self, person, words):
#         self.person = person
#         self.words = words
#     def who(self):
#         return self.person
#     def says(self):
#         return self.words + '.'

# class QuestionQuote(Quote):
#     def says(self):
#         return self.words + '?'

# class ExclamationQuote(Quote):
#     def says(self):
#         return self.words + '!'

# hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
# print(hunter.who(), 'says:', hunter.says())

# hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
# print(hunted1.who(), 'says:', hunted1.says())

# hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
# print(hunted2.who(), 'says:', hunted2.says())

# class BabblingBrook:
#     def who(self):
#         return 'Brook'
#     def says(self):
#         return 'Babble'

# brook = BabblingBrook()

# print(brook.who(), 'says:', brook.says())

# # 特殊メソッド
# class Word:
#     def __init__(self, text):
#         self.text = text
#     def __eq__(self, word2):
#         return self.text.lower() == word2.text.lower()
#     def __str__(self):
#         return self.text
#     def __repr__(self):
#         return 'Word("' + self.text + '")'

# first = Word('ha')
# second = Word('HA')
# third = Word('eh')

# print(first == second)
# print(first == third)
# print(first)
# print(repr(first))

# # 10.9 集約とコンポジション
# class Bill:
#     def __init__(self, description):
#         self.description = description

# class Tail:
#     def __init__(self, length):
#         self.length = length

# class Duck:
#     def __init__(self, bill, tail):
#         self.bill = bill
#         self.tail = tail
#     def about(self):
#         print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')

# a_tail = Tail('long')
# a_bill = Bill('wide orange')
# duck = Duck(a_bill, a_tail)
# duck.about()

# # 10.11 名前付きタプル
# from collections import namedtuple
# Duck = namedtuple('Duck', 'bill tail')
# duck = Duck('wide orange', 'long')
# print(duck)
# print(duck.bill)
# print(duck.tail)

# parts = {'bill': 'wide orange', 'tail': 'long'}
# duck2 = Duck(**parts)
# print(duck2)

# duck3 = duck2._replace(tail='magnificent', bill='crushing')
# print(duck3)

# # 10.12 データクラス
# from dataclasses import dataclass
# @dataclass
# class AnimalClass:
#     name: str
#     habitat: str
#     teeth: int = 0

# snowman = AnimalClass('yeti', 'Himalayas', 46)
# duck = AnimalClass(habitat='lake', name='duck')
# print(snowman)
# print(duck)


# q 10.1
from collections import namedtuple


class Thing:
    pass

example = Thing()
print(Thing)
print(example)

# q 10.2
class Thing2:
    letters = 'abc'

print(Thing2.letters)

# q 10.3
class Thing3:
    def __init__(self):
        self.letters = 'xyz'
thing3 = Thing3()
print(thing3.letters)

# q 10.4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
element = Element('Hydrogen', 'H', 1)
print(element)

# q 10.5
a_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**a_dict)
print(hydrogen)

# q 10.6
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(f'{self.name}, {self.symbol}, {self.number}')
hydrogen = Element(**a_dict)
hydrogen.dump()

# q 10.7
print(hydrogen)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return f'{self.name}, {self.symbol}, {self.number}'
hydrogen = Element(**a_dict)
print(hydrogen)

# q 10.8
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
    def __str__(self):
        return f'{self.name}, {self.symbol}, {self.number}'

hydrogen = Element(**a_dict)
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)

# q 10.9
class Bear:
    def eats(self):
        return 'berries'
class Rabbit:
    def eats(self):
        return 'clover'
class Octothorpe:
    def eats(self):
        return 'campers'
bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
print(bear.eats())
print(rabbit.eats())
print(octothorpe.eats())

# q 10.10
class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class SmartPhone:
    def does(self):
        return 'ring'
class Robot:
    def __init__(self, laser, claw, smart_phone):
        self.laser = laser
        self.claw = claw
        self.smart_phone = smart_phone
    def does(self):
        return f'{self.laser.does()}, {self.claw.does()}, {self.smart_phone.does()}'

a_laser = Laser()
a_claw = Claw()
a_smart_phone = SmartPhone()
robot = Robot(a_laser, a_claw, a_smart_phone)
print(robot.does())