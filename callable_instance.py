import random

class RandomWord:
    def __init__(self):
        self._words = open('DATA/words.txt').read().splitlines()
    
    def __call__(self):
        return random.choice(self._words)

if __name__ == "__main__":
    random_word = RandomWord()
    for i in range(10):
        print(random_word())