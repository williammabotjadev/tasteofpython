import random 

def main():
    guessingGame()
    print("Game Over!")

def guessingGame():
    number = random.randint(1, 10)
    tries = 0
    
    while True:
        userNumber = int(input("Guess the Number: "))
        if number == userNumber:
            print("You Win!")
            break
        elif number > userNumber:
            print(userNumber, " is too low!")
        elif number < userNumber:
            print(userNumber, " is too high!")
        tries += 1
        if(tries == 3): break 

main()