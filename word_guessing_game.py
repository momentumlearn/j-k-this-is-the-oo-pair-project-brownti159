word = "SPAM"
print("Welcome to Wheel of Fortune!")

# display the number of letters in word
def show_mystery_word(word):
    return '_ ' * len(word)
    print(show_mystery_word(word))
    print("")

#https://stackoverflow.com/questions/60617366/how-to-reveal-a-specific-letter-in-a-string-for-python
def attempt_guess():
    total_guesses= 8
    guesses = 0
    gameboard= show_mystery_word(word)
    print(gameboard)
    gameboard = list(gameboard)
    while guesses < total_guesses:
        guess = input("Please guess a letter: ")
        if guess.upper() not in word:
            guesses += 1
            print("Incorrect, guesses remaining:", total_guesses - guesses, "Try again.")
        else: 
            print("Correct!")
           
            for letter in word:
                if guess.upper() == letter:
                    gameboard[word.index(letter) * 2] = guess.upper()
                
               
            print("".join(gameboard))
            print(guesses)
            if not "_" in gameboard:
                print("Congratulations, You win! Would you like to play again?")
attempt_guess()
print()
                