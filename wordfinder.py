"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, words_file):
        with open(words_file, 'r') as w:
            self.words = w.read().split()
        self.count = len(self.words)
        print(self.count, "words read")

    def random(self):
        return random.choice(self.words)
        
    

class SpecialWordFinder(WordFinder):
    def __init__(self,words_file, word):
        super().__init__(words_file)
        self.word = word
    def only_words(self):
        words = []
        for word in self.words:
            if not word.startswith('#'):
                words.append(word)
        return words
    
    def random_word(self):
        words = self.only_words()
        return random.choice(words)

    
    


