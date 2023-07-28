import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for i in range(len(self.word))]
        self.list_of_guesses = []
        self.num_letters = len(set(self.word))
        self.game_over = False

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word and guess not in self.word_guessed:
            print(f"Good guess! {guess} is in the word.")
            for idx, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1
            if self.num_letters == 0:
                self.game_over = True
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            if self.num_lives <= 0:
                self.game_over = True

    def ask_for_input(self):
        while True:
            if self.game_over:
                break
            guess = input("Guess a letter: ")
            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while True:
        game.ask_for_input()
        if game.game_over:
            break

    if game.num_lives <= 0:
        print("You lost!")
    elif game.num_letters == 0:
        print("Congratulations. You won the game!")


play_game(["apple", "pear", "lychee", "mangosteen", "pineapple"])
