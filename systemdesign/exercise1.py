import random

hidden = random.randrange(1)

guess = int(input("guess the hidden num: "))

while guess != hidden:
    print(guess, "is not correct")
    guess = int(input("try again"))
print(guess, "correct!")
