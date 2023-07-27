from milestone_2 import (
    word,
)

# from milestone_3 import check_guess, ask_for_input
import string

# check this import is correct at the end - milestone_2.py should take care of the random word choice from word_list, milestone_3.py already has a check_guess function (DRY)


# Remember, this takes in word from milestone 2 - can adapt the below to arbitrary word list if needed
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word  # initalise attributes inside of the init function? word here accesses word from import?
        self.word_guessed = [
            "_" for i in range(len(word))
        ]  #  initialise blanks output to user of the same length as the secret word
        self.num_letters = {
            letter for letter in string.ascii_letters
        }  # initalises all asci_letters as a set, before user has made their choice. After, these will be removed/popped. What if this weren't a set?
        self.list_of_guesses = []  # keeps track of all unique guesses

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            for idx, letter in enumerate(
                word
            ):  # takes care of the case where the same letter exists in the word in different locations
                if guess == letter:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not (guess.isalpha() and len(guess) == 1):  # checks input is valid
                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
