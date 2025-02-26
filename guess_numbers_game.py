# project name: Guess the number game
# Description: A simple game to guess the number 



# import random
# def guess_numbers_game():
#     """play guess the number game."""
#     number =random.randint(1,100)
#     guess_right=7
#     #welcome message
#     print("Welcome to the Guess the Number Game")
#     print("I am thinking of a number between 1 and 100")
#     #loop through the number of guesses
#     while guess_right>0:
#         print(f"\n You have {guess_right} guesses remaining .")
#         try:
#             guess= int(input("Make a guess: "))
#         except ValueError:
#             print("Please enter a valid number")
#             continue
#         #guess  the secrete number

#         if guess <number:
#             print("Your guess is too low, try again.")
#         elif guess >number:
#                 print("Your guess is too high, try again.")
#         else:
#             print(f"Congratulations! You guessed the number {number} correctly.")
#             #check if the guess is correct
#             if guess==number:
#                 print(f"Congratulations! You guessed the number {number} correctly in {7-guess_right +1} tries.")
#                 return
#             guess_right -= 1
#     print(f"Sorry! You have run out of guesses. The number was {number}.")
# guess_numbers_game()

import random

def guess_numbers_game():
    """Play the Guess the Number game."""
    number = random.randint(1, 100)
    guess_right = 7
    
    # Welcome message
    print("Welcome to the Guess the Number Game")
    print("I am thinking of a number between 1 and 100.")
    
    # Loop through the number of guesses
    while guess_right > 0:
        print(f"\nYou have {guess_right} guesses remaining.")
        
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Guess the secret number
        if guess < number:
            print("Your guess is too low, try again.")
        elif guess > number:
            print("Your guess is too high, try again.")
        else:
            # If the guess is correct
            print(f"Congratulations! You guessed the number {number} correctly in {7 - guess_right + 1} tries.")
            return
        
        # Decrease the number of guesses remaining
        guess_right -= 1
    
    # If the player runs out of guesses
    print(f"Sorry! You have run out of guesses. The number was {number}.")

guess_numbers_game()
