import random
import string

word_list = ["apple", "pear", "lychee", "mangosteen", "pineapple"]
print(word_list)

word = random.choice(word_list)
print(f"The randomly chosen word from the list: {word}")

# defining alphabet lists for validating user input
lowercase_alphabets = list(string.ascii_lowercase)
uppercase_alphabets = list(string.ascii_uppercase)
alphabets = lowercase_alphabets + uppercase_alphabets

guess = input("Type the first letter of your guess: ")
if len(guess) == 1 and guess in alphabets:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
