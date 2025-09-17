#The program randomly selects a number between 1 and 10.
#The user has 3 attempts to guess the number.
#After each guess, the program tells the user if they’re correct or not.
#If the guess is wrong, it gives a hint: “Too high” or “Too low”.
#If the user guesses correctly, the game ends with a congratulatory message.
#If the user fails after 3 attempts, the game ends and reveals the number.

import random
guesses = 1
number_to_guess = random.randint(1, 10)
replaygame = True
replayInput = ""

print("Welcome to the Guessing Game!")

while replaygame == True:
    print("I have selected a number between 1 and 10. You have 3 attempts to guess it.")
    while guesses < 4:
        try:
            number = int(input(f"Guess number {guesses}, insert a number."))
        except ValueError:
            print("Invalid input, insert a number")
            continue
        
        if number > 0 and number < 11:
            if number == number_to_guess:
                print(f"Correct, the number was {number_to_guess}! You've won!")
                break

            elif number < number_to_guess:
                print("Too low")
                guesses += 1
            
            elif number > number_to_guess:
                print("Too high")
                guesses += 1

        else:
            print("Please input a number between 1 and 10")

    if guesses == 4:
        print(f"You ran out of attempts, the number to guess was {number_to_guess}, good luck next time!")

    while True:
        replayInput = input("Would you like to play a again?: [Y/N]").upper()

        if replayInput == "Y":
            replaygame = True
            guesses = 1
            break
        
        elif replayInput == "N":
            replaygame = False
            print("Thank you for playing!")
            break

        else:
            print("Invalid input")