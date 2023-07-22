# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1:
- Set up Github repo : local and remote, add remote origin, initialise Git on local repo

## Milestone 2:
- Create milestone_2.py.
- Import modules: random and string
- Declare a list of words from which the secret word is chosen
- Prompt user for input - the first letter of the word (their guess)
- Validate user input by checking whether they entered an alphabetic string, of length 1

## Milestone 3:
-Edited milestone 2, so that the secret word isn't printed, or the word list, but the secret word can be imported as a variable when milestone_3.py is run 
-Defined two functions: ask_for_input() and check_guess(guess: str) -> bool 
-ask_for_input prompts the user to input their guess (a single alphanumeric character), checks validity of inputs
-then uses that validated input as a parameter for the check_guess() function
-check_guess checks whether the guessed letter is in the secret word and outputs messages to let the user know whether their guess was correct


"""Good job so far! But your code probably doesn't look great. It's hard to tell which lines do what.

Create 2 functions, check_guess and ask_for_input functions which contain the code for those two things.

The check_guess function will take the guessed letter as an argument and check if the letter is in the word.

Step 1: Define a function called check_guess. pass in the guess as a parameter for the function. Write the code for the following steps in the body of this function.

Step 2: Convert the guess into lower case.

Step 3. Move the code that you wrote to check if the guess is in the word into this function block.

The ask_for_input function.

Step 1. Define a function called ask_for_input.

Step 2. Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.

Step 3. Outside the while loop, but within this function, call the check_guess function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.

Step 4. Outside the function, call the ask_for_input function to test your code.

"""


