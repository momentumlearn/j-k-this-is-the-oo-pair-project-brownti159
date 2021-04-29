#import random
#import words.txt



#ask user for mode "Easy", "Normal", or "Hard"


#select word
#function for selecting word
#def get_word()

word = "GOOGLE"

#display the number of letters in word
def show_mystery_word(word):
    return ' _ ' * len(word)
print(show_mystery_word(word))


# def show_word(word):
#     for i in range(0, len(word)):
#         if ord(word[i]) != 32:
#             new_word = word.replace(word[i], '_')
#     print(new_word)


# For character in word:
#     if character in guesses:
#         print("_"character "_")
#     else:
#         print("_")

#function to play game
#def play_game():

#ask for user input /print statement to guess letter

#user inputs guess

#return whether the letter is in the word or not

#if true: return the word with the remaining letters to be guessed

#if false return "incorrect, guess again.
# show_word(word)