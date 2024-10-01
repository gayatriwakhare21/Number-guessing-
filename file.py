import random

def number_guessing_game():
    # Define the range of numbers
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    # Generate a random number between the bounds
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    print(f"\nI have selected a number between {lower_bound} and {upper_bound}. Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

# Start the game
number_guessing_game()
