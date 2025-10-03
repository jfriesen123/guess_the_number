import random
import art

EASY_LEVEL = 10
HARD_LEVEL = 5

# Generate a random number
random_num = random.randint(1,100)

# Compare guess to random number 
def compare(user_guess, answer, lives):
    '''Compare the user's guess to the randomly generated number'''
    if user_guess > random_num:
        print("Too high.")
        return lives - 1

    elif user_guess < random_num:
        print("Too low.")
        return lives - 1

    else:
        print(f"You got it! The answer was {random_num}.")
        return


# Choose a difficulty type -> Easy or Hard
def difficulty_level():
    ''' Determine the difficulty level'''
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        return EASY_LEVEL

    else:
        return HARD_LEVEL




def game():
    
    print(art.logo)
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100. \n")

    num_of_lives = difficulty_level()

    guess = 0   

    while guess != random_num:
        # Compare guess to random_num, then adjust number of lives accordingly 
        print(f"You have {num_of_lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        num_of_lives = compare(guess, random_num, num_of_lives)

        # If lives reach 0 the game is over
        if num_of_lives == 0:
            print(f"You ran out of guesses. The number we were looking for is {random_num}.")
            return


game()

