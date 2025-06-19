import random

#Guessing Game
guess = int(input("\nI'm thiking of a number between 1 and 20, can you think of it?: "))

while guess != 4:
    if guess in[3, 5]:
        print("So close!")
    elif guess < 4:
        print("A little bit higher")
    elif guess > 4 and guess <= 10:
        print("A little bit lower")
    else:
        print("Bit too high mate")
    guess = int(input("Guess again: "))

print("\nCongratulations young sigma!")
