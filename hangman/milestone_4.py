# Create a new script called milestone_4.py. This file will contain the code for the third milestone.

# Define the init method of the Hangman class.

# Step 1. Create a class called Hangman.

# Step 2. Inside the class, create an init method to initialise the attributes of the class. Pass in word_list and num_lives as parameters. Make num_lives a default parameter and set the value to 5.

# Step 3. Initialise the following attributes:

# word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.

# word_guessed: list - A list of the letters of the word, with for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. If the player guesses 'a', the list would be ['a', '', '', '', ''].

# num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.

# num_lives: int - The number of lives the player has at the start of the game.

# word_list: list - A list of words.

# list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.


from milestone_2 import (
    word,
)  # check this import is correct at the end - milestone_2.py should take care of the random word choice from word_list
import string


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word  # initalise attributes inside of the init function? word here accesses word from import?
        self.word_guessed = [
            None for i in range(len(word))
        ]  # attempts to initialise blanks output to user of the same length as the secret word
        self.num_letters = {
            letter for letter in string.ascii_letters
        }  # initalises all asci_letters as a set, before user has made their choice. After, these will be removed/popped. What if this weren't a set?
