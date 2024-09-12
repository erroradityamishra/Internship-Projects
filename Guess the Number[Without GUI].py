import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts_left = 10  # Number of attempts allowed

    while attempts_left > 0:
        try:
            guess = int(input(f"You have {attempts_left} attempts left. Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < number_to_guess:
            print("Your guess is too low!")
        elif guess > number_to_guess:
            print("Your guess is too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess}.")
            break

        attempts_left -= 1

    if attempts_left == 0:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_number()
