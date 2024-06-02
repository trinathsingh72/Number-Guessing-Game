import random

def number_guessing_game():
    # Generate a random number between 1 and 30
    secret_number = random.randint(1, 30)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 30.")
    
    while True:
        # Ask the user for their guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1


            if guess < 1 or guess > 30:
                print("Please enter a number between 1 and 30.")
                continue

            # Check the user's guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()
