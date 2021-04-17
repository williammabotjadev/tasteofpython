import random 

def main():
    guessingGame()
    print("Game Over!")

def guessingGame():
    number = random.randint(1, 10)
    tries = 0
    userNumber = input("Guess the Number: ")
    while tries < 4:
        if number == userNumber:
            print("You Win!")
        elif number > userNumber:
            print(userNumber, " is too low!")
        elif number < userNumber:
            print(userNumber, " is too high!")
        tries += 1

main()