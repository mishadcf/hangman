import random
import string

word_list = ["apple", "pear", "lychee", "mangosteen", "pineapple"]


word = random.choice(word_list)


# defining alphabet lists for validating user input. Didn't use these, as I discovered .isalpha() method
lowercase_alphabets = list(string.ascii_lowercase)
uppercase_alphabets = list(string.ascii_uppercase)
alphabets = lowercase_alphabets + uppercase_alphabets


# should only run if I run milestone 2 directly - need to import secret word from this into milestone 3
# the print statements are pretty redundant functionally
if __name__ == "__main__":
    guess = input("Type the first letter of your guess: ")
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
        print(f"word list: {word_list}")
        print(f"The randomly chosen word from the list: {word}")
