import random
randNum = random.randint(1,100)
guess:int = 0
count:int = 0

while guess != randNum:
    guess = int(input("Guess a number: "))
    count += 1
    if guess > randNum:
        print(guess, "is too high")
    elif guess < randNum:
        print(guess, "is too low")
    else:
        print(guess, "is correct! You took",count,"attempts")
