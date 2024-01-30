from exceptions import *
from pretty_prints import PrettyPrints
from wordle import WordBank

class Game():
    def __init__(self, user, wordbank):
        self.user = user
        self.prettyprints = PrettyPrints()
        self.wordsize = self.lenPrompt()
        self.guesses = self.noOfGuessesPrompt()
        self.word = wordbank.getWord(self.wordsize).lower()
        self.guess_count = 0
        self.prev_guesses = []
        self.victory = False
        self.score = 0

    def lenPrompt(self):
        print(self.prettyprints.word_len_info)
        while True:
            word_length = input("Enter a word length: ")
            try:
                if word_length.isdigit() is False:
                    raise InvalidInputException
                elif 2 <= int(word_length) <= 12:
                    return int(word_length)
                else:
                    raise InvalidInputException
            except InvalidInputException:    
                print("Invalid input!") 

    def noOfGuessesPrompt(self):
        print(self.prettyprints.num_of_guesses_info)
        while True:
            no_of_guesses = input("Enter a number: ")
            try:
                if no_of_guesses.isdigit() is False:
                    raise InvalidInputException
                elif 1 <= int(no_of_guesses) <= 10:
                    return int(no_of_guesses)
                else:
                    raise InvalidInputException
            except InvalidInputException:
                print("Invalid input!")

    def playGame(self):
        while self.guess_count < self.guesses and self.victory is False:
            guess = self.get_guess()
            self.guess_count += 1
            if self.checkIfEqual(guess):
                self.victory = True
            else:
                self.printCorrectLetters(guess)
        self.calcScore()

    def get_guess(self): 
        while True:
            guess = input("Enter guess: ")
            if self.validateGuess(guess):
                return guess.lower()
            else:
                print("Invalid Input!")
    
    def validateGuess(self, guess):
        for i in guess:
            if i.isdigit():
                return False
        if len(guess) != len(self.word):
            return False
        return True
            
    def compareWords(self, guess):
        return_string = guess + " "
        used_ch = [] ## Prevent from getting correct multiple times for the same letter
        for i in range(self.wordsize):
            if self.word[i] == guess[i]:
                return_string += "C"
                used_ch.append(guess[i]) 
            else:
                if guess[i] in self.word and guess[i] not in used_ch:
                    return_string += "c"
                    used_ch.append(guess[i])
                else:
                    return_string += "-"
        return return_string

    def checkIfEqual(self, guess):
        if self.word == guess:
            return True
        return False

    def printCorrectLetters(self, guess):
        self.prev_guesses.append(self.compareWords(guess))
        for i in self.prev_guesses:
            print(i + " " + str(self.guesses - self.guess_count) + " guesses left.")

    def calcScore(self):
        if self.victory:
            self.score = int(self.wordsize//(self.guess_count/self.guesses))

    
