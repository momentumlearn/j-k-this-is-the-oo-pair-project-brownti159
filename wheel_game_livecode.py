import random


class Word:
    def __init__(self):
        with open('words.txt', 'r') as file:
            word_list = file.read()
        word_list = word_list.splitlines()

        self.characters = random.choice(word_list)
        self.word_length = len(self.characters)
        

        # use word_length to build a function for difficulty: "easy", "normal" or "hard" levels
        print(self.characters)    
        # return word.upper()
    # def sort_word(self):
    #     easy_list =[]
    #     normal_list=[]
    #     hard_list=[]
    #     for word in word_list:
    #         if word_length < 6:
    #             append.easy_list
    #         elif word_length == 6 or 7:
    #             apppend.normal_list 
    #         else:
    #             append.hard_list 
                
              
    def show_mystery_word(self):
        gameboard = '_ ' * self.word_length
        print(gameboard)
        return gameboard
    


#https://stackoverflow.com/questions/60617366/how-to-reveal-a-specific-letter-in-a-string-for-python

class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def attempt_guess(self):
        total_guesses= 8
        guesses = 0
        word = Word()
        print(word.characters)
        gameboard = word.show_mystery_word()
        gameboard = list(gameboard)
        while guesses < total_guesses:
            guess = input("Please guess a letter: ")
            
            if guess.lower() not in word.characters:
                guesses += 1
                print("Incorrect, guesses remaining:", total_guesses - guesses, "Try again.")
            else: 
                print("Correct!")
            
                for i in range(len(word.characters)):
                    print(i)
                    if guess.lower() == word.characters[i]:
                        gameboard[i * 2] = guess.upper()
                
                  
                print("".join(gameboard))
            print(guesses)
            if not "_" in gameboard:
                print("Congratulations, You win! Would you like to play again?")


# difficulty = input("Do you want to play difficulty level Easy, Normal, or Hard?" )
new_game = Game('easy')

new_game.attempt_guess()