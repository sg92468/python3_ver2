total = 1 + \
      2 + \
      3 + \
      4
print(total)

vowels = 'aeiou'
letter = 'o'
if letter in vowels:
      print(letter, 'is a vowel')

tweet_limit = 280
tweet_string = "Blah" * 50
if (diff := tweet_limit - len(tweet_string)) >= 0:
      print("A fitting tweet")
else:
      print("Went over by", abs(diff))

secret = 4
guess = 5
if guess < secret:
      print("too low")
elif guess > secret:
      print("too high")
elif guess == secret:
      print("just right")

small = True
green = False
if (small == True) and (green == True):
      print("It is a pea")
elif (small == True) and (green == False):
      print("It is a cherry")
elif (small == False) and (green == True):
      print("It is a watermelon")
elif (small == False) and (green == False):
      print("It is a pumpkin")