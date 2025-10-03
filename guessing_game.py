import art
import random

# Generate a random number
random_num = random.randint(1,100)
# Intro
print(art.logo)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100. \n")

# Choose a difficulty type -> Easy or Hard
def difficulty_level():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
       return 10

    else:
        return 5

num_of_lives = difficulty_level()

continue_guessing = True

# User guesses
def make_guess():
    return int(input("Make a guess: "))

while continue_guessing:
    # Compare guess to random_num
    print(f"You have {num_of_lives} attempts remaining to guess the number.")
    guess = make_guess()

    if guess > random_num:
        print("Too high.")
        num_of_lives -= 1

    elif guess < random_num:
        print("Too low.")
        num_of_lives -= 1
    else:
        print(f"You got it! The answer was {random_num}.")
        continue_guessing = False

    # If lives reach 0 the game is over
    if num_of_lives <= 0:
        print(f"You ran out of guesses. The number we were looking for is {random_num}.")
        continue_guessing = False




