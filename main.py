# Necessary import to return a random word
import random

# List of words used for the Hangman game
WORDS = ["Bailey", "Munchkin", "Guster", "Bunion", "Trollson", "Meegan", "parrot", "bunny"]

# Symbol used to represent hidden letters
HIDDEN_SYMBOL = "_"

# Maximum number of incorrect guesses allowed
MAX_ATTEMPTS = 3

# Return a random word
def choose_word_random():
    return random.choice(WORDS)

def main():
    # Entry point for the game
    pass


if __name__ == "__main__":
    main()
