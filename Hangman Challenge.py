import random
import tkinter as tk
from tkinter import messagebox

# List of words for the game
words = ['apple', 'banana', 'grape', 'orange', 'mango']

# Function to get a random word from the list
def get_random_word():
    return random.choice(words)

# Function to display the current progress of the word
def show_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "  # Show guessed letter
        else:
            display += "_ "  # Show underscore for unguessed letter
    return display

# Function to handle letter guesses
def guess_letter():
    letter = entry.get().lower()  # Get the letter from input box
    entry.delete(0, tk.END)  # Clear the input box

    if letter in guessed_letters:
        messagebox.showinfo("Oops", "You already guessed that letter.")
    elif letter in word:
        guessed_letters.append(letter)
        word_label.config(text=show_word(word, guessed_letters))
        if all(letter in guessed_letters for letter in word):
            messagebox.showinfo("Congratulations!", f"You guessed the word: {word}")
            window.quit()
    else:
        guessed_letters.append(letter)
        wrong_guesses[0] -= 1
        wrong_label.config(text=f"Attempts remaining: {wrong_guesses[0]}")
        if wrong_guesses[0] == 0:
            messagebox.showinfo("Game Over", f"You've run out of attempts! The word was: {word}")
            window.quit()

# Initialize game variables
word = get_random_word()
guessed_letters = []
wrong_guesses = [6]  # Keeping it as a list to make it mutable in functions

# Setting up the GUI window
window = tk.Tk()
window.title("Hangman Challenge")

# Display the current word progress
word_label = tk.Label(window, text=show_word(word, guessed_letters), font=("Helvetica", 20))
word_label.pack(pady=10)

# Entry box for guessing a letter
entry_label = tk.Label(window, text="Guess a letter:")
entry_label.pack()

entry = tk.Entry(window, font=("Helvetica", 14))
entry.pack(pady=5)

# Button to submit the guessed letter
guess_button = tk.Button(window, text="Guess", command=guess_letter)
guess_button.pack(pady=10)

# Label to show remaining attempts
wrong_label = tk.Label(window, text=f"Attempts remaining: {wrong_guesses[0]}", font=("Helvetica", 14))
wrong_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
