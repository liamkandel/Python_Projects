import sys
from random import randint

while True: # first integer passed in by terminal
    try:
        first_num = int(sys.argv[1])
        break
    except ValueError:
        first_num = input("Please enter an integer: ")
        if first_num.isdigit():
            break

while True: # second integer passed in by terminal
    try:
        second_num = int(sys.argv[2])
        break
    except ValueError:
        second_num = input("Please enter an integer 2: ")
        if second_num.isdigit():
            break

# error handling to switch numbers to avoid a range error
try:
    random_num = randint(int(first_num), int(second_num))
except ValueError:
    random_num = randint(int(second_num), int(first_num))

# function to allow user to make a guess for the random number
def guess():
    while True:
        try:
            choice = int(input(f"Please guess a number between {first_num} and {second_num}: "))
            return int(choice)
        except ValueError:
            choice = input(f"Please guess a number between {first_num} and {second_num}: ")
            if choice.isdigit():
                    return int(choice)

choice = guess()

while choice != random_num:
    if choice > random_num:
        print("You guessed too high, try again")
        choice = guess()
    elif choice < random_num:
        print("You guessed too low, try again")
        choice = guess()

print("You got it!")

