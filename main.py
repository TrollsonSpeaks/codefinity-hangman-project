import random
import os
import sys

# List of words used for the Hangman game
WORDS = [
    "python",
    "hangman",
    "developer",
    "console",
    "project",
    "function",
    "integer",
    "variable"
]

# Symbol used to represent hidden letters
HIDDEN_SYMBOL = "_"

# Maximum number of incorrect attempts allowed
MAX_ATTEMPTS = 6

# ASCII art stages for the Hangman game
stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    """
]

def choose_word_random():
    return random.choice(WORDS)

def is_word_guessed(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)

def get_guessed_word(secret_word, guessed_letters):
    return "".join(
        letter if letter in guessed_letters else HIDDEN_SYMBOL
        for letter in secret_word
    )

def get_available_letters(guessed_letters):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return "".join(char for char in alphabet if char not in guessed_letters)

def hints_match(pattern, candidate):
    if len(pattern) != len(candidate):
        return False
    for i, ch in enumerate(pattern):
        if ch != HIDDEN_SYMBOL and ch != candidate[i]:
            return False
    return True

def show_possible_matches(pattern):
    return [w for w in WORDS if hints_match(pattern, w)]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def hangman(secret_word):
    guessed_letters = []
    mistakes = 0

    while not is_word_guessed(secret_word, guessed_letters) and mistakes < MAX_ATTEMPTS:
        clear_screen()
        print(stages[mistakes])
        print("Word:", get_guessed_word(secret_word, guessed_letters))
        print("Available letters:", get_available_letters(guessed_letters))

        sys.stdout.write("Guess a letter or '?' for a hint: ")
        sys.stdout.flush()
        guess = sys.stdin.readline().strip().lower()

        if guess == "?":
            pattern = get_guessed_word(secret_word, guessed_letters)
            matches = show_possible_matches(pattern)
            print("Possible matches:", ", ".join(matches))
            sys.stdout.write("Press Enter to continue...")
            sys.stdout.flush()
            sys.stdin.readline()
            continue

        if len(guess) == 1 and guess in secret_word and guess not in guessed_letters:
            guessed_letters.append(guess)
        elif len(guess) == 1 and guess not in secret_word:
            mistakes += 1

    clear_screen()
    print(stages[mistakes])
    if is_word_guessed(secret_word, guessed_letters):
        print("You won!")
    else:
        print("You lost. The word was:", secret_word)

def main():
    secret_word = choose_word_random()
    hangman(secret_word)

if __name__ == "__main__":
    main()