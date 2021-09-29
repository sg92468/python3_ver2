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

class Cat:
    def __init__(self, name):
        self.name = name

furball = Cat('Grumpy')
print(furball.name)

class Car:
    def exclaim(self):
        print("I'm a Car!")
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!")

print(issubclass(Yugo, Car))

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

class Person:
    def __init__(self, name):
        self.name = name
class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name
class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)

# mixin
import pprint
class PrettyMixin:
    def dump(self):
        pprint.pprint(vars(self))

class Thing(PrettyMixin):
    pass

t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"

print(t.dump())

# 属性へのアクセス
class Duck:
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)

# 計算用プロパティ
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.diameter)
c.radius = 7
print(c.diameter)

# クラスメソッド
class A:
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

# 静的メソッド
class CoyoteWeapon:
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')
CoyoteWeapon.commercial()

