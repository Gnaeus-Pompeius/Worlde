import random

class WordBank:
    def __init__(self):
        self.textfile = "wordlists/words{}.txt"
       

    def open_file(self,word_len):
        with open(self.textfile.format(str(word_len)), 'r') as file:
            alltext = file.read()
            allwords = list(map(str, alltext.split()))
            file.close()
            return allwords
    
    def write_file(self, word_to_file, filename):
        with open(filename, 'a') as file:
            file.write("\n" + word_to_file)
            file.close()
    
    def getWord(self,w_len):
        return random.choice(self.open_file(w_len))

    def addToFile(self):
        while True:
            word = input("Enter a word to add with length between 2-12: ").lower()
            if self.validateGuess(word):
                self.write_file(word, self.textfile.format(str(len(word))))
                print("Word added successfully")
                return
            else:
                print("Invalid input!")

    def validateGuess(self, word):
        for i in word:
            if i.isdigit():
                return False
        if 2 > len(word) > 12:
            return False
        return True

    def getWordToAdd():
        word_allowed = False
        while not word_allowed:
            word = input("Enter a word of length 2-12 to add")
            

    def __str__(self) -> str:
        return self.word
