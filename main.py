import random

def runGame():
    randNum = random.randint(1,100)
    guess:int = 0
    count:int = 0

    while guess != randNum:
        try:
            guess = input("Guess a number (or type \"q\" to quit): ")
            if guess.lower() == 'q':
                print("The correct answer was", randNum)
                break
            else: 
                guess = int(guess)
        except ValueError:
            print("Incorrect input, type a number")
            continue

        count += 1

        if (abs(guess - randNum) <= 5 and guess != randNum):
            print("You are very close!")
        if guess > randNum:
            print(guess, "is too high")
        elif guess < randNum:
            print(guess, "is too low")
        else:
            print(guess, "is correct! You took",count,"attempts")

runGame()
guess = ''
while guess != 'n':
    try:
        guess = input("Would you like to play again? (y/n)")
    except ValueError:
        print('Invalid input, type either "y" or "n"')
    if guess.lower() == 'y':
        runGame()
    elif guess.lower() == 'n':
        break
    else:
        print('Invalid input, type either "y" or "n"')


