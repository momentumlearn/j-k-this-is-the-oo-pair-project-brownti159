attemps = 8

word = "GOOGLE"
print("Welcome to Wheel of Fortune!")

#display the number of letters in word
def show_mystery_word(word):
    return ' _ ' * len(word)
print(show_mystery_word(word))
print("")

#https://stackoverflow.com/questions/60617366/how-to-reveal-a-specific-letter-in-a-string-for-python
def attempt_guess():
    total_guesses= 8
    guesses = 0
    gameboard = show_mystery_word(word)
    print(gameboard)
    while guesses < total_guesses:
        guess = input("Please guess a letter: ")
        if guess.upper() not in word:
            guess += 1
            print("Incorrect, guesses remaining:", total_guesses - guesses, "Try again.")
        else: 
            print("Correct!")
            new_gameboard = ''
            for w,l in zip(word, gameboard):
                if guess.upper() == w:
                    new_gameboard += guess.upper()
                else:
                    new_gameboard += l
            gameboard= new_gameboard
            print(gameboard)
            if not " _ " in gameboard:
                print("Congratulations, You win! Would you like to play again?")
attempt_guess()
print()
    

# guess = input("Please guess a letter:  ").upper()



# if guess not in word:
#     print(guess "is not in the word.")
#     tries -= 1
#     guessed_letters.append(guess)
# else:
#     print("Good job!")
#     tries -= 1
#     guessed_letters.append(guess)    

