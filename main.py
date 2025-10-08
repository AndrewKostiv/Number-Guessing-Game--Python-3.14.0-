import random

def runGame():
    guess = None
    count = 0
    randNum = random.randint(1,100)

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
            updateScore(count)

def playAgain():
    guess = ''
    while guess != 'n':
        try:
            guess = input("Would you like to play again? (y/n)")
        except ValueError:
            print('Invalid input, type either "y" or "n"')
        if guess.lower() == 'y':
            return True
        elif guess.lower() == 'n':
            return False
        else:
            print('Invalid input, type either "y" or "n"')

def updateScore(count:int):
    highScore:int = None
    try:
        with open("highScore.txt", "r") as file:
            highScore = int(file.read())
    except FileNotFoundError:
        print("There is no previous high score")
        with open("highScore.txt", "w") as file:
            file.write(str(count))
        print("Your current high score is", count)
        return
    
    if count < highScore:
        print("New high score of", count)
        with open("highScore.txt", "w") as file:
            file.write(str(count))
    else:
        print("High score is still", highScore)


isGameDone = False
while not isGameDone:
    runGame()
    isGameDone = not playAgain()


