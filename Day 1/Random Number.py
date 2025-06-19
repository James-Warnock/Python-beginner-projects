import random

secretnumber = random.randint(1,20)

guess = int(input("Are you thinking what I'm thinking? Guess the number..: "))

while guess != secretnumber:
    guess = int(input("Guess again: "))
print("Congratulations!")
