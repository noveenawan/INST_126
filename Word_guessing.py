import random

#list of words
words = ["blue", "red", "green", "brown", "black"]

#chooses a random word within the list
guess_word = random.choice(words)

#starts the game
print("Now begin, The Word Guessing Game!")
print("Try to guess the random word!")

guesses = ''
turns = 10  #max of 10 turns before they lose

while turns > 0:
    failed = 0
    for char in guess_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("You won! The word was:", guess_word)
        break

    guess = input("\nGuess a letter: ")  #guess by getting input via user
    guesses += guess

    if guess not in guess_word:
        turns -= 1
        print("Wrong! You have", turns, 'more guesses')
        if turns == 0:
            print("You Lose! The word was:", guess_word)
