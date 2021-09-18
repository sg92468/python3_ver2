# start = 'Na ' * 4
# print(start)

# blurt = "What the...!??"
# print(blurt.strip('.!?'))
# import string
# print(blurt.strip(string.punctuation))

# setup = 'a duck goes into a bar...'
# print(setup.strip('.'))
# print(setup.capitalize())
# print(setup.title())
# print(setup.swapcase())
# print(setup.center(30))
# print(setup.rjust(30))
# print(setup.ljust(30))

# print("{1} word is {0}.".format(start, blurt.strip('.!?')))
# print(f"{blurt.strip('.!?') =} word is {start =}.")

# 5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

print(song.replace(" m", " M"))
# 5.2
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day is the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

q_a = ((0, 1), (1, 2), (2, 0))

for q, a in q_a:
    print(f"Q: {questions[q]}")
    print(f"A: {answers[a]}")
# 5.3
words = ("roast beef", "ham", "head", "calm")
poem = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s,
And now thinks he's a %s."""
print(poem % words)
# 5.4
letter = """Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handing.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
"""
# 5.5
salutation = "Mr."
name = "Bob"
product = "pen"
verbed = "sent"
room = "canpas"
amount = "50"
animals = "cats"
percent = "50"
spokesman = "John"
job_title = "professor"

print(letter.format(salutation=salutation, name=name, product=product, verbed=verbed, room=room, amount=amount, animals=animals, percent=percent, spokesman=spokesman, job_title=job_title))
# 5.6
base_name = "%sy Mc%sface"
names = ["duck", "gourd", "spitz"]
for name in names:
    cap_name = name.capitalize()
    print(base_name % (cap_name, name))
# 5.7
base_name = "{}y Mc{}face"
names = ["duck", "gourd", "spitz"]
for name in names:
    cap_name = name.capitalize()
    print(base_name.format(cap_name, name))
# 5.8
names = ["duck", "gourd", "spitz"]
for name in names:
    cap_name = name.capitalize()
    print(f"{cap_name}y Mc{name}face")