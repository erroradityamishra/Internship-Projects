import random

# Predefined word list
words = ['python', 'java', 'hangman', 'programming', 'challenge']

def hangman():
    word = random.choice(words)
    guessed, attempts, max_attempts = set(), 0, 6

    while attempts < max_attempts:
        display = ' '.join([letter if letter in guessed else '_' for letter in word])
        print(f"Word: {display} | Attempts left: {max_attempts - attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("Already guessed!")
        elif guess in word:
            guessed.add(guess)
            if all(letter in guessed for letter in word):
                print(f"Congrats! You've guessed the word: {word}")
                break
        else:
            attempts += 1
            print(f"Wrong guess! Attempts left: {max_attempts - attempts}")

    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
