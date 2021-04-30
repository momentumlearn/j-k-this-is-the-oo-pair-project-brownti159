import random
import list of random words txt.failed



print("Welcome to Wheel of Fortune!")

words = ['cats', 'dogs', 'baby', 'duck', 'tree', 'bird', 'code']

word = random.choice(words)

print("Guess a letter.")

guesses = ' '
turns = 8

while turns > 0:
    failed = 0
    for letter in word:
        if letter in guesses:
            print(letter)
        else:
            print(" __ ")
            failed += 1

    if failed == 0:
        print("You win!")
        print("The word is: ", word)
        break
                