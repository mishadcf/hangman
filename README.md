# Hangman - AICore Project 
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
- Edited milestone 2, so that the secret word isn't printed, or the word list, but the secret word can be imported as a variable when milestone_3.py is run 
- Defined two functions: ask_for_input() and check_guess(guess: str) -> bool 
- ask_for_input prompts the user to input their guess (a single alphanumeric character), checks validity of inputs- then uses that validated input as a parameter for the check_guess() function
- check_guess checks whether the guessed letter is in the secret word and outputs messages to let the user know whether their guess was correct

## Milestone 4:
- Defined a Hangman class with init method taking in a word_list parameter and num_lives (number of lives) with value 5 as a default
- Defined the following attributes of hangman instances: word, word_guessed (starts with blanks and updates with correct letter guesses), num_letters (number of unique letters that have not been guessed yet), num_lives, word_list (list of words), list_of_guesses (list of unique guesses that have been tried)
- Defined instance methods: ask_for_input, check_guess 
- ask_for_input checks validity of user guesses, then checks whether the input letter has already been guessed. If both of these conditions aren't met, then the check_guess method is run
- check_guess is defined to check if the validated guess is in the secret word. If it is, then a message to that effect is printed and the letter takes the position(s) of the underscore ('_') in the word_guessed attribute of that instance.
- if the guess is not in word, a message to that effect is printed and the player loses a life (self.num_lives reduces by 1)



