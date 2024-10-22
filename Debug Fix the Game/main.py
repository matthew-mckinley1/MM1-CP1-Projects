#Matthew McKinley Fix the Game
#how many attempts, if you already guessed that
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: ")) #needs to be an integer to see if it's greater or less than the number (runtime), couldn't get past that and gave an error because you can't compare a string to an integer
        attempts = attempts + 1 #you have to add attempts, can't just go infinite (logic), gives 10 guesses but it actually gave more (max_attempts = 10)
        if guess == number_to_guess: #should check if you guessed it right before the max attempts, (logic), swapping that changes the elif and if
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else: #make it an else to make it end instead of continue (syntax), it would continue even if you didn't do anything
            guess < number_to_guess
            print("Too low! Try again.")
    print("Game Over. Thanks for playing!")
start_game()