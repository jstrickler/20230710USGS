

class Silly:
    WORDS = ['wombat', 'tractor', 'coatimundi']
    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.WORDS):
            raise StopIteration
        value = self.WORDS[self.index]
        self.index += 1
        return value

s = Silly()
for value in s:
    print(value)