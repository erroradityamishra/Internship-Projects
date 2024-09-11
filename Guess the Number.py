import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")

        # Generate a random number between 1 and 100
        self.number_to_guess = random.randint(1, 100)
        self.attempts_left = 10

        # GUI Elements
        self.label_message = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14))
        self.label_message.pack(pady=10)

        self.entry_guess = tk.Entry(root, font=("Arial", 14))
        self.entry_guess.pack(pady=10)

        self.button_submit = tk.Button(root, text="Submit Guess", font=("Arial", 14), command=self.check_guess)
        self.button_submit.pack(pady=10)

        self.label_attempts = tk.Label(root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 12))
        self.label_attempts.pack(pady=10)

        self.label_feedback = tk.Label(root, text="", font=("Arial", 12))
        self.label_feedback.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
        except ValueError:
            self.label_feedback.config(text="Please enter a valid number!")
            return

        # Check the guess
        if guess < self.number_to_guess:
            self.label_feedback.config(text="Too low!")
        elif guess > self.number_to_guess:
            self.label_feedback.config(text="Too high!")
        else:
            self.label_feedback.config(text=f"Correct! The number was {self.number_to_guess}.")
            self.button_submit.config(state=tk.DISABLED)
            return

        # Decrease attempts
        self.attempts_left -= 1
        self.label_attempts.config(text=f"Attempts left: {self.attempts_left}")

        # Check if attempts are finished
        if self.attempts_left == 0:
            self.label_feedback.config(text=f"Game over! The number was {self.number_to_guess}.")
            self.button_submit.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
game = GuessNumberGame(root)

# Start the Tkinter event loop
root.mainloop()

import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")

        # Generate a random number between 1 and 100
        self.number_to_guess = random.randint(1, 100)
        self.attempts_left = 10

        # GUI Elements
        self.label_message = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14))
        self.label_message.pack(pady=10)

        self.entry_guess = tk.Entry(root, font=("Arial", 14))
        self.entry_guess.pack(pady=10)

        self.button_submit = tk.Button(root, text="Submit Guess", font=("Arial", 14), command=self.check_guess)
        self.button_submit.pack(pady=10)

        self.label_attempts = tk.Label(root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 12))
        self.label_attempts.pack(pady=10)

        self.label_feedback = tk.Label(root, text="", font=("Arial", 12))
        self.label_feedback.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
        except ValueError:
            self.label_feedback.config(text="Please enter a valid number!")
            return

        # Check the guess
        if guess < self.number_to_guess:
            self.label_feedback.config(text="Too low!")
        elif guess > self.number_to_guess:
            self.label_feedback.config(text="Too high!")
        else:
            self.label_feedback.config(text=f"Correct! The number was {self.number_to_guess}.")
            self.button_submit.config(state=tk.DISABLED)
            return

        # Decrease attempts
        self.attempts_left -= 1
        self.label_attempts.config(text=f"Attempts left: {self.attempts_left}")

        # Check if attempts are finished
        if self.attempts_left == 0:
            self.label_feedback.config(text=f"Game over! The number was {self.number_to_guess}.")
            self.button_submit.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
game = GuessNumberGame(root)

# Start the Tkinter event loop
root.mainloop()
