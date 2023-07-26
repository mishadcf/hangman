


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
