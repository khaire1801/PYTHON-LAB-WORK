import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)  # Generate random number between 1 and 10
    chances = 3  # Total chances

    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 10.")
    print(f"You have {chances} chances to guess the correct number.")

    for attempt in range(1, chances + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == number_to_guess:
            print("Congratulations! You guessed the correct number!")
            break
        elif attempt < chances:
            print("Wrong guess. Try again!")
        else:
            print(f"You lost the game. The correct number was {number_to_guess}.")

# Run the game
guess_the_number()
